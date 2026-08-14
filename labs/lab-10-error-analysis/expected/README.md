# Reference result - lab-10-error-analysis

## Oracle

Review errors with a sampling rule and support. Propose one data fix and one model fix.

## Required receipt

- Run `python scripts/run_lab.py --lab 10` from the repository root. The full PowerShell and Bash commands are in the lab README.
- The JSON must contain `status=starter-example-completed`; in `result`, look for slice metrics, capped failure records, and a taxonomy.
- Keep a local learning log with the seed or config, runtime, the lab-specific check, and at least one limitation or failure.
- Answer in your own words: "What does this output prove, and what does it not prove?"

## Terminology oracle

**Expected reasoning:** Every slice metric needs its support. The sampled failures should lead to an evidence-based taxonomy and an experiment that could disprove the proposed explanation.

**Evidence mapping:** For each slice, read the rule, support, false-positive and false-negative counts, and metric together. Then connect the capped failure records to their categories and proposed tests.

**Misconception check:** A few memorable errors are not systematic error analysis, and a tiny group does not support a broad fairness claim. The starter output only shows the expected format.

## If your result differs

If no pattern appears, make the error sample more diverse instead of selecting only confident-wrong cases.

This is a self-check, not an assignment to submit. Keep evidence local. Do not commit secrets, personal data, large raw datasets, or paid cloud output.
