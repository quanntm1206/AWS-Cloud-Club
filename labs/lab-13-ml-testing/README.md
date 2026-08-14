# Lab 13 - Test data, models, and artifacts

## Goal

ML tests must check data and artifacts, not only whether a function returns the right type. Focus on failures that often appear after a model is packaged.

## Terms used in this lab

**New terms:** `data contract`, `parity`

**Review:** `schema`, `pipeline`, `artifact`, `reproducibility`

**Use in this lab:** Write a `data contract` for the schema. Test fit-save-load-predict `parity` for the pipeline and artifact, add negative cases for invalid samples, and set a reproducibility tolerance.

**Explain it yourself:** How is a data contract more than a schema? How does parity protect an artifact?


## Apply the concepts

### Accepted data boundary

**Terms:** `data contract`, `schema`, `pipeline`

**What they mean here:** The `schema` covers columns and data types. The `data contract` also defines rules for missing values, finite numbers, empty input, and errors before data enters the `pipeline`.

**Where you will see them:** Valid data plus missing-column, dtype, NaN/Inf, empty, and unseen-category cases exercise the boundary.

**Common mistake:** Calling a dtype check a complete contract.

**Evidence to keep:** Keep every case, rule, expected result, error, and pipeline entry point.

**Explain after the lab:** Name one rule beyond the schema and the negative test that proves the rule is enforced.

### Saved behavior

**Terms:** `parity`, `artifact`, `reproducibility`

**What they mean here:** `parity` means predictions before and after loading the `artifact` agree within tolerance; seeded tests make the `reproducibility` check useful.

**Where you will see them:** Fit-save-load-predict ends at `artifact_reload_parity=true`, with a synthetic-signal baseline gate.

**Common mistake:** Accepting a file that loads without comparing outputs, or demanding brittle exact floats.

**Evidence to keep:** Keep prediction arrays, tolerance, checksum, seed, and baseline result.

**Explain after the lab:** Explain what reload parity catches and which tests it cannot replace.

## Before you start

Read `roadmap/weeks/week-14.md`, work from the repository root, and prepare a local place for evidence. Do not put credentials, personal data, or large artifacts in Git.

## Steps

1. Test the valid schema plus missing column, wrong dtype, NaN or Inf, and empty input cases.
2. Send an unseen category through the correct preprocessing pipeline.
3. Fit, save, load, and predict, then check parity within tolerance.
4. Create synthetic data with a signal. Confirm that the model passes a reasonable gate against the dummy model.

## Run the smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 13
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 13
```

The result is saved to `.artifacts/lab-13-evidence.json`. In `result`, you will see `artifact_reload_parity=true` and your added negative cases.
`status=starter-example-completed` only confirms that the example code ran. It does **not** mean that you met all acceptance criteria.

## When you are done

- `artifact_reload_parity=true`, and every added negative case produces an intentional error.
- Tests are small and deterministic. Metric assertions use tolerances instead of fragile exact stochastic values.

## When you get stuck

Run each test separately with small synthetic data. If a test is flaky, list randomness sources and lock the seed before relaxing the assertion.

Predict the output first, then compare it with [`expected/README.md`](expected/README.md) and record what you learned locally. No submission is required.
