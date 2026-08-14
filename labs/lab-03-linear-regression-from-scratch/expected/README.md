# Reference result - lab-03-linear-regression-from-scratch

## Oracle

Try several `epsilon` values. Both gradients must be close within the recorded tolerance.

## Required receipt

- Run `python scripts/run_lab.py --lab 3` from the repository root. The full PowerShell and Bash commands are in the lab README.
- The JSON must contain `status=starter-example-completed`; in `result`, look for the analytic gradient, finite-difference gradient, and `gradient_check=true`.
- Keep a local learning log with the seed or config, runtime, the lab-specific check, and at least one limitation or failure.
- Answer in your own words: "What does this output prove, and what does it not prove?"

## Terminology oracle

**Expected reasoning:** With a suitable learning rate, the loss should decrease. Agreement between the analytic gradient and finite differences supports the derivative code for these checked inputs.

**Evidence mapping:** Use the hand calculation to explain the prediction and loss. Compare the two gradient values for `gradient_check=true`, then connect the parameter and loss history to the learning-rate updates.

**Misconception check:** A passing gradient check does not prove that training will converge or that linear regression suits every dataset. The starter status only exercises the reference path.

## If your result differs

If the gradients differ, check the sign, averaging, and the central-difference formula.

This is a self-check, not an assignment to submit. Keep evidence local. Do not commit secrets, personal data, large raw datasets, or paid cloud output.
