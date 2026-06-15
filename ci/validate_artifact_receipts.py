#!/usr/bin/env python3
"""
Validate that every artifact has a corresponding QA receipt.
"""

import json
import sys
from pathlib import Path

ARTIFACTS_DIR = Path("artifacts")
RECEIPTS_DIR = Path("receipts")

def validate_artifact_receipts():
    """Check that all artifacts have receipts."""
    if not ARTIFACTS_DIR.exists():
        print("⚠ Artifacts directory not found (skipping)")
        return True

    artifacts_file = ARTIFACTS_DIR / "artifacts.jsonl"
    receipts_file = RECEIPTS_DIR / "qa_receipts.jsonl"

    if not artifacts_file.exists():
        print("⚠ artifacts.jsonl not found (skipping)")
        return True

    # Load artifacts
    artifact_ids = set()
    with open(artifacts_file, 'r') as f:
        for line in f:
            if line.strip():
                entry = json.loads(line)
                artifact_ids.add(entry.get('artifact_id'))

    # Load receipts
    receipt_artifact_ids = set()
    if receipts_file.exists():
        with open(receipts_file, 'r') as f:
            for line in f:
                if line.strip():
                    entry = json.loads(line)
                    receipt_artifact_ids.add(entry.get('artifact_id'))

    # Check for missing receipts
    missing_receipts = artifact_ids - receipt_artifact_ids
    if missing_receipts:
        print(f"✗ {len(missing_receipts)} artifacts missing receipts")
        for artifact_id in missing_receipts:
            print(f"  - {artifact_id}")
        return False
    else:
        print(f"✓ All {len(artifact_ids)} artifacts have receipts")
        return True

if __name__ == "__main__":
    sys.exit(0 if validate_artifact_receipts() else 1)
