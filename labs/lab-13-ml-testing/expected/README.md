# Reference result - lab-13-ml-testing

## Oracle

Add checks for a missing column, wrong dtype, unseen category, and damaged artifact.

## Required receipt

- Run `python scripts/run_lab.py --lab 13` from the repository root. The full PowerShell and Bash commands are in the lab README.
- The JSON must contain `status=starter-example-completed`; in `result`, look for `artifact_reload_parity=true` and your added negative cases.
- Keep a local learning log with the seed or config, runtime, the lab-specific check, and at least one limitation or failure.
- Answer in your own words: "What does this output prove, and what does it not prove?"

## Terminology oracle

**Expected reasoning:** The data contract should reject each intentional boundary violation. The fit-save-load-predict check should also preserve numerical behavior within a stated tolerance.

**Evidence mapping:** Match every invalid case with its rule and expected error. Then compare the predictions, checksum, tolerance, and `artifact_reload_parity=true` result for the saved artifact.

**Misconception check:** A file that loads has not yet proved parity, and exact floating-point equality can be too strict. The starter status does not replace the negative tests.

## If your result differs

Use small synthetic data. Avoid exact metric assertions while randomness remains unlocked.

This is a self-check, not an assignment to submit. Keep evidence local. Do not commit secrets, personal data, large raw datasets, or paid cloud output.
