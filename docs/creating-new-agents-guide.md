# Creating New Brad Method Agents: Complete Guide

## Overview

This document provides a step-by-step guide for creating new Brad Method agents, including both the legacy hook-based system and the modern BMAD (Brad Method Agent Definition) bundle format.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Agent Creation Process](#agent-creation-process)
3. [File Structure Requirements](#file-structure-requirements)
4. [Bundle Creation](#bundle-creation)
5. [Activation System Integration](#activation-system-integration)
6. [Testing and Validation](#testing-and-validation)
7. [Best Practices](#best-practices)
8. [Troubleshooting](#troubleshooting)

## Prerequisites

### Required Knowledge
- Understanding of YAML syntax
- Familiarity with Brad Method architecture
- Basic understanding of Claude Code hooks system
- Knowledge of the target domain/API integrations

### Required Files Access
- `.brad-core/agents/` directory for agent definitions
- `.brad-core/bundles/` directory for bundle files
- `.claude/hooks/agent_activation_v2.py` for activation system
- `projects/agent-inventory.yaml` for agent registry

### Template Files
- `projects/activation-template.yaml` - Standard activation template
- `projects/bundle-format-spec.md` - Bundle format specification

## Agent Creation Process

### Step 1: Define Agent Concept

Before creating any files, clearly define:

1. **Agent Purpose**: What specific problem does this agent solve?
2. **Target Domain**: What APIs, databases, or systems will it work with?
3. **Core Capabilities**: What are the 5-10 main functions?
4. **Integration Points**: How does it connect with existing Brad Method agents?

**Example from DummySearch Agents:**
- **Purpose**: Extract market intelligence from Reddit discussions
- **Domain**: Reddit API + PostgreSQL database
- **Capabilities**: Problem detection, audience analysis, solution mapping
- **Integration**: Works with existing database and API infrastructure

### Step 2: Create Agent Definition File

Create the agent definition file in `.brad-core/agents/{agent-id}.md`:

```yaml
# Agent Name

```yaml
activation-instructions:
  - STEP 1: Read this entire file - it contains your complete persona definition
  - STEP 2: Adopt the {Agent Role} persona
  - STEP 3: Execute the startup greeting exactly as specified
  - STEP 4: Initialize all commands and prepare dependency access
  - STEP 5: STAY IN CHARACTER until explicitly told to exit
  - CRITICAL: The persona.customization field ALWAYS overrides default behaviors
  - IMPORTANT: Only load specific dependencies when user requests them via commands
  - USER INTERACTION: Present all options as numbered lists for easy selection

agent:
  name: Agent Name
  id: agent-id
  title: Agent Title
  icon: 🔍
  whenToUse: Description of when to use this agent

persona:
  role: Agent Role
  identity: Detailed identity description
  core_principles:
    - Principle 1
    - Principle 2
    - Process user requests with NLP and relate to available commands
  customization: |
    Detailed customization instructions that override default behaviors.
    This section is critical for defining agent-specific behavior patterns.

commands:
  - command-name: Description of what this command does
  - help: Show these listed commands in a numbered list
  - exit: Exit agent mode (confirm)

startup:
  greeting: |
    🔍 **Agent Name Activated**
    
    **Role:** Agent Role
    **Identity:** Agent Identity
    
    Detailed greeting message explaining capabilities.
    
    **Available Commands:**
    1. command1 - Description
    2. command2 - Description
    3. help - Show all commands
    
    Type a command name or number to execute.
```

### Step 3: Create BMAD Bundle File

Create the comprehensive bundle file in `.brad-core/bundles/{agent-id}.bundle.txt`:

#### Bundle Structure Template

```markdown
# Web Agent Bundle Instructions

[Standard bundle header with navigation instructions]

---

==================== START: .brad-core/agents/{agent-id}.md ====================
# Agent Name

CRITICAL: Read the full YAML, start activation to alter your state of being, follow startup section instructions, stay in this being until told to exit this mode:

```yaml
[Complete agent YAML configuration]
```
==================== END: .brad-core/agents/{agent-id}.md ====================

==================== START: .brad-core/tasks/{task-name}.md ====================
[Task definition with parameters, steps, and outputs]
==================== END: .brad-core/tasks/{task-name}.md ====================

==================== START: .brad-core/workflows/{workflow-name}.yaml ====================
[Workflow definition with steps and dependencies]
==================== END: .brad-core/workflows/{workflow-name}.yaml ====================

==================== START: .brad-core/templates/{template-name}.yaml ====================
[Template definitions for reports and outputs]
==================== END: .brad-core/templates/{template-name}.yaml ====================

==================== START: .brad-core/data/{data-name}.md ====================
[Data schemas, patterns, and reference information]
==================== END: .brad-core/data/{data-name}.md ====================

---

You have now loaded the complete {Agent Name} bundle. Execute the startup sequence and begin operating as {Agent Name}. Stay in character until explicitly told to exit agent mode.
```

#### Key Bundle Components

1. **Tasks**: Define specific operations the agent can perform
2. **Workflows**: Multi-step processes that coordinate multiple tasks
3. **Templates**: Output formats for reports and responses
4. **Data**: Schemas, patterns, and reference information
5. **Integrations**: API configurations and connection details

### Step 4: Update Activation System

#### 4.1 Add Aliases to Activation Hook

Edit `.claude/hooks/agent_activation_v2.py`:

```python
# In the alias_map section (around line 163):
alias_map = {
    "existing-agents": "aliases",
    "new-agent-id": "short-alias",
}

# In the simplified_map section (around line 205):
simplified_map = {
    "existing-aliases": "existing-agent-ids",
    "short-alias": "new-agent-id",
}
```

#### 4.2 Update Agent Inventory

Edit `projects/agent-inventory.yaml`:

```yaml
agents:
  # ... existing agents ...
  
  new-agent-id:
    id: new-agent-id
    name: Agent Name
    title: Agent Title
    icon: 🔍
    file_path: .brad-core/agents/new-agent-id.md
    whenToUse: Description of when to use this agent
    role: Agent Role
    identity: Agent Identity Description
    commands:
      - name: command1
        params: parameter description
        description: Command description
      - name: help
        params: none
        description: Show available commands
    dependencies:
      databases:
        database_name:
          host: hostname
          port: port
          tables:
            - table1
            - table2
      integrations:
        - api1
        - api2
      data_sources:
        - source1
        - source2
```

### Step 5: Environment Configuration

If your agent requires specific database or API configurations:

#### 5.1 Update Environment Variables

Edit `.env` file:

```bash
# Agent-specific configuration
AGENT_API_KEY=your_api_key
AGENT_DATABASE_URL=connection_string
```

#### 5.2 Update Database Configuration

If using custom databases, update `src/database.py`:

```python
# Add environment-specific database connections
if ENVIRONMENT == "production":
    AGENT_DB_HOST = os.getenv("AGENT_PROD_HOST", "default_host")
else:
    AGENT_DB_HOST = os.getenv("AGENT_DEV_HOST", "localhost")
```

## File Structure Requirements

### Required Directory Structure

```
.brad-core/
├── agents/
│   ├── existing-agent.md
│   └── new-agent-id.md          # Step 2: Agent definition
├── bundles/
│   ├── existing-agent.bundle.txt
│   └── new-agent-id.bundle.txt  # Step 3: Complete bundle
└── tasks/
    └── agent-specific-task.md

.claude/
└── hooks/
    └── agent_activation_v2.py   # Step 4.1: Add aliases

projects/
├── agent-inventory.yaml         # Step 4.2: Registry update
├── activation-template.yaml     # Reference template
└── bundle-format-spec.md        # Bundle format guide

src/
└── database.py                  # Step 5.2: DB config (if needed)

.env                             # Step 5.1: Environment vars (if needed)
```

### File Naming Conventions

- **Agent ID**: Use kebab-case (e.g., `reddit-youtube-agent`)
- **File Names**: Match agent ID exactly
- **Aliases**: Use short, memorable names (e.g., `youtube`, `reddit`)
- **Bundle Sections**: Use full path format (e.g., `.brad-core/tasks/task-name.md`)

## Bundle Creation

### Task Definitions

Create task files with this structure:

```markdown
# Task Name

## Overview
Brief description of what this task accomplishes.

## Task Parameters
```yaml
task:
  name: task-name
  type: task-type
  category: task-category
  
inputs:
  parameter1:
    type: string
    description: Parameter description
    required: true
    default: default_value

outputs:
  result:
    type: object
    structure:
      - field1: type
      - field2: type
```

## Execution Steps

1. **Step 1 Name**
   - Detailed description of what happens
   - Technical implementation notes
   - Expected outcomes

2. **Step 2 Name**
   - Continue with clear, actionable steps
   - Include error handling considerations
```

### Workflow Definitions

Create workflow YAML files:

```yaml
name: workflow-name
description: Workflow description
version: 1.0.0

triggers:
  - manual: User initiated workflow
  - scheduled: Automated triggers

inputs:
  input1:
    type: string
    required: true
    description: Input description

steps:
  - id: step1
    task: task-name
    description: Step description
    config:
      parameter: value
    outputs:
      - output_name
    
  - id: step2
    task: another-task
    depends_on: step1
    config:
      input: "{{step1.output_name}}"

outputs:
  final_result:
    type: object
    description: Final workflow output
```

### Template Definitions

Create output templates:

```yaml
name: template-name
description: Template for specific output type
version: 1.0.0

sections:
  - header:
      title: "{{title}}"
      date: "{{date}}"
      
  - content:
      title: "Main Content"
      subsections:
        - section1:
            title: "Section Title"
            content: "{{variable_content}}"
            
formatting:
  styles:
    - headers: "bold, larger font"
    - tables: "striped rows, sortable"
```

## Activation System Integration

### Testing Agent Discovery

After creating files, test that the system can discover your agent:

```bash
# Check if agent is discovered
python .claude/hooks/agent_activation_v2.py @list-agents

# Test specific agent activation
python .claude/hooks/agent_activation_v2.py @your-alias
```

### Hook System Limitations

The current hook system has limitations:
- Can display activation messages but cannot change Claude's persona
- Requires manual bundle loading for full capabilities
- State tracking works but behavior change is limited

### BMAD Bundle Advantages

The bundle approach:
- Enables immediate persona adoption through content loading
- Contains all necessary resources in a single file
- Works independently of hook system
- More portable and reliable

## Testing and Validation

### Step 1: File Validation

Verify all files are created correctly:

```bash
# Check agent definition exists
ls -la .brad-core/agents/your-agent-id.md

# Check bundle exists
ls -la .brad-core/bundles/your-agent-id.bundle.txt

# Validate YAML syntax
python -c "import yaml; yaml.safe_load(open('.brad-core/agents/your-agent-id.md').read())"
```

### Step 2: Activation Testing

Test the activation system:

```bash
# Test agent discovery
@list-agents

# Test activation with alias
@your-alias

# Test activation with full ID
@your-agent-id
```

### Step 3: Bundle Testing

Load and test the complete bundle:

1. Copy bundle content
2. Paste into Claude Code session
3. Verify persona adoption
4. Test individual commands
5. Validate resource loading

### Step 4: Integration Testing

Test integration with existing systems:

- Database connections
- API authentication
- Cross-agent coordination
- Data flow validation

## Best Practices

### Agent Design

1. **Single Responsibility**: Each agent should have a clear, focused purpose
2. **Clear Commands**: Command names should be intuitive and self-explanatory
3. **Comprehensive Help**: Always include detailed help and command descriptions
4. **Error Handling**: Build in graceful error handling and user feedback
5. **State Management**: Design for stateless operations when possible

### Bundle Organization

1. **Logical Grouping**: Group related tasks and workflows together
2. **Resource Optimization**: Include only necessary dependencies
3. **Size Management**: Keep bundles under 50KB when possible
4. **Clear Documentation**: Include comprehensive inline documentation

### Code Quality

1. **YAML Validation**: Always validate YAML syntax before committing
2. **Template Variables**: Use consistent variable naming conventions
3. **Version Control**: Track changes to agent definitions
4. **Documentation**: Keep documentation up-to-date with changes

### Security Considerations

1. **API Keys**: Never hardcode API keys in agent definitions
2. **Database Access**: Use environment variables for connection strings
3. **Input Validation**: Validate all user inputs in tasks
4. **Permission Checks**: Implement appropriate access controls

## Troubleshooting

### Common Issues

#### Agent Not Discovered

**Problem**: Agent doesn't appear in `@list-agents`

**Solutions**:
- Check file naming matches agent ID exactly
- Verify YAML syntax is valid
- Ensure file is in correct directory
- Check file permissions

#### Activation Fails

**Problem**: `@agent-alias` returns "not found"

**Solutions**:
- Verify alias mapping in `agent_activation_v2.py`
- Check agent ID matches between files
- Restart Claude Code session
- Clear agent state: `rm .claude/agent_state.json`

#### Bundle Loading Issues

**Problem**: Bundle doesn't activate persona correctly

**Solutions**:
- Check bundle format follows specification exactly
- Verify all START/END tags are properly formatted
- Ensure activation instructions are complete
- Test bundle size (may be too large)

#### Database Connection Problems

**Problem**: Agent can't connect to required databases

**Solutions**:
- Verify environment variables are set correctly
- Check database server is running and accessible
- Validate connection strings and credentials
- Test network connectivity

### Debugging Tools

1. **Agent Debug Log**: Check `.claude/agent_debug.log`
2. **YAML Validation**: Use online YAML validators
3. **Bundle Size**: Check bundle file size
4. **Network Testing**: Use `ping` and `telnet` for connectivity

### Getting Help

1. **Documentation**: Refer to `projects/bundle-format-spec.md`
2. **Examples**: Study existing agent implementations
3. **Templates**: Use `projects/activation-template.yaml`
4. **Community**: Consult Brad Method documentation

## Example: DummySearch Agents

### Case Study: Reddit-YouTube Agent Creation

This guide was developed while creating two DummySearch agents:

1. **DummySearch Agent** (`@reddit`): Reddit intelligence and analysis
2. **Reddit-YouTube Agent** (`@youtube`): Cross-platform problem-solution mapping

#### Key Decisions Made

1. **Separate Agents**: Created two focused agents rather than one complex agent
2. **Database Integration**: Connected to existing PostgreSQL database at `192.168.0.135:5434`
3. **API Integration**: Integrated with both Reddit API and YouTube API
4. **Short Aliases**: Used memorable aliases (`@reddit`, `@youtube`)

#### Lessons Learned

1. **Bundle Size**: Comprehensive bundles can become large; consider selective resource inclusion
2. **Environment Configuration**: Database connections need both dev and prod configurations
3. **Template Reuse**: Templates can be shared between related agents
4. **Testing Order**: Test basic activation before building complex bundles

## Conclusion

Creating new Brad Method agents involves:

1. Clear conceptual design
2. Proper file structure and naming
3. Complete YAML configuration
4. Comprehensive bundle creation
5. Activation system integration
6. Thorough testing and validation

Following this guide ensures agents are properly integrated, discoverable, and functional within the Brad Method ecosystem.

---

**Document Version**: 1.0  
**Created**: 2025-07-31  
**Author**: Claude Code Agent Development Process  
**Last Updated**: 2025-07-31