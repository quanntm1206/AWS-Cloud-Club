# Week 11 - Interpretability and error analysis

## Weekly goals

Interpret the model with caution; subgroup/failure analysis.

## Why this week matters

The average good model can still be bad for a small group. Error analysis turns individual errors into verifiable follow-ups.

**Close example:** Accuracy is generally good but monthly contract customers have many false negatives; This is a signal that requires viewing data or thresholds in groups.

## Core knowledge

- Global importance describes the average; local explanation describes a prediction; none of them prove causality.
- Permutation importance is affected when features are correlated.
- Slice metric always includes sample count to avoid drawing conclusions from too small a group; View the difference as a signal to investigate fairness, do not rush to conclude the cause.
- When labels arrive late, monitor schema, missing rate, prediction distribution and feature drift before having quality metrics.
- Failure taxonomy groups errors into data quality, boundary, missing signal, label noise or shift.

## Keywords for this week

**New or focus terms:** `error analysis`, `slice`, `failure taxonomy`

**Review:** `metric`, `validation set`, `feature engineering`

**Use:** Run `error analysis` for each `slice`, always recording sample count; Create `failure taxonomy` from wrong prediction, contact feature engineering and metrics on validation set.

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


1. Set up FP/FN counts by region/contract.
2. Review up to 20 errors according to sampling rule.
3. Propose a data fix and a model fix with tests.

## Lab

**lab-10:** Slice metrics and failure taxonomy. Main environment: `local`.

## Signs that you understand

You report the slice metric with sample count, group errors and propose a data fix and a model fix with tests.

## Test yourself

1. Is importance different from causality?
2. What risks does a small Sample Count pose?
3. What action should error analysis lead to?

## Result oriented

error analysis; Saves executed commands, configuration, metrics, runtime and one limitation.

## Core vs stretch

- **Core:** Report slice metrics with sample count, review errors according to rules and suggest next experiment.
- **Expansion:** Add a subgroup-risk check or a monitoring signal such as missing rate/prediction distribution.

## Common errors

- Choose errors that are convenient to the eye.
- Use an explanation to validate the error.

## When you get stuck

Don't choose eye-catching errors. Take samples according to fixed rules and describe what you see before explaining the cause.

## Source

Recommended sources: scikit-learn permutation importance and model inspection; model-card guidance in `docs/sources.yml`.