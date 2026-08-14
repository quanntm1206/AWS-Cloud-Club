# Lab 08 - Compare tree ensembles fairly

## Goal

Trees, random forests, and boosting learn differently. A comparison is meaningful only when the data, metric, and budget are the same.

## Terms used in this lab

**New terms:** `hyperparameter`, `ensemble`, `bagging / boosting`

**Review:** `baseline`, `validation set`, `metric`, `overfitting`

**Use in this lab:** Keep the dataset, validation set, metric, and budget fixed. Compare each `ensemble` using bagging / boosting, change exactly one hyperparameter, then compare with the baseline and check for overfitting.

**Explain it yourself:** How is a parameter different from a hyperparameter? What is the intuitive difference between bagging and boosting?


## Apply the concepts

### Controlled candidates

**Terms:** `baseline`, `validation set`, `metric`, `hyperparameter`, `overfitting`

**What they mean here:** Keep the `baseline`, split, `metric`, and compute budget fixed while one `hyperparameter` changes. A growing gap between training and validation results may indicate `overfitting`.

**Where you will see them:** Candidates report validation AUC, runtime, and saved size under one split.

**Common mistake:** Giving the preferred model more tuning or compute.

**Evidence to keep:** Keep settings, runtime, size, and train-validation results.

**Explain after the lab:** State what was controlled and why test AUC did not choose a hyperparameter.

### Ensemble strategies

**Terms:** `ensemble`, `bagging / boosting`

**What they mean here:** An `ensemble` combines learners; `bagging / boosting` contrasts parallel variance reduction with sequential error correction.

**Where you will see them:** Random forest represents bagging and gradient boosting represents boosting.

**Common mistake:** Explaining both as interchangeable averaging of identical trees.

**Evidence to keep:** Keep selected model, strategy, changed complexity limit, and observed effect.

**Explain after the lab:** Describe learner dependence in each strategy and connect it to results.

## Before you start

Read `roadmap/weeks/week-09.md`, work from the repository root, and prepare a local place for evidence. Do not put credentials, personal data, or large result files in Git.

## Steps

1. Train logistic regression, random forest, and gradient boosting on the same train-validation split.
2. Record validation AUC, runtime, and saved-model size for each candidate.
3. Choose a candidate with a written rule. Only then evaluate the final test set.
4. Change exactly one complexity limit. Explain the effect on train and validation results.

## Run the smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 8
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 8
```

The result is saved to `.artifacts/lab-08-evidence.json`. In `result`, you will see each candidate's validation score, the selected model, and final test AUC.
`status=starter-example-completed` only confirms that the example code ran. It does **not** mean that you met all acceptance criteria.

## When you are done

- The output identifies validation scores, the selected candidate, the selection split, and final test AUC.
- You can describe bagging and boosting, and you do not use the test set to choose a hyperparameter.

## When you get stuck

Lock the split and seed first. Reduce the comparison to two candidates if needed. A difference smaller than the variability is not enough to declare a winner.

Predict the output first, then compare it with [`expected/README.md`](expected/README.md) and record what you learned locally. No submission is required.
