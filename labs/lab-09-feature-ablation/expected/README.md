# Reference result - lab-09-feature-ablation

## Oracle

Change only one feature group. Record the hypothesis, metric delta, and keep/drop decision.

## Required receipt

- Run `python scripts/run_lab.py --lab 9` from the repository root. The full PowerShell and Bash commands are in the lab README.
- The JSON must contain `status=starter-example-completed`; in `result`, look for validation AUC by feature group and `test_set_touched=false`.
- Keep a local learning log with the seed or config, runtime, the lab-specific check, and at least one limitation or failure.
- Answer in your own words: "What does this output prove, and what does it not prove?"

## Terminology oracle

**Expected reasoning:** An ablation can link a score change to one feature group only when the split, seed, model, and hyperparameters stay fixed.

**Evidence mapping:** The written hypothesis explains the feature-engineering idea. AUC by feature group and `single_change` show the controlled comparison, while `test_set_touched=false` confirms the evaluation boundary.

**Misconception check:** A positive score difference is not automatically stable or causal. The starter status is not the final decision to keep the feature.

## If your result differs

If the result is hard to explain, lock the seed and model, then check availability time and missing-value handling.

This is a self-check, not an assignment to submit. Keep evidence local. Do not commit secrets, personal data, large raw datasets, or paid cloud output.
