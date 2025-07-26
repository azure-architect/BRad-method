# Assign Project Resources Task

**Task ID**: assign-project-resources
**Description**: Allocate and assign specific resources to project components and team members
**Agent**: project-manager-agent
**Elicit**: true

## Task Workflow

### Step 1: Resource Assignment Requirements
**MANDATORY USER INTERACTION - DO NOT SKIP**

Please provide the following resource assignment details:

1. **Project Information**:
   - Project ID: 
   - Project Name: 
   - Current Phase: (Planning, Development, Testing, Deployment)

2. **Team Resource Assignment**:
   - Project Manager: 
   - Technical Lead: 
   - Developers: (names and roles)
   - QA Engineers: 
   - DevOps Engineers: 
   - Designers: (if applicable)

3. **Infrastructure Resource Assignment**:
   - Development Environment: (assign to specific team members)
   - Staging Environment: (shared access)
   - Production Environment: (restricted access)
   - Database Resources: (assign admin and user roles)

4. **Tool and Service Access**:
   - Repository Access: (assign roles and permissions)
   - Notion Database Access: (assign edit/view permissions)
   - Monitoring Tools: (assign dashboard access)
   - Deployment Tools: (assign deployment permissions)

5. **Time and Budget Allocation**:
   - Resource allocation percentage per team member
   - Budget allocation per resource category
   - Timeline constraints and deadlines
   - Priority levels for resource usage

### Step 2: Current Resource Inventory

Assess available resources across all systems:

1. **Team Availability Assessment**:
   - Query team member current commitments
   - Check availability percentages
   - Identify scheduling conflicts
   - Assess skill requirements vs availability

2. **Infrastructure Resource Check**:
   - Review allocated infrastructure status
   - Check resource utilization levels
   - Verify resource health and performance
   - Assess capacity for additional allocation

3. **Tool and License Availability**:
   - Check software license availability
   - Verify service subscription limits
   - Assess tool integration capacity
   - Review access control limits

**Output**: Resource availability matrix

### Step 3: Resource Allocation Planning

Create detailed resource allocation plan:

1. **Team Resource Allocation**:
   - Assign specific roles and responsibilities
   - Define reporting relationships
   - Set collaboration workflows
   - Establish communication protocols

2. **Infrastructure Resource Mapping**:
   - Map infrastructure to project phases
   - Assign environment ownership
   - Define resource sharing policies
   - Set resource usage monitoring

3. **Tool and Service Assignment**:
   - Assign tool access levels
   - Configure service permissions
   - Set up integration workflows
   - Define usage monitoring

**Output**: Comprehensive resource allocation plan

### Step 4: Access Control Configuration

Configure access controls across all systems:

1. **Notion Database Access**:
   - Assign database permissions (view, edit, admin)
   - Configure project-specific access
   - Set up notification preferences
   - Create resource sharing rules

2. **GitHub Repository Access**:
   - Assign repository roles (read, write, admin)
   - Configure branch access permissions
   - Set up code review assignments
   - Configure deployment permissions

3. **Infrastructure Access**:
   - Configure SSH/VPN access
   - Set up service account permissions
   - Configure monitoring access
   - Set up logging and audit access

**Output**: Access control configuration summary

### Step 5: Resource Provisioning and Assignment

Execute resource assignments:

1. **Team Member Onboarding**:
   - Send access credentials securely
   - Provide resource access documentation
   - Schedule orientation sessions
   - Set up communication channels

2. **Infrastructure Assignment**:
   - Allocate specific infrastructure components
   - Configure resource monitoring and alerts
   - Set up backup and recovery access
   - Document resource usage guidelines

3. **Tool and Service Activation**:
   - Activate user accounts and licenses
   - Configure tool integrations
   - Set up automated workflows
   - Provide training materials

**Output**: Resource assignment execution summary

### Step 6: Resource Monitoring Setup

Establish resource monitoring and tracking:

1. **Usage Monitoring**:
   - Set up resource utilization tracking
   - Configure usage reporting
   - Establish threshold alerts
   - Create usage dashboards

2. **Performance Monitoring**:
   - Monitor team productivity metrics
   - Track infrastructure performance
   - Monitor tool usage effectiveness
   - Set up performance alerts

3. **Cost Monitoring**:
   - Track resource costs by category
   - Monitor budget utilization
   - Set up cost threshold alerts
   - Generate cost optimization reports

**Output**: Monitoring and tracking configuration

### Step 7: Workflow Integration

Integrate resource assignments with project workflows:

1. **Task Assignment Integration**:
   - Link Notion tasks to assigned team members
   - Configure automated task routing
   - Set up progress tracking
   - Enable status synchronization

2. **Development Workflow Integration**:
   - Configure GitHub issue assignments
   - Set up automated code review assignments
   - Configure deployment workflow permissions
   - Enable automated status updates

3. **Resource Workflow Automation**:
   - Set up resource allocation triggers
   - Configure auto-scaling policies
   - Enable resource cleanup automation
   - Set up resource optimization workflows

**Output**: Workflow integration configuration

### Step 8: Documentation and Communication

Document assignments and communicate to stakeholders:

1. **Resource Assignment Documentation**:
   - Create resource assignment matrix
   - Document access procedures
   - Create resource usage guidelines
   - Document escalation procedures

2. **Team Communication**:
   - Send assignment notifications
   - Schedule team orientation
   - Provide resource access training
   - Set up regular review meetings

3. **Stakeholder Reporting**:
   - Update project stakeholders
   - Provide resource utilization reports
   - Share cost and timeline impacts
   - Schedule progress review meetings

**Output**: Documentation and communication completion

### Step 9: Validation and Testing

Validate resource assignments and access:

1. **Access Validation**:
   - Test all assigned access permissions
   - Verify tool and service functionality
   - Validate integration workflows
   - Check monitoring and alerting

2. **Resource Functionality Testing**:
   - Test infrastructure accessibility
   - Verify development environment setup
   - Validate deployment permissions
   - Check backup and recovery access

3. **Workflow Testing**:
   - Test automated resource allocation
   - Verify task assignment workflows
   - Test escalation procedures
   - Validate reporting mechanisms

**Output**: Validation and testing results

### Step 10: Ongoing Resource Management

Establish ongoing resource management procedures:

1. **Regular Review Processes**:
   - Schedule weekly resource utilization reviews
   - Plan monthly resource optimization sessions
   - Conduct quarterly resource allocation reviews
   - Annual resource planning sessions

2. **Change Management**:
   - Define resource change request procedures
   - Set up approval workflows
   - Configure change notification systems
   - Establish rollback procedures

3. **Optimization and Scaling**:
   - Monitor resource efficiency
   - Implement optimization recommendations
   - Plan resource scaling strategies
   - Manage resource lifecycle

**Output**: Ongoing management procedures documentation

## Success Criteria

- ✅ All team members have appropriate resource access
- ✅ Infrastructure resources properly allocated and accessible
- ✅ Tool and service permissions configured correctly
- ✅ Resource monitoring and tracking operational
- ✅ Workflow integrations functional
- ✅ Documentation complete and distributed
- ✅ Validation testing successful
- ✅ Ongoing management procedures established

## Error Handling

- **Access Permission Failures**: Verify account status, check permission hierarchies, escalate to system administrators
- **Resource Conflicts**: Analyze conflicts, propose alternatives, escalate to resource owners
- **Integration Issues**: Test connections, verify configurations, implement fallback procedures
- **Monitoring Failures**: Check monitoring service status, verify configuration, implement manual tracking

## Dependencies

- Team member availability and onboarding status
- Infrastructure provisioning completion
- Tool and service subscription status
- Access control system availability
- Project timeline and milestone requirements

## Post-Assignment Tasks

- Regular resource utilization monitoring
- Periodic access permission audits
- Resource optimization and right-sizing
- Team feedback collection and analysis
- Resource allocation effectiveness measurement