# Week 08 - Cross-validation and learning curve

## Weekly goals

Use cross-validation and learning curves.

## Why this week matters

A data split can be lucky or unlucky. Cross-validation helps you see how stable the model is, while the learning curve suggests whether you should add more data or change the way you learn.

**Close example:** Mean CV is the same as GPA; The difference between folds indicates how strongly the result depends on the division.

## Core knowledge

- Cross-validation estimates variation over many folds; Report each score, mean, std and runtime.
- StratifiedKFold for independent classification; GroupKFold/time split for entity/time.
- Transform must be in the pipeline to fit inside each fold.
- Learning curve compared to training/validation according to amount of data: both low suggests underfitting/high bias; High training but low validation suggests overfitting/high variance.
- Fold score is a finite sample, not an absolute truth; Always report dispersion and avoid drawing strong conclusions from small differences.

## Keywords for this week

**New or focus terms:** `cross-validation`, `fold`, `overfitting`, `bias / variance`

**Review:** `data split`, `pipeline`, `metric`

**Use:** Put the entire pipeline in `cross-validation`; read each `fold`, mean/std and learning curve to distinguish overfitting from bias / variance; keep metrics and data splits consistent.

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


1. Run 3-fold CV fixed seed.
2. Compare pipeline correctly with preprocessing outside CV.
3. Draw the learning curve three train sizes.

## Lab

**lab-07:** Evaluation harness has mean/std/runtime. Main environment: `local`.

## Signs that you understand

You report each fold, mean, std, runtime and know how to split by entity or time when needed.

## Test yourself

1. What does the big mid-fold std suggest?
2. Does CV replace final test?
3. Why is the Shuffle time series wrong?

## Result oriented

competency milestone 2; Saves executed commands, configuration, metrics, runtime and one limitation.

## Core vs stretch

- **Core:** Run 3-fold CV with pipeline; Report each fold, mean, std and learning curve.
- **Extension:** Compare StratifiedKFold with GroupKFold on a hypothetical grouping; Don't increase folds just to get more numbers.

## Common errors

- Tune and report with CV as final test.
- Use many folds but do not add insight.

## When you get stuck

Reduced to 3 folds and mini data. If the score fluctuates, check the class/group by fold before tuning the model.

## Source

Recommended sources: scikit-learn cross-validation and learning curve documentation.