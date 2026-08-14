# Reference result - lab-18-checkpoint-and-resume

## Oracle

Stop after one epoch, load the checkpoint, and continue. Distinguish the best checkpoint from the last one.

## Required receipt

- Run `python scripts/run_lab.py --lab 18` from the repository root. The full PowerShell and Bash commands are in the lab README.
- The JSON must contain `status=starter-example-completed`; in `result`, look for smoke metadata; the real notebook saves model, optimizer, epoch, and config.
- Keep a local learning log with the seed or config, runtime, the lab-specific check, and at least one limitation or failure.
- Answer in your own words: "What does this output prove, and what does it not prove?"

## Terminology oracle

**Expected reasoning:** A genuine resume restores the complete training state and continues from the next epoch. Early stopping must use validation history, not the test set.

**Evidence mapping:** The parameter groups identify the frozen or fine-tuning phase. Compare the best and last checkpoint metadata, checksums, epoch numbers, and optimizer state to show continuity across processes.

**Misconception check:** Loading model weights while restarting the optimizer is not a resume. The starter metadata only demonstrates the expected output shape.

## If your result differs

If resume fails, compare architecture, config, label mapping, epoch, and optimizer state.

This is a self-check, not an assignment to submit. Keep evidence local. Do not commit secrets, personal data, large raw datasets, or paid cloud output.
