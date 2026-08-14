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

**Use:** Create the `data split` first, fit each `preprocessing` and `transform` step only on the `training set`, then assemble the `pipeline`; use the `schema` and split lineage to rule out `data leakage` into validation or test data.

## Concept walkthrough

### Learning a transformation

**Mental model:** `preprocessing`: Preprocessing prepares raw data for a model by filling missing values, scaling numbers, or encoding categories. Some steps are fixed, while others learn values such as medians, category lists, or scaling statistics. `transform`: A transform applies a fixed rule or state learned from the training set to input data. The same fitted transform should then be reused for validation, test, and inference data.

**Why it matters:** Every preprocessing rule that learns statistics must learn them from the training data only.

**Worked example:** `preprocessing`: Fill in the median and then one-hot encode the contract column. `transform`: StandardScaler learns mean and std from training and applies it to validation.

**Easy to confuse:** Preprocessing may learn state, so it is not always a harmless fixed cleanup. A transform applies a rule; fit learns any state required by that rule.

**Check yourself:** Which state may `preprocessing` learn, and how must the same `transform` reach later data?

### Pipeline order and leakage

**Mental model:** `pipeline`: A pipeline runs preprocessing and modeling steps in a fixed order. When the pipeline is fitted, each learned preprocessing step sees only training data. `data leakage`: Data leakage happens when training uses information from validation, testing, or the future. Leakage can come from future data, target-derived features, duplicate customers, or preprocessing before a split.

**Why it matters:** A pipeline preserves operation order; that boundary prevents information from leaking from validation or test data.

**Worked example:** `pipeline`: A Pipeline connects a ColumnTransformer to logistic regression. `data leakage`: Fitting a scaler on the entire dataset before splitting leaks test information.

**Easy to confuse:** A pipeline is the ordered container; preprocessing is only the data-preparation part. Leakage can occur without duplicate rows, such as fitting a scaler before splitting.

**Check yourself:** Where can `data leakage` enter when the `pipeline` is fitted in the wrong order?

### Fit learns state

**Mental model:** `fit`: The step of learning parameters or transform states from training data. For a scaler, fit learns statistics; for a model, fit learns predictive parameters.

**Why it matters:** Fit changes an object's state, so recording what was fitted and on which rows is part of reproducibility.

**Worked example:** `fit`: Call pipeline.fit(X_train, y_train).

**Easy to confuse:** Fit learns state; transform applies a learned or fixed transformation.

**Check yourself:** Which rows are allowed to influence state during `fit`?

## Connect earlier terms

The earlier `data split`, `training set`, `validation set`, `test set`, and `schema` define where preprocessing may learn state. Fitted-state metadata and unchanged held-out rows show that the pipeline respects those boundaries.

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