# Lab 12 - Move notebook logic into configuration and a CLI

## Goal

Move training logic out of the notebook without changing behavior. The goal is not more files; it is clear input and output with one source of logic.

## Terms used in this lab

**New terms:** `package`, `configuration`

**Review:** `reproducibility`, `pipeline`, `artifact`

**Use in this lab:** Move the pipeline into a `package`. Put the seed and hyperparameters in `configuration`, then rerun it so reproducibility, the artifact, and inference do not depend on notebook state.

**Explain it yourself:** How do a package and configuration remove hidden notebook state?

## Before you start

Read `roadmap/weeks/week-13.md`, work from the repository root, and prepare a local place for evidence. Do not put credentials, personal data, or large artifacts in Git.

## Steps

1. Mark which cells handle data, features, training, evaluation, and artifact I/O.
2. Move core logic into a module. The notebook should only import and call it.
3. Create a config with a schema and a CLI that accepts config, data, and output paths.
4. Run the same config from the notebook and a clean shell. Compare metrics and artifacts within tolerance.

## Run the smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 12
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 12
```

The result is saved to `.artifacts/lab-12-evidence.json`. In `result`, you will see the config key list and `notebook_state_required=false`.
`status=starter-example-completed` only confirms that the example code ran. It does **not** mean that you met all acceptance criteria.

## When you are done

- The output shows clear config keys and `notebook_state_required=false`.
- Training logic is not copied in two places. The CLI gives a useful error for invalid config.

## When you get stuck

Restart the kernel and open a clean shell. Any variable or file that exists only after an earlier cell is a hidden dependency to remove.

Predict the output first, then compare it with [`expected/README.md`](expected/README.md) and record what you learned locally. No submission is required.
