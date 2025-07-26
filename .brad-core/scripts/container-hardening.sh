#!/bin/bash
# PXM Container Hardening Script
# Purpose: Set up secure SSH access, claude service account, and essential security configurations

set -e

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== PXM Container Hardening Script ===${NC}"

# Variables
CLAUDE_USER="claude"
CLAUDE_PASS="claude"
SSH_KEY="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDeQ/s/Dh+fJVSRoMJiHqSkQUwWnI8qjGH9jcS4m8K+1lEmUaINOcTpkW5+tOz0uRnL/CVGoz1kho3qw1F6UrMGOjvzR8wAX9h7IjDpawXPrw9pcNiP20YyzCDpOrDIb1mXGGIPYXhCyMWfaIoGSvhoVuDc/w6EQmwzfWzgPOmLYjNIwQOyTkCxXPAXr+cNBCok/sTjtVrVPyaDwhKA/AhIFBAUzPqXccCvH6N++yyXV49g3N1DLRc8y9WE8exa1+xTtSNdoPqcBICl9Fi0ie0MSmoem6rmaorvHCIdzjcMOZcLXOAdKJOI+WEvUfyiC6UGiuHgqHWSYegYXq5N6MdbKUu3AsncD0Tgebonj1ezZrFdlxNI3jfnk3K68O6AoOV3DeeNF87MeGzgKKqV7Ahs6Twbo4eyCOV1hdKW+lH625QFDhA/WZW+A3xLetW9klvqhcYweWjuIcFvmave/OPQHgoa6s2VR1yWEZcHFttGldF5jX4bjH/4kpX2EumHgmLgv85kqseQkgf5yLYj90yvcuYtnF527a+eXgoNAk5S0g+ACue8EiRpSEwuW6XYL+M2GHLARzeUpaNCiSAACIPIK/TV9WBD02PvOAXyT67FprObCSQz6llsSD+S4ZRF9djck7VTUWh1grlkyy1fNo5ftlusGgjjx7iFBxcJ7ZzEIw== admin@locallyknown.pro"

# Function to check if we're running as root
check_root() {
    if [[ $EUID -ne 0 ]]; then
        echo -e "${RED}This script must be run as root${NC}"
        exit 1
    fi
}

# Function to update and install packages
install_packages() {
    echo -e "${YELLOW}Updating package list...${NC}"
    apt-get update -qq
    
    echo -e "${YELLOW}Installing essential packages...${NC}"
    # Install sudo if not present (Debian containers don't have it by default)
    apt-get install -y sudo openssh-server curl wget
}

# Function to setup claude service account
setup_claude_account() {
    echo -e "${YELLOW}Setting up claude service account...${NC}"
    
    # Check if user exists
    if id "$CLAUDE_USER" &>/dev/null; then
        echo -e "${GREEN}User $CLAUDE_USER already exists${NC}"
    else
        useradd -m -s /bin/bash "$CLAUDE_USER"
        echo -e "${GREEN}Created user $CLAUDE_USER${NC}"
    fi
    
    # Set password
    echo "$CLAUDE_USER:$CLAUDE_PASS" | chpasswd
    
    # Add to sudo group
    usermod -aG sudo "$CLAUDE_USER"
    
    # Configure passwordless sudo
    echo "$CLAUDE_USER ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/$CLAUDE_USER
    chmod 440 /etc/sudoers.d/$CLAUDE_USER
    
    echo -e "${GREEN}Claude service account configured with sudo access${NC}"
}

# Function to setup SSH keys
setup_ssh_keys() {
    echo -e "${YELLOW}Setting up SSH keys...${NC}"
    
    # Setup root SSH key (temporarily, will be disabled later)
    mkdir -p /root/.ssh
    chmod 700 /root/.ssh
    echo "$SSH_KEY" > /root/.ssh/authorized_keys
    chmod 600 /root/.ssh/authorized_keys
    
    # Setup claude SSH key
    mkdir -p /home/$CLAUDE_USER/.ssh
    chmod 700 /home/$CLAUDE_USER/.ssh
    echo "$SSH_KEY" > /home/$CLAUDE_USER/.ssh/authorized_keys
    chmod 600 /home/$CLAUDE_USER/.ssh/authorized_keys
    chown -R $CLAUDE_USER:$CLAUDE_USER /home/$CLAUDE_USER/.ssh
    
    echo -e "${GREEN}SSH keys configured for claude user${NC}"
}

# Function to harden SSH configuration
harden_ssh() {
    echo -e "${YELLOW}Hardening SSH configuration...${NC}"
    
    # Backup original SSH config
    cp /etc/ssh/sshd_config /etc/ssh/sshd_config.backup
    
    # Update SSH configuration
    cat > /etc/ssh/sshd_config.d/99-hardening.conf << EOF
# PXM Container Hardening Configuration
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
ChallengeResponseAuthentication no
UsePAM yes
X11Forwarding no
PrintMotd no
AcceptEnv LANG LC_*
Subsystem sftp /usr/lib/openssh/sftp-server

# Allow claude user
AllowUsers claude

# Security settings
Protocol 2
StrictModes yes
IgnoreRhosts yes
HostbasedAuthentication no
PermitEmptyPasswords no
MaxAuthTries 3
ClientAliveInterval 300
ClientAliveCountMax 2
EOF
    
    # Restart SSH service
    systemctl restart sshd || service ssh restart
    
    echo -e "${GREEN}SSH hardening complete - root login disabled${NC}"
}

# Function to setup basic firewall rules
setup_firewall() {
    echo -e "${YELLOW}Setting up basic firewall rules...${NC}"
    
    # Install iptables-persistent if available
    apt-get install -y iptables-persistent || true
    
    # Basic firewall rules
    iptables -F
    iptables -A INPUT -i lo -j ACCEPT
    iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
    iptables -A INPUT -p tcp --dport 22 -j ACCEPT
    iptables -A INPUT -p icmp -j ACCEPT
    iptables -P INPUT DROP
    iptables -P FORWARD DROP
    iptables -P OUTPUT ACCEPT
    
    # Save rules
    iptables-save > /etc/iptables/rules.v4 2>/dev/null || true
    
    echo -e "${GREEN}Basic firewall rules configured${NC}"
}

# Function to create system info file
create_system_info() {
    echo -e "${YELLOW}Creating system information file...${NC}"
    
    cat > /etc/pxm-container-info << EOF
# PXM Container Information
HARDENING_DATE=$(date)
CONTAINER_ID=$(hostname | grep -oE '[0-9]+$' || echo "unknown")
IP_ADDRESS=$(ip -4 addr show | grep inet | grep -v 127.0.0.1 | awk '{print $2}' | cut -d/ -f1 | head -1)
CLAUDE_USER=claude
SSH_ACCESS=key-only
ROOT_LOGIN=disabled
MANAGED_BY=PXM-Manager
EOF
    
    chmod 644 /etc/pxm-container-info
    echo -e "${GREEN}System information file created${NC}"
}

# Main execution
main() {
    check_root
    install_packages
    setup_claude_account
    setup_ssh_keys
    harden_ssh
    setup_firewall
    create_system_info
    
    echo -e "${GREEN}=== Container hardening complete! ===${NC}"
    echo -e "${GREEN}Summary:${NC}"
    echo -e "  - Claude service account: ${GREEN}active${NC}"
    echo -e "  - SSH key authentication: ${GREEN}enabled${NC}"
    echo -e "  - Root SSH login: ${RED}disabled${NC}"
    echo -e "  - Password authentication: ${RED}disabled${NC}"
    echo -e "  - Basic firewall: ${GREEN}active${NC}"
    echo
    echo -e "${YELLOW}Test connection with:${NC}"
    echo -e "  ssh claude@$(ip -4 addr show | grep inet | grep -v 127.0.0.1 | awk '{print $2}' | cut -d/ -f1 | head -1)"
}

# Run main function
main "$@"