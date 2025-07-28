# Agent Activation System

## Overview

The BRad Method Agent Activation System provides dynamic switching between specialized AI agents through Claude Code hooks. Each agent has specific capabilities and expertise areas.

## Usage

### Available Commands

- `@list-agents` - Show all available agents with descriptions
- `@agent-id` - Activate a specific agent (e.g., `@brad-master`)
- `@status` - Check which agent is currently active
- `@deactivate` - Return to Claude Code default mode

### Example Workflow

```bash
# List available agents
@list-agents

# Activate Brad Master for project orchestration
@brad-master

# Check current status
@status

# Work with the active agent...

# Deactivate and return to Claude Code
@deactivate
```

## Available Agents

1. **🎯 BRad Master** (`@brad-master`)
   - Master Project Orchestrator & BRad Method Expert
   - Use for comprehensive project orchestration, Notion integration, or running any BRad Method tasks

2. **🐙 GitHub Agent** (`@github-agent`)
   - GitHub Repository Specialist
   - Use for all GitHub repository operations, code management, and CI/CD tasks

3. **📝 Notion Agent** (`@notion-agent`)
   - Notion Database Specialist
   - Use for all Notion database operations, queries, and synchronization tasks

4. **🖥️ PXM Manager** (`@pxm-manager`)
   - Proxmox Infrastructure Resource Manager
   - Use for all Proxmox operations, infrastructure provisioning, resource allocation

5. **📋 Project Manager Agent** (`@project-manager-agent`)
   - Project Coordination Specialist
   - Use for project orchestration, timeline management, and cross-system coordination

## Implementation Details

### Hook System
- **Trigger**: `UserPromptSubmit` hook with `@*` matcher
- **Script**: `.claude/hooks/agent_activation.py`
- **State Management**: `.claude/agent_state.json`

### Agent Discovery
- Agents defined in `.brad-core/agents/*.md` files
- YAML configuration blocks within markdown files
- Dynamic parsing and registration

### Session Persistence
- Agent state persists across Claude Code sessions
- Automatic state restoration on hook execution
- Clean deactivation when switching agents

## Configuration

Agents are configured in `.brad-core/agents/` with this structure:

```yaml
agent:
  name: Agent Name
  id: agent-id
  title: Agent Description
  icon: 🤖
  whenToUse: When to use this agent

persona:
  role: Primary Role
  identity: Detailed identity description

commands:
  - command-name: Command description
```

## Troubleshooting

### Common Issues

1. **Agent not found**: Check agent ID matches filename
2. **YAML parse errors**: Validate YAML syntax in agent files
3. **Hook not triggering**: Verify `@` prefix in commands
4. **State persistence**: Check `.claude/agent_state.json` exists

### Debug Commands

```bash
# Test agent discovery
python .claude/hooks/agent_activation.py "@list-agents"

# Test specific activation
python .claude/hooks/agent_activation.py "@brad-master"

# Check current state
python .claude/hooks/agent_activation.py "@status"
```