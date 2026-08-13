# Reference result - lab-03-linear-regression-from-scratch

## Oracle

Try several `epsilon` values. Both gradients must be close within the recorded tolerance.

## Required receipt

- Run `python scripts/run_lab.py --lab 3` from the repository root. The full PowerShell and Bash commands are in the lab README.
- The JSON must contain `status=starter-example-completed`; in `result`, look for the analytic gradient, finite-difference gradient, and `gradient_check=true`.
- Keep a local learning log with the seed or config, runtime, the lab-specific check, and at least one limitation or failure.
- Answer in your own words: "What does this output prove, and what does it not prove?"

## Terminology oracle

- The history shows `loss`, and the gradient check compares the `gradient`. The learning log explains how the `learning rate` updates a parameter and changes the prediction.
- Answer the `Explain it yourself` question in your own words and point to the evidence. Do not only copy a glossary.

## If your result differs

If the gradients differ, check the sign, averaging, and the central-difference formula.

This is a self-check, not an assignment to submit. Keep evidence local. Do not commit secrets, personal data, large raw datasets, or paid cloud output.
