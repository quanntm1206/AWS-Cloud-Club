# Lab 04 - Compare a dummy baseline with logistic regression

## Goal

A classifier matters only when it beats a simple guess under the same rules. Make the baseline a required condition, not a footnote in the report.

## Terms used in this lab

**New terms:** `baseline`, `confusion matrix`, `data split`, `fit`, `metric`, `model validation`, `precision / recall / F1`, `test set`, `training set`, `validation set`

**Review:** `dataset`, `sample`, `feature`, `label / target`, `prediction`

**Use in this lab:** Create a `data split` from the `dataset` with no overlapping samples: a `training set`, `validation set`, and `test set`. `fit` a baseline on the features. Use the same `metric`, `precision / recall / F1`, and `confusion matrix` for `model validation`, comparing each prediction with the label / target.

**Explain it yourself:** How are data validation, a validation set, and model validation different?

## Before you start

Read `roadmap/weeks/week-05.md`, work from the repository root, and prepare a local place for evidence. Do not put credentials, personal data, or large result files in Git.

## Steps

1. Check class balance. Create stratified train, validation, and test sets, then confirm that IDs do not overlap.
2. Train a dummy classifier. Record F1 and the confusion matrix.
3. Train logistic regression on exactly the same split and metric.
4. State whether the model beats the baseline. Compare the `label / target` with each prediction. Do not change the decision threshold after viewing the test set.

## Run the smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 4
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 4
```

The result is saved to `.artifacts/lab-04-evidence.json`. In `result`, you will see `dummy_f1` and `logistic_f1`.
`status=starter-example-completed` only confirms that the example code ran. It does **not** mean that you met all acceptance criteria.

## When you are done

- The JSON contains `dummy_f1` and `logistic_f1`, compared with the same split, seed, and metric.
- You can explain why high accuracy may be unhelpful when the positive class is rare.

## When you get stuck

If both models are similar, check the signal and target first. Do not add a complex model only to find a higher number.

Predict the output first, then compare it with [`expected/README.md`](expected/README.md) and record what you learned locally. No submission is required.
