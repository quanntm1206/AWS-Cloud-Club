# Reference result - lab-11-tabular-mini-project

## Oracle

Train, save, and load in a new process. Complete the local experiment report and model card.

## Required receipt

- Run `python scripts/run_lab.py --lab 11` from the repository root. The full PowerShell and Bash commands are in the lab README.
- The JSON must contain `status=starter-example-completed`; in `result`, look for metrics and the artifact contract.
- Keep a local learning log with the seed or config, runtime, the lab-specific check, and at least one limitation or failure.
- Answer in your own words: "What does this output prove, and what does it not prove?"

## Terminology oracle

**Expected reasoning:** A fixed schema, split, and pipeline should create an artifact whose contract is recorded in the manifest. Loading it in a new process should preserve predictions within tolerance.

**Evidence mapping:** The command, configuration, schema, and split describe the training run. The manifest and checksum identify the saved files, while the paired predictions show inference parity.

**Misconception check:** Saving only the estimator does not preserve the complete artifact contract. The starter status is smoke evidence, not proof that the mini-project is reproducible.

## If your result differs

If reproduction differs, compare config, feature order, threshold, and dependencies first.

This is a self-check, not an assignment to submit. Keep evidence local. Do not commit secrets, personal data, large raw datasets, or paid cloud output.
