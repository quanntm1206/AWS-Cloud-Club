# Reference result - lab-12-notebook-to-package

## Oracle

Run from a clean shell. The notebook calls the package and does not copy training logic.

## Required receipt

- Run `python scripts/run_lab.py --lab 12` from the repository root. The full PowerShell and Bash commands are in the lab README.
- The JSON must contain `status=starter-example-completed`; in `result`, look for the config key list and `notebook_state_required=false`.
- Keep a local learning log with the seed or config, runtime, the lab-specific check, and at least one limitation or failure.
- Answer in your own words: "What does this output prove, and what does it not prove?"

## Terminology oracle

**Expected reasoning:** The refactor succeeds when the notebook and CLI call one implementation with explicit configuration and produce equivalent outputs.

**Evidence mapping:** The configuration keys record the run inputs, and `notebook_state_required=false` shows that a clean shell can run the code. Compare the metrics and checksums from both entry points.

**Misconception check:** Copying logic into both the notebook and module creates two sources of truth. The starter status does not prove that the refactor preserved behavior.

## If your result differs

If only the notebook runs, look for global state, the working directory, and cells executed out of order.

This is a self-check, not an assignment to submit. Keep evidence local. Do not commit secrets, personal data, large raw datasets, or paid cloud output.
