# Week 09 - Tree ensembles

## Weekly goals

Compare tree, random forest and limited boosting.

## Why this week matters

Tree ensembles give you strong options with panel data, but the goal is still to make a fair comparison, not hunt for a winning model at all costs.

**Close example:** Random forest reduces fluctuations with many trees; boosting so that the next tree can focus on fixing errors in the previous tree.

## Core knowledge

- Tree splits features to reduce impurity; Large depth/leaves make it easier to learn noise.
- Random forest bagging tree on bootstrap/feature subset to reduce variance.
- Gradient boosting adds sequential learners to correct errors; learning_rate interactive number estimator.
- Limit depth/leaves or add regularization to help the model reduce noisy learning; Check by train-validation distance, not just train score.
- Compare candidates using the same split, pipeline, metrics and runtime budget.

## Keywords for this week

**New or focus terms:** `hyperparameter`, `ensemble`, `bagging / boosting`

**Review:** `baseline`, `validation set`, `metric`, `overfitting`

**Use:** Keep dataset, validation set, metrics and budget fixed; so `ensemble` uses bagging / boosting, changes the exact hyperparameter and compares the baseline and overfitting signs.

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


1. Train logistic, random forest, gradient boosting on a split.
2. Compare ROC-AUC, F1, runtime, saved-model size.
3. Change max_depth exactly once and explain bias/variance.

## Lab

**lab-08:** Three candidates, same split and metric. Main environment: `local`.

## Signs that you understand

You compare three candidates on the same harness, if you can trade between metric, runtime and saved-model size.

## Test yourself

1. How is Bagging different from boosting?
2. What preprocessing does Tree need?
3. How does Depth impact training/validation?

## Result oriented

model comparison; Saves executed commands, configuration, metrics, runtime and one limitation.

## Core vs stretch

- **Core:** So logistics, random forest and boosting follow the same harness and runtime budget.
- **Extension:** Correctly change a depth/leaf constraint, relating train-validation distance to regularization.

## Common errors

- Large hyperparameter sweep.
- Each model uses a different split.

## When you get stuck

Split, seed and metric keys. Just change one parameter like `max_depth`; Don't open a sweep without first understanding the results.

## Source

Recommended source: scikit-learn ensemble guide on random forests and gradient boosting.