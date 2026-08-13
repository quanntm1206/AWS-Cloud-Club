# Lab 11 - Combine the tabular pipeline into a mini-project

## Goal

This mini-project checks whether the complete path from data to artifact can run again. A good model that exists only in a notebook is not a reproducible product.

## Terms used in this lab

**New terms:** `artifact`, `manifest`, `inference`

**Review:** `schema`, `data split`, `pipeline`

**Use in this lab:** Lock the schema and data split, then run the pipeline. Save an `artifact` with a `manifest`, load it in a new process for inference, and compare the baseline, metric, and checksum.

**Explain it yourself:** How do artifact, manifest, and inference work together to make the pipeline repeatable?

## Before you start

Read `roadmap/weeks/week-12.md`, work from the repository root, and prepare a local place for evidence. Do not put credentials, personal data, or large artifacts in Git.

## Steps

1. Lock the problem, schema, split, baseline, and success criteria before training.
2. Run the churn mini-project end to end. Save metrics, the model, and the manifest.
3. Load the artifact in a new process. Check prediction agreement and the checksum.
4. Complete the local model card and experiment report with misuse, failures, and limitations.

## Run the smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 11
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 11
```

The result is saved to `.artifacts/lab-11-evidence.json`. In `result`, you will see metrics and the artifact contract.
`status=starter-example-completed` only confirms that the example code ran. It does **not** mean that you met all acceptance criteria.

## When you are done

- The pipeline runs from a clean shell. Its artifact contract includes the model, feature names, threshold, and checksum.
- Predictions match before and after loading. The report records the command, config, seed, and a negative result.

## When you get stuck

If predictions differ, compare feature order, preprocessing, and threshold. If a clean shell fails, look for hidden state or a relative path.

Predict the output first, then compare it with [`expected/README.md`](expected/README.md) and record what you learned locally. No submission is required.
