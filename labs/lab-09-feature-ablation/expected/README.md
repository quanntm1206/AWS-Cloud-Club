# Reference result - lab-09-feature-ablation

## Oracle

Change only one feature group. Record the hypothesis, metric delta, and keep/drop decision.

## Required receipt

- Run `python scripts/run_lab.py --lab 9` from the repository root. The full PowerShell and Bash commands are in the lab README.
- The JSON must contain `status=starter-example-completed`; in `result`, look for validation AUC by feature group and `test_set_touched=false`.
- Keep a local learning log with the seed or config, runtime, the lab-specific check, and at least one limitation or failure.
- Answer in your own words: "What does this output prove, and what does it not prove?"

## Terminology oracle

- The ablation changes one feature-engineering group and keeps the data split and baseline fixed. The receipt records the metric delta and decision.
- Answer the `Explain it yourself` question in your own words and point to the evidence. Do not only copy a glossary.

## If your result differs

If the result is hard to explain, lock the seed and model, then check availability time and missing-value handling.

This is a self-check, not an assignment to submit. Keep evidence local. Do not commit secrets, personal data, large raw datasets, or paid cloud output.
