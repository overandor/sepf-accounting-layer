# {{project_name}} - R&D Artifact Repo

**Project ID**: {{project_id}}
**Business Component**: {{business_component}}
**Proof Tier**: {{proof_tier}}
**Recognition Status**: {{recognition_status}}

---

## README.md

### Project Summary

**Objective**: {{objective}}
**Technical Uncertainty**: {{technical_uncertainty}}
**Permitted Purpose**: {{permitted_purpose}}

### Artifact Overview

This repo contains AI-assisted R&D artifacts for {{business_component}}.

**Disclaimer**: This is an R&D artifact candidate. External accounting, tax, lender, buyer, or legal acceptance is required before it becomes formal collateral or recognized value.

### Quick Start

```bash
# Clone repo
git clone {{repo_url}}

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/

# Build attestation
npm run build
```

### Repo Structure

```
.
├── README.md
├── RND_MEMO.md
├── SPEC.md
├── CLAIMS.yaml
├── EXPERIMENT_LOG.jsonl
├── VALUATION.yaml
├── QA_RECEIPTS.jsonl
├── PROVENANCE.md
├── COLLATERAL_PACKET.md
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── attest.yml
└── src/
    └── {{project_id}}/
```

---

## RND_MEMO.md

### Business Component

**Component Name**: {{business_component}}
**Current State**: {{current_state}}
**Target State**: {{target_state}}
**Business Value**: {{business_value}}

### Technical Uncertainty

**Uncertainty Description**:
{{uncertainty_description}}

**Why Unknown**:
{{why_unknown}}

**Impact if Unresolved**:
{{impact_if_unresolved}}

### Experimentation Process

**Hypothesis**:
{{hypothesis}}

**Design Attempts**:
{{design_attempts}}

**Model Changes**:
{{model_changes}}

**Bug Fixes**:
{{bug_fixes}}

**Backtests**:
{{backtests}}

**Dry Runs**:
{{dry_runs}}

**CI Checks**:
{{ci_checks}}

### Permitted Purpose

- [ ] Performance
- [ ] Reliability
- [ ] Quality
- [ ] Functionality

### Alternatives Tested

{{alternatives_tested}}

### Failure or Repair Log

{{failure_repair_log}}

### Artifact Created

**Artifact Type**: {{artifact_type}}
**Artifact ID**: {{artifact_id}}
**Artifact Hash**: {{artifact_hash}}

### CI Result

**Status**: {{ci_status}}
**Run ID**: {{ci_run_id}}
**Build Digest**: {{build_digest}}

### Claim Labels

- Verified: {{verified_claims}}
- User-Claimed: {{user_claimed_claims}}
- Inferred: {{inferred_claims}}
- Blocked: {{blocked_claims}}

### Accounting Boundary

**Recognition Status**: {{recognition_status}}
**Valuation Basis**: {{valuation_basis}}
**Low/Base/High**: ${{valuation_low}} / ${{valuation_base}} / ${{valuation_high}}

### Tax Review Required

- [ ] Yes - Requires tax professional review
- [ ] No - Not tax credit eligible
- [ ] Pending - Awaiting tax review

---

## SPEC.md

### Specification

**Artifact Type**: {{artifact_type}}
**Version**: {{version}}

### Requirements

{{requirements}}

### Design

{{design}}

### Implementation

{{implementation}}

### Testing

{{testing}}

---

## CLAIMS.yaml

```yaml
claims:
  - claim_id: CLM-000001
    claim_text: "{{claim_text_1}}"
    claim_label: verified
    evidence_refs:
      - source_file: {{source_file}}
        line_number: {{line_number}}
    risk_level: low

  - claim_id: CLM-000002
    claim_text: "{{claim_text_2}}"
    claim_label: user_claimed
    evidence_refs: []
    risk_level: medium

blocked_claims:
  - hidden_model_weight_contribution
  - provider_savings_without_records
  - tax_credit_eligibility_without_review
```

---

## EXPERIMENT_LOG.jsonl

```jsonl
{"experiment_id": "EXP-000001", "hypothesis": "{{hypothesis}}", "test_method": "{{test_method}}", "result": "{{result}}", "timestamp": "{{timestamp}}"}
{"experiment_id": "EXP-000002", "hypothesis": "{{hypothesis}}", "test_method": "{{test_method}}", "result": "{{result}}", "timestamp": "{{timestamp}}"}
```

---

## VALUATION.yaml

```yaml
valuation_basis: replacement_cost
labor_components:
  artifact_labor:
    hours: {{artifact_labor_hours}}
    rate: {{hourly_rate}}
    cost: {{artifact_labor_cost}}
  evaluation_labor:
    hours: {{evaluation_labor_hours}}
    rate: {{hourly_rate}}
    cost: {{evaluation_labor_cost}}
  product_feedback:
    hours: {{feedback_hours}}
    rate: {{hourly_rate}}
    cost: {{feedback_cost}}
  protocol_design:
    hours: {{protocol_hours}}
    rate: {{hourly_rate}}
    cost: {{protocol_cost}}

total_labor_cost: {{total_labor_cost}}

adjustments:
  uncertainty_discount: 0.30
  duplication_discount: 0.10
  ownership_risk_discount: 0.15
  external_validation_premium: 0.00
  monetization_premium: 0.00

net_adjustments: {{net_adjustments}}

final_valuation:
  low_usd: {{valuation_low}}
  base_usd: {{valuation_base}}
  high_usd: {{valuation_high}}

error_band: {{error_band}}
confidence: {{confidence}}

assumptions:
  - {{assumption_1}}
  - {{assumption_2}}
```

---

## QA_RECEIPTS.jsonl

```jsonl
{"receipt_id": "RCP-000001", "artifact_id": "{{artifact_id}}", "created": {{created}}, "verified": {{verified}}, "inferred": {{inferred}}, "blocked": {{blocked}}, "next_repo_delta": "{{next_repo_delta}}", "next_proof_upgrade": {{next_proof_upgrade}}, "receipt_hash": "{{receipt_hash}}"}
```

---

## PROVENANCE.md

### Source Chain

| Source ID | Source Type | Source Path | Hash | Timestamp |
|-----------|-------------|-------------|------|-----------|
{{source_chain}}

### Hash Chain Verification

{{hash_chain_verification}}

### CI/CD Provenance

**CI Run ID**: {{ci_run_id}}
**Commit Hash**: {{commit_hash}}
**Build Digest**: {{build_digest}}
**Attestation Bundle**: {{attestation_bundle}}

### GitHub Actions Attestation

This repo uses GitHub Actions artifact attestations to establish build provenance. Attestations are cryptographically signed claims showing where and how software was built.

---

## COLLATERAL_PACKET.md

See [COLLATERAL_PACKET.md](COLLATERAL_PACKET.md) for the full collateral packet.

---

## .github/workflows/ci.yml

```yaml
name: CI/CD

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest tests/
      - name: Lint
        run: flake8 src/
      - name: Schema validation
        run: python ci/validate_schemas.py
```

---

## .github/workflows/attest.yml

```yaml
name: Attest

on:
  workflow_run:
    workflows: [CI/CD]
    types: [completed]

jobs:
  attest:
    runs-on: ubuntu-latest
    if: ${{ github.event.workflow_run.conclusion == 'success' }}
    permissions:
      contents: write
      id-token: write
    steps:
      - uses: actions/checkout@v4
      - name: Generate attestation
        uses: actions/attest-build-provenance@v1
        with:
          subject-path: './dist/*'
```

---

## References

- IAS 38 Intangible Assets: https://www.ifrs.org/issued-standards/list-of-standards/ias-38-intangible-assets/
- IRS Research Credit: https://www.irs.gov/businesses/audit-techniques-guide-credit-for-increasing-research-activities
- GitHub Actions Attestations: https://docs.github.com/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds
- SLSA: https://slsa.dev/
