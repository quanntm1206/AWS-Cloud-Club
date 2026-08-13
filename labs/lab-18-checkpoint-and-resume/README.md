# Lab 18 - Save and resume a complete checkpoint

## Goal

A useful checkpoint is a contract for continuing training, not only a weights file. Stop a run deliberately, then restore all required state.

## Terms used in this lab

**New terms:** `early stopping`, `fine-tuning`

**Review:** `transfer learning`, `freeze`, `checkpoint`, `optimizer`, `epoch`, `validation set`

**Use in this lab:** Run a frozen `transfer learning` baseline, then optionally use `fine-tuning`. Use `freeze` to keep the backbone fixed. Save a `checkpoint` with optimizer and epoch state, apply `early stopping` on the validation set, and resume to prove that state was preserved.

**Explain it yourself:** How is a checkpoint different from model weights? How do fine-tuning and early stopping use the validation set?

## Before you start

Read `roadmap/weeks/week-19.md`, work from the repository root, and prepare a local place for evidence. Do not put credentials, personal data, or large artifacts in Git.

## Steps

1. Run the local smoke demo. Read the best epoch, resume epoch, and patience.
2. In the real notebook, train for 1 epoch. Save the model, optimizer, epoch, best metric, config, seed, and label mapping.
3. Start a new runtime or process. Upload `last_checkpoint.pt` or `artifacts.zip`, set `RESUME=True`, and keep `RUN_EPOCHS=1` so epoch 1 loads and epoch 2 runs. If the file is missing, the notebook must stop instead of silently restarting training.
4. Compare best and last checkpoints. Export the ZIP and checksum before closing the session.

## Run the smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 18
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 18
```

The result is saved to `.artifacts/lab-18-evidence.json`. In `result`, you will see smoke metadata; the real notebook saves model, optimizer, epoch, and config.
`status=starter-example-completed` only confirms that the example code ran. It does **not** mean that you met all acceptance criteria.


## Complete exercise in PyTorch

The local command is only a quick smoke demo. Real training and evaluation are in these notebooks:

- Colab: [`notebooks/colab/cv_transfer_learning_colab.ipynb`](../../notebooks/colab/cv_transfer_learning_colab.ipynb)
- Kaggle: [`notebooks/kaggle/cv_transfer_learning_kaggle.ipynb`](../../notebooks/kaggle/cv_transfer_learning_kaggle.ipynb)

Choose **one** platform. Run `cpu-mini` first and move to `gpu-free` only when an accelerator is available. Download `artifacts.zip` before the session ends.
`RUN_EPOCHS` is the number of additional epochs in each session, not the total number of epochs from the beginning.

## When you are done

- The resumed run starts at the correct epoch, preserves optimizer state and history, and does not use the test set for early stopping.
- You can distinguish inference weights from a resumable checkpoint, and you download the artifact locally.

## When you get stuck

If loading fails, compare architecture, config, and label mapping first. If optimizer loading fails, check parameter groups instead of silently dropping its state.

Predict the output first, then compare it with [`expected/README.md`](expected/README.md) and record what you learned locally. No submission is required.
