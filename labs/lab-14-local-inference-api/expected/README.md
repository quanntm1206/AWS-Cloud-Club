# Reference result - lab-14-local-inference-api

## Oracle

Send a valid payload, a missing column, and a wrong type. Do not log sensitive raw features.

## Required receipt

- Run `python scripts/run_lab.py --lab 14` from the repository root. The full PowerShell and Bash commands are in the lab README.
- The JSON must contain `status=starter-example-completed`; in `result`, look for the `/health` and `/predict` contracts, 422, and 503.
- Keep a local learning log with the seed or config, runtime, the lab-specific check, and at least one limitation or failure.
- Answer in your own words: "What does this output prove, and what does it not prove?"

## Terminology oracle

**Expected reasoning:** The API should separate successful predictions, client data errors, and an unavailable model. Its latency claim should cover only the stated local warm-request conditions.

**Evidence mapping:** Use `/health`, successful `/predict`, 422, and 503 responses to check the API contract. Use the validated schema and artifact identity for inference, then record the payload, environment, and timing sample for latency.

**Misconception check:** A 500 response is not a suitable client-error contract, and one warm request is not production latency. The starter status is smoke evidence only.

## If your result differs

If a client error returns 500, move validation to the boundary before calling the model.

This is a self-check, not an assignment to submit. Keep evidence local. Do not commit secrets, personal data, large raw datasets, or paid cloud output.
