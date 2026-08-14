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

**Use:** Hold the dataset, `validation set`, `metric`, and budget fixed; compare an `ensemble` built with `bagging / boosting`, change one `hyperparameter`, then check improvement over the `baseline` and signs of `overfitting`.

## Concept walkthrough

### Hyperparameters and ensembles

**Mental model:** `hyperparameter`: A hyperparameter is a setting chosen by the practitioner rather than learned directly during fit. Examples include tree depth, regularization strength, and the number of trees. `ensemble`: The model combines multiple sub-models to create a common prediction. The member predictions are combined by voting, averaging, or another aggregation rule.

**Why it matters:** Hyperparameters control how learners are built; an ensemble combines learners, so both must be selected without consulting the test set.

**Worked example:** `hyperparameter`: Number of trees and maximum depth of random forest. `ensemble`: Random forest takes results from many decision trees.

**Easy to confuse:** A hyperparameter is selected; a parameter is learned from training data. An ensemble is the combined model; bagging and boosting are ways to build one.

**Check yourself:** Which evidence should select a `hyperparameter` before several models become an `ensemble`?

### Bagging compared with boosting

**Mental model:** `bagging / boosting`: Bagging trains several models mostly independently, while boosting trains them in sequence to correct earlier errors. Bagging mainly reduces instability; boosting focuses later models on earlier mistakes.

**Why it matters:** Bagging mainly reduces variance through parallel learners, while boosting builds learners sequentially to correct earlier errors.

**Worked example:** `bagging / boosting`: Random forest uses bagging, gradient boosting uses boosting.

**Easy to confuse:** Bagging and boosting are different ensemble strategies, not interchangeable names.

**Check yourself:** Why does `bagging / boosting` describe two different ways to combine learners?

## Connect earlier terms

The `baseline`, `validation set`, and `metric` remain the comparison contract for every ensemble candidate. Training-validation gaps provide the `overfitting` evidence needed before accepting a hyperparameter change.

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