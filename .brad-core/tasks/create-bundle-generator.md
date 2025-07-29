# Task: Create Bundle Generator

## Objective
Build automated script to convert Brad Method agent files into BMAD-style self-contained bundles.

## Prerequisites
- Completed bundle format design
- Python environment with YAML support
- Access to all agent files and dependencies

## Steps

### 1. Core Generator Script
- [ ] Create `bundle_generator.py` main script
- [ ] Implement agent file parser
- [ ] Build YAML extraction logic
- [ ] Create bundle assembly function
- [ ] Add file I/O handling

### 2. Dependency Resolution
- [ ] Build dependency scanner
- [ ] Implement recursive dependency loader
- [ ] Create resource path resolver
- [ ] Handle missing dependencies gracefully
- [ ] Add circular dependency detection

### 3. Resource Embedding
- [ ] Implement file content reader
- [ ] Create START/END tag generator
- [ ] Build resource section formatter
- [ ] Add content validation
- [ ] Optimize large file handling

### 4. Bundle Validation
- [ ] Create format validator
- [ ] Implement YAML syntax checker
- [ ] Add resource completeness check
- [ ] Build activation instruction validator
- [ ] Create error reporting system

### 5. CLI Interface
- [ ] Add command-line argument parsing
- [ ] Implement batch conversion mode
- [ ] Create single agent conversion
- [ ] Add verbose/quiet modes
- [ ] Include dry-run option

## Script Structure
```python
#!/usr/bin/env python3
"""
Brad to BMAD Bundle Generator
Converts Brad Method agents to self-contained bundles
"""

import yaml
import argparse
from pathlib import Path
from typing import Dict, List, Set

class BundleGenerator:
    def __init__(self, brad_root: Path):
        self.brad_root = brad_root
        self.agents_dir = brad_root / ".brad-core" / "agents"
        self.loaded_resources: Set[str] = set()
    
    def generate_bundle(self, agent_id: str) -> str:
        """Generate complete bundle for an agent"""
        # Load agent definition
        # Extract YAML configuration
        # Resolve dependencies
        # Embed resources
        # Generate final bundle
        pass
    
    def resolve_dependencies(self, deps: Dict) -> List[str]:
        """Recursively resolve all dependencies"""
        pass
    
    def embed_resource(self, resource_path: str) -> str:
        """Embed a resource with START/END tags"""
        pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("agent", help="Agent ID to convert")
    parser.add_argument("-o", "--output", help="Output file path")
    parser.add_argument("-a", "--all", action="store_true", 
                       help="Convert all agents")
    args = parser.parse_args()
    
    generator = BundleGenerator(Path("."))
    # Implementation...
```

## Deliverables
1. `bundle_generator.py` - Main conversion script
2. `requirements.txt` - Python dependencies
3. `test_bundles/` - Test output directory
4. `generator_tests.py` - Unit tests
5. `README-generator.md` - Usage documentation

## Success Criteria
- Accurately converts all agent types
- Handles all dependency types
- Produces valid BMAD bundles
- Clear error messages
- Efficient processing

## Time Estimate
6-8 hours