#!/usr/bin/env python3
"""
Check that source files have hash values in provenance manifests.
"""

import json
import hashlib
import sys
from pathlib import Path

PROVENANCE_DIR = Path("provenance")

def check_source_hashes():
    """Check source hashes in manifest files."""
    if not PROVENANCE_DIR.exists():
        print("⚠ Provenance directory not found (skipping)")
        return True

    manifest_files = list(PROVENANCE_DIR.glob("*.jsonl"))
    all_valid = True

    for manifest_file in manifest_files:
        with open(manifest_file, 'r') as f:
            for line in f:
                if line.strip():
                    entry = json.loads(line)
                    source_hash = entry.get('source_hash')
                    if not source_hash or len(source_hash) != 64:
                        print(f"✗ {manifest_file.name}: Invalid or missing source hash")
                        all_valid = False
                    else:
                        print(f"✓ {manifest_file.name}: Valid source hash")

    if all_valid:
        print("\n✓ All source hashes validated")
        return True
    else:
        print("\n✗ Some source hashes failed validation")
        return False

if __name__ == "__main__":
    sys.exit(0 if check_source_hashes() else 1)
