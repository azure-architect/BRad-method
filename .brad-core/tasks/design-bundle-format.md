# Task: Design Bundle Format

## Objective
Create BMAD-compatible bundle format specification for Brad Method agents that enables self-activation through content loading.

## Prerequisites
- Completed agent structure analysis
- Understanding of BMAD bundle format
- Knowledge of YAML activation instructions

## Steps

### 1. Bundle Structure Design
- [ ] Define top-level bundle format
- [ ] Create activation instruction template
- [ ] Design resource embedding sections
- [ ] Plan section markers and navigation
- [ ] Establish naming conventions

### 2. Activation Instructions
- [ ] Create YAML template for activation
- [ ] Define startup command sequence
- [ ] Design persona adoption instructions
- [ ] Add character maintenance rules
- [ ] Include dependency loading logic

### 3. Resource Embedding Strategy
- [ ] Design START/END tag format
- [ ] Create path mapping convention
- [ ] Plan resource organization
- [ ] Define embedding priorities
- [ ] Handle large resource optimization

### 4. Dependency Resolution
- [ ] Create dependency graph structure
- [ ] Design lazy loading approach
- [ ] Plan circular dependency handling
- [ ] Define resource reference format
- [ ] Create fallback mechanisms

### 5. Format Specification
- [ ] Write formal bundle specification
- [ ] Create validation schema
- [ ] Document section requirements
- [ ] Define metadata format
- [ ] Establish versioning strategy

## Bundle Format Template
```
# Web Agent Bundle Instructions

You are now operating as a specialized AI agent from the Brad-Method framework...

## Important Instructions
[Standard instructions for bundle usage]

==================== START: .brad-core/agents/{agent-id}.md ====================
# {agent-name}

CRITICAL: Read the full YAML, start activation...

```yaml
activation-instructions:
  - ONLY load dependency files when user selects them
  - The agent.customization field ALWAYS takes precedence
  - STAY IN CHARACTER!

agent:
  name: {name}
  id: {id}
  title: {title}
  icon: {icon}
  whenToUse: {when-to-use}

persona:
  role: {role}
  identity: {identity}
  core_principles:
    - {principles}

commands:
  - {command}: {description}

dependencies:
  {dependency-map}
```
==================== END: .brad-core/agents/{agent-id}.md ====================

[Embedded resources follow...]
```

## Deliverables
1. `bundle-format-spec.md` - Complete format specification
2. `activation-template.yaml` - Reusable activation instructions
3. `resource-embedding-guide.md` - How to embed resources
4. `bundle-examples/` - Sample bundles for reference

## Success Criteria
- Bundle format enables immediate agent activation
- All Brad Method features supported
- Clear navigation and resource access
- Efficient resource embedding
- Backward compatibility maintained

## Time Estimate
3-4 hours