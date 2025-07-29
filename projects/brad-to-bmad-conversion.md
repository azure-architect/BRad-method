# Brad to BMAD Agent System Conversion Project

## Project Overview
Convert the Brad Method's hook-based agent system to use BMAD's self-contained bundle approach, where agents are activated through content loading rather than external hooks.

## Problem Statement
The current Brad Method uses Python hooks to intercept `@agent` commands, but Claude Code's architecture doesn't support dynamic persona switching through hooks. The BMAD method bypasses this limitation by making agents self-activating through bundled content.

## Goals
1. Maintain all existing Brad Method agent capabilities
2. Remove dependency on hook system for agent activation
3. Create self-contained agent bundles that activate on load
4. Preserve agent state tracking and management
5. Enable seamless agent switching through content loading

## Success Criteria
- Agents activate immediately when their bundle is loaded
- All agent commands and capabilities function as designed
- Agent switching works reliably without hooks
- Existing agent definitions are preserved and enhanced
- System is more portable and doesn't require Claude Code specific features

## Technical Approach
- Bundle agent definitions with their dependencies
- Add YAML activation instructions to each agent
- Create a bundle generator from existing agent files
- Implement a simple command system for agent loading
- Maintain compatibility with existing Brad Method resources

## Project Tasks

### Task 1: Analyze Existing Agent Structure
- Inventory all Brad Method agents and their dependencies
- Document current agent activation flow
- Identify all resources referenced by agents
- Map agent commands and capabilities
- Create compatibility requirements list

### Task 2: Design Bundle Format
- Define BMAD-compatible bundle structure
- Create activation instruction template
- Design resource embedding strategy
- Plan dependency resolution approach
- Document bundle format specification

### Task 3: Create Bundle Generator
- Build script to convert agent.md files to bundles
- Implement dependency resolution and embedding
- Add YAML activation instructions generator
- Create bundle validation system
- Test with sample agent conversion

### Task 4: Convert Core Agents
- Convert brad-master agent to bundle format
- Convert notion-agent with database schemas
- Convert video-ingestion-agent with workflows
- Convert idea-man agent with processing logic
- Convert remaining agents (github, pxm, project-manager)

### Task 5: Implement Agent Loader
- Create simple command for loading agent bundles
- Build agent state tracking without hooks
- Implement agent switching mechanism
- Add agent discovery and listing
- Create fallback for direct bundle loading

### Task 6: Test and Validate
- Test each converted agent individually
- Verify all commands work as expected
- Test agent switching scenarios
- Validate resource loading and dependencies
- Check compatibility with existing workflows

### Task 7: Create Migration Guide
- Document conversion process
- Create usage instructions for new system
- Build troubleshooting guide
- Provide examples of agent usage
- Archive old hook-based system

### Task 8: Deploy and Monitor
- Replace hook system with bundle loader
- Update all agent references
- Monitor for issues or edge cases
- Collect feedback on new system
- Optimize bundle generation if needed

## Dependencies
- Existing Brad Method agent definitions
- BMAD bundle format examples
- Python for bundle generation scripts
- YAML processing capabilities
- File system access for resource embedding

## Risks and Mitigations
- **Risk**: Large bundle sizes with embedded resources
  - **Mitigation**: Implement smart dependency loading and caching
- **Risk**: Loss of dynamic resource updates
  - **Mitigation**: Create regeneration workflow for bundles
- **Risk**: Compatibility with existing workflows
  - **Mitigation**: Maintain backward compatibility layer

## Timeline Estimate
- Task 1-2: 1 day (Analysis and Design)
- Task 3: 1 day (Bundle Generator)
- Task 4: 2 days (Agent Conversion)
- Task 5: 1 day (Loader Implementation)
- Task 6-7: 1 day (Testing and Documentation)
- Task 8: Ongoing (Deployment and Monitoring)

Total: ~6 days of focused work

## Next Steps
1. Begin with Task 1: Analyze Existing Agent Structure
2. Create detailed inventory of all agents and dependencies
3. Start designing the bundle format based on BMAD examples