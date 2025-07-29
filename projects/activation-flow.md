# Brad Method Agent Activation Flow Documentation

## Current Hook-Based System

### Overview
The Brad Method uses a Python hook system that intercepts user prompts starting with `@` to activate specific agents. The system is designed to work within Claude Code's hook architecture.

### Components

#### 1. Hook Configuration (`.claude/settings.json`)
```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "matcher": "@*",
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/agent_activation_v2.py"
          }
        ]
      }
    ]
  }
}
```

#### 2. Agent Registry (`agent_activation_v2.py`)
- **Location**: `.claude/hooks/agent_activation_v2.py`
- **Purpose**: Discovers, parses, and manages agent activation
- **Key Functions**:
  - `discover_agents()`: Scans `.brad-core/agents/` for agent files
  - `_parse_agent_file()`: Extracts YAML configuration from Markdown
  - `activate_agent()`: Sets active agent and saves state
  - `handle_agent_command()`: Processes user activation commands

#### 3. Agent State Management
- **State File**: `.claude/agent_state.json`
- **Format**:
  ```json
  {
    "active_agent": "agent-id",
    "last_updated": "/path/to/brad-method"
  }
  ```

### Activation Flow Steps

#### Step 1: User Input Detection
1. User types command starting with `@` (e.g., `@master`)
2. Claude Code's `UserPromptSubmit` hook triggers
3. Pattern matcher `@*` matches the input
4. Hook executes `python .claude/hooks/agent_activation_v2.py`

#### Step 2: Command Processing
1. Python script reads user input from stdin
2. `handle_agent_command()` parses the command
3. Command types processed:
   - `@list-agents`: Show all available agents
   - `@agent-id`: Activate specific agent
   - `@status`: Show currently active agent
   - `@deactivate`: Clear active agent

#### Step 3: Agent Discovery and Parsing
1. `AgentRegistry.discover_agents()` scans `.brad-core/agents/`
2. For each `.md` file found:
   - Extract YAML blocks using regex pattern
   - Parse agent configuration (name, id, commands, etc.)
   - Build agent registry dictionary

#### Step 4: Agent Activation
1. `activate_agent(agent_id)` called with parsed agent ID
2. Agent state updated in memory and saved to `.claude/agent_state.json`
3. Activation response generated with agent info and commands
4. Response printed to stdout for Claude Code to display

#### Step 5: Response Generation
```python
response = f"{agent_data['icon']} **{agent_data['name']} Activated**\n\n"
response += f"**Role:** {agent_data['persona'].get('role', 'Agent')}\n"
# Add available commands
# Add deactivation instructions
```

### Agent File Structure
Each agent file follows this pattern:
```markdown
# Agent Name

```yaml
activation-instructions:
  - STEP 1: Read THIS ENTIRE FILE
  - STEP 2: Adopt the persona defined below
  - STEP 3: Greet user as Agent and mention capabilities

agent:
  name: Agent Name
  id: agent-id
  title: Agent Title
  icon: 🔸
  whenToUse: Usage description

persona:
  role: Role Description
  identity: Identity Description
  core_principles:
    - Principle 1
    - Principle 2

commands:
  - command1: Description
  - command2: Description
```

### Command Aliases
The system supports simplified agent names:
```python
simplified_map = {
    "master": "brad-master",
    "notion": "notion-agent",
    "github": "github-agent",
    "idea": "idea-man",
    "project": "project-manager-agent",
    "pxm": "pxm-master",
    "video": "video-ingestion"
}
```

## Issues with Current System

### 1. Hook Output Limitation
- **Problem**: Hook output doesn't change Claude's behavior/persona
- **Impact**: Agents are "activated" in state but Claude doesn't adopt persona
- **Root Cause**: Claude Code architecture doesn't support dynamic persona switching

### 2. Context Isolation
- **Problem**: Hook runs in separate process from Claude
- **Impact**: Agent activation messages display but persona change doesn't occur
- **Root Cause**: Hook cannot modify Claude's system prompt or behavior

### 3. State Tracking vs Behavior
- **Problem**: State tracking works but behavior change doesn't
- **Impact**: System shows agent as "active" but Claude responds as default
- **Root Cause**: Disconnect between state management and AI behavior

### 4. Debug Information
Debug logging shows the system works:
```
Received command: '@master'
Agent 'brad-master' activated successfully
Response generated and printed
```

But Claude doesn't receive or act on the persona change.

## Current Workarounds

### 1. Manual Agent Loading
Users can manually copy/paste agent definitions, but this defeats the automation purpose.

### 2. Explicit Instructions
Include agent persona in conversation, but loses the seamless switching experience.

### 3. Hook State Checking
Claude could theoretically check `.claude/agent_state.json` and adopt persona based on file content, but this requires explicit programming.

## Requirements for BMAD Conversion

### 1. Self-Contained Activation
- Agents must activate through content loading, not external hooks
- Full agent definition and resources embedded in single file
- Activation instructions that Claude can follow directly

### 2. Immediate Context Switch
- Agent bundle loading must trigger immediate persona adoption
- No dependency on external state files or hook systems
- Clear activation confirmation built into the bundle

### 3. Resource Embedding
- All dependencies (tasks, workflows, templates) embedded in bundle
- No external file references that could break
- Optimized for Claude's context window

### 4. Simple Loading Mechanism
- Easy command or instruction to load agent bundle
- No technical barriers for users
- Works reliably across different Claude interfaces

## Success Criteria for New System

1. **Immediate Activation**: Agent persona adopted instantly when bundle loaded
2. **No External Dependencies**: Everything needed contained in bundle file
3. **Clear Feedback**: Obvious confirmation when agent is active
4. **Reliable Switching**: Consistent behavior across sessions
5. **Preserved Functionality**: All current agent capabilities maintained

## Migration Path

1. **Convert Agents**: Transform current `.md` files to BMAD bundle format
2. **Embed Resources**: Include all dependencies within bundle files
3. **Remove Hooks**: Eliminate dependency on hook system
4. **Simple Loading**: Create straightforward bundle loading instructions
5. **Test Thoroughly**: Ensure all functionality works as expected