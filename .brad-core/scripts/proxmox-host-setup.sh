#!/bin/bash
# Proxmox Host SSH Setup Script
# Purpose: Configure SSH access for PXM Manager to run PCT commands

set -e

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== Proxmox Host SSH Configuration ===${NC}"

# Your Mac Studio SSH public key
SSH_KEY="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDeQ/s/Dh+fJVSRoMJiHqSkQUwWnI8qjGH9jcS4m8K+1lEmUaINOcTpkW5+tOz0uRnL/CVGoz1kho3qw1F6UrMGOjvzR8wAX9h7IjDpawXPrw9pcNiP20YyzCDpOrDIb1mXGGIPYXhCyMWfaIoGSvhoVuDc/w6EQmwzfWzgPOmLYjNIwQOyTkCxXPAXr+cNBCok/sTjtVrVPyaDwhKA/AhIFBAUzPqXccCvH6N++yyXV49g3N1DLRc8y9WE8exa1+xTtSNdoPqcBICl9Fi0ie0MSmoem6rmaorvHCIdzjcMOZcLXOAdKJOI+WEvUfyiC6UGiuHgqHWSYegYXq5N6MdbKUu3AsncD0Tgebonj1ezZrFdlxNI3jfnk3K68O6AoOV3DeeNF87MeGzgKKqV7Ahs6Twbo4eyCOV1hdKW+lH625QFDhA/WZW+A3xLetW9klvqhcYweWjuIcFvmave/OPQHgoa6s2VR1yWEZcHFttGldF5jX4bjH/4kpX2EumHgmLgv85kqseQkgf5yLYj90yvcuYtnF527a+eXgoNAk5S0g+ACue8EiRpSEwuW6XYL+M2GHLARzeUpaNCiSAACIPIK/TV9WBD02PvOAXyT67FprObCSQz6llsSD+S4ZRF9djck7VTUWh1grlkyy1fNo5ftlusGgjjx7iFBxcJ7ZzEIw== admin@locallyknown.pro"

# Management user for PXM Manager
PXM_USER="pxm-admin"
PXM_PASS="pxm-secure-2024"  # Should be changed

echo -e "${YELLOW}Step 1: Installing SSH key for root (temporary)${NC}"
mkdir -p /root/.ssh
chmod 700 /root/.ssh
echo "$SSH_KEY" >> /root/.ssh/authorized_keys
chmod 600 /root/.ssh/authorized_keys
echo -e "${GREEN}✓ SSH key added for root${NC}"

echo -e "${YELLOW}Step 2: Creating PXM management account${NC}"
# Create pxm-admin user if it doesn't exist
if ! id "$PXM_USER" &>/dev/null; then
    useradd -m -s /bin/bash "$PXM_USER"
    echo "$PXM_USER:$PXM_PASS" | chpasswd
    echo -e "${GREEN}✓ Created user $PXM_USER${NC}"
else
    echo -e "${GREEN}✓ User $PXM_USER already exists${NC}"
fi

# Add to sudo group (Proxmox uses sudo group)
usermod -aG sudo "$PXM_USER"

# Configure passwordless sudo for PCT commands
cat > /etc/sudoers.d/$PXM_USER << EOF
# PXM Manager administrative access
$PXM_USER ALL=(ALL) NOPASSWD: /usr/sbin/pct, /usr/sbin/qm, /usr/sbin/pvesh, /usr/sbin/pvesm
$PXM_USER ALL=(ALL) NOPASSWD: /usr/bin/ssh
EOF
chmod 440 /etc/sudoers.d/$PXM_USER

echo -e "${YELLOW}Step 3: Setting up SSH keys for PXM admin${NC}"
mkdir -p /home/$PXM_USER/.ssh
chmod 700 /home/$PXM_USER/.ssh
echo "$SSH_KEY" > /home/$PXM_USER/.ssh/authorized_keys
chmod 600 /home/$PXM_USER/.ssh/authorized_keys
chown -R $PXM_USER:$PXM_USER /home/$PXM_USER/.ssh
echo -e "${GREEN}✓ SSH key configured for $PXM_USER${NC}"

echo -e "${YELLOW}Step 4: Updating SSH configuration${NC}"
# Backup current SSH config
cp /etc/ssh/sshd_config /etc/ssh/sshd_config.backup.$(date +%Y%m%d)

# Check if we need to update SSH config
if grep -q "^PermitRootLogin yes" /etc/ssh/sshd_config; then
    echo -e "${YELLOW}Disabling root SSH login...${NC}"
    sed -i 's/^PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config
elif ! grep -q "^PermitRootLogin" /etc/ssh/sshd_config; then
    echo "PermitRootLogin no" >> /etc/ssh/sshd_config
fi

# Ensure key authentication is enabled
sed -i 's/^#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config
sed -i 's/^PubkeyAuthentication no/PubkeyAuthentication yes/' /etc/ssh/sshd_config

echo -e "${GREEN}✓ SSH configuration updated${NC}"

echo -e "${YELLOW}Step 5: Restarting SSH service${NC}"
systemctl restart sshd
echo -e "${GREEN}✓ SSH service restarted${NC}"

echo -e "${GREEN}=== Proxmox Host Configuration Complete! ===${NC}"
echo
echo -e "${GREEN}Summary:${NC}"
echo -e "  - PXM admin account: ${GREEN}$PXM_USER${NC}"
echo -e "  - SSH key authentication: ${GREEN}enabled${NC}"
echo -e "  - Root SSH login: ${RED}disabled${NC}"
echo -e "  - PCT/QM commands: ${GREEN}sudo enabled${NC}"
echo
echo -e "${YELLOW}Test connection:${NC}"
echo -e "  ssh $PXM_USER@$(hostname -I | awk '{print $1}')"
echo
echo -e "${YELLOW}PXM Manager can now run PCT commands via:${NC}"
echo -e "  ssh $PXM_USER@192.168.0.199 'sudo pct exec 115 -- command'"
echo
echo -e "${RED}IMPORTANT:${NC} Change the $PXM_USER password after first login!"