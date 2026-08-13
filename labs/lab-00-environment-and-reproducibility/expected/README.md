# Reference result - lab-00-environment-and-reproducibility

## Oracle

Run it twice; the row count, schema, and seed must match.

## Required receipt

- Run `python scripts/run_lab.py --lab 0` from the repository root. The full PowerShell and Bash commands are in the lab README.
- The JSON must contain `status=starter-example-completed`; in `result`, look for `rows`, `dtypes`, and `seed`.
- Keep a local learning log with the seed or config, runtime, the lab-specific check, and at least one limitation or failure.
- Answer in your own words: "What does this output prove, and what does it not prove?"

## Terminology oracle

- Both environment reports have the same `schema`, `seed`, and number of `sample` rows. The learning log identifies the `dataset` and explains the limits of `reproducibility`.
- Answer the `Explain it yourself` question in your own words and point to the evidence. Do not only copy a glossary.

## If your result differs

If an import fails, rerun the bootstrap check and confirm that Python comes from `.venv`.

This is a self-check, not an assignment to submit. Keep evidence local. Do not commit secrets, personal data, large raw datasets, or paid cloud output.
