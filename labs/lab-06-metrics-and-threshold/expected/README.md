# Reference result - lab-06-metrics-and-threshold

## Oracle

Write the threshold rule before viewing the test set. Compare at least three thresholds.

## Required receipt

- Run `python scripts/run_lab.py --lab 6` from the repository root. The full PowerShell and Bash commands are in the lab README.
- The JSON must contain `status=starter-example-completed`; in `result`, look for the validation threshold, F1, PR-AUC, FP/FN cost, and test metrics.
- Keep a local learning log with the seed or config, runtime, the lab-specific check, and at least one limitation or failure.
- Answer in your own words: "What does this output prove, and what does it not prove?"

## Terminology oracle

**Expected reasoning:** The chosen threshold should follow the written validation rule and the stated costs of false positives and false negatives. It must remain unchanged for the test set.

**Evidence mapping:** Class counts and the baseline give context. Candidate confusion matrices, costs, and metrics explain the selection of `validation_threshold`, which is then applied once to the test data.

**Misconception check:** Do not adjust the threshold after reading the test result. The starter status only confirms that the smoke output contains the expected fields.

## If your result differs

If AUC is unclear, return to the confusion matrix and FP/FN counts at each threshold.

This is a self-check, not an assignment to submit. Keep evidence local. Do not commit secrets, personal data, large raw datasets, or paid cloud output.
