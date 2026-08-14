# Reference result - lab-08-tree-ensemble-comparison

## Oracle

Every candidate uses the same split, metric, and runtime budget. Open the test set only after selection.

## Required receipt

- Run `python scripts/run_lab.py --lab 8` from the repository root. The full PowerShell and Bash commands are in the lab README.
- The JSON must contain `status=starter-example-completed`; in `result`, look for each candidate's validation score, the selected model, and final test AUC.
- Keep a local learning log with the seed or config, runtime, the lab-specific check, and at least one limitation or failure.
- Answer in your own words: "What does this output prove, and what does it not prove?"

## Terminology oracle

**Expected reasoning:** A fair comparison keeps the data, metric, and compute budget fixed. Select the candidate on validation results, then use the test set once.

**Evidence mapping:** Validation AUC, runtime, and model size describe the shared comparison. The random forest represents bagging, gradient boosting represents boosting, and the chosen candidate produces the final test AUC.

**Misconception check:** Giving one candidate more tuning or compute makes the result unfair. The starter status does not prove that the complete comparison followed the fixed rules.

## If your result differs

If one model wins by very little, compare CV variability and artifact size before deciding.

This is a self-check, not an assignment to submit. Keep evidence local. Do not commit secrets, personal data, large raw datasets, or paid cloud output.
