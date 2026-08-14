# Week 05 - Supervised learning and baseline

## Weekly goals

Set baseline; split train/validation/test is correct.

## Why this week matters

Baseline creates an honest starting line. If the model is not yet beyond simple guessing, increasing complexity will not bring value.

**Close example:** A data set with 90% of customers not churning will give a dummy accuracy of 90%, but is almost useless when looking for people who are about to leave.

## Core knowledge

- Classification predicts class/probability; regression predicts continuous values.
- Dummy baseline measures the minimum level; Logistic regression creates linear logit then sigmoid.
- Train to fit, validate to select, test only when the decision is locked.
- Use stratified split for classes; Use group/time split when the pattern involves or has time.

## Keywords for this week

**New or focus terms:** `data split`, `training set`, `validation set`, `test set`, `baseline`, `model validation`

**Review:** `dataset`, `sample`, `feature`, `label / target`, `prediction`

**Use:** Create a `data split` with no duplicated `sample` across the `training set`, `validation set`, and `test set`; fit a `baseline`, perform `model validation`, then compare each `prediction` with its `label / target`.

## Concept walkthrough

### Splitting data for training

**Mental model:** `data split`: How to divide a dataset into parts with different and non-overlapping roles. Typical roles are training, validation, and testing, with no sample shared across them. `training set`: The data subset used to learn model parameters and preprocessing state. Validation and test samples must not influence anything learned from this subset.

**Why it matters:** A data split assigns roles before modeling, and only the training set may fit parameters.

**Worked example:** `data split`: Divide 70% training, 15% validation, 15% testing. `training set`: Logistic regression calls fit only with the training set.

**Easy to confuse:** A data split creates subsets; cross-validation rotates several folds through roles. The training set teaches the model; the validation set only guides choices.

**Check yourself:** Why may the `training set`, but not the other splits, teach model parameters?

### Validation and the untouched test

**Mental model:** `validation set`: The data subset used to choose a model, threshold, or hyperparameter without fitting on it. It may be examined many times for decisions, but its labels must not enter fit. `test set`: A held-back data subset opened only after model and threshold choices are fixed. It must remain untouched by preprocessing fit, model selection, and threshold tuning.

**Why it matters:** The validation set supports choices; the test set stays untouched until those choices are locked.

**Worked example:** `validation set`: Choose a threshold with satisfactory recall on the validation set. `test set`: Run the test once after selecting logistic regression.

**Easy to confuse:** The validation set guides choices; the test set checks the locked result. The test set is not another validation set for repeated tuning.

**Check yourself:** Which decisions use the `validation set`, and when may the `test set` be opened?

### Baseline and model validation

**Mental model:** `baseline`: A simple benchmark used to judge whether a more complex model provides a real improvement. It can be a simple rule, a dummy model, or the smallest reasonable learned model. `model validation`: The process of evaluating model choices on data that was not used to fit the model. It includes comparing candidates and thresholds on validation data before the final test.

**Why it matters:** A baseline defines the minimum useful result, while model validation tests whether an improvement survives unseen data.

**Worked example:** `baseline`: A dummy classifier always predicts the most common class. `model validation`: Compare F1 on the validation set before opening the test set.

**Easy to confuse:** A baseline is a comparison point, not necessarily the final model. Validation guides choices; testing estimates the final chosen system once.

**Check yourself:** What evidence shows that a model beats the `baseline` under honest `model validation`?

## Connect earlier terms

The `dataset` and its `sample` rows now receive fixed roles before any model choice. Saved split indices show that each `feature` and `label / target` reaches exactly one split, while held-out `prediction` evidence remains independent.

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


1. So dummy and logistic above are exactly the same split/workflow/quality measure.
2. Check class balance and ID do not overlap between sets.
3. Write a quality measure gate model that must exceed the baseline.

## Lab

**lab-04:** Dummy and logistic classifier. Main environment: `local`.

## Signs that you understand

You use the same split and quality measure to compare dummy with logistic regression; Test set has not yet participated in model selection.

## Test yourself

1. When is Dummy accuracy high?
2. In which space is linear logistics?
3. When does random split cause leakage?

## Result oriented

baseline report; Saves the executed command, configuration, quality measure, run time and one limitation.

## Core vs stretch

- **Core:** So dummy with logistic on top split, quality measure and seed; keep the test without participating in the selection.
- **Extension:** Try group/time split on a hypothetical situation and state why random split might be wrong.

## Common errors

- Compare models on different splits.
- Remove baseline to run complex models.

## When you get stuck

Check label distribution, duplicate IDs and previous times. When in doubt, plot the sets instead of changing the model.

## Source

Recommended source: scikit-learn documentation on model selection, train-test split and DummyClassifier.