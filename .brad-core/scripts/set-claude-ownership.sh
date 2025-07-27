#!/bin/bash
# Set Claude Ownership Script
# Purpose: Grant claude user ownership of /resources and /opt directories on all containers

set -e

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== Claude Ownership Configuration Script ===${NC}"

# PXM Admin connection details
PXM_HOST="192.168.0.199"
PXM_USER="pxm-admin"

# List of containers to configure
CONTAINERS=(
    "115:lxc-jellyfin-1:192.168.0.115"
    "116:lxc-files-1:192.168.0.116"
    "135:lxc-docker-135:192.168.0.135"
)

# Function to set ownership on a single container
set_container_ownership() {
    local container_id=$1
    local container_name=$2
    local container_ip=$3
    
    echo -e "${YELLOW}Processing container ${container_id} (${container_name})...${NC}"
    
    # Create directories if they don't exist and set ownership
    echo -e "Creating directories and setting ownership..."
    
    # Execute commands via PCT from Proxmox host
    ssh ${PXM_USER}@${PXM_HOST} "sudo pct exec ${container_id} -- /bin/bash << 'EOF'
        # Create directories if they don't exist
        mkdir -p /resources /opt
        
        # Set ownership to claude user
        chown -R claude:claude /resources
        chown -R claude:claude /opt
        
        # Set proper permissions
        chmod 755 /resources /opt
        
        # Verify ownership
        echo \"Ownership verification:\"
        ls -ld /resources /opt
EOF"
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓ Successfully configured ownership for container ${container_id}${NC}"
    else
        echo -e "${RED}✗ Failed to configure ownership for container ${container_id}${NC}"
        return 1
    fi
}

# Function to verify claude user exists on container
verify_claude_user() {
    local container_id=$1
    
    echo -e "Verifying claude user exists..."
    ssh ${PXM_USER}@${PXM_HOST} "sudo pct exec ${container_id} -- id claude" >/dev/null 2>&1
    
    if [ $? -ne 0 ]; then
        echo -e "${RED}✗ Claude user does not exist on container ${container_id}${NC}"
        echo -e "${YELLOW}Run the container hardening script first to create claude user${NC}"
        return 1
    fi
    
    return 0
}

# Main execution
main() {
    echo -e "${YELLOW}Configuring ownership on all containers...${NC}"
    echo
    
    local success_count=0
    local failed_containers=()
    
    for container_info in "${CONTAINERS[@]}"; do
        IFS=':' read -r container_id container_name container_ip <<< "$container_info"
        
        echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
        
        # First verify claude user exists
        if verify_claude_user "${container_id}"; then
            # Set ownership
            if set_container_ownership "${container_id}" "${container_name}" "${container_ip}"; then
                ((success_count++))
            else
                failed_containers+=("${container_id}:${container_name}")
            fi
        else
            failed_containers+=("${container_id}:${container_name}")
        fi
        
        echo
    done
    
    echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}=== Ownership Configuration Complete ===${NC}"
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
    echo -e "${YELLOW}Verification commands:${NC}"
    echo -e "  Check ownership: ssh ${PXM_USER}@${PXM_HOST} 'sudo pct exec <container_id> -- ls -ld /resources /opt'"
    echo -e "  Check from container: ssh claude@<container_ip> 'ls -ld /resources /opt'"
}

# Run main function
main "$@"