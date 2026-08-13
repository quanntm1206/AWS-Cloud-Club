# Lab 15 - Package the service and run a CI smoke test

## Goal

A container makes the runtime consistent, but a successful image build does not prove that the service is safe. Check the user, health endpoint, prediction path, and container cleanup.

## Terms used in this lab

**New terms:** `container`, `CI`

**Review:** `API contract`, `artifact`, `reproducibility`, `latency`

**Use in this lab:** Package the service and API contract in a `container`. Use `CI` for data validation, parity, and artifact tests. Measure a small latency sample, then clean up the container to preserve reproducibility.

**Explain it yourself:** Which parts of reproducibility do containers and CI improve, and which tests do they not replace?

## Before you start

Read `roadmap/weeks/week-16.md`, work from the repository root, and prepare a local place for evidence. Do not put credentials, personal data, or large artifacts in Git.

## Steps

1. Run the Python smoke demo to inspect the static Docker and CI contract.
2. Build the image, run `id`, and confirm that the process is not root.
3. Start the container. Call `/health` and `/predict` with valid and invalid payloads, then read the logs.
4. Stop the container even when the smoke test fails. Confirm that CI runs offline checks and does not deploy to AWS.

## Run the smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 15
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 15
```

The result is saved to `.artifacts/lab-15-evidence.json`. In `result`, you will see the non-root user, health and prediction smoke checks, and confirmation that CI does not deploy to AWS.
`status=starter-example-completed` only confirms that the example code ran. It does **not** mean that you met all acceptance criteria.


## Run the real Docker smoke test

The Python smoke demo checks only the static contract. The commands below require Docker Desktop or Docker Engine:

```powershell
docker build -t ml-roadmap:lab15 .
docker run --rm ml-roadmap:lab15 id
docker run --rm -d --name ml-roadmap-lab15 -p 8000:8000 ml-roadmap:lab15
Invoke-RestMethod http://127.0.0.1:8000/health
$body = @{age=35; tenure_months=12; monthly_charge=79; region='north'; contract='monthly'} | ConvertTo-Json
try { Invoke-WebRequest http://127.0.0.1:8000/predict -Method Post -ContentType application/json -Body $body } catch { $_.Exception.Response.StatusCode.value__ }
docker logs ml-roadmap-lab15
docker stop ml-roadmap-lab15
```

`id` must show a non-root user. Without a mounted artifact, health returns `degraded` and prediction safely returns `503`. With a local artifact, mount its directory as read-only, set `ML_ROADMAP_ARTIFACT_DIR=/artifacts`, then check `model_loaded=true`. If any step fails, still run `docker logs` and `docker stop`; do not leave the container running.

## When you are done

- The evidence covers build, run, non-root, health, prediction, logs, and stop. No container remains running.
- Health is degraded and prediction returns 503 when the artifact is missing. A read-only mount allows `model_loaded=true`.

## When you get stuck

Read the first build error, then check `.dockerignore` and the build context. If the service fails, read `docker logs` and still run `docker stop`.

Predict the output first, then compare it with [`expected/README.md`](expected/README.md) and record what you learned locally. No submission is required.
