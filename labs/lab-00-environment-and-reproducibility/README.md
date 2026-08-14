# Lab 00 - Check the environment and reproducibility

## Goal

You do not need to train a model in the first session. Build a trustworthy starting point: the same code, seed, and environment should produce the same small report.

## Terms used in this lab

**New terms:** `dataset`, `sample`, `schema`, `reproducibility`, `seed`

**Review:** None - this is the first lab.

**Use in this lab:** Open the smoke `dataset`, count its `sample` rows, check its `schema`, fix the `seed`, then run twice to test `reproducibility`.

**Explain it yourself:** How is a dataset different from a sample? How far do schema and seed support reproducibility? Here, support means provide evidence for the claim.


## Apply the concepts

### Data and repeatability

**Terms:** `dataset`, `sample`, `schema`, `reproducibility`, `seed`

**What they mean here:** The CSV is the `dataset`, one row is a `sample`, and the column names and data types form the `schema`. The `seed` controls the demo's random choices. Here, `reproducibility` means getting the same checked result from the same recorded inputs and environment.

**Where you will see them:** Compare the sample file with `rows`, `dtypes`, and `seed` in `.artifacts/lab-00-evidence.json`, then repeat from a new terminal.

**Common mistake:** Treating the same row count and seed as proof that the data values, dependencies, and devices are also identical.

**Evidence to keep:** Keep both JSON reports, Python/dependency/OS versions, and any observed difference or tolerance.

**Explain after the lab:** Point to evidence for the dataset, one sample-level fact, the schema, and one factor the seed does not control.

## Before you start

Read `roadmap/weeks/week-01.md`, work from the repository root, and prepare a local place for evidence. Do not put credentials, personal data, or large result files in Git.

## Steps

1. Run the bootstrap check. Record the Python version, dependencies, and operating system.
2. Open the smoke-demo JSON. Compare its row count, dtypes, and seed with the sample data.
3. Run it again from a new terminal. Compare both reports and record any tolerance or observed difference.
4. Create the week 01 learning log. Record one limitation of this check.

## Run the smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 0
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 0
```

The result is saved to `.artifacts/lab-00-evidence.json`. In `result`, you will see `rows`, `dtypes`, and `seed`.
`status=starter-example-completed` only confirms that the example code ran. It does **not** mean that you met all acceptance criteria.

## When you are done

- Two runs have the same row count, schema, and seed. You record any environment difference.
- You can explain why a seed supports reproducibility but does not guarantee bit-identical results on all hardware.

## When you get stuck

If an import fails, confirm that the terminal uses Python from `.venv`, then rerun the bootstrap check. If the runs differ, compare versions and inputs before changing code.

Predict the output first, then compare it with [`expected/README.md`](expected/README.md) and record what you learned locally. No submission is required.
