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

**Use:** Place the complete `pipeline` inside `cross-validation`; inspect every `fold`, the mean and standard deviation, and the learning curve to distinguish `overfitting` from `bias / variance` while keeping the `metric` and `data split` fixed.

## Concept walkthrough

### Rotating the validation role

**Mental model:** `cross-validation`: Cross-validation repeatedly evaluates a model on different folds to estimate its stability. Each sample is used for validation in one fold and for training in the others. `fold`: A fold is one subset that takes a turn as validation data during cross-validation. Folds should preserve important structure, such as class balance or customer grouping.

**Why it matters:** Cross-validation reveals whether a result is stable across several plausible folds instead of one lucky split.

**Worked example:** `cross-validation`: 3-fold CV generates three validation scores. `fold`: In fold 2, the second group is kept for evaluation.

**Easy to confuse:** Cross-validation estimates variability; it does not create more independent data. A fold is one subset inside cross-validation, not the final test set.

**Check yourself:** What does variation among `fold` scores reveal that one `cross-validation` mean hides?

### Overfitting through bias and variance

**Mental model:** `overfitting`: The model remembers training data but performs poorly on new data. It appears as a gap between training performance and performance on unseen data. `bias / variance`: High bias often means a model is too simple, while high variance means it is too sensitive to its training data. Bias causes systematic underfitting, while variance causes unstable behavior across datasets.

**Why it matters:** The gap and variation across folds help distinguish overfitting from a model with too much bias.

**Worked example:** `overfitting`: Train score increases and validation score decreases. `bias / variance`: Low training and validation scores together suggest high bias.

**Easy to confuse:** Overfitting is a generalization gap, not simply a model with many parameters. Bias and variance are error tendencies, not the protected attributes called demographic bias.

**Check yourself:** Which learning-curve pattern suggests `overfitting`, high `bias`, or high `variance`?

## Connect earlier terms

The existing `data split`, `pipeline`, and `metric` are held constant while folds rotate through validation. Per-fold scores and their spread reveal stability that one split cannot show.

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