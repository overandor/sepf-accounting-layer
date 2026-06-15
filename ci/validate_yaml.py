#!/usr/bin/env python3
"""
Validate YAML files in accounting, rnd, provenance, and collateral directories.
"""

import yaml
import sys
from pathlib import Path

DIRECTORIES = ['accounting', 'rnd', 'provenance', 'collateral']

def validate_yaml_file(filepath):
    """Validate a single YAML file."""
    try:
        with open(filepath, 'r') as f:
            data = yaml.safe_load(f)
        print(f"✓ {filepath.name}: Valid YAML")
        return True, data
    except yaml.YAMLError as e:
        print(f"✗ {filepath.name}: Invalid YAML - {e}")
        return False, None

def main():
    """Validate all YAML files."""
    all_valid = True
    for directory in DIRECTORIES:
        dir_path = Path(directory)
        if not dir_path.exists():
            print(f"⚠ {directory}: Directory not found (skipping)")
            continue

        yaml_files = list(dir_path.glob("*.yaml")) + list(dir_path.glob("*.yml"))
        for filepath in yaml_files:
            valid, _ = validate_yaml_file(filepath)
            if not valid:
                all_valid = False

    if all_valid:
        print("\n✓ All YAML files validated successfully")
        sys.exit(0)
    else:
        print("\n✗ Some YAML files failed validation")
        sys.exit(1)

if __name__ == "__main__":
    main()
