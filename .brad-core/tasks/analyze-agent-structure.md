# Task: Analyze Existing Agent Structure

## Objective
Create comprehensive inventory of Brad Method agents and their dependencies to prepare for BMAD-style bundle conversion.

## Prerequisites
- Access to `.brad-core/agents/` directory
- Understanding of current hook-based system
- Knowledge of agent YAML structure

## Steps

### 1. Agent Inventory
- [ ] List all agent files in `.brad-core/agents/`
- [ ] Extract agent metadata (id, name, title, icon)
- [ ] Document agent purpose and whenToUse criteria
- [ ] Note any special activation requirements

### 2. Dependency Mapping
For each agent, document:
- [ ] Database schemas referenced
- [ ] External files or resources needed
- [ ] Commands and their implementations
- [ ] Integration points with other agents
- [ ] Notion database IDs used

### 3. Command Analysis
- [ ] List all commands for each agent
- [ ] Identify command parameters and options
- [ ] Map command implementations to code/logic
- [ ] Note any external tool dependencies

### 4. Resource Dependencies
- [ ] Identify all files referenced by agents
- [ ] List external APIs or services used
- [ ] Document configuration requirements
- [ ] Map resource paths and locations

### 5. Activation Flow Documentation
- [ ] Document current hook-based activation
- [ ] Trace agent state management
- [ ] Identify activation success/failure points
- [ ] Note any initialization requirements

## Deliverables
1. `agent-inventory.yaml` - Complete list of agents and metadata
2. `dependency-map.json` - All agent dependencies mapped
3. `activation-flow.md` - Current system documentation
4. `compatibility-requirements.md` - Must-have features for new system

## Success Criteria
- All agents documented with complete dependency lists
- Clear understanding of resource requirements
- Activation flow fully mapped
- No missing dependencies or hidden requirements

## Time Estimate
4-6 hours

## Output Format
```yaml
agents:
  brad-master:
    id: brad-master
    name: BRad Master
    title: BRad Master Project Orchestrator
    icon: 🎯
    dependencies:
      databases:
        - projects
        - tasks
      files:
        - external_docs/notion-api.md
      integrations:
        - notion
        - github
    commands:
      - name: status
        params: none
        description: Check system status
```