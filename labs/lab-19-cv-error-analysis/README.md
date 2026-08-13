# Lab 19 - Evaluate computer vision by class and failure

## Goal

The final computer-vision lab turns metrics into an understanding of failures. The local smoke demo gives the format; meaningful analysis must use predictions from the real notebook.

## Terms used in this lab

**New terms:** `macro average`, `weighted average`

**Review:** `confusion matrix`, `support`, `metric`, `validation set`, `error analysis`, `failure taxonomy`

**Use in this lab:** Create a confusion matrix, `macro average`, `weighted average`, and per-class metrics with `support`. Run error analysis on the `validation set` predictions and assign a failure taxonomy to real samples. Do not use FakeData for model validation.

**Explain it yourself:** How is macro average different from weighted average? How do the confusion matrix and support explain that difference?

## Before you start

Read `roadmap/weeks/week-20.md`, work from the repository root, and prepare a local place for evidence. Do not put credentials, personal data, or large artifacts in Git.

## Steps

1. Run the smoke demo to inspect the structure of per-class metrics and failure records.
2. From a real run, calculate precision, recall, F1, and support for every class, plus macro and weighted aggregates.
3. Plot a confusion matrix normalized by true class. Review no more than 20 errors with a confident-wrong sampling rule.
4. The notebook uses `error_type='unreviewed'`. Open each image, assign an evidence-based error group, then write a limitation and a testable next experiment. A placeholder is not a completed taxonomy.

## Run the smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 19
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 19
```

The result is saved to `.artifacts/lab-19-evidence.json`. In `result`, you will see per-class metrics and failure records.
`status=starter-example-completed` only confirms that the example code ran. It does **not** mean that you met all acceptance criteria.


## Complete exercise in PyTorch

The local command is only a quick smoke demo. Real training and evaluation are in these notebooks:

- Colab: [`notebooks/colab/cv_transfer_learning_colab.ipynb`](../../notebooks/colab/cv_transfer_learning_colab.ipynb)
- Kaggle: [`notebooks/kaggle/cv_transfer_learning_kaggle.ipynb`](../../notebooks/kaggle/cv_transfer_learning_kaggle.ipynb)

Choose **one** platform. Run `cpu-mini` first and move to `gpu-free` only when an accelerator is available. Download `artifacts.zip` before the session ends.

## When you are done

- The per-class table, confusion matrix, and failure taxonomy point to the same dataset, split, and config.
- FakeData does not support quality conclusions. For sensitive images, store only an ID and a safe local description.

## When you get stuck

Start with 5-10 errors and check the label mapping. If one class performs poorly, inspect support, the split, and transforms before fine-tuning.

Predict the output first, then compare it with [`expected/README.md`](expected/README.md) and record what you learned locally. No submission is required.
