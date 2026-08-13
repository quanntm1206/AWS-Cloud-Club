# Reference result - lab-18-checkpoint-and-resume

## Oracle

Stop after one epoch, load the checkpoint, and continue. Distinguish the best checkpoint from the last one.

## Required receipt

- Run `python scripts/run_lab.py --lab 18` from the repository root. The full PowerShell and Bash commands are in the lab README.
- The JSON must contain `status=starter-example-completed`; in `result`, look for smoke metadata; the real notebook saves model, optimizer, epoch, and config.
- Keep a local learning log with the seed or config, runtime, the lab-specific check, and at least one limitation or failure.
- Answer in your own words: "What does this output prove, and what does it not prove?"

## Terminology oracle

- The checkpoint stores model, optimizer, epoch, config, and transfer-learning state. Fine-tuning and early stopping use the validation set, not the test set.
- Answer the `Explain it yourself` question in your own words and point to the evidence. Do not only copy a glossary.

## If your result differs

If resume fails, compare architecture, config, label mapping, epoch, and optimizer state.

This is a self-check, not an assignment to submit. Keep evidence local. Do not commit secrets, personal data, large raw datasets, or paid cloud output.
