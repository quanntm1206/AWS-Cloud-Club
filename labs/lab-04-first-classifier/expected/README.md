# Reference result - lab-04-first-classifier

## Oracle

Keep the same split and metric. Explain whether the model beats the baseline.

## Required receipt

- Run `python scripts/run_lab.py --lab 4` from the repository root. The full PowerShell and Bash commands are in the lab README.
- The JSON must contain `status=starter-example-completed`; in `result`, look for `dummy_f1` and `logistic_f1`.
- Keep a local learning log with the seed or config, runtime, the lab-specific check, and at least one limitation or failure.
- Answer in your own words: "What does this output prove, and what does it not prove?"

## Terminology oracle

- The receipt records the `data split` and training, validation, and test sets. The baseline and model use the same metric; the confusion matrix and precision / recall / F1 support model validation.
- Answer the `Explain it yourself` question in your own words and point to the evidence. Do not only copy a glossary.

## If your result differs

If both F1 scores are low, check class balance and signal before changing the algorithm.

This is a self-check, not an assignment to submit. Keep evidence local. Do not commit secrets, personal data, large raw datasets, or paid cloud output.
