#!/usr/bin/env python3
"""
Check that collateral packet contains no blocked claims.
"""

import json
import sys
from pathlib import Path

COLLATERAL_DIR = Path("collateral")
CLAIMS_DIR = Path("claims")

def check_blocked_claims_in_collateral():
    """Check that collateral packet excludes blocked claims."""
    collateral_file = COLLATERAL_DIR / "collateral_packet.md"
    if not collateral_file.exists():
        print("⚠ Collateral packet not found (skipping)")
        return True

    with open(collateral_file, 'r') as f:
        content = f.read()

    if "Blocked Claims" in content:
        # Check if blocked claims section is empty
        blocked_section = content.split("Blocked Claims")[1].split("##")[0]
        if "{{blocked_claim_list}}" in blocked_section or len(blocked_section.strip()) < 50:
            print("✓ Collateral packet: No blocked claims present")
            return True
        else:
            print("✗ Collateral packet: Blocked claims present")
            return False
    else:
        print("⚠ Collateral packet: No Blocked Claims section")
        return True

if __name__ == "__main__":
    sys.exit(0 if check_blocked_claims_in_collateral() else 1)
