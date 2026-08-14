# Lab 14 - Check the local inference API contract

## Goal

An API is where outside data meets the model. Give client errors, artifact errors, and successful responses different contracts instead of turning everything into a 500 response.

## Terms used in this lab

**New terms:** `API contract`, `latency`

**Review:** `data contract`, `artifact`, `inference`, `schema`

**Use in this lab:** Define the `API contract`, measure `latency`, and send valid and invalid samples through inference. The data contract rejects an invalid schema before the artifact runs, and responses do not expose raw features.

**Explain it yourself:** How is an API contract different from a data contract? What does the measured latency not prove?


## Apply the concepts

### Two contracts

**Terms:** `API contract`, `data contract`, `schema`

**What they mean here:** The `API contract` defines endpoints, payloads, status codes, and response bodies. Within that boundary, the `data contract` validates the model-input `schema`.

**Where you will see them:** `/health`, successful `/predict`, 422 input errors, and 503 unavailable-model responses use distinct paths.

**Common mistake:** Returning 500 for client schema errors or exposing raw data and stack traces.

**Evidence to keep:** Keep sanitized request shapes, status codes, response bodies, and logs for all paths.

**Explain after the lab:** Explain which contract rejects a wrong type and which represents that rejection.

### Measured inference

**Terms:** `artifact`, `inference`, `latency`

**What they mean here:** `inference` loads the intended `artifact`; measured `latency` covers a declared warm local payload, not every deployment.

**Where you will see them:** Artifact identity, health state, output, payload size, and warm timings form the record.

**Common mistake:** Calling one warm local request production latency.

**Evidence to keep:** Keep checksum/version, payload and batch, warm-up rule, timings, and environment.

**Explain after the lab:** State exactly what the latency covers and one unmeasured condition.

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
