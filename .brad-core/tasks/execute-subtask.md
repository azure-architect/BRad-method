# Execute Subtask Task

**Task ID**: execute-subtask
**Description**: Execute specific subtasks within project workflows with proper coordination
**Agent**: project-manager-agent
**Elicit**: true

## Task Workflow

### Step 1: Subtask Analysis and Preparation
**MANDATORY USER INTERACTION - DO NOT SKIP**

Please provide the following subtask details:

1. **Subtask Information**:
   - Subtask ID: 
   - Parent Task: 
   - Project ID: 
   - Subtask Type: (development, testing, deployment, documentation, review)

2. **Execution Details**:
   - Assigned Agent: (notion-agent, github-agent, resource-agent, project-manager-agent)
   - Priority Level: (High, Medium, Low)
   - Estimated Duration: 
   - Deadline: 

3. **Dependencies**:
   - Prerequisite Tasks: 
   - Required Resources: 
   - Blocking Issues: 
   - Team Dependencies: 

4. **Success Criteria**:
   - Completion Requirements: 
   - Quality Gates: 
   - Acceptance Criteria: 
   - Deliverables: 

5. **Execution Context**:
   - Environment: (development, staging, production)
   - Access Requirements: 
   - Tool Requirements: 
   - Data Requirements: 

### Step 2: Prerequisite Validation

Validate all prerequisites are met:

1. **Dependency Check**:
   - Verify prerequisite tasks are completed
   - Check resource availability
   - Validate access permissions
   - Confirm tool accessibility

2. **Resource Readiness**:
   - Verify assigned team member availability
   - Check infrastructure resource status
   - Validate service and tool readiness
   - Confirm data availability

3. **Environment Preparation**:
   - Validate target environment status
   - Check configuration consistency
   - Verify backup and rollback procedures
   - Confirm monitoring and alerting

**Output**: Prerequisite validation report

### Step 3: Execution Planning

Create detailed execution plan:

1. **Task Breakdown**:
   - Break subtask into atomic steps
   - Define execution sequence
   - Identify decision points
   - Plan error handling procedures

2. **Resource Allocation**:
   - Assign specific resources to steps
   - Plan resource utilization schedule
   - Configure monitoring and tracking
   - Set up progress reporting

3. **Risk Assessment**:
   - Identify potential failure points
   - Plan mitigation strategies
   - Define contingency procedures
   - Set up early warning systems

**Output**: Detailed execution plan

### Step 4: Agent Coordination

Coordinate with appropriate specialized agent:

1. **Agent Selection and Briefing**:
   - Route to appropriate specialized agent
   - Provide complete context and requirements
   - Configure agent-specific parameters
   - Set up progress monitoring

2. **Execution Handoff**:
   - Transfer execution control to specialized agent
   - Maintain oversight and coordination
   - Monitor execution progress
   - Handle escalations and issues

3. **Inter-Agent Communication**:
   - Facilitate communication between agents
   - Coordinate shared resource usage
   - Manage workflow dependencies
   - Sync progress updates

**Output**: Agent coordination status and execution initiation

### Step 5: Execution Monitoring

Monitor subtask execution progress:

1. **Progress Tracking**:
   - Track execution steps completion
   - Monitor resource utilization
   - Track time and budget consumption
   - Monitor quality metrics

2. **Issue Detection and Response**:
   - Monitor for errors and exceptions
   - Detect performance issues
   - Identify resource constraints
   - Escalate critical issues

3. **Stakeholder Communication**:
   - Provide regular progress updates
   - Communicate milestone achievements
   - Report issues and delays
   - Coordinate stakeholder decisions

**Output**: Execution monitoring reports

### Step 6: Quality Assurance

Ensure quality standards are met:

1. **Quality Gate Validation**:
   - Verify completion criteria met
   - Validate deliverable quality
   - Check compliance requirements
   - Confirm acceptance criteria

2. **Testing and Validation**:
   - Execute required tests
   - Perform validation procedures
   - Verify integration compatibility
   - Confirm performance requirements

3. **Review and Approval**:
   - Coordinate required reviews
   - Facilitate approval processes
   - Document review outcomes
   - Handle review feedback

**Output**: Quality assurance validation results

### Step 7: Integration and Synchronization

Integrate subtask results with broader project:

1. **Result Integration**:
   - Integrate deliverables into project
   - Update project status and progress
   - Sync with related components
   - Validate integration success

2. **Database Synchronization**:
   - Update Notion task status
   - Sync GitHub repository changes
   - Update resource allocation status
   - Maintain data consistency

3. **Workflow Continuation**:
   - Trigger dependent tasks
   - Update project timeline
   - Adjust resource allocations
   - Communicate workflow changes

**Output**: Integration and synchronization summary

### Step 8: Documentation and Reporting

Document execution results and lessons learned:

1. **Execution Documentation**:
   - Document execution steps and decisions
   - Record issues encountered and resolutions
   - Document configuration changes
   - Create operational notes

2. **Results Reporting**:
   - Generate completion report
   - Document deliverables and outcomes
   - Report performance metrics
   - Analyze variance from plan

3. **Lessons Learned**:
   - Capture improvement opportunities
   - Document best practices
   - Record process optimizations
   - Update execution templates

**Output**: Comprehensive documentation and reporting

### Step 9: Cleanup and Resource Release

Clean up temporary resources and environments:

1. **Resource Cleanup**:
   - Release temporary resources
   - Clean up test environments
   - Archive temporary data
   - Update resource allocation tracking

2. **Environment Reset**:
   - Reset shared environments to baseline
   - Clean up temporary configurations
   - Remove test data and artifacts
   - Validate environment readiness

3. **Access and Permission Cleanup**:
   - Remove temporary access permissions
   - Clean up service accounts
   - Update access control lists
   - Audit permission changes

**Output**: Cleanup completion confirmation

### Step 10: Handoff and Closure

Complete subtask handoff and closure:

1. **Deliverable Handoff**:
   - Transfer deliverables to stakeholders
   - Provide usage documentation
   - Conduct knowledge transfer
   - Confirm acceptance

2. **Task Closure**:
   - Mark subtask as complete
   - Update project progress tracking
   - Release assigned resources
   - Update team availability

3. **Process Improvement**:
   - Analyze execution efficiency
   - Implement process improvements
   - Update execution templates
   - Share best practices

**Output**: Complete subtask closure and handoff confirmation

## Success Criteria

- ✅ Prerequisites validated and met
- ✅ Execution plan successfully implemented
- ✅ Quality gates passed
- ✅ Results integrated into project
- ✅ Documentation complete and accurate
- ✅ Resources cleaned up and released
- ✅ Stakeholder acceptance achieved
- ✅ Task marked as complete in all systems

## Error Handling

- **Prerequisite Failures**: Address blocking issues, reschedule execution, escalate to project manager
- **Execution Errors**: Implement rollback procedures, retry with alternative approaches, escalate to technical leads
- **Quality Gate Failures**: Return to previous phase, implement corrections, re-validate
- **Integration Issues**: Debug integration problems, implement workarounds, coordinate with affected teams

## Dependencies

- Prerequisite task completion
- Resource availability and access
- Agent availability and capability
- System and tool availability
- Stakeholder availability for decisions

## Performance Metrics

- Execution time vs estimate
- Quality gate pass rate
- Resource utilization efficiency
- Error rate and resolution time
- Stakeholder satisfaction score