# PXM Infrastructure Scripts

This directory contains automation scripts for Proxmox infrastructure management.

## Scripts

### container-hardening.sh
**Purpose:** Secure new and existing containers with standard configuration
- Installs sudo package (required for Debian containers)
- Creates claude service account with passwordless sudo
- Configures SSH key authentication
- Disables root SSH login
- Sets up basic firewall rules
- Creates system information file

**Usage:**
```bash
# For new containers (via PCT from Proxmox host)
ssh pxm-admin@192.168.0.199 "sudo pct exec <container_id> -- bash" < container-hardening.sh

# For existing containers (with root access)
ssh root@<container_ip> 'bash -s' < container-hardening.sh
```

### proxmox-host-setup.sh
**Purpose:** Configure Proxmox host for secure PXM Manager access
- Creates pxm-admin user with limited sudo (PCT/QM commands only)
- Installs SSH keys for key-based authentication
- Disables root SSH login for security
- Configures SSH hardening settings

**Usage:**
```bash
# Run on Proxmox host as root
./proxmox-host-setup.sh
```

**Important:** This script must be run manually on the Proxmox host as it changes SSH configuration.

## Security Model

```
┌─────────────────────┐
│   Mac Studio        │
│  (PXM Manager)      │
└──────────┬──────────┘
           │ SSH Key Auth
           ▼
┌─────────────────────┐
│  Proxmox Host       │
│  pxm-admin user     │◄── Limited sudo (PCT/QM only)
└──────────┬──────────┘
           │ PCT exec
           ▼
┌─────────────────────┐
│  Containers         │
│  claude user        │◄── Full sudo access
└─────────────────────┘
```

## Automated Workflow

1. **Initial Setup** (one-time)
   - Run `proxmox-host-setup.sh` on Proxmox host
   - Creates pxm-admin account with SSH key access

2. **New Container Creation**
   - PXM Manager creates container via API or PCT
   - Automatically runs `container-hardening.sh`
   - Container ready with claude service account

3. **Container Management**
   - PXM Manager SSHs to containers as claude
   - Full sudo access for all management tasks
   - No root login required

## Environment Variables

Scripts expect these to be available:
- `SSH_KEY`: Your Mac Studio public SSH key (embedded in scripts)
- `CLAUDE_USER`: Service account name (default: claude)
- `CLAUDE_PASS`: Service account password (default: claude)

## Notes

- Always backup SSH configurations before running setup scripts
- Test SSH access after running scripts to ensure connectivity
- Change default passwords after initial setup
- Keep scripts updated with latest security practices