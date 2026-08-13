# Reference result - lab-12-notebook-to-package

## Oracle

Run from a clean shell. The notebook calls the package and does not copy training logic.

## Required receipt

- Run `python scripts/run_lab.py --lab 12` from the repository root. The full PowerShell and Bash commands are in the lab README.
- The JSON must contain `status=starter-example-completed`; in `result`, look for the config key list and `notebook_state_required=false`.
- Keep a local learning log with the seed or config, runtime, the lab-specific check, and at least one limitation or failure.
- Answer in your own words: "What does this output prove, and what does it not prove?"

## Terminology oracle

- The package and CLI use clear configuration. The same config gives equivalent output, and the notebook keeps no hidden logic.
- Answer the `Explain it yourself` question in your own words and point to the evidence. Do not only copy a glossary.

## If your result differs

If only the notebook runs, look for global state, the working directory, and cells executed out of order.

This is a self-check, not an assignment to submit. Keep evidence local. Do not commit secrets, personal data, large raw datasets, or paid cloud output.
