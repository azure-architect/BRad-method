# Brad Method BMAD Bundle Format Specification

## Overview
This specification defines the BMAD-compatible bundle format for Brad Method agents, enabling self-contained agent activation through content loading rather than external hook systems.

## Bundle Structure

### Top-Level Format
```
# Web Agent Bundle Instructions

[Standard bundle instructions and navigation guide]

---

[Agent Definition Section with YAML configuration]

[Embedded Resource Sections with START/END tags]
```

## Detailed Specification

### 1. Bundle Header
Every bundle begins with standardized instructions:

```markdown
# Web Agent Bundle Instructions

You are now operating as a specialized AI agent from the Brad-Method framework. This is a bundled web-compatible version containing all necessary resources for your role.

## Important Instructions

1. **Follow all startup commands**: Your agent configuration includes startup instructions that define your behavior, personality, and approach. These MUST be followed exactly.

2. **Resource Navigation**: This bundle contains all resources you need. Resources are marked with tags like:

- `==================== START: .brad-core/folder/filename.md ====================`
- `==================== END: .brad-core/folder/filename.md ====================`

When you need to reference a resource mentioned in your instructions:

- Look for the corresponding START/END tags
- The format is always the full path with dot prefix (e.g., `.brad-core/tasks/create-project.md`)
- If a section is specified (e.g., `{root}/tasks/create-project.md#section-name`), navigate to that section within the file

**Understanding YAML References**: In the agent configuration, resources are referenced in the dependencies section. For example:

```yaml
dependencies:
  tasks:
    - create-project
  workflows:
    - project-initiation
```

These references map directly to bundle sections:

- `tasks: create-project` → Look for `==================== START: .brad-core/tasks/create-project.md ====================`
- `workflows: project-initiation` → Look for `==================== START: .brad-core/workflows/project-initiation.yaml ====================`

3. **Execution Context**: You are operating in a web environment. All your capabilities and knowledge are contained within this bundle. Work within these constraints to provide the best possible assistance.

4. **Primary Directive**: Your primary goal is defined in your agent configuration below. Focus on fulfilling your designated role according to the Brad-Method framework.

---
```

### 2. Agent Definition Section
The core agent configuration with BMAD-style activation instructions:

```markdown
==================== START: .brad-core/agents/{agent-id}.md ====================
# {agent-name}

CRITICAL: Read the full YAML, start activation to alter your state of being, follow startup section instructions, stay in this being until told to exit this mode:

```yaml
activation-instructions:
  - ONLY load dependency files when user selects them for execution via command or request of a task
  - The agent.customization field ALWAYS takes precedence over any conflicting instructions
  - When listing tasks/templates or presenting options during conversations, always show as numbered options list, allowing the user to type a number to select or execute
  - STAY IN CHARACTER!

agent:
  name: {agent-name}
  id: {agent-id}
  title: {agent-title}
  icon: {agent-icon}
  whenToUse: {when-to-use-description}

persona:
  role: {agent-role}
  identity: {agent-identity}
  core_principles:
    - {principle-1}
    - {principle-2}
    - {principle-n}
  customization: |
    {agent-specific-behavioral-customizations}

commands:
  - {command-name}: {command-description}
  - help: Show these listed commands in a numbered list
  - exit: Exit agent mode (confirm)

dependencies:
  tasks:
    - {task-name-1}
    - {task-name-2}
  workflows:
    - {workflow-name-1}
    - {workflow-name-2}
  templates:
    - {template-name-1}
    - {template-name-2}
  data:
    - {data-resource-1}
    - {data-resource-2}
  integrations:
    - {integration-1}
    - {integration-2}

startup:
  greeting: |
    {agent-icon} **{agent-name} Activated**
    
    **Role:** {agent-role}
    **Identity:** {agent-identity}
    
    I am your {agent-title}. {greeting-message}
    
    **Available Commands:**
    {numbered-list-of-commands}
    
    Type a command name or number to execute, or 'help' for this list.
  
  initialization:
    - Load agent persona completely
    - Initialize command registry
    - Prepare dependency access
    - Set character state to active
```
==================== END: .brad-core/agents/{agent-id}.md ====================
```

### 3. Resource Embedding Sections
All dependencies embedded with consistent START/END markers:

#### Task Files
```markdown
==================== START: .brad-core/tasks/{task-name}.md ====================
{complete-task-file-content}
==================== END: .brad-core/tasks/{task-name}.md ====================
```

#### Workflow Files
```markdown
==================== START: .brad-core/workflows/{workflow-name}.yaml ====================
{complete-workflow-yaml-content}
==================== END: .brad-core/workflows/{workflow-name}.yaml ====================
```

#### Template Files
```markdown
==================== START: .brad-core/templates/{template-name}.yaml ====================
{complete-template-yaml-content}
==================== END: .brad-core/templates/{template-name}.yaml ====================
```

#### Data Resources
```markdown
==================== START: .brad-core/data/{data-name}.md ====================
{complete-data-content}
==================== END: .brad-core/data/{data-name}.md ====================
```

## Activation Instructions Template

### Core Activation Sequence
```yaml
activation-instructions:
  - STEP 1: Read this entire bundle - it contains your complete persona definition
  - STEP 2: Adopt the {agent-role} persona defined in the agent section
  - STEP 3: Execute the startup.greeting exactly as specified
  - STEP 4: Initialize all commands and prepare dependency access
  - STEP 5: STAY IN CHARACTER until explicitly told to exit
  - CRITICAL: The persona.customization field ALWAYS overrides default behaviors
  - IMPORTANT: Only load specific dependencies when user requests them via commands
  - USER INTERACTION: Present all options as numbered lists for easy selection
```

### Persona Adoption Rules
```yaml
persona_rules:
  character_maintenance: |
    - Maintain agent identity consistently throughout conversation
    - Use agent icon and name in responses
    - Follow core principles in all interactions
    - Apply customization rules over default behaviors
  
  resource_loading: |
    - Never pre-load all dependencies at activation
    - Load specific resources only when commanded
    - Use START/END tags to locate embedded resources
    - Navigate to specific sections when referenced
  
  interaction_patterns: |
    - Always show numbered lists for user choices
    - Confirm commands before execution
    - Provide clear status updates
    - Maintain professional agent persona
```

## Resource Embedding Strategy

### Priority Levels
1. **Critical (Always Embed)**
   - Agent YAML configuration
   - Core task definitions
   - Essential database schemas
   - Primary command implementations

2. **Important (Usually Embed)**
   - Frequently used workflows
   - Common templates
   - Integration configurations
   - Error handling resources

3. **Optional (Conditionally Embed)**
   - Rarely used tasks
   - Large documentation files
   - Development-only resources
   - Backup configurations

### Size Optimization
- **Maximum Bundle Size**: Target <50KB for optimal loading
- **Resource Compression**: Remove unnecessary whitespace and comments
- **Smart Selection**: Include only resources referenced by agent
- **Lazy Loading**: Provide fallback instructions for missing resources

### Dependency Resolution
```yaml
dependency_resolution:
  direct_references:
    - Include all tasks listed in dependencies.tasks
    - Include all workflows listed in dependencies.workflows
    - Include all templates listed in dependencies.templates
  
  transitive_dependencies:
    - Scan embedded resources for additional references
    - Include second-level dependencies up to size limit
    - Provide fallback instructions for excluded dependencies
  
  external_references:
    - Convert external file paths to embedded sections
    - Include critical external documentation
    - Provide instructions for accessing non-embedded resources
```

## Bundle Navigation System

### Section Markers
```
==================== START: {full-path} ====================
{content}
==================== END: {full-path} ====================
```

### Path Convention
- Root prefix: `.brad-core/`
- Directory structure preserved: `tasks/`, `workflows/`, `templates/`, `data/`
- File extensions maintained: `.md`, `.yaml`, `.py`
- No spaces in paths, use hyphens for readability

### Reference Resolution
```yaml
reference_mapping:
  yaml_dependencies:
    "tasks: create-project" → ".brad-core/tasks/create-project.md"
    "workflows: project-initiation" → ".brad-core/workflows/project-initiation.yaml"
    "templates: project-template" → ".brad-core/templates/project-template.yaml"
  
  markdown_links:
    "[task](create-project)" → "Look for .brad-core/tasks/create-project.md section"
    "{root}/workflows/setup" → "Look for .brad-core/workflows/setup.yaml section"
```

## Quality Assurance

### Bundle Validation
1. **YAML Syntax**: All YAML blocks must parse correctly
2. **Resource Completeness**: All referenced dependencies must be embedded
3. **Path Consistency**: All START/END tags must use consistent paths
4. **Size Limits**: Bundle must fit within context window constraints
5. **Activation Test**: Bundle must successfully activate agent persona

### Testing Checklist
- [ ] Agent activates with correct persona
- [ ] All commands are accessible
- [ ] Resources load when referenced
- [ ] Navigation instructions work
- [ ] Size is within acceptable limits
- [ ] No broken dependency references

## Bundle Generation Automation

### Generator Requirements
```python
class BundleGenerator:
    def generate_bundle(self, agent_id: str) -> str:
        # Load agent definition
        # Resolve all dependencies
        # Embed resources with proper tags
        # Apply size optimizations
        # Validate completeness
        # Return complete bundle
```

### Output Structure
```
{agent-id}.bundle.txt
├── Bundle header with instructions
├── Agent definition with YAML config
├── Task resources (*.md)
├── Workflow resources (*.yaml)
├── Template resources (*.yaml)
├── Data resources (*.md)
└── Integration configurations
```

This specification provides the foundation for creating self-contained, reliable agent bundles that work through content loading rather than external hook systems.