# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains a sophisticated Claude Code integration setup with automated hooks, custom slash commands, and comprehensive tooling for Python, JavaScript, PHP, and YAML development.

## Development Commands

### Python Development
- **Format and lint**: Code is automatically formatted with `black` and `isort`, type-checked with `mypy`
- **Test execution**: `pytest` for running tests
- **Style checking**: `pylint` for code quality analysis
- **Type checking**: `mypy` for static type analysis

### Available Bash Commands
The following commands are pre-approved in the settings:
- `black *` - Python code formatting
- `pytest *` - Run Python tests
- `mypy *` - Type checking
- `pylint *` - Code linting
- `isort *` - Import sorting
- `docker *` and `docker compose *` - Container operations
- `git *` - Git operations
- `python *` - Python script execution

## Hook System Architecture

### Pre-Tool Use Hooks
Validation hooks run before file modifications:
- **Python files**: Validates max 500 lines, security checks, required imports
- **JavaScript/JSX files**: Code validation before changes
- **PHP files**: Pre-modification validation
- **YAML files**: Schema validation

### Post-Tool Use Hooks
Formatting and quality checks after file modifications:
- **Python files**: Runs `black`, `isort`, and `mypy` automatically
- **JavaScript/JSX files**: Code formatting and linting
- **PHP files**: Code formatting

### Stop Hooks
Session cleanup operations run when stopping Claude Code sessions.

## Custom Slash Commands

### `/test`
Creates comprehensive test suites with:
- Unit tests for each method and function
- Edge cases and error conditions
- Mock dependencies for isolation
- Parametrized tests for different scenarios
- Target: 90%+ code coverage

### `/implement`
Implements components following strict patterns:
- Clear class hierarchies with proper inheritance
- Interface definitions with type annotations
- Dependency injection patterns
- Error handling and logging
- Maximum 50 lines per method
- Comprehensive docstrings

### `/document`
Generates detailed component documentation:
- Component purpose and responsibilities
- Class and method descriptions
- Interface specifications
- Usage examples and configuration options
- Markdown formatting with code examples

## Development Environment

### Python Configuration
- **PYTHONPATH**: Automatically includes `${PWD}/src`
- **Code Quality**: Enforced through automated hooks
- **Security**: Prevents `os.system()` usage and other security anti-patterns

### File Organization
- Hooks located in `.claude/hooks/` with language-specific subdirectories
- Logs stored in `.claude/logs/` with session summaries and transcripts
- Settings in `.claude/settings.json` and `.claude/settings.local.json`

## Quality Standards

### Code Requirements
- Maximum 500 lines per Python file
- Type annotations required for all functions and classes
- Comprehensive docstrings for all public methods
- No methods longer than 50 lines
- Security-conscious coding (no shell injection vulnerabilities)

### Testing Standards
- Minimum 90% test coverage
- Proper fixture setup and teardown
- Clear test case descriptions
- Edge case and error condition coverage

## Important Notes
- All file modifications trigger automatic formatting and validation
- The hook system ensures code quality without manual intervention
- Custom commands provide templated approaches for common development tasks
- Multiple programming languages are supported with consistent tooling patterns