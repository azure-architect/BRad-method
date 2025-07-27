#!/bin/bash
# Setup App Admin Group Script
# Purpose: Create app-admin group and configure proper permissions for claude user
# This allows claude to manage applications without needing sudo for every operation

set -e

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== App Admin Group Configuration Script ===${NC}"

# PXM Admin connection details
PXM_HOST="192.168.0.199"
PXM_USER="pxm-admin"

# Group configuration
APP_GROUP="app-admin"
APP_GROUP_GID="2000"  # Using a high GID to avoid conflicts

# List of containers to configure
CONTAINERS=(
    "115:lxc-jellyfin-1:192.168.0.115"
    "116:lxc-files-1:192.168.0.116"
    "135:lxc-docker-135:192.168.0.135"
)

# Function to setup group on a single container
setup_container_group() {
    local container_id=$1
    local container_name=$2
    local container_ip=$3
    
    echo -e "${YELLOW}Processing container ${container_id} (${container_name})...${NC}"
    
    # Execute commands via PCT from Proxmox host
    ssh ${PXM_USER}@${PXM_HOST} "sudo pct exec ${container_id} -- /bin/bash << 'EOF'
        # Create app-admin group if it doesn't exist
        if ! getent group ${APP_GROUP} > /dev/null 2>&1; then
            echo \"Creating ${APP_GROUP} group...\"
            # Try with specific GID first, fall back to auto-assigned if it fails
            if ! groupadd -g ${APP_GROUP_GID} ${APP_GROUP} 2>/dev/null; then
                echo \"GID ${APP_GROUP_GID} already taken, using auto-assigned GID...\"
                groupadd ${APP_GROUP}
            fi
        else
            echo \"Group ${APP_GROUP} already exists\"
        fi
        
        # Add claude user to app-admin group
        echo \"Adding claude to ${APP_GROUP} group...\"
        usermod -a -G ${APP_GROUP} claude
        
        # Create directories if they don't exist
        echo \"Creating directories if needed...\"
        mkdir -p /resources /opt/apps
        
        # Set group ownership and permissions for /resources
        echo \"Configuring /resources directory...\"
        chgrp -R ${APP_GROUP} /resources
        chmod -R 775 /resources
        # Set setgid bit so new files inherit the group
        chmod g+s /resources
        
        # Set group ownership and permissions for /opt/apps
        echo \"Configuring /opt/apps directory...\"
        mkdir -p /opt/apps
        chgrp -R ${APP_GROUP} /opt/apps
        chmod -R 775 /opt/apps
        # Set setgid bit so new files inherit the group
        chmod g+s /opt/apps
        
        # Create app-specific directories with proper permissions
        echo \"Creating app-specific directories...\"
        for dir in /opt/apps/bin /opt/apps/config /opt/apps/data /opt/apps/logs; do
            mkdir -p \$dir
            chgrp ${APP_GROUP} \$dir
            chmod 775 \$dir
            chmod g+s \$dir
        done
        
        # Set ACL if available for more granular control
        if command -v setfacl &> /dev/null; then
            echo \"Setting ACL permissions...\"
            setfacl -R -m g:${APP_GROUP}:rwx /resources /opt/apps
            setfacl -R -d -m g:${APP_GROUP}:rwx /resources /opt/apps
        fi
        
        # Verify configuration
        echo
        echo \"Verification:\"
        echo \"App-admin group info: \$(getent group ${APP_GROUP})\"
        echo \"Claude user info: \$(id claude)\"
        echo \"Claude groups: \$(groups claude | cut -d: -f2)\"
        echo \"Directory permissions:\"
        ls -ld /resources /opt/apps /opt/apps/* 2>/dev/null || true
        
        # Test write access without sudo
        echo
        echo \"Testing write access for claude user...\"
        sudo -u claude touch /resources/test-group-access.txt && echo \"✓ Write access to /resources confirmed\" && rm /resources/test-group-access.txt
        sudo -u claude touch /opt/apps/test-group-access.txt && echo \"✓ Write access to /opt/apps confirmed\" && rm /opt/apps/test-group-access.txt
EOF"
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓ Successfully configured app-admin group for container ${container_id}${NC}"
    else
        echo -e "${RED}✗ Failed to configure app-admin group for container ${container_id}${NC}"
        return 1
    fi
}

# Function to create sudoers configuration for limited sudo access
create_limited_sudo_config() {
    local container_id=$1
    
    echo -e "${BLUE}Creating limited sudo configuration...${NC}"
    
    ssh ${PXM_USER}@${PXM_HOST} "sudo pct exec ${container_id} -- /bin/bash << 'EOF'
        # Create sudoers configuration for app management
        cat > /etc/sudoers.d/claude-app-admin << 'SUDO_EOF'
# Claude app management permissions
# Service management (no password required)
claude ALL=(ALL) NOPASSWD: /bin/systemctl start *, /bin/systemctl stop *, /bin/systemctl restart *, /bin/systemctl reload *, /bin/systemctl status *
claude ALL=(ALL) NOPASSWD: /usr/sbin/service * start, /usr/sbin/service * stop, /usr/sbin/service * restart, /usr/sbin/service * reload, /usr/sbin/service * status

# Package management for app installations (no password required)
claude ALL=(ALL) NOPASSWD: /usr/bin/apt-get install -y *, /usr/bin/apt-get update
claude ALL=(ALL) NOPASSWD: /usr/bin/apt install -y *, /usr/bin/apt update

# Docker management (if applicable)
claude ALL=(ALL) NOPASSWD: /usr/bin/docker *, /usr/bin/docker-compose *

# Log viewing
claude ALL=(ALL) NOPASSWD: /usr/bin/journalctl *

# Network diagnostics
claude ALL=(ALL) NOPASSWD: /usr/bin/netstat *, /usr/sbin/ss *, /usr/bin/lsof -i *
SUDO_EOF
        
        chmod 440 /etc/sudoers.d/claude-app-admin
        echo \"Limited sudo configuration created\"
EOF"
}

# Main execution
main() {
    echo -e "${YELLOW}Configuring app-admin group on all containers...${NC}"
    echo -e "${BLUE}This setup will:${NC}"
    echo -e "  - Create '${APP_GROUP}' group for application management"
    echo -e "  - Add claude user to this group"
    echo -e "  - Set group permissions on /resources and /opt/apps"
    echo -e "  - Configure setgid for proper permission inheritance"
    echo -e "  - Create limited sudo rules for service management only"
    echo
    
    local success_count=0
    local failed_containers=()
    
    for container_info in "${CONTAINERS[@]}"; do
        IFS=':' read -r container_id container_name container_ip <<< "$container_info"
        
        echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
        
        if setup_container_group "${container_id}" "${container_name}" "${container_ip}"; then
            create_limited_sudo_config "${container_id}"
            ((success_count++))
        else
            failed_containers+=("${container_id}:${container_name}")
        fi
        
        echo
    done
    
    echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}=== App Admin Group Configuration Complete ===${NC}"
    echo
    echo -e "${GREEN}Summary:${NC}"
    echo -e "  - Containers processed: ${#CONTAINERS[@]}"
    echo -e "  - Successful: ${GREEN}${success_count}${NC}"
    echo -e "  - Failed: ${RED}${#failed_containers[@]}${NC}"
    
    if [ ${#failed_containers[@]} -gt 0 ]; then
        echo
        echo -e "${RED}Failed containers:${NC}"
        for container in "${failed_containers[@]}"; do
            echo -e "  - ${container}"
        done
    fi
    
    echo
    echo -e "${GREEN}Benefits of this approach:${NC}"
    echo -e "  ✓ Claude can manage apps without full sudo access"
    echo -e "  ✓ Files created by any app-admin member are group-accessible"
    echo -e "  ✓ Setgid ensures new files inherit proper group permissions"
    echo -e "  ✓ Limited sudo only for service management tasks"
    echo -e "  ✓ Better security through principle of least privilege"
    echo
    echo -e "${YELLOW}Usage examples:${NC}"
    echo -e "  # Claude can now manage files without sudo:"
    echo -e "  ssh claude@<container_ip> 'echo \"test\" > /resources/myfile.txt'"
    echo -e "  ssh claude@<container_ip> 'mkdir /opt/apps/myapp'"
    echo -e "  "
    echo -e "  # Service management still requires sudo but no password:"
    echo -e "  ssh claude@<container_ip> 'sudo systemctl restart nginx'"
    echo -e "  ssh claude@<container_ip> 'sudo docker ps'"
}

# Run main function
main "$@"