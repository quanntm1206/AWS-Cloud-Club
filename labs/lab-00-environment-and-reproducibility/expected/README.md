# Reference result - lab-00-environment-and-reproducibility

## Oracle

Run it twice; the row count, schema, and seed must match.

## Required receipt

- Run `python scripts/run_lab.py --lab 0` from the repository root. The full PowerShell and Bash commands are in the lab README.
- The JSON must contain `status=starter-example-completed`; in `result`, look for `rows`, `dtypes`, and `seed`.
- Keep a local learning log with the seed or config, runtime, the lab-specific check, and at least one limitation or failure.
- Answer in your own words: "What does this output prove, and what does it not prove?"

## Terminology oracle

**Expected reasoning:** The two runs should have the same `rows`, `dtypes`, and `seed`. This supports a limited reproducibility claim for the recorded input and environment.

**Evidence mapping:** In each report, `rows` counts the samples, `dtypes` describes the schema, and `seed` records the random setting. Read these fields together with the Python, dependency, and operating-system versions.

**Misconception check:** `status=starter-example-completed` only means that the smoke example ran. The same seed cannot guarantee identical results when the data, software, or hardware changes.

## If your result differs

If an import fails, rerun the bootstrap check and confirm that Python comes from `.venv`.

This is a self-check, not an assignment to submit. Keep evidence local. Do not commit secrets, personal data, large raw datasets, or paid cloud output.
