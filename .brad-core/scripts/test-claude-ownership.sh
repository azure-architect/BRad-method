#!/bin/bash
# Test Claude Ownership Script
# Purpose: Test ownership configuration on a single container

set -e

# Colors for output  
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== Test Claude Ownership Configuration ===${NC}"

# PXM Admin connection details
PXM_HOST="192.168.0.199"
PXM_USER="pxm-admin"

# Test on container 116 (lxc-files-1) first
TEST_CONTAINER_ID="116"
TEST_CONTAINER_NAME="lxc-files-1"
TEST_CONTAINER_IP="192.168.0.116"

echo -e "${YELLOW}Testing on container ${TEST_CONTAINER_ID} (${TEST_CONTAINER_NAME})...${NC}"
echo

# First, check current state
echo -e "${YELLOW}Current state:${NC}"
ssh ${PXM_USER}@${PXM_HOST} "sudo pct exec ${TEST_CONTAINER_ID} -- bash -c '
    echo \"Checking if directories exist:\"
    ls -ld /resources 2>/dev/null || echo \"/resources does not exist\"
    ls -ld /opt 2>/dev/null || echo \"/opt does not exist\"
    echo
    echo \"Checking claude user:\"
    id claude 2>/dev/null || echo \"claude user does not exist\"
'"

echo
echo -e "${YELLOW}Applying ownership configuration...${NC}"

# Apply ownership
ssh ${PXM_USER}@${PXM_HOST} "sudo pct exec ${TEST_CONTAINER_ID} -- /bin/bash << 'EOF'
    # Create directories if they don't exist
    echo \"Creating directories if needed...\"
    mkdir -p /resources /opt
    
    # Set ownership to claude user
    echo \"Setting ownership to claude...\"
    chown -R claude:claude /resources
    chown -R claude:claude /opt
    
    # Set proper permissions
    echo \"Setting permissions...\"
    chmod 755 /resources /opt
    
    # Create a test file to verify write access
    echo \"Creating test file...\"
    sudo -u claude touch /resources/test-claude-access.txt
    sudo -u claude touch /opt/test-claude-access.txt
    
    echo
    echo \"Final state:\"
    ls -ld /resources /opt
    ls -la /resources/test-claude-access.txt
    ls -la /opt/test-claude-access.txt
EOF"

echo
echo -e "${GREEN}✓ Test completed${NC}"
echo
echo -e "${YELLOW}To verify from the container directly:${NC}"
echo -e "  ssh claude@${TEST_CONTAINER_IP} 'ls -ld /resources /opt'"
echo
echo -e "${YELLOW}If successful, run the full script:${NC}"
echo -e "  ./.brad-core/scripts/set-claude-ownership.sh"