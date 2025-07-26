# Infrastructure Automation Guide
## PXM Manager with Claude Service Account Integration

### Overview
This guide documents the complete infrastructure automation configuration for the BRad Method system, ensuring the PXM Manager agent has persistent access to the fully configured Proxmox environment.

## Current Infrastructure Configuration

### Proxmox Host (192.168.0.199)
- **Host User**: `pxm-admin` (SSH key authentication only)
- **Capabilities**: Limited sudo for PCT/QM commands only
- **Root SSH**: Disabled for security
- **Setup Script**: `.brad-core/scripts/proxmox-host-setup.sh` (already executed)

### Container Infrastructure
All containers are configured with standardized security:

| Container | ID | IP | Service Accounts | SSH Access | Security Level |
|-----------|----|----|-----------------|------------|----------------|
| lxc-files-1 | 116 | 192.168.0.116 | claude, root | Claude (Service Account) | Hardened |
| lxc-jellyfin-1 | 115 | 192.168.0.115 | claude, root | Claude (Service Account) | Hardened |
| lxc-docker-135 | 135 | 192.168.0.135 | claude, root | Claude (Service Account) | Hardened |

### Service Account Configuration
- **Username**: `claude`
- **Password**: `claude` (configurable)
- **Sudo Access**: `NOPASSWD:ALL`
- **SSH Authentication**: Key-based only
- **Purpose**: Automated infrastructure management

## Access Patterns for PXM Manager

### 1. Proxmox Host Operations
```bash
# List all containers
ssh pxm-admin@192.168.0.199 "sudo pct list"

# Execute commands in containers
ssh pxm-admin@192.168.0.199 "sudo pct exec 115 -- systemctl status jellyfin"

# Create new containers
ssh pxm-admin@192.168.0.199 "sudo pct create 120 local:vztmpl/debian-12.tmpl --hostname new-service --net0 name=eth0,bridge=vmbr0,ip=192.168.0.120/24"
```

### 2. Direct Container Management
```bash
# Service management via claude account
ssh claude@192.168.0.116 "sudo systemctl restart nginx"
ssh claude@192.168.0.115 "sudo systemctl status jellyfin"
ssh claude@192.168.0.135 "sudo docker ps"

# Package installation and updates
ssh claude@192.168.0.116 "sudo apt-get update && sudo apt-get install -y htop"

# Log monitoring and troubleshooting
ssh claude@192.168.0.115 "sudo journalctl -u jellyfin -f"
```

### 3. New Container Setup Automation
```bash
# Automatic hardening script execution
ssh pxm-admin@192.168.0.199 "sudo pct exec <new_container_id> -- bash -c 'curl -sSL <hardening_script_url> | bash'"

# Verify claude account setup
ssh claude@192.168.0.<new_container_id> "sudo whoami"
```

## Agent Configuration Reference

### PXM Manager Commands
The agent has these built-in commands available:

| Command | Purpose | Example Usage |
|---------|---------|---------------|
| `*test-connectivity` | Test Proxmox API connection | Auto-validates before operations |
| `*list-containers` | List all containers with status | Returns current infrastructure state |
| `*allocate` | Create new containers/VMs | Automated resource provisioning |
| `*harden-container` | Apply security hardening | Auto-runs on new containers |
| `*verify-security` | Check security compliance | Validates claude access and hardening |
| `*sync-notion` | Update Notion database | Real-time resource tracking |

### Notion Database Integration
- **Database ID**: `23cbf6e5-4d3b-81a3-ab7e-d413450cd07b`
- **Workspace ID**: `bd6eb337-4c7c-47c1-9321-5f8b7e2a1b4c`
- **Sync**: Real-time updates for all resource changes
- **Standard Metadata**: Automatically applied to all resources

## Automated Workflows

### Resource Allocation Workflow
1. **Requirements Analysis** - Parse project needs and validate capacity
2. **Resource Provisioning** - Create containers/VMs with PCT commands
3. **Security Configuration** - Apply hardening script and claude account setup
4. **Service Deployment** - Install services via claude account
5. **Documentation Update** - Sync all metadata to Notion database

### Container Hardening Process
1. Install sudo package (not default in Debian)
2. Create claude service account with sudo access
3. Configure SSH key authentication
4. Disable root SSH login
5. Set up basic firewall rules
6. Verify security configuration

## Security Architecture

```
Mac Studio (PXM Manager)
    ↓ SSH Key Auth
Proxmox Host (pxm-admin)
    ↓ PCT exec
Containers (claude user)
    ↓ Full sudo access
Services & Applications
```

### Security Benefits
- **No Root SSH**: Root login disabled on all systems
- **Limited Proxmox Access**: pxm-admin can only run PCT/QM commands
- **Key-Only Authentication**: Password authentication disabled
- **Service Account Isolation**: Dedicated claude account for automation
- **Audit Trail**: All actions logged with user accountability

## Persistent Agent Knowledge

### Resource Discovery
The PXM Manager automatically knows:
- Container naming pattern: `lxc-[service]-[container_id]`
- IP mapping rule: `192.168.0.[container_id]`
- Access method: `ssh claude@<ip>` for all containers
- Security level: All containers are hardened by default

### Infrastructure State
- **Proxmox Host**: Accessible via pxm-admin account
- **Container Access**: All containers have claude service account
- **Security Posture**: All systems are hardened and compliant
- **Documentation**: Real-time sync with Notion Resources database

### Automation Capabilities
The PXM Manager can autonomously:
1. **Provision Resources**: Create new containers/VMs via PCT
2. **Apply Security**: Automatically harden new containers
3. **Deploy Services**: Install and configure applications
4. **Monitor Status**: Check health and performance
5. **Update Documentation**: Sync changes to Notion

## Future Resource Creation

When the PXM Manager creates new resources, it will automatically:
1. Follow naming convention (lxc-[service]-[id])
2. Assign IP based on container ID pattern
3. Run container hardening script
4. Set up claude service account
5. Update Notion database with security metadata
6. Provide SSH access instructions

This ensures every new resource is immediately accessible and secure without manual intervention.

## Troubleshooting

### Common Issues
- **SSH Key Problems**: Verify key permissions (600 for private, 644 for public)
- **PCT Command Failures**: Check pxm-admin sudo permissions with `sudo -l`
- **Container Access Issues**: Verify claude account exists with `sudo pct exec <id> -- id claude`

### Emergency Access
- **Proxmox Console**: Available for all containers if SSH fails
- **Root Access**: Available via console only (SSH disabled)
- **Host Access**: Physical or IPMI access to Proxmox host

## Integration Points

### Notion Synchronization
- Resource creation → Update Resources database
- Status changes → Update resource status
- Security updates → Update security metadata
- Performance metrics → Update monitoring data

### GitHub Integration
- Repository creation → Trigger environment setup
- Release deployment → Update production resources
- Branch creation → Create development environments

This configuration ensures the PXM Manager has complete, persistent access to manage the infrastructure autonomously while maintaining security best practices.