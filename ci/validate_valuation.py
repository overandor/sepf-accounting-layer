#!/usr/bin/env python3
"""
Validate that valuation entries have low/base/high structure.
"""

import json
import sys
from pathlib import Path

VALUATION_DIR = Path("valuation")

def validate_valuation_structure():
    """Check that valuations have low/base/high."""
    if not VALUATION_DIR.exists():
        print("⚠ Valuation directory not found (skipping)")
        return True

    valuation_file = VALUATION_DIR / "replacement_cost.yaml"
    if not valuation_file.exists():
        print("⚠ replacement_cost.yaml not found (skipping)")
        return True

    import yaml
    with open(valuation_file, 'r') as f:
        data = yaml.safe_load(f)

    required_fields = ['low_usd', 'base_usd', 'high_usd', 'error_band', 'confidence']
    all_valid = True

    for field in required_fields:
        if field not in data:
            print(f"✗ Missing required field: {field}")
            all_valid = False
        else:
            print(f"✓ Valuation has {field}")

    # Check that low <= base <= high
    if all_valid:
        low = data.get('low_usd', 0)
        base = data.get('base_usd', 0)
        high = data.get('high_usd', 0)

        if not (low <= base <= high):
            print(f"✗ Valuation range invalid: low={low}, base={base}, high={high}")
            all_valid = False
        else:
            print(f"✓ Valuation range valid: {low} <= {base} <= {high}")

    if all_valid:
        print("\n✓ Valuation structure validated")
        return True
    else:
        print("\n✗ Valuation structure failed validation")
        return False

if __name__ == "__main__":
    sys.exit(0 if validate_valuation_structure() else 1)
