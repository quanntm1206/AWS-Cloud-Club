# Lab 07 - Measure stability with cross-validation

## Goal

A lucky split can make a model look more stable than it is. Cross-validation shows how results change when data is split again under controlled rules.

## Terms used in this lab

**New terms:** `cross-validation`, `fold`, `overfitting`, `bias / variance`

**Review:** `data split`, `pipeline`, `metric`

**Use in this lab:** Put the complete pipeline inside `cross-validation`. Read each `fold`, the mean and standard deviation, and the learning curve to distinguish overfitting from bias / variance. Keep the metric and data split rules consistent.

**Explain it yourself:** How is a fold different from a test set? How can a learning curve suggest overfitting or bias / variance?

## Before you start

Read `roadmap/weeks/week-08.md`, work from the repository root, and prepare a local place for evidence. Do not put credentials, personal data, or large result files in Git.

## Steps

1. Put the full pipeline inside 3-fold CV. Lock the seed and scoring rule.
2. Record every fold score and runtime, then calculate the mean and standard deviation.
3. Compare this with incorrect preprocessing outside CV and describe the leakage risk.
4. Plot a learning curve at three training sizes. Describe signs of bias or variance.

## Run the smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 7
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 7
```

The result is saved to `.artifacts/lab-07-evidence.json`. In `result`, you will see fold scores, `cv_mean`, and `cv_std`.
`status=starter-example-completed` only confirms that the example code ran. It does **not** mean that you met all acceptance criteria.

## When you are done

- The JSON contains fold scores, mean, and standard deviation. Every transform is fit again inside each fold.
- You can choose a stratified, group, or time split from the relationships between samples instead of shuffling by default.

## When you get stuck

If fold scores vary widely, inspect the class, group, or time distribution in each fold. Do not increase the number of folds before understanding the cause.

Predict the output first, then compare it with [`expected/README.md`](expected/README.md) and record what you learned locally. No submission is required.
