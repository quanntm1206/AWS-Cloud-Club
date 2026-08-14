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

**Use:** Write a `data contract` for the `schema`; test `parity` across fit, save, load, and predict for the `pipeline` and `artifact`, including an invalid sample and a stated reproducibility tolerance.

## Concept walkthrough

### A contract at the boundary

**Mental model:** `data contract`: A data contract is a machine-readable agreement about data schema, allowed values, and validation errors. Both producers and consumers can validate the same contract at their boundary.

**Why it matters:** A data contract turns schema expectations into checks at the boundary before bad inputs reach the model.

**Worked example:** `data contract`: A request missing the tenure field is rejected before it reaches the model.

**Easy to confuse:** A data contract governs data; an API contract governs service requests and responses.

**Check yourself:** Which invalid input should the `data contract` reject before the model runs?

### Training-serving parity

**Mental model:** `parity`: Parity means two paths produce sufficiently consistent results for the same input. The acceptable tolerance depends on whether outputs are labels, probabilities, or floating-point arrays.

**Why it matters:** Parity evidence shows that training and serving apply the same feature order, transformations, and decision rule.

**Worked example:** `parity`: Predictions before and after save/load match within the stated tolerance.

**Easy to confuse:** Parity means sufficiently matching behavior, not necessarily byte-identical files.

**Check yourself:** What tolerance proves `parity` between the training and serving paths?

## Connect earlier terms

The `schema` becomes an executable data contract around the `pipeline` and `artifact`. Matching predictions within a stated tolerance demonstrate `reproducibility` across save and load boundaries.

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