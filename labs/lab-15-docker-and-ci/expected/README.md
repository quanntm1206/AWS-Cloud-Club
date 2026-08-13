# Reference result - lab-15-docker-and-ci

## Oracle

Run build, start, logs, health, prediction, and stop as described in the lab.

## Required receipt

- Run `python scripts/run_lab.py --lab 15` from the repository root. The full PowerShell and Bash commands are in the lab README.
- The JSON must contain `status=starter-example-completed`; in `result`, look for the non-root user, health and prediction smoke checks, and confirmation that CI does not deploy to AWS.
- Keep a local learning log with the seed or config, runtime, the lab-specific check, and at least one limitation or failure.
- Answer in your own words: "What does this output prove, and what does it not prove?"

## Terminology oracle

- The container runs as non-root. CI tests the package, artifact, and API contract offline. The container is cleaned up, and CI does not deploy to AWS.
- Answer the `Explain it yourself` question in your own words and point to the evidence. Do not only copy a glossary.

## If your result differs

If the build is slow or the image is large, check `.dockerignore` and dependency layer order.

This is a self-check, not an assignment to submit. Keep evidence local. Do not commit secrets, personal data, large raw datasets, or paid cloud output.
