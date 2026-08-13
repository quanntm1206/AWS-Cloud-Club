# Lab 01 - Read NumPy shapes and check vectorization

## Goal

Matrix multiplication is useful only when you know what each dimension represents. Connect `X @ w` to a dataset with many rows instead of treating vectorization as a shortcut for shorter code.

## Terms used in this lab

**New terms:** `feature`, `label / target`, `parameter`, `vectorization`

**Review:** `dataset`, `sample`, `schema`

**Use in this lab:** Represent each `sample` as a `feature` vector and keep the `label / target` for interpretation. Use `vectorization` to calculate model output from a `parameter`, then record the array `dataset` and `schema`.

**Explain it yourself:** What roles do feature, label / target, and parameter play in `X @ w`?

## Before you start

Read `roadmap/weeks/week-02.md`, work from the repository root, and prepare a local place for evidence. Do not put credentials, personal data, or large result files in Git.

## Steps

1. Write the expected shapes of `X`, `w`, and `X @ w` before running the code.
2. Calculate the score for one row by hand. Then run the loop and vectorized multiplication.
3. Use `np.allclose` to compare them. Deliberately change one shape or axis and read the error.
4. Calculate MAE and standardization on a small array. Check zero variance and empty input.

## Run the smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 1
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 1
```

The result is saved to `.artifacts/lab-01-evidence.json`. In `result`, you will see `vectorization_matches_loop=true` and the first five scores.
`status=starter-example-completed` only confirms that the example code ran. It does **not** mean that you met all acceptance criteria.

## When you are done

- `vectorization_matches_loop=true`, and one hand-calculated row matches the output within tolerance.
- You can explain valid broadcasting and why an arbitrary `reshape` can hide a business-logic error.

## When you get stuck

Reduce the example to two rows, print each `shape`, and name every axis. Do not add `reshape` until you can explain the meaning of the new dimension.

Predict the output first, then compare it with [`expected/README.md`](expected/README.md) and record what you learned locally. No submission is required.
