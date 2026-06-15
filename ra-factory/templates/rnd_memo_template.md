# R&D Memo: {{project_name}}

**Memo ID**: {{memo_id}}
**Project ID**: {{project_id}}
**Artifact ID**: {{artifact_id}}
**Generated**: {{generated_date}}
**Proof Tier**: {{proof_tier}}
**Recognition Status**: {{recognition_status}}

---

## Executive Summary

**Business Component**: {{business_component}}
**Technical Uncertainty**: {{technical_uncertainty}}
**Experiment Result**: {{experiment_result}}
**Artifact Created**: {{artifact_type}}
**CI Status**: {{ci_status}}

**Disclaimer**: This is an R&D artifact candidate. External accounting, tax, lender, buyer, or legal acceptance is required before it becomes formal collateral or recognized value.

---

## Business Component

**Component Name**: {{component_name}}
**Current State**: {{current_state}}
**Target State**: {{target_state}}
**Business Value**: {{business_value}}

**Impact Assessment**:
{{impact_assessment}}

---

## Technical Uncertainty

### Uncertainty Description

{{uncertainty_description}}

### Why This Was Unknown

{{why_unknown}}

### Impact if Unresolved

{{impact_if_unresolved}}

### Uncertainty Type

- [ ] Technological
- [ ] Process
- [ ] Design
- [ ] Performance

### Business Component Scope

Per IRS qualified research requirements, this uncertainty is applied specifically to the business component: {{business_component}}.

---

## Experimentation Process

### Hypothesis

{{hypothesis}}

### Test Methods

{{test_methods}}

### Design Attempts

{{design_attempts}}

### Model Changes

{{model_changes}}

### Bug Fixes

{{bug_fixes}}

### Backtests

{{backtests}}

### Dry Runs

{{dry_runs}}

### CI Checks

{{ci_checks}}

---

## Alternatives Tested

### Alternative 1: {{alternative_1_name}}

**Description**: {{alternative_1_description}}
**Result**: {{alternative_1_result}}
**Why Rejected**: {{alternative_1_rejection_reason}}

### Alternative 2: {{alternative_2_name}}

**Description**: {{alternative_2_description}}
**Result**: {{alternative_2_result}}
**Why Rejected**: {{alternative_2_rejection_reason}}

---

## Failure or Repair Log

### Failure 1: {{failure_1_name}}

**Date**: {{failure_1_date}}
**Description**: {{failure_1_description}}
**Root Cause**: {{failure_1_root_cause}}
**Repair Applied**: {{failure_1_repair}}
**Verification**: {{failure_1_verification}}

### Failure 2: {{failure_2_name}}

**Date**: {{failure_2_date}}
**Description**: {{failure_2_description}}
**Root Cause**: {{failure_2_root_cause}}
**Repair Applied**: {{failure_2_repair}}
**Verification**: {{failure_2_verification}}

---

## Artifact Created

### Artifact Details

**Artifact Type**: {{artifact_type}}
**Artifact ID**: {{artifact_id}}
**Title**: {{artifact_title}}
**Summary**: {{artifact_summary}}
**Artifact Hash**: {{artifact_hash}}

### Source Events

| Event ID | Source Type | Timestamp |
|----------|-------------|-----------|
{{source_events_table}}

### Reuse Potential

{{reuse_potential}}

### Financeability Score

{{financeability_score}}/1.0

---

## CI/CD Results

### Test Results

**Status**: {{ci_status}}
**Run ID**: {{ci_run_id}}
**Build Digest**: {{build_digest}}

### Validation Checks

- [ ] YAML Valid
- [ ] JSONL Valid
- [ ] Source Hash Present
- [ ] All Artifacts Have Receipts
- [ ] All Claims Labeled
- [ ] No Blocked Claims in Collateral
- [ ] Valuation Has Low/Base/High
- [ ] Proof Boundary Present
- [ ] Citations Present
- [ ] No Secrets/PII

### Build Artifacts

{{build_artifacts}}

---

## Claim Labels

### Verified Claims

{{verified_claims}}

### User-Claimed Claims

{{user_claimed_claims}}

### Inferred Claims

{{inferred_claims}}

### Unknown Claims

{{unknown_claims}}

### Blocked Claims

{{blocked_claims}}

### Externally Validated Claims

{{externally_validated_claims}}

### Monetized Claims

{{monetized_claims}}

---

## Accounting Boundary

### Recognition Status

**Current Status**: {{recognition_status}}

**Status Definitions**:
- **Evidence Only**: Raw chat or untested artifact exists
- **Internal Management Asset Candidate**: Extracted, hashed, classified, valued by replacement cost
- **Validated Collateral Candidate**: Repo exists, CI passed, provenance attached, valuation packet created
- **Externally Validated Asset**: Third party reviewed, used, bought, licensed, funded, or accepted
- **Blocked**: Ownership, legality, originality, or proof boundary failed

### Valuation Basis

**Method**: {{valuation_method}}
**Low**: ${{valuation_low}}
**Base**: ${{valuation_base}}
**High**: ${{valuation_high}}
**Error Band**: ±{{error_band}}%
**Confidence**: {{confidence}}%

### Labor Components

| Component | Hours | Rate | Cost |
|-----------|-------|------|------|
{{labor_components_table}}

### Adjustments

| Adjustment Type | Rate | Amount |
|-----------------|------|--------|
{{adjustments_table}}

### Journal Entry

**Entry ID**: {{journal_entry_id}}
**Debit**: {{debit_account}}
**Credit**: {{credit_account}}
**Amount**: ${{amount_base_usd}}
**Recognition Status**: {{recognition_status}}

---

## Tax Review Required

### IRS Qualified Research Tests

**Permitted Purpose**: {{permitted_purpose_status}}
- [ ] New or improved function
- [ ] Performance
- [ ] Reliability
- [ ] Quality

**Technological Nature**: {{technological_nature_status}}
- [ ] Relies on principles of physical or biological sciences, engineering, or computer science

**Elimination of Uncertainty**: {{elimination_of_uncertainty_status}}
- [ ] Intended to discover information that could eliminate uncertainty

**Process of Experimentation**: {{process_of_experimentation_status}}
- [ ] Systematic trial and error
- [ ] Documented experimentation

### Tax Review Status

- [ ] **Yes** - Requires tax professional review
- [ ] **No** - Not tax credit eligible
- [ ] **Pending** - Awaiting tax review

**Tax Professional Notes**:
{{tax_professional_notes}}

---

## Proof Upgrade Needed

### Required External Validation

- [ ] External reviewer
- [ ] Paid pilot
- [ ] Buyer quote
- [ ] Signed license
- [ ] Accountant review
- [ ] Tax professional review

### Monetization Paths

{{monetization_paths}}

---

## QA Receipt

```yaml
created:
{{qa_created}}

verified:
{{qa_verified}}

inferred:
{{qa_inferred}}

blocked:
{{qa_blocked}}

next_repo_delta:
{{next_repo_delta}}

next_proof_upgrade:
{{next_proof_upgrade}}
```

**Receipt Hash**: {{receipt_hash}}

---

## References

- IAS 38 Intangible Assets: https://www.ifrs.org/issued-standards/list-of-standards/ias-38-intangible-assets/
- IRS Research Credit: https://www.irs.gov/businesses/audit-techniques-guide-credit-for-increasing-research-activities
- GitHub Actions Attestations: https://docs.github.com/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds
- SLSA: https://slsa.dev/
- FASB Internal-Use Software: https://www.fasb.org/Page/Document?pdf=ASU+2025-06.pdf&title=Accounting+Standards+Update+2025-06%E2%80%94Intangibles%E2%80%94Goodwill+and+Other%E2%80%94Internal-Use+Software+%28Subtopic+350-40%29%3A+Targeted+Improvements+to+the+Accounting+for+Internal-Use+Software

---

**Disclaimer**: This R&D memo is for internal management accounting purposes. Formal recognition as intangible assets, tax credit eligibility, or collateral value requires external validation or monetization in accordance with IAS 38, IRS guidelines, and applicable accounting standards.
