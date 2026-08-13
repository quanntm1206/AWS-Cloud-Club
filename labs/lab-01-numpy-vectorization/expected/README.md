# Reference result - lab-01-numpy-vectorization

## Oracle

Calculate one row by hand, then compare the loop with `X @ w` using `np.allclose`.

## Required receipt

- Run `python scripts/run_lab.py --lab 1` from the repository root. The full PowerShell and Bash commands are in the lab README.
- The JSON must contain `status=starter-example-completed`; in `result`, look for `vectorization_matches_loop=true` and the first five scores.
- Keep a local learning log with the seed or config, runtime, the lab-specific check, and at least one limitation or failure.
- Answer in your own words: "What does this output prove, and what does it not prove?"

## Terminology oracle

- The evidence records the shapes of `feature`, `label / target`, and `parameter`. `vectorization` matches the loop within tolerance on the same dataset and samples.
- Answer the `Explain it yourself` question in your own words and point to the evidence. Do not only copy a glossary.

## If your result differs

If the shapes do not match, print `X.shape` and `w.shape`. Do not use `reshape` until you understand the axis.

This is a self-check, not an assignment to submit. Keep evidence local. Do not commit secrets, personal data, large raw datasets, or paid cloud output.
