# Lab 17 - Run real transfer learning on free compute

## Goal

The local smoke demo only shows which layers are frozen. The main exercise is a real PyTorch notebook: use a pretrained backbone as a feature extractor and train only the classifier head.

## Terms used in this lab

**New terms:** `augmentation`, `backbone`, `checkpoint`, `freeze`, `transfer learning`

**Review:** `tensor`, `batch`, `epoch`, `device`, `overfitting`

**Use in this lab:** Apply `augmentation` only to each training `batch` and keep validation transforms deterministic. Load the pretrained `backbone` on the correct `device`, `freeze` its parameters, run `transfer learning` on tensors, save a `checkpoint`, and track epoch and loss for overfitting.

**Explain it yourself:** How is augmentation different from deterministic preprocessing? What does freezing the backbone achieve?

## Before you start

Read `roadmap/weeks/week-18.md`, work from the repository root, and prepare a local place for evidence. Do not put credentials, personal data, or large artifacts in Git.

## Steps

1. Run the local smoke demo. Explain `requires_grad` for the backbone and head.
2. Choose one Colab or Kaggle notebook. Run `cpu-mini` from the start and confirm that pretrained weights load.
3. Confirm pretrained normalization, frozen parameters, and a trainable head.
4. If a free GPU is available, run `gpu-free`. Export the checkpoint, metrics, and manifest.

## Run the smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 17
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 17
```

The result is saved to `.artifacts/lab-17-evidence.json`. In `result`, you will see a smoke dictionary of frozen layers; the real notebook exports a checkpoint and metrics.
`status=starter-example-completed` only confirms that the example code ran. It does **not** mean that you met all acceptance criteria.


## Complete exercise in PyTorch

The local command is only a quick smoke demo. Real training and evaluation are in these notebooks:

- Colab: [`notebooks/colab/cv_transfer_learning_colab.ipynb`](../../notebooks/colab/cv_transfer_learning_colab.ipynb)
- Kaggle: [`notebooks/kaggle/cv_transfer_learning_kaggle.ipynb`](../../notebooks/kaggle/cv_transfer_learning_kaggle.ipynb)

Choose **one** platform. Run `cpu-mini` first and move to `gpu-free` only when an accelerator is available. Download `artifacts.zip` before the session ends.

## When you are done

- Only the head is trainable in the smoke output. The real notebook completes at least CPU-mini and exports a local artifact.
- If you use FakeData, call the result a pipeline smoke test, not model quality.
- If the notebook uses random weights, the result is only an execution smoke test and does not pass the transfer-learning gate.

## When you get stuck

If data cannot download, use the FakeData fallback and record the limitation. If pretrained weights cannot download, check only the execution path and retry later with internet or cache. If loss does not change, check trainable parameters, the optimizer, and normalization.

Predict the output first, then compare it with [`expected/README.md`](expected/README.md) and record what you learned locally. No submission is required.
