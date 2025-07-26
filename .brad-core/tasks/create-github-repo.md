# Create GitHub Repository Task

**Task ID**: create-github-repo
**Description**: Create and configure GitHub repository with proper structure and integrations
**Agent**: github-agent
**Elicit**: true

## Task Workflow

### Step 1: Repository Requirements Elicitation
**MANDATORY USER INTERACTION - DO NOT SKIP**

Please provide the following repository details:

1. **Repository Information**:
   - Repository Name: 
   - Description: 
   - Visibility: (Private/Public)
   - Organization: (leave blank for personal)

2. **Project Type Template**:
   - web-app (React/Vue/Angular application)
   - api-service (REST/GraphQL API)
   - data-pipeline (ETL/Data processing)
   - infrastructure (Terraform/Ansible)
   - automation-tool (Scripts/CLI tools)
   - mobile-app (React Native/Flutter)
   - other (specify)

3. **Technology Stack**:
   - Primary Language: 
   - Framework: 
   - Database: 
   - Additional technologies: 

4. **Development Workflow**:
   - Branching Strategy: (GitFlow, GitHub Flow, Custom)
   - Required Reviewers: (1, 2, 3+)
   - Automated Testing: (Yes/No)
   - Deployment Pipeline: (Manual, Automated)

5. **Team Access**:
   - Team Members: (GitHub usernames)
   - Access Levels: (Read, Write, Admin)
   - External Collaborators: 

6. **Integration Requirements**:
   - Notion Integration: (Yes/No)
   - Issue Tracking: (GitHub Issues, External)
   - CI/CD Platform: (GitHub Actions, Jenkins, Other)
   - Code Quality Tools: (ESLint, SonarQube, etc.)

### Step 2: Repository Creation

Create GitHub repository with proper configuration:

1. **Repository Setup**:
   - Create repository with specified name and description
   - Set visibility (public/private)
   - Initialize with README.md
   - Add appropriate .gitignore for technology stack
   - Create initial LICENSE file if required

2. **Branch Structure**:
   - Create main branch (protected)
   - Create develop branch (if using GitFlow)
   - Set up branch naming conventions
   - Configure default branch settings

**Output**: Repository URL and basic configuration confirmation

### Step 3: Template Structure Implementation

Set up project structure based on type:

1. **Web Application Template**:
   ```
   /src
     /components
     /pages
     /utils
     /assets
   /public
   /tests
   /__tests__
   /docs
   package.json
   README.md
   .env.example
   ```

2. **API Service Template**:
   ```
   /src
     /controllers
     /models
     /routes
     /middleware
     /utils
   /tests
   /docs
     /api
   /config
   package.json or requirements.txt
   README.md
   .env.example
   ```

3. **Infrastructure Template**:
   ```
   /terraform or /ansible
   /scripts
   /docs
     /architecture
   /environments
     /dev
     /staging
     /prod
   README.md
   ```

**Output**: Initial project structure with template files

### Step 4: Branch Protection Configuration

Configure branch protection rules:

1. **Main Branch Protection**:
   - Require pull request reviews (specified number)
   - Dismiss stale reviews when new commits are pushed
   - Require status checks to pass
   - Require branches to be up to date
   - Restrict pushes to administrators only

2. **Develop Branch Protection** (if applicable):
   - Require pull request reviews (reduced number)
   - Require status checks to pass
   - Allow force pushes for administrators

3. **Branch Naming Rules**:
   - feature/* for new features
   - bugfix/* for bug fixes
   - hotfix/* for emergency fixes
   - release/* for release preparation

**Output**: Branch protection configuration summary

### Step 5: GitHub Actions Workflow Setup

Create CI/CD workflows based on project type:

1. **Basic CI Workflow** (.github/workflows/ci.yml):
   - Trigger on push and pull requests
   - Run linting and code quality checks
   - Execute test suite
   - Build project artifacts
   - Report test coverage

2. **Deployment Workflow** (.github/workflows/deploy.yml):
   - Trigger on push to main branch
   - Run full test suite
   - Build production artifacts
   - Deploy to staging environment
   - Run smoke tests
   - Deploy to production (with approval)

3. **Security Workflow** (.github/workflows/security.yml):
   - Dependency vulnerability scanning
   - Code security analysis
   - License compliance checks
   - Container image scanning (if applicable)

**Output**: GitHub Actions workflow files and configuration

### Step 6: Issue and PR Templates

Create templates for consistent issue and PR management:

1. **Issue Templates**:
   - Bug report template
   - Feature request template
   - Task/improvement template
   - Question/support template

2. **Pull Request Template**:
   - Description requirements
   - Testing checklist
   - Review guidelines
   - Breaking changes notification

3. **Contributing Guidelines**:
   - Code style guidelines
   - Commit message conventions
   - PR submission process
   - Code review expectations

**Output**: Template files in .github/ directory

### Step 7: Integrations and Webhooks

Set up external integrations:

1. **Notion Integration**:
   - Configure webhook for issue creation
   - Set up repository linking in Notion
   - Configure automatic status updates
   - Link commits to Notion tasks

2. **Code Quality Integrations**:
   - Configure automated code review tools
   - Set up security scanning services
   - Enable dependency update automation
   - Configure code coverage reporting

3. **Deployment Integrations**:
   - Configure deployment webhooks
   - Set up environment-specific deployments
   - Configure rollback mechanisms
   - Set up monitoring integrations

**Output**: Integration configuration summary

### Step 8: Team Access and Permissions

Configure team access and permissions:

1. **Team Member Access**:
   - Add specified team members with appropriate roles
   - Configure team-based permissions
   - Set up code review assignments
   - Configure notification preferences

2. **External Collaborator Access**:
   - Add external collaborators with limited permissions
   - Configure specific repository access
   - Set up review requirements for external contributions
   - Configure security restrictions

**Output**: Team access configuration summary

### Step 9: Local Repository Setup

Prepare local development environment:

1. **Repository Cloning**:
   - Clone repository to local development directory
   - Set up remote tracking branches
   - Configure local git settings
   - Set up development branch

2. **Development Environment**:
   - Install required dependencies
   - Set up environment configuration
   - Configure development tools
   - Run initial setup scripts

3. **IDE Integration**:
   - Configure VS Code settings
   - Set up debugging configuration
   - Configure code formatting and linting
   - Set up testing integration

**Output**: Local repository setup confirmation

### Step 10: Documentation and Handover

Create comprehensive repository documentation:

1. **README.md Enhancement**:
   - Project overview and purpose
   - Installation and setup instructions
   - Usage examples and API documentation
   - Contributing guidelines
   - License information

2. **Development Documentation**:
   - Architecture overview
   - Development setup guide
   - Testing procedures
   - Deployment instructions
   - Troubleshooting guide

3. **Update Notion Project**:
   - Link repository URL to Notion project
   - Create initial GitHub issues for project tasks
   - Set up bidirectional sync configuration
   - Update project status in Notion

**Output**: Complete repository documentation and Notion integration

## Success Criteria

- ✅ Repository created with proper configuration
- ✅ Project structure implemented based on template
- ✅ Branch protection rules configured
- ✅ CI/CD workflows operational
- ✅ Issue and PR templates created
- ✅ External integrations configured
- ✅ Team access properly set up
- ✅ Local development environment ready
- ✅ Documentation complete and current
- ✅ Notion integration active

## Error Handling

- **Repository Creation Failure**: Check naming conflicts, permissions, and organization access
- **Template Setup Issues**: Verify template compatibility, fix file structure issues
- **Integration Failures**: Validate API keys, check service availability, retry configurations
- **Permission Issues**: Verify GitHub organization settings, check team memberships

## Dependencies

- GitHub API access and permissions
- Organization or personal account access
- Template repositories and configurations
- External service API keys for integrations
- Local development environment setup

## Post-Creation Tasks

- First commit and push
- Initial issue creation from Notion tasks  
- Team onboarding and access verification
- CI/CD pipeline testing
- Integration testing and validation