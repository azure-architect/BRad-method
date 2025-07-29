# Task: Create Migration Guide

## Objective
Document the complete migration process from hook-based to bundle-based agent system.

## Prerequisites
- New system tested and validated
- Understanding of both old and new systems
- Migration strategy defined

## Steps

### 1. Migration Overview
- [ ] Document system differences
- [ ] Explain migration benefits
- [ ] List breaking changes
- [ ] Create timeline
- [ ] Define rollback plan

### 2. User Migration Guide
- [ ] Old vs new command mapping
- [ ] Step-by-step migration
- [ ] Common scenarios
- [ ] Troubleshooting guide
- [ ] FAQ section

### 3. Technical Migration
- [ ] Archive old hook system
- [ ] Update configuration files
- [ ] Modify documentation
- [ ] Update CI/CD if needed
- [ ] Clean up old files

### 4. Training Materials
- [ ] Create quick start guide
- [ ] Build video tutorials
- [ ] Write example workflows
- [ ] Design cheat sheet
- [ ] Create practice exercises

### 5. Communication Plan
- [ ] Announce migration
- [ ] Share benefits
- [ ] Provide support channels
- [ ] Gather feedback
- [ ] Iterate on issues

## Migration Guide Structure

### For Users
```markdown
# Brad Method Agent System Migration Guide

## What's Changing
- Hook-based activation → Bundle-based activation
- @agent commands → /brad load agent
- Automatic switching → Explicit loading

## Quick Start
1. Instead of `@master`, use `/brad load master`
2. Agents now load their full context
3. No external dependencies needed

## Command Mapping
| Old Command | New Command |
|------------|-------------|
| @master | /brad load master |
| @list-agents | /brad list |
| @status | /brad status |
| @deactivate | /brad unload |
```

### For Developers
```markdown
# Technical Migration Guide

## Architecture Changes
- Python hooks removed
- Self-contained bundles
- Stateless activation
- Content-based personas

## File Structure
Old:
.claude/hooks/agent_activation.py
.brad-core/agents/*.md

New:
.brad-core/bundles/*.bundle.txt
No hooks required

## Bundle Generation
python bundle_generator.py --all
```

## Deliverables
1. `MIGRATION.md` - Complete migration guide
2. `user-guide.md` - End user documentation
3. `developer-guide.md` - Technical details
4. `quick-reference.pdf` - Printable cheat sheet
5. `video-tutorials/` - Screen recordings

## Success Criteria
- Clear migration path documented
- All use cases covered
- No ambiguous instructions
- Rollback process defined
- Support resources available

## Time Estimate
4-5 hours