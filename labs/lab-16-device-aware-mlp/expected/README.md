# Reference result - lab-16-device-aware-mlp

## Oracle

The smoke demo uses NumPy on CPU. Then write and run the small PyTorch loop from week 17.

## Required receipt

- Run `python scripts/run_lab.py --lab 16` from the repository root. The full PowerShell and Bash commands are in the lab README.
- The JSON must contain `status=starter-example-completed`; in `result`, look for decreasing losses, the device, and the parameter count.
- Keep a local learning log with the seed or config, runtime, the lab-specific check, and at least one limitation or failure.
- Answer in your own words: "What does this output prove, and what does it not prove?"

## Terminology oracle

- The receipt records tensor shapes, batch, epoch, optimizer, and device. Loss decreases, and the parameter count is correct.
- Answer the `Explain it yourself` question in your own words and point to the evidence. Do not only copy a glossary.

## If your result differs

Print model, input, and target shape, dtype, and device. Check `zero_grad`, `eval`, and `no_grad`.

This is a self-check, not an assignment to submit. Keep evidence local. Do not commit secrets, personal data, large raw datasets, or paid cloud output.
