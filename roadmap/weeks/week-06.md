# Week 06 - Preprocessing and preventing leakage

## Weekly goals

Handle missing/categories with a leakage-free pipeline.

## Why this week matters

Preprocessing also learns from data. Placing it in the pipeline keeps the train/validation boundaries clean and avoids the model from running differently when generating new predictions.

**Close example:** The average value used to fill in the missing must come from the train, not before the customers in the test.

## Core knowledge

- Imputer, scaler, encoder all learn state and can only be fitted on the train.
- ColumnTransformer separates numeric/categorical; Pipeline holds the preprocess and model along the lifecycle.
- OneHotEncoder needs to handle unseen categories to predict new input without breaking.
- Schema validation catches missing columns, wrong dtype/range and target mixed in as input before transform.

## Keywords for this week

**New or focus terms:** `preprocessing`, `transform`, `pipeline`, `data leakage`, `fit`

**Review:** `data split`, `training set`, `validation set`, `test set`, `schema`

**Use:** Divide by `data split` first, fit each `preprocessing`/`transform` step only on `training set`, merge into `pipeline`; Use schema to prove there is no `data leakage` to validation set/test set.

## 8-10 hour schedule

| Activities | Hours |
|---|---:|
| Read and take notes | 2 |
| Guided practice | 2 |
| Lab | 3 |
| Assessment/failure review | 1 |
| Learning log and self-assessment | 1 |
| Review/complete | 0 |

## Guided practice


1. Create impute-scale and impute-one-hot pipelines.
2. Inject unseen categories into validation.
3. Test scaler mean does not take test data.

## Lab

**lab-05:** Leakage-safe preprocessing. Main environment: `local`.

## Signs that you understand

You handle unprecedented missing and categories, and prove that the scaler doesn't learn from testing.

## Test yourself

1. Why is fit_transform before split is leakage?
2. What trade-offs does handle_unknown have?
3. How does Pipeline reduce train/serve skew?

## Result oriented

pipeline + schema; Saves executed commands, configuration, metrics, runtime and one limitation.

## Core vs stretch

- **Core:** Build an impute/scale/encode pipeline that only fits the train; Check the category but don't see it.
- **Extension:** Add a schema failure like missing columns or wrong dtype and turn it into a test.

## Common errors

- Save the model but forget the transformer.
- Impute according to test distribution.

## When you get stuck

Create a validation row with a strange category. If the pipeline breaks, fix the encoder and add more tests before retraining.

## Source

Recommended sources: scikit-learn Pipeline, ColumnTransformer, SimpleImputer and OneHotEncoder.