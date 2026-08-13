# Reference result - lab-07-cross-validation

## Oracle

Report every fold and its runtime. Explain whether the variation matters compared with the metric gain.

## Required receipt

- Run `python scripts/run_lab.py --lab 7` from the repository root. The full PowerShell and Bash commands are in the lab README.
- The JSON must contain `status=starter-example-completed`; in `result`, look for fold scores, `cv_mean`, and `cv_std`.
- Keep a local learning log with the seed or config, runtime, the lab-specific check, and at least one limitation or failure.
- Answer in your own words: "What does this output prove, and what does it not prove?"

## Terminology oracle

- The receipt has every fold score, mean, and standard deviation. Cross-validation refits the pipeline, and the learning curve explains overfitting or bias / variance.
- Answer the `Explain it yourself` question in your own words and point to the evidence. Do not only copy a glossary.

## If your result differs

If folds differ strongly, check class, group, and time distributions before increasing the number of folds.

This is a self-check, not an assignment to submit. Keep evidence local. Do not commit secrets, personal data, large raw datasets, or paid cloud output.
