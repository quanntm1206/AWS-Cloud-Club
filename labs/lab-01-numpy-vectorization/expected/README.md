# Reference result - lab-01-numpy-vectorization

## Oracle

Calculate one row by hand, then compare the loop with `X @ w` using `np.allclose`.

## Required receipt

- Run `python scripts/run_lab.py --lab 1` from the repository root. The full PowerShell and Bash commands are in the lab README.
- The JSON must contain `status=starter-example-completed`; in `result`, look for `vectorization_matches_loop=true` and the first five scores.
- Keep a local learning log with the seed or config, runtime, the lab-specific check, and at least one limitation or failure.
- Answer in your own words: "What does this output prove, and what does it not prove?"

## Terminology oracle

**Expected reasoning:** The loop and vectorized code should calculate the same dot product for every sample when the feature and parameter shapes match.

**Evidence mapping:** Use the predicted shapes and hand calculation to explain the array roles. Then use both output arrays and `vectorization_matches_loop=true` to show that the two implementations agree within tolerance.

**Misconception check:** Faster code is not automatically correct. The starter status does not replace the shape prediction, hand calculation, or comparison with the loop.

## If your result differs

If the shapes do not match, print `X.shape` and `w.shape`. Do not use `reshape` until you understand the axis.

This is a self-check, not an assignment to submit. Keep evidence local. Do not commit secrets, personal data, large raw datasets, or paid cloud output.
