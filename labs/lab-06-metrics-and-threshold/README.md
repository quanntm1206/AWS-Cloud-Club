# Lab 06 - Choose a metric and threshold from error costs

## Goal

A threshold of 0.5 does not understand business costs. Choose a threshold from validation evidence, then lock the decision before touching the test set.

## Terms used in this lab

**New terms:** `class imbalance`, `threshold`

**Review:** `validation set`, `model validation`, `baseline`, `metric`, `precision / recall / F1`

**Use in this lab:** Use the `validation set` for `model validation`. Choose a `precision / recall / F1` metric and a threshold that reflect class imbalance, compare them with the baseline, and keep the test set closed until the end.

**Explain it yourself:** Which metric and threshold suit the class imbalance? How is the validation set used?


## Apply the concepts

### Error costs

**Terms:** `class imbalance`, `baseline`, `metric`, `precision / recall / F1`

**What they mean here:** With `class imbalance`, the chosen `metric` and the trade-off between `precision / recall / F1` should reflect the costs of false positives and false negatives. Compare the result with the `baseline`.

**Where you will see them:** Class counts, confusion matrices, F1, PR-AUC, and dummy results appear together.

**Common mistake:** Choosing whichever metric makes the current model look strongest.

**Evidence to keep:** Keep support, metric declaration, baseline, and FP/FN cost assumptions.

**Explain after the lab:** Explain which error matters more and why the metric exposes it.

### Locked cutoff

**Terms:** `threshold`, `validation set`, `model validation`

**What they mean here:** A `threshold` turns probability scores into class predictions. During `model validation`, choose it on the `validation set` with a written rule, then keep it unchanged for the test set.

**Where you will see them:** Candidate validation matrices lead to `validation_threshold`, reused for test metrics.

**Common mistake:** Moving the threshold after reading the test confusion matrix.

**Evidence to keep:** Keep all candidates, validation costs, rule, chosen threshold, and locked test result.

**Explain after the lab:** Reconstruct the choice without using test performance as selection evidence.

## Before you start

Read `roadmap/weeks/week-07.md`, work from the repository root, and prepare a local place for evidence. Do not put credentials, personal data, or large result files in Git.

## Steps

1. Build confusion matrices at at least three thresholds and assign costs to FP and FN.
2. Write a selection rule, such as minimum recall followed by lowest cost.
3. Choose the threshold on validation. Record F1 and PR-AUC.
4. Apply the locked threshold to the test set. Compare results without tuning again.

## Run the smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 6
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 6
```

The result is saved to `.artifacts/lab-06-evidence.json`. In `result`, you will see the validation threshold, F1, PR-AUC, FP/FN cost, and test metrics.
`status=starter-example-completed` only confirms that the example code ran. It does **not** mean that you met all acceptance criteria.

## When you are done

- The output records the selection rule, selected threshold, validation and test metrics, and FP/FN cost.
- You can explain the precision-recall trade-off, log loss, and what a calibration check asks.

## When you get stuck

If the metrics are confusing, return to TP, FP, FN, and TN counts. Choose a metric only after writing which error costs more.

Predict the output first, then compare it with [`expected/README.md`](expected/README.md) and record what you learned locally. No submission is required.
