# Lab 16 - Make tensors, gradients, and devices visible

## Goal

This local lab exposes the neural-network training loop without depending on a GPU. The smoke demo uses NumPy; use it to check the loss before moving to the week 17 PyTorch loop.

## Terms used in this lab

**New terms:** `tensor`, `batch`, `epoch`, `optimizer`, `device`

**Review:** `parameter`, `gradient`, `loss`, `validation set`

**Use in this lab:** Create each `tensor` in a `batch` and run several `epoch` cycles. Use the `optimizer` to update parameters from the gradient and loss, keep the model and input on the same `device`, and evaluate on the validation set.

**Explain it yourself:** How do batch, epoch, loss, and optimizer form one training loop?

## Before you start

Read `roadmap/weeks/week-17.md`, work from the repository root, and prepare a local place for evidence. Do not put credentials, personal data, or large artifacts in Git.

## Steps

1. Print the shapes of inputs, hidden values, logits, and targets. Predict the parameter count.
2. Run the seeded mini MLP. Record the loss over the steps and confirm the trend.
3. In a small PyTorch loop, omit the gradient reset once, observe the result, then restore it.
4. Run validation with `eval()` and `no_grad()`. Print device and dtype.

## Run the smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 16
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 16
```

The result is saved to `.artifacts/lab-16-evidence.json`. In `result`, you will see decreasing losses, the device, and the parameter count.
`status=starter-example-completed` only confirms that the example code ran. It does **not** mean that you met all acceptance criteria.

## When you are done

- The output contains decreasing loss, device, and parameter count. You can explain zero-grad, forward, backward, and step.
- The loop runs on CPU. The model, inputs, and targets share a device, and targets have the correct dtype for the loss.

## When you get stuck

Print shape, dtype, and device immediately before forward and loss. Fix the first mismatch; do not move to GPU to avoid a logic error.

Predict the output first, then compare it with [`expected/README.md`](expected/README.md) and record what you learned locally. No submission is required.
