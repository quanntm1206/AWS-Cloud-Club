# Week 10 - Feature engineering and ablation

## Weekly goals

Feature engineering has a hypothesis; ablation of a variable.

## Why this week matters

Feature engineering turns understanding of the problem into usable model signals. Ablation helps check whether the new feature is really useful or just duplicate noise.

**Close example:** The ratio of spend to engagement time can be useful, but must deal with zero denominators and only use data available at prediction time.

## Core knowledge

- Feature must exist at prediction time, be stable, reproducible and meaningful.
- Ratio/log/interaction requires hypothesis; Handles zero, missing and range.
- Ablation replaces exactly one feature group in the same harness.
- Metric delta is smaller than CV variability, which has not proven to be a useful feature.

## Keywords for this week

**New or focus terms:** `feature engineering`, `ablation`

**Review:** `feature`, `baseline`, `validation set`, `hyperparameter`

**Use:** Write a `feature engineering` hypothesis, run `ablation` to add/remove a feature; lock the baseline, validation set, hyperparameter, and data split to make the delta metric meaningful.

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


1. Write feature hypothesis and availability time.
2. Compare all-features with without-monthly-charge.
3. Record metric/runtime delta and keep/drop decision.

## Lab

**lab-09:** Feature ablation log. Main environment: `local`.

## Signs that you understand

Each feature has a hypothesis and availability date; Keep/drop decision based on same harness and same variability.

## Test yourself

1. How is availability different from correlation?
2. Why does Ablation keep seed/model?
3. When to remove a feature even though the metric increases?

## Result oriented

ablation report; Saves executed commands, configuration, metrics, runtime and one limitation.

## Core vs stretch

- **Core:** Run an ablation with a hypothesis, clear availability time, and untouched testing.
- **Extension:** Try a safe feature ratio with zero/missing and then measure both the metric and runtime.

## Common errors

- Use future/target-proxy feature.
- Change features and hyperparameters at the same time.

## When you get stuck

Write the feature in words before the code. If it cannot be said when it will be available, temporarily remove it from the model.

## Source

Recommended source: feature engineering/model inspection section in the official documentation at `docs/sources.yml`.