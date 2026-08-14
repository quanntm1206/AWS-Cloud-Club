# Reference result - lab-15-docker-and-ci

## Oracle

Run build, start, logs, health, prediction, and stop as described in the lab.

## Required receipt

- Run `python scripts/run_lab.py --lab 15` from the repository root. The full PowerShell and Bash commands are in the lab README.
- The JSON must contain `status=starter-example-completed`; in `result`, look for the non-root user, health and prediction smoke checks, and confirmation that CI does not deploy to AWS.
- Keep a local learning log with the seed or config, runtime, the lab-specific check, and at least one limitation or failure.
- Answer in your own words: "What does this output prove, and what does it not prove?"

## Terminology oracle

**Expected reasoning:** The container must run the artifact-backed API as a non-root user and be stopped after the checks. CI should repeat offline tests without deploying anything to AWS.

**Evidence mapping:** The image tag, user ID, API responses, logs, timings, and stop result describe the container lifecycle. The workflow results and explicit no-deploy check describe the CI path.

**Misconception check:** A successful image build does not prove that the service is healthy, and CI is not production monitoring. The starter status only inspects the reference contract.

## If your result differs

If the build is slow or the image is large, check `.dockerignore` and dependency layer order.

This is a self-check, not an assignment to submit. Keep evidence local. Do not commit secrets, personal data, large raw datasets, or paid cloud output.
