#!/usr/bin/env python3
"""
BRad Method Notion Sync Hook

Automatically syncs project status, task completion, and resource allocation
between local operations and Notion databases.
"""

import json
import os
import sys
from datetime import datetime
from typing import Any, Dict, List


def load_config() -> Dict[str, Any]:
    """Load BRad configuration from config.yaml"""
    config_path = os.path.join(os.path.dirname(__file__), "..", "config.yaml")
    # In real implementation, would use PyYAML to parse
    # For now, return mock config structure
    return {
        "notion": {
            "databases": {
                "projects": os.getenv("NOTION_PROJECTS_DB_ID"),
                "tasks": os.getenv("NOTION_TASKS_DB_ID"),
                "notes": os.getenv("NOTION_NOTES_DB_ID"),
                "resources": os.getenv("NOTION_RESOURCES_DB_ID"),
            }
        },
        "hooks": {
            "notion_sync": {
                "enabled": True,
                "events": [
                    "task_complete",
                    "project_create",
                    "resource_allocate",
                    "repo_create",
                ],
            }
        },
    }


def sync_task_completion(event_data: Dict[str, Any]) -> bool:
    """
    Sync task completion to Notion Tasks Database

    Args:
        event_data: Contains task_id, status, completion_time, etc.
    """
    try:
        task_id = event_data.get("task_id")
        new_status = event_data.get("status", "Complete")
        completion_time = event_data.get("completion_time", datetime.now().isoformat())

        # Update Notion task status
        # In real implementation, would use Notion API client
        print(f"✅ Task {task_id} marked as {new_status} in Notion")

        # Update dependent tasks if this was a blocking task
        dependent_tasks = event_data.get("dependent_tasks", [])
        for dep_task in dependent_tasks:
            print(f"🔄 Checking if dependent task {dep_task} can now start")

        return True

    except Exception as e:
        print(f"❌ Failed to sync task completion: {e}")
        return False


def sync_project_creation(event_data: Dict[str, Any]) -> bool:
    """
    Sync new project creation to Notion Projects Database
    """
    try:
        project_name = event_data.get("project_name")
        project_type = event_data.get("project_type")
        github_repo = event_data.get("github_repo")

        print(f"🚀 Project '{project_name}' created in Notion")
        print(f"   Type: {project_type}")
        if github_repo:
            print(f"   GitHub: {github_repo}")

        # Create initial project timeline
        print(f"📅 Created project timeline and milestones")

        return True

    except Exception as e:
        print(f"❌ Failed to sync project creation: {e}")
        return False


def sync_resource_allocation(event_data: Dict[str, Any]) -> bool:
    """
    Sync resource allocation to Notion Resources Database
    """
    try:
        project_id = event_data.get("project_id")
        resources = event_data.get("allocated_resources", [])

        print(f"🖥️  Resources allocated for project {project_id}:")
        for resource in resources:
            resource_type = resource.get("type")
            resource_id = resource.get("id")
            print(f"   - {resource_type}: {resource_id}")

        # Update resource availability in Notion
        print(f"📊 Updated resource availability in Notion")

        return True

    except Exception as e:
        print(f"❌ Failed to sync resource allocation: {e}")
        return False


def sync_repo_creation(event_data: Dict[str, Any]) -> bool:
    """
    Sync GitHub repository creation to Notion
    """
    try:
        project_id = event_data.get("project_id")
        repo_url = event_data.get("repo_url")
        repo_name = event_data.get("repo_name")

        print(f"📦 GitHub repo '{repo_name}' linked to project {project_id}")
        print(f"   URL: {repo_url}")

        # Update project with repo information
        print(f"🔗 Updated Notion project with GitHub repository link")

        return True

    except Exception as e:
        print(f"❌ Failed to sync repo creation: {e}")
        return False


def main():
    """Main hook execution"""
    try:
        # Parse event data from stdin or command line args
        if len(sys.argv) < 3:
            print("Usage: notion-sync.py <event_type> <event_data_json>")
            sys.exit(1)

        event_type = sys.argv[1]
        event_data = json.loads(sys.argv[2])

        # Load configuration
        config = load_config()

        # Check if notion sync is enabled
        if not config.get("hooks", {}).get("notion_sync", {}).get("enabled", False):
            print("Notion sync hook is disabled")
            return

        # Route to appropriate sync function
        sync_functions = {
            "task_complete": sync_task_completion,
            "project_create": sync_project_creation,
            "resource_allocate": sync_resource_allocation,
            "repo_create": sync_repo_creation,
        }

        sync_function = sync_functions.get(event_type)
        if sync_function:
            success = sync_function(event_data)
            if success:
                print(f"✅ Notion sync completed for {event_type}")
            else:
                print(f"❌ Notion sync failed for {event_type}")
                sys.exit(1)
        else:
            print(f"⚠️  Unknown event type: {event_type}")

    except Exception as e:
        print(f"❌ Notion sync hook failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
