# Reference result - lab-06-metrics-and-threshold

## Oracle

Write the threshold rule before viewing the test set. Compare at least three thresholds.

## Required receipt

- Run `python scripts/run_lab.py --lab 6` from the repository root. The full PowerShell and Bash commands are in the lab README.
- The JSON must contain `status=starter-example-completed`; in `result`, look for the validation threshold, F1, PR-AUC, FP/FN cost, and test metrics.
- Keep a local learning log with the seed or config, runtime, the lab-specific check, and at least one limitation or failure.
- Answer in your own words: "What does this output prove, and what does it not prove?"

## Terminology oracle

- The receipt records class imbalance, the metric, and the threshold selected on the validation set. The test set does not tune the decision.
- Answer the `Explain it yourself` question in your own words and point to the evidence. Do not only copy a glossary.

## If your result differs

If AUC is unclear, return to the confusion matrix and FP/FN counts at each threshold.

This is a self-check, not an assignment to submit. Keep evidence local. Do not commit secrets, personal data, large raw datasets, or paid cloud output.
