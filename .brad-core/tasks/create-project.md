# Create Project Task

**Task ID**: create-project
**Description**: Create a new project in Notion and optionally GitHub with proper resource allocation
**Agent**: brad-master
**Elicit**: true

## Task Workflow

### Step 1: Project Information Elicitation
**MANDATORY USER INTERACTION - DO NOT SKIP**

Please provide the following project details:

1. **Project Name**: 
2. **Project Type** (select one):
   - web-app
   - api-service  
   - data-pipeline
   - infrastructure
   - automation-tool
   - mobile-app
   - other (specify)

3. **Project Description** (1-2 sentences):

4. **GitHub Repository** (select one):
   - Create new repository
   - Link to existing repository: [URL]
   - No repository needed

5. **Infrastructure Requirements** (select all that apply):
   - Database (PostgreSQL, MongoDB, etc.)
   - Container hosting
   - Web server
   - API gateway
   - Monitoring
   - None required

6. **Team Members** (if any):

7. **Priority Level** (High, Medium, Low):

### Step 2: Notion Project Creation

Using the Notion MCP tools:

1. Create entry in Projects Database with:
   - Name: {provided name}
   - Type: {selected type}
   - Description: {provided description}
   - Status: "Planning"
   - Priority: {selected priority}
   - Created Date: {current date}
   - GitHub Repo: {if applicable}
   - Infrastructure Needs: {selected requirements}

2. Generate Project ID from Notion response

### Step 3: Initial Task Generation

Based on project type, create initial tasks in Tasks Database:

**For web-app projects:**
- Setup development environment
- Create project structure
- Implement authentication
- Design database schema
- Build frontend components
- API development
- Testing setup
- Deployment configuration

**For api-service projects:**
- API specification design
- Database schema design
- Core API endpoints
- Authentication/authorization
- Documentation
- Testing suite
- Deployment pipeline

**For infrastructure projects:**
- Requirements analysis
- Architecture design
- Resource provisioning
- Configuration management
- Monitoring setup
- Security hardening

### Step 4: GitHub Repository Creation (if requested)

If "Create new repository" was selected:

1. Use GitHub MCP tools to create repository:
   - Name: {project-name}
   - Description: {project description}
   - Private: true (default)
   - Initialize with README

2. Update Notion project with GitHub URL

3. Clone repository locally to projects/{project-name}

### Step 5: Resource Allocation (if needed)

If infrastructure requirements specified:

1. Query Resource Databases for available infrastructure
2. Allocate required resources (databases, containers, etc.)
3. Update Resources Database with allocation
4. Link allocated resources to project in Notion

### Step 6: Initial Documentation

Create entry in Notes Database:
- Title: "{Project Name} - Project Overview"
- Type: "Project Documentation"
- Content: Project requirements, architecture decisions, setup instructions
- Linked to: {project-id}

### Step 7: Trigger Hooks

Execute post-creation hooks:
- notion-sync: Ensure all databases are updated
- github-sync: If repository created, sync initial structure
- resource-allocation: If infrastructure allocated, update resource tracking

### Step 8: Summary

Provide user with:
- Notion project URL
- GitHub repository URL (if created)
- List of initial tasks created
- Allocated resources summary
- Next steps recommendation

## Success Criteria

- ✅ Project created in Notion Projects Database
- ✅ Initial tasks generated in Tasks Database  
- ✅ GitHub repository created (if requested)
- ✅ Resources allocated (if needed)
- ✅ Project documentation created in Notes Database
- ✅ All hooks executed successfully

## Error Handling

- If Notion creation fails: Retry once, then prompt user for manual intervention
- If GitHub creation fails: Continue with Notion-only project, note GitHub failure
- If resource allocation fails: Continue with project creation, flag resource needs

## Dependencies

- Notion MCP tools for database operations
- GitHub MCP tools for repository management  
- Resource management system for infrastructure allocation
- Hook system for post-creation automation