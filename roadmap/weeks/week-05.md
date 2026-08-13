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

**Use:** Create `data split` from `dataset` without duplicate samples into `training set`, `validation set`, `test set`; fit `baseline` on feature, perform `model validation`, compare prediction with label / target.

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