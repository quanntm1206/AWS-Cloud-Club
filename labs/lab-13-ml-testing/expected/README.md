# Reference result - lab-13-ml-testing

## Oracle

Add checks for a missing column, wrong dtype, unseen category, and damaged artifact.

## Required receipt

- Run `python scripts/run_lab.py --lab 13` from the repository root. The full PowerShell and Bash commands are in the lab README.
- The JSON must contain `status=starter-example-completed`; in `result`, look for `artifact_reload_parity=true` and your added negative cases.
- Keep a local learning log with the seed or config, runtime, the lab-specific check, and at least one limitation or failure.
- Answer in your own words: "What does this output prove, and what does it not prove?"

## Terminology oracle

- The data contract rejects an invalid schema. Artifact reload parity meets the tolerance, and negative tests produce intentional errors.
- Answer the `Explain it yourself` question in your own words and point to the evidence. Do not only copy a glossary.

## If your result differs

Use small synthetic data. Avoid exact metric assertions while randomness remains unlocked.

This is a self-check, not an assignment to submit. Keep evidence local. Do not commit secrets, personal data, large raw datasets, or paid cloud output.
