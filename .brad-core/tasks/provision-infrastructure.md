# Provision Infrastructure Task

**Task ID**: provision-infrastructure
**Description**: Allocate and configure infrastructure resources for project requirements
**Agent**: resource-agent
**Elicit**: true

## Task Workflow

### Step 1: Requirements Elicitation
**MANDATORY USER INTERACTION - DO NOT SKIP**

Please provide the following infrastructure requirements:

1. **Project Information**:
   - Project ID: 
   - Project Type: (web-app, api-service, data-pipeline, infrastructure, etc.)

2. **Environment Type**:
   - Development
   - Staging
   - Production
   - All environments

3. **Resource Requirements**:
   - Compute: (CPU cores, RAM, number of instances)
   - Storage: (Type, size, performance requirements)
   - Network: (Bandwidth, load balancing, CDN)
   - Database: (Type, size, replication needs)

4. **Scalability Requirements**:
   - Expected concurrent users/requests
   - Growth projections
   - Auto-scaling preferences
   - Peak capacity planning

5. **Compliance and Security**:
   - Data classification level
   - Regulatory requirements
   - Security certifications needed
   - Backup and DR requirements

6. **Budget Constraints**:
   - Monthly budget limit
   - Cost optimization preferences
   - Reserved vs on-demand preference

### Step 2: Resource Assessment

Analyze available infrastructure capacity:

1. **Proxmox Resource Discovery**:
   - Query available nodes and capacity
   - Check resource pool availability
   - Assess network and storage capacity
   - Review current allocation levels

2. **Capacity Planning**:
   - Calculate resource requirements
   - Plan for redundancy and failover
   - Consider maintenance windows
   - Account for growth projections

3. **Cost Estimation**:
   - Calculate resource costs
   - Include operational overhead
   - Project monthly and annual costs
   - Identify cost optimization opportunities

**Output**: Resource availability report and cost estimate

### Step 3: Architecture Design

Design infrastructure architecture:

1. **Component Selection**:
   - Virtual machines vs containers
   - Load balancer configuration
   - Database architecture
   - Caching strategy
   - CDN requirements

2. **Network Design**:
   - VLAN segmentation
   - Security group configuration
   - Firewall rules
   - VPN access requirements

3. **High Availability Design**:
   - Redundancy planning
   - Failover mechanisms
   - Backup strategies
   - Disaster recovery procedures

**Output**: Infrastructure architecture diagram and specifications

### Step 4: Resource Allocation

Allocate and reserve resources:

1. **Virtual Machine Provisioning**:
   - Create VM instances with specified configurations
   - Install base operating systems
   - Configure initial networking
   - Set up basic security hardening

2. **Storage Allocation**:
   - Provision storage volumes
   - Configure backup storage
   - Set up shared storage if needed
   - Implement storage encryption

3. **Network Configuration**:
   - Configure VLANs and subnets
   - Set up load balancers
   - Configure DNS entries
   - Implement firewall rules

4. **Database Setup**:
   - Deploy database instances
   - Configure replication if required
   - Set up backup procedures
   - Implement security measures

**Output**: Allocated resource inventory with access details

### Step 5: Security Hardening

Implement security measures:

1. **Access Control**:
   - Configure user accounts and permissions
   - Set up SSH key authentication
   - Implement multi-factor authentication
   - Configure audit logging

2. **Network Security**:
   - Deploy intrusion detection systems
   - Configure firewall policies
   - Set up VPN access
   - Implement network monitoring

3. **Data Protection**:
   - Enable encryption at rest and in transit
   - Configure backup encryption
   - Implement data loss prevention
   - Set up compliance monitoring

**Output**: Security configuration report

### Step 6: Monitoring and Alerting

Set up monitoring infrastructure:

1. **System Monitoring**:
   - Deploy monitoring agents
   - Configure performance dashboards
   - Set up resource utilization tracking
   - Implement log aggregation

2. **Application Monitoring**:
   - Configure application performance monitoring
   - Set up synthetic monitoring
   - Implement error tracking
   - Configure user experience monitoring

3. **Alerting Configuration**:
   - Define alert thresholds
   - Configure notification channels
   - Set up escalation procedures
   - Implement alert correlation

**Output**: Monitoring and alerting configuration

### Step 7: Testing and Validation

Validate infrastructure deployment:

1. **Connectivity Testing**:
   - Test all network connections
   - Validate load balancer functionality
   - Check database connectivity
   - Verify external integrations

2. **Performance Testing**:
   - Run baseline performance tests
   - Validate capacity under load
   - Test failover scenarios
   - Verify backup and recovery procedures

3. **Security Testing**:
   - Run vulnerability scans
   - Test access controls
   - Validate encryption
   - Check compliance requirements

**Output**: Infrastructure validation report

### Step 8: Documentation and Handover

Create comprehensive documentation:

1. **Infrastructure Documentation**:
   - Architecture diagrams
   - Configuration details
   - Access procedures
   - Operational runbooks

2. **Update Notion Databases**:
   - Create resource entries in Resources database
   - Link resources to project
   - Update project infrastructure status
   - Document resource allocation details

3. **Team Handover**:
   - Provide access credentials securely
   - Conduct infrastructure walkthrough
   - Share operational procedures
   - Set up training sessions if needed

**Output**: Complete infrastructure documentation and team handover confirmation

## Success Criteria

- ✅ Infrastructure requirements validated and documented
- ✅ Resources successfully allocated and configured
- ✅ Security measures implemented and tested
- ✅ Monitoring and alerting operational
- ✅ Infrastructure tested and validated
- ✅ Documentation complete and team briefed
- ✅ Notion databases updated with resource details

## Error Handling

- **Resource Shortage**: Queue request, suggest alternatives, escalate to infrastructure team
- **Provisioning Failures**: Retry with backoff, try alternative configurations, rollback partial deployments
- **Security Validation Failures**: Block activation until resolved, provide remediation guidance
- **Performance Issues**: Scale resources, optimize configuration, implement performance improvements

## Dependencies

- Proxmox API access and permissions
- Resource allocation quotas and policies
- Network infrastructure and IP address pools
- Security policies and compliance requirements
- Monitoring and alerting infrastructure

## Post-Provisioning Tasks

- Regular health checks and maintenance
- Resource utilization monitoring
- Cost optimization reviews
- Security compliance audits
- Backup and recovery testing