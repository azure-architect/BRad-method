# Task: Implement Agent Loader

## Objective
Create simple, hook-free mechanism for loading and managing BMAD-style agent bundles in Brad Method.

## Prerequisites
- Agent bundles created and tested
- Understanding of Claude's context window
- No dependency on hook system

## Steps

### 1. Loader Command Design
- [ ] Create `/brad load {agent}` command
- [ ] Design agent discovery mechanism
- [ ] Implement bundle file reading
- [ ] Add agent listing capability
- [ ] Create status checking

### 2. State Management
- [ ] Design stateless activation
- [ ] Create agent context tracking
- [ ] Implement session persistence
- [ ] Add agent history tracking
- [ ] Build transition management

### 3. Bundle Discovery
- [ ] Scan bundles directory
- [ ] Extract agent metadata
- [ ] Create agent registry
- [ ] Build quick lookup index
- [ ] Cache discovery results

### 4. User Interface
- [ ] Create clear activation messages
- [ ] Design agent switch prompts
- [ ] Build help system
- [ ] Add error handling
- [ ] Implement feedback messages

### 5. Integration Points
- [ ] Replace hook-based commands
- [ ] Update documentation
- [ ] Create migration aliases
- [ ] Add backward compatibility
- [ ] Test with existing workflows

## Implementation Approach

### Option 1: Slash Command
```markdown
/brad load master
# System loads brad-master.bundle.txt into context
# Agent activates through content instructions

/brad list
# Shows available agents from bundles directory

/brad status
# Current agent and available commands
```

### Option 2: Direct Instructions
```markdown
User: "Load the Brad Master agent"
Assistant: *Loads bundle and activates agent*

User: "Show available agents"
Assistant: *Lists agents from bundle directory*
```

### Option 3: Hybrid Approach
- Slash commands for power users
- Natural language for casual use
- Both methods load same bundles

## State Tracking
Since hooks can't change behavior, track state through:
1. Bundle content includes state
2. User awareness of active agent
3. Clear activation confirmations
4. Explicit mode indicators

## Deliverables
1. `agent-loader-guide.md` - Usage instructions
2. `bundle-directory-setup.md` - Organization guide
3. `loader-examples.md` - Common scenarios
4. `troubleshooting.md` - Common issues

## Success Criteria
- Agents load without hooks
- Clear activation feedback
- Simple user commands
- Reliable agent switching
- No technical barriers

## Time Estimate
4-6 hours