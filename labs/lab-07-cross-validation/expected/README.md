# Reference result - lab-07-cross-validation

## Oracle

Report every fold and its runtime. Explain whether the variation matters compared with the metric gain.

## Required receipt

- Run `python scripts/run_lab.py --lab 7` from the repository root. The full PowerShell and Bash commands are in the lab README.
- The JSON must contain `status=starter-example-completed`; in `result`, look for fold scores, `cv_mean`, and `cv_std`.
- Keep a local learning log with the seed or config, runtime, the lab-specific check, and at least one limitation or failure.
- Answer in your own words: "What does this output prove, and what does it not prove?"

## Terminology oracle

**Expected reasoning:** Cross-validation estimates how sensitive the score is to the split only when the full pipeline is fitted again inside every fold.

**Evidence mapping:** Each fold score and runtime belongs to a separate fit. `cv_mean` and `cv_std` summarize stability, while the training and validation learning curves support the bias, variance, or overfitting discussion.

**Misconception check:** The best fold is not the expected performance, and a fold is not the final untouched test set. The starter status is smoke evidence only.

## If your result differs

If folds differ strongly, check class, group, and time distributions before increasing the number of folds.

This is a self-check, not an assignment to submit. Keep evidence local. Do not commit secrets, personal data, large raw datasets, or paid cloud output.
