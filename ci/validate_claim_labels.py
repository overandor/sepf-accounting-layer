#!/usr/bin/env python3
"""
Validate that all major claims have proper labels.
"""

import json
import sys
from pathlib import Path

CLAIMS_DIR = Path("claims")

VALID_LABELS = ['verified', 'user_claimed', 'inferred', 'unknown', 'quarantined', 'blocked', 'externally_validated', 'monetized']

def validate_claim_labels():
    """Check that all claims have valid labels."""
    if not CLAIMS_DIR.exists():
        print("⚠ Claims directory not found (skipping)")
        return True

    claims_file = CLAIMS_DIR / "claims.jsonl"
    if not claims_file.exists():
        print("⚠ claims.jsonl not found (skipping)")
        return True

    all_valid = True
    with open(claims_file, 'r') as f:
        for line_num, line in enumerate(f, 1):
            if line.strip():
                entry = json.loads(line)
                claim_label = entry.get('claim_label')
                if claim_label not in VALID_LABELS:
                    print(f"✗ Line {line_num}: Invalid claim label '{claim_label}'")
                    all_valid = False
                else:
                    print(f"✓ Line {line_num}: Valid claim label '{claim_label}'")

    if all_valid:
        print("\n✓ All claim labels validated")
        return True
    else:
        print("\n✗ Some claim labels failed validation")
        return False

if __name__ == "__main__":
    sys.exit(0 if validate_claim_labels() else 1)
