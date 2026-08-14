# Reference result - lab-16-device-aware-mlp

## Oracle

The smoke demo uses NumPy on CPU. Then write and run the small PyTorch loop from week 17.

## Required receipt

- Run `python scripts/run_lab.py --lab 16` from the repository root. The full PowerShell and Bash commands are in the lab README.
- The JSON must contain `status=starter-example-completed`; in `result`, look for decreasing losses, the device, and the parameter count.
- Keep a local learning log with the seed or config, runtime, the lab-specific check, and at least one limitation or failure.
- Answer in your own words: "What does this output prove, and what does it not prove?"

## Terminology oracle

**Expected reasoning:** Tensor shapes and devices must match through the loss calculation. Training follows zero-grad, forward, backward, and step, while validation changes no parameters.

**Evidence mapping:** The printed shapes, dtypes, device, and parameter count describe the tensor path. The loss history and gradient-reset comparison show training behavior, while `eval()` and `no_grad()` show validation behavior.

**Misconception check:** A decreasing loss in a tiny seeded demo does not prove generalization. The starter status is smoke evidence only.

## If your result differs

Print model, input, and target shape, dtype, and device. Check `zero_grad`, `eval`, and `no_grad`.

This is a self-check, not an assignment to submit. Keep evidence local. Do not commit secrets, personal data, large raw datasets, or paid cloud output.
