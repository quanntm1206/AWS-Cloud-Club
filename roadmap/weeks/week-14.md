# Week 14 - Testing for ML systems

## Weekly goals

Test schema, transform, model and artifact.

## Why this week matters

ML systems fail not just because of poor models. Schema changes, strange categories, or artifact errors often appear before metrics drop.

**Close example:** An API that receives age as a string should be explicitly denied, instead of silently mutating and returning unbelievable prediction.

## Core knowledge

- ML tests cover schema, transforms, determinism, metric sanity, reload and API boundary.
- Unit uses small synthetic; integration runs a short pipeline.
- Negative cases: missing column, wrong dtype, unseen category, NaN/Inf, empty input group, broken artifact.
- Metric assertion uses threshold/tolerance for a reason, not blocking the fragile stochastic number.

## Keywords for this week

**New or focus terms:** `data contract`, `parity`

**Review:** `schema`, `pipeline`, `artifact`, `reproducibility`

**Use:** Write `data contract` for schema; test `parity` fit-save-load-predict of pipeline/artifact, negative case for wrong sample and tolerance for reproducibility.

## 8-10 hour schedule

| Activities | Hours |
|---|---:|
| Read and take notes | 2 |
| Guided practice | 2 |
| Lab | 3 |
| Assessment/error analysis | 1 |
| Learning log and self-assessment | 1 |
| Review/complete | 0 |

## Guided practice


1. Test valid/invalid schema and unseen category.
2. Fit-save-load-predict, parity check.
3. Check the model exceeds the dummy on data with signal.

## Lab

**lab-13:** ML tests with edge cases. Main environment: `local`.

## Signs that you understand

You have tests for happy path and missing, wrong dtype, unseen category, NaN/Inf and save-load parity.

## Test yourself

1. Which randomness source needs seeding?
2. Why is exact metric flaky?
3. Which test captures train/serve skew?

## Result oriented

test evidence; Saves executed commands, configuration, metrics, runtime and one limitation.

## Core vs stretch

- **Core:** Test schema, negative cases, reload parity and model-over-dummy on small synthetic data.
- **Expansion:** Add test artifact checksum is broken or input group is empty; Avoid exact metrics that are easy to flaky.

## Common errors

- Only test happy paths.
- Automated checks use large/sensitive production datasets.

## When you get stuck

Use small synthetic data and edit one test at a time. Avoid exact metric locking if the algorithm involves randomization.

## Source

Recommended sources: pytest documentation and scikit-learn guidance on common pitfalls/reproducibility.