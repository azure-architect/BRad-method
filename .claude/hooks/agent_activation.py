#!/usr/bin/env python3
"""
Claude Hook: Agent Activation System
Manages dynamic activation of BRad Method agents
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
        content = file_path.read_text()

        # Extract YAML block
        yaml_match = re.search(r"```yaml\n(.*?)\n```", content, re.DOTALL)
        if not yaml_match:
            return None

        try:
            agent_config = yaml.safe_load(yaml_match.group(1))

            # Extract agent metadata
            agent_data = {
                "id": agent_config.get("agent", {}).get("id", file_path.stem),
                "name": agent_config.get("agent", {}).get("name", file_path.stem),
                "title": agent_config.get("agent", {}).get("title", ""),
                "icon": agent_config.get("agent", {}).get("icon", "🤖"),
                "whenToUse": agent_config.get("agent", {}).get("whenToUse", ""),
                "file_path": str(file_path),
                "config": agent_config,
                "activation_instructions": agent_config.get(
                    "activation-instructions", []
                ),
                "commands": agent_config.get("commands", []),
                "persona": agent_config.get("persona", {}),
            }

            return agent_data

        except yaml.YAMLError as e:
            print(f"Error parsing YAML in {file_path}: {e}", file=sys.stderr)
            return None

    def list_agents(self) -> List[Dict[str, str]]:
        """Get list of available agents for display"""
        agents_list: List[Dict[str, str]] = []
        for agent_id, agent_data in self.agents.items():
            agents_list.append(
                {
                    "id": agent_id,
                    "name": agent_data["name"],
                    "title": agent_data["title"],
                    "icon": agent_data["icon"],
                    "whenToUse": agent_data["whenToUse"],
                }
            )
        return sorted(agents_list, key=lambda x: x["name"])

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
        response += "**Example:** `@brad-master` or `@notion-agent`"
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
    if len(sys.argv) < 2:
        return

    # Get the command from user prompt
    user_input = " ".join(sys.argv[1:])

    # Initialize registry
    registry = AgentRegistry()
    registry.discover_agents()
    registry._load_state()

    # Check for agent commands
    response = handle_agent_command(user_input, registry)

    if response:
        print(f"\n🎯 **Agent System Response:**\n{response}\n")


if __name__ == "__main__":
    main()
