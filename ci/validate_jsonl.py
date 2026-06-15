#!/usr/bin/env python3
"""
Validate JSONL files in accounting, rnd, provenance, and collateral directories.
"""

import json
import sys
from pathlib import Path

DIRECTORIES = ['accounting', 'rnd', 'provenance', 'collateral']

def validate_jsonl_file(filepath):
    """Validate a single JSONL file."""
    try:
        with open(filepath, 'r') as f:
            for line_num, line in enumerate(f, 1):
                if line.strip():
                    json.loads(line)
        print(f"✓ {filepath.name}: Valid JSONL")
        return True
    except json.JSONDecodeError as e:
        print(f"✗ {filepath.name}: Invalid JSONL at line {line_num} - {e}")
        return False

def main():
    """Validate all JSONL files."""
    all_valid = True
    for directory in DIRECTORIES:
        dir_path = Path(directory)
        if not dir_path.exists():
            continue

        jsonl_files = list(dir_path.glob("*.jsonl"))
        for filepath in jsonl_files:
            if not validate_jsonl_file(filepath):
                all_valid = False

    if all_valid:
        print("\n✓ All JSONL files validated successfully")
        sys.exit(0)
    else:
        print("\n✗ Some JSONL files failed validation")
        sys.exit(1)

if __name__ == "__main__":
    main()
