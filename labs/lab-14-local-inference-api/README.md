# Lab 14 - Check the local inference API contract

## Goal

An API is where outside data meets the model. Give client errors, artifact errors, and successful responses different contracts instead of turning everything into a 500 response.

## Terms used in this lab

**New terms:** `API contract`, `latency`

**Review:** `data contract`, `artifact`, `inference`, `schema`

**Use in this lab:** Define the `API contract`, measure `latency`, and send valid and invalid samples through inference. The data contract rejects an invalid schema before the artifact runs, and responses do not expose raw features.

**Explain it yourself:** How is an API contract different from a data contract? What does the measured latency not prove?

## Before you start

Read `roadmap/weeks/week-15.md`, work from the repository root, and prepare a local place for evidence. Do not put credentials, personal data, or large artifacts in Git.

## Steps

1. Call `/health` and `/predict` with a valid payload.
2. Try a missing field, wrong type, and unknown category. Check that each 4xx response contains enough information without exposing internals.
3. Simulate an unavailable model. Check for a 503 response without a stack trace.
4. Measure warm latency for a small input group. Record payload and input limits plus the measurement limitation.

## Run the smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 14
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 14
```

The result is saved to `.artifacts/lab-14-evidence.json`. In `result`, you will see the `/health` and `/predict` contracts, 422, and 503.
`status=starter-example-completed` only confirms that the example code ran. It does **not** mean that you met all acceptance criteria.

## When you are done

- The contract covers `/health`, `/predict`, 422, and 503. Preprocessing matches the training artifact.
- Logs contain no sensitive raw features. The health endpoint does not train or modify the model.

## When you get stuck

Call the handler with the smallest valid payload first. If a client error becomes 500, move validation to the boundary and keep the internal exception in logs.

Predict the output first, then compare it with [`expected/README.md`](expected/README.md) and record what you learned locally. No submission is required.
