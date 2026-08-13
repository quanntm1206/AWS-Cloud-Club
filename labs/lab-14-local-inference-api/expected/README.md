# Reference result - lab-14-local-inference-api

## Oracle

Send a valid payload, a missing column, and a wrong type. Do not log sensitive raw features.

## Required receipt

- Run `python scripts/run_lab.py --lab 14` from the repository root. The full PowerShell and Bash commands are in the lab README.
- The JSON must contain `status=starter-example-completed`; in `result`, look for the `/health` and `/predict` contracts, 422, and 503.
- Keep a local learning log with the seed or config, runtime, the lab-specific check, and at least one limitation or failure.
- Answer in your own words: "What does this output prove, and what does it not prove?"

## Terminology oracle

- The API contract separates success, 422, and 503. Inference uses the correct artifact, and the latency record includes sample or batch limits.
- Answer the `Explain it yourself` question in your own words and point to the evidence. Do not only copy a glossary.

## If your result differs

If a client error returns 500, move validation to the boundary before calling the model.

This is a self-check, not an assignment to submit. Keep evidence local. Do not commit secrets, personal data, large raw datasets, or paid cloud output.
