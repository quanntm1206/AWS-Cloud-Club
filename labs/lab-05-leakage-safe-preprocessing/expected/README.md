# Reference result - lab-05-leakage-safe-preprocessing

## Oracle

Add an unseen category. The pipeline must still predict without fitting again.

## Required receipt

- Run `python scripts/run_lab.py --lab 5` from the repository root. The full PowerShell and Bash commands are in the lab README.
- The JSON must contain `status=starter-example-completed`; in `result`, look for a prediction for the unknown category and `leakage_guard=true`.
- Keep a local learning log with the seed or config, runtime, the lab-specific check, and at least one limitation or failure.
- Answer in your own words: "What does this output prove, and what does it not prove?"

## Terminology oracle

- The evidence shows that preprocessing transforms are fit only on the training set inside the pipeline. The new category is handled, with no data leakage.
- Answer the `Explain it yourself` question in your own words and point to the evidence. Do not only copy a glossary.

## If your result differs

If the encoder fails, check `handle_unknown`. If the score looks unusually strong, look for a fit before the split.

This is a self-check, not an assignment to submit. Keep evidence local. Do not commit secrets, personal data, large raw datasets, or paid cloud output.
