# PXM Manager SSH Access Setup Guide

## Overview
This guide establishes secure SSH access for the PXM Manager to control Proxmox infrastructure without requiring root access.

## Architecture

```
Mac Studio (Claude/PXM Manager)
    ↓ SSH Key Auth
Proxmox Host (192.168.0.199)
    - pxm-admin user (PCT/QM commands)
    ↓ PCT exec
Containers (115, 116, 135, etc.)
    - claude user (sudo access)
```

## Setup Process

### 1. Proxmox Host Configuration

**Manual Step Required:** Copy and run this on your Proxmox host as root:

```bash
# Download and execute the setup script
wget https://raw.githubusercontent.com/[your-repo]/brad-method/.brad-core/scripts/proxmox-host-setup.sh
# OR copy the script manually
chmod +x proxmox-host-setup.sh
./proxmox-host-setup.sh
```

This script will:
- Add your Mac Studio SSH key to root (temporarily)
- Create `pxm-admin` user with limited sudo for PCT/QM commands
- Configure SSH key authentication for pxm-admin
- Disable root SSH login for security
- Restart SSH service

### 2. Test Proxmox Host Access

From your Mac Studio:
```bash
# Test pxm-admin access
ssh pxm-admin@192.168.0.199

# Test PCT command execution
ssh pxm-admin@192.168.0.199 "sudo pct list"
```

### 3. Container Hardening (New Containers)

When creating new containers, run the hardening script via PCT:

```bash
# Example for new container 120
ssh pxm-admin@192.168.0.199 "sudo pct exec 120 -- bash -c 'wget -qO- https://raw.githubusercontent.com/[your-repo]/brad-method/.brad-core/scripts/container-hardening.sh | bash'"
```

Or if you have the script locally:
```bash
# Copy script to Proxmox host first
scp .brad-core/scripts/container-hardening.sh pxm-admin@192.168.0.199:/tmp/

# Execute in container
ssh pxm-admin@192.168.0.199 "sudo pct exec 120 -- bash < /tmp/container-hardening.sh"
```

### 4. Container Hardening (Existing Containers)

For containers where you still have root access:

```bash
# Direct execution
ssh root@192.168.0.116 'bash -s' < .brad-core/scripts/container-hardening.sh
```

## Access Methods After Setup

### Proxmox Host Operations
```bash
# List containers
ssh pxm-admin@192.168.0.199 "sudo pct list"

# Execute commands in containers
ssh pxm-admin@192.168.0.199 "sudo pct exec 115 -- systemctl status jellyfin"

# Create new container
ssh pxm-admin@192.168.0.199 "sudo pct create 120 local:vztmpl/debian-12-standard_12.0-1_amd64.tar.zst --hostname test --password test123"
```

### Container Operations
```bash
# Direct container access via claude account
ssh claude@192.168.0.116 "sudo apt-get update"
ssh claude@192.168.0.115 "sudo systemctl restart jellyfin"
ssh claude@192.168.0.135 "sudo docker ps"
```

## Security Benefits

1. **No Root SSH Access**: Root login disabled on all systems
2. **Limited Sudo**: pxm-admin can only run PCT/QM commands
3. **Key-Only Auth**: Password authentication disabled
4. **Service Accounts**: Dedicated accounts for automation
5. **Audit Trail**: All actions logged with user accountability

## Troubleshooting

### SSH Key Not Working
```bash
# Check key permissions
ls -la ~/.ssh/id_rsa*
# Should be 600 for private key, 644 for public

# Verify key on remote
ssh pxm-admin@192.168.0.199 "cat ~/.ssh/authorized_keys"
```

### PCT Commands Failing
```bash
# Check sudo permissions
ssh pxm-admin@192.168.0.199 "sudo -l"
# Should show PCT/QM commands allowed
```

### Container Access Issues
```bash
# Verify claude account exists
ssh pxm-admin@192.168.0.199 "sudo pct exec 116 -- id claude"
```

## Integration with PXM Manager

The PXM Manager can now:
1. Execute PCT commands on Proxmox host via pxm-admin
2. Run commands in containers via claude account
3. Create and configure new containers with automatic hardening
4. Manage services without root access

## Next Steps

1. Run `proxmox-host-setup.sh` on your Proxmox host
2. Test access with `ssh pxm-admin@192.168.0.199`
3. Update any existing containers with the hardening script
4. Configure new containers to run hardening automatically

This setup provides secure, automated infrastructure management while following security best practices.