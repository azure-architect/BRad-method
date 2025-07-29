#!/usr/bin/env python3
"""
Claude Hook: Agent Activation System V2
Fixed version that properly reads from stdin
"""

import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    import yaml  # type: ignore
except ImportError:
    print(
        "Warning: PyYAML not available. Agent activation requires PyYAML.",
        file=sys.stderr,
    )
    sys.exit(1)


class AgentRegistry:
    """Registry for discovering and managing BRad Method agents"""

    def __init__(self, agents_dir: str = ".brad-core/agents") -> None:
        self.agents_dir = Path(agents_dir)
        self.agents: Dict[str, Dict[str, Any]] = {}
        self.active_agent: Optional[str] = None
        self.state_file = Path(".claude/agent_state.json")

    def discover_agents(self) -> Dict[str, Dict[str, Any]]:
        """Discover all agent definition files"""
        agents: Dict[str, Dict[str, Any]] = {}

        if not self.agents_dir.exists():
            return agents

        for agent_file in self.agents_dir.glob("*.md"):
            try:
                agent_data = self._parse_agent_file(agent_file)
                if agent_data:
                    agents[agent_data["id"]] = agent_data
            except Exception as e:
                print(f"Warning: Failed to parse {agent_file}: {e}", file=sys.stderr)

        self.agents = agents
        return agents

    def _parse_agent_file(self, file_path: Path) -> Optional[Dict[str, Any]]:
        """Parse agent definition from markdown file"""
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Look for YAML blocks in the markdown
        yaml_pattern = r"```yaml\s*(.*?)\s*```"
        yaml_blocks = re.findall(yaml_pattern, content, re.DOTALL)

        for block in yaml_blocks:
            try:
                data = yaml.safe_load(block)
                if data and isinstance(data, dict) and "agent" in data:
                    agent_info = data["agent"]

                    # Add persona data if available
                    if "persona" in data:
                        agent_info["persona"] = data["persona"]
                    else:
                        agent_info["persona"] = {}

                    # Add commands if available
                    if "commands" in data:
                        agent_info["commands"] = data["commands"]

                    # Set file path for reference
                    agent_info["file_path"] = str(file_path)

                    return agent_info
            except yaml.YAMLError:
                continue

        return None

    def list_agents(self) -> List[Dict[str, str]]:
        """List all discovered agents with key info"""
        agent_list: List[Dict[str, str]] = []

        for agent_id, agent_data in self.agents.items():
            agent_list.append(
                {
                    "id": agent_id,
                    "name": agent_data.get("name", "Unknown"),
                    "title": agent_data.get("title", ""),
                    "icon": agent_data.get("icon", "🤖"),
                    "whenToUse": agent_data.get("whenToUse", ""),
                }
            )

        return sorted(agent_list, key=lambda x: x["name"])

    def activate_agent(self, agent_id: str) -> Optional[Dict[str, Any]]:
        """Activate a specific agent"""
        if agent_id not in self.agents:
            return None

        self.active_agent = agent_id
        self._save_state()
        return self.agents[agent_id]

    def get_active_agent(self) -> Optional[Dict[str, Any]]:
        """Get currently active agent"""
        if self.active_agent and self.active_agent in self.agents:
            return self.agents[self.active_agent]
        return None

    def deactivate_agent(self) -> None:
        """Deactivate current agent"""
        self.active_agent = None
        self._save_state()

    def _save_state(self) -> None:
        """Save current agent state"""
        state = {"active_agent": self.active_agent, "last_updated": str(Path.cwd())}

        os.makedirs(self.state_file.parent, exist_ok=True)
        with open(self.state_file, "w") as f:
            json.dump(state, f, indent=2)

    def _load_state(self) -> None:
        """Load saved agent state"""
        if self.state_file.exists():
            try:
                with open(self.state_file, "r") as f:
                    state = json.load(f)
                    self.active_agent = state.get("active_agent")
            except Exception:
                pass


def handle_agent_command(command: str, registry: AgentRegistry) -> str:
    """Handle agent activation commands"""
    # Debug logging
    with open(".claude/agent_debug.log", "a") as f:
        f.write(f"Received command: {repr(command)}\n")

    parts = command.strip().split()

    if not parts:
        return ""

    cmd = parts[0].lower()

    # Handle special commands first
    if cmd == "@list-agents":
        agents = registry.list_agents()
        if not agents:
            return "No agents found in .brad-core/agents/"

        response = "🤖 **Available BRad Method Agents:**\n\n"
        for i, agent in enumerate(agents, 1):
            response += f"{i}. {agent['icon']} **{agent['name']}** (`@{agent['id']}`)\n"
            response += f"   {agent['title']}\n"
            if agent["whenToUse"]:
                response += f"   *{agent['whenToUse']}*\n"
            response += "\n"

        response += "**Usage:** Type `@agent-id` to activate an agent\n"
        response += "**Example:** `@master` or `@notion`"
        return response

    elif cmd == "@deactivate":
        active = registry.get_active_agent()
        if active:
            registry.deactivate_agent()
            return f"✅ Deactivated {active['name']}. Returned to Claude Code."
        else:
            return "ℹ️ No agent currently active."

    elif cmd == "@status":
        active = registry.get_active_agent()
        if active:
            return f"🔹 **Active Agent:** {active['icon']} {active['name']}"
        else:
            return "🔹 **Active Agent:** None (Claude Code default)"

    # Handle agent activation
    elif cmd.startswith("@") and len(cmd) > 1:
        agent_id = cmd[1:]  # Remove @ prefix

        # Handle simplified names
        simplified_map = {
            "master": "brad-master",
            "notion": "notion-agent",
            "github": "github-agent",
            "idea": "idea-man",
            "project": "project-manager-agent",
            "pxm": "pxm-master",
            "video": "video-ingestion",
        }

        # Check if it's a simplified name
        if agent_id in simplified_map:
            agent_id = simplified_map[agent_id]

        agent_data = registry.activate_agent(agent_id)

        if not agent_data:
            available = [f"@{aid}" for aid in registry.agents.keys()]
            return f"❌ Agent '{agent_id}' not found. Available: {', '.join(available)}"

        # Generate activation response
        response = f"{agent_data['icon']} **{agent_data['name']} Activated**\n\n"
        response += f"**Role:** {agent_data['persona'].get('role', 'Agent')}\n"

        if agent_data["persona"].get("identity"):
            response += f"**Identity:** {agent_data['persona']['identity']}\n"

        # Show available commands
        commands = agent_data.get("commands", [])
        if commands:
            response += f"\n**Available Commands:**\n"
            for i, cmd_item in enumerate(commands, 1):
                if isinstance(cmd_item, str):
                    response += f"{i}. `{cmd_item}`\n"
                elif isinstance(cmd_item, dict):
                    cmd_name = list(cmd_item.keys())[0]
                    cmd_desc = cmd_item[cmd_name]
                    response += f"{i}. `{cmd_name}` - {cmd_desc}\n"

        response += f"\n**Deactivate:** Type `@deactivate` to return to Claude Code"
        return response

    return ""


def main() -> None:
    """Main hook execution"""
    # Read user input from stdin (how Claude Code passes it)
    try:
        # Try reading from stdin first
        user_input = sys.stdin.read().strip()
        if not user_input and len(sys.argv) > 1:
            # Fallback to command line args
            user_input = " ".join(sys.argv[1:])
    except Exception as e:
        # Log error for debugging
        with open(".claude/agent_debug.log", "a") as f:
            f.write(f"Error reading input: {e}\n")
        return

    if not user_input:
        return

    # Initialize registry
    registry = AgentRegistry()
    registry.discover_agents()
    registry._load_state()

    # Check for agent commands
    response = handle_agent_command(user_input, registry)

    if response:
        # Output to stdout for Claude Code to display
        print(response)
        sys.stdout.flush()


if __name__ == "__main__":
    main()
