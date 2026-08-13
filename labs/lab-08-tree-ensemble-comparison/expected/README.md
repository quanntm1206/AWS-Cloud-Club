# Reference result - lab-08-tree-ensemble-comparison

## Oracle

Every candidate uses the same split, metric, and runtime budget. Open the test set only after selection.

## Required receipt

- Run `python scripts/run_lab.py --lab 8` from the repository root. The full PowerShell and Bash commands are in the lab README.
- The JSON must contain `status=starter-example-completed`; in `result`, look for each candidate's validation score, the selected model, and final test AUC.
- Keep a local learning log with the seed or config, runtime, the lab-specific check, and at least one limitation or failure.
- Answer in your own words: "What does this output prove, and what does it not prove?"

## Terminology oracle

- The ensemble comparison keeps the same baseline, metric, and budget. It changes one hyperparameter and explains bagging / boosting.
- Answer the `Explain it yourself` question in your own words and point to the evidence. Do not only copy a glossary.

## If your result differs

If one model wins by very little, compare CV variability and artifact size before deciding.

This is a self-check, not an assignment to submit. Keep evidence local. Do not commit secrets, personal data, large raw datasets, or paid cloud output.
