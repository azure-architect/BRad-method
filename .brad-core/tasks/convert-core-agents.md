# Task: Convert Core Agents

## Objective
Convert all Brad Method agents to BMAD-style bundles using the bundle generator.

## Prerequisites
- Working bundle generator script
- All agent source files available
- Bundle format specification finalized

## Steps

### 1. Brad Master Agent
- [ ] Run generator on `brad-master.md`
- [ ] Verify all workflows embedded
- [ ] Test activation instructions
- [ ] Validate command functionality
- [ ] Check resource references

### 2. Notion Agent
- [ ] Convert `notion-agent.md`
- [ ] Embed all database schemas
- [ ] Include Notion API documentation
- [ ] Verify database operations
- [ ] Test query commands

### 3. Video Ingestion Agent
- [ ] Convert `video-ingestion-agent.md`
- [ ] Embed workflow definitions
- [ ] Include Johnny Decimal categories
- [ ] Add processing pipelines
- [ ] Verify NAS integration info

### 4. Idea-Man Agent
- [ ] Convert `idea-man.md`
- [ ] Embed processing workflows
- [ ] Include idea templates
- [ ] Add context generation logic
- [ ] Test dictation processing

### 5. Supporting Agents
- [ ] Convert `github-agent.md`
- [ ] Convert `pxm-master.md`
- [ ] Convert `project-manager-agent.md`
- [ ] Verify all dependencies included
- [ ] Test inter-agent references

## Conversion Checklist (per agent)
- [ ] Run bundle generator
- [ ] Review generated bundle
- [ ] Test activation sequence
- [ ] Verify all commands present
- [ ] Check resource accessibility
- [ ] Validate formatting
- [ ] Test in Claude interface
- [ ] Document any issues

## Testing Protocol
1. Load bundle in fresh Claude session
2. Check agent activation message
3. Test primary commands
4. Verify resource access
5. Test agent-specific features
6. Check state persistence
7. Test deactivation

## Output Structure
```
.brad-core/bundles/
├── brad-master.bundle.txt
├── notion-agent.bundle.txt
├── video-ingestion-agent.bundle.txt
├── idea-man.bundle.txt
├── github-agent.bundle.txt
├── pxm-master.bundle.txt
└── project-manager-agent.bundle.txt
```

## Deliverables
1. All agent bundles in `.brad-core/bundles/`
2. `conversion-log.md` - Issues and solutions
3. `agent-testing-results.md` - Test outcomes
4. `bundle-optimization.md` - Size/performance notes

## Success Criteria
- All agents successfully converted
- Bundles activate without errors
- All functionality preserved
- Resource access working
- No missing dependencies

## Time Estimate
8-10 hours (1-2 hours per major agent)