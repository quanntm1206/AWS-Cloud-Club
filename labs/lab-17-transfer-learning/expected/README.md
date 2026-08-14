# Reference result - lab-17-transfer-learning

## Oracle

Choose exactly one Colab or Kaggle notebook. Run `cpu-mini` before using a GPU, if one is available.

## Required receipt

- Run `python scripts/run_lab.py --lab 17` from the repository root. The full PowerShell and Bash commands are in the lab README.
- The JSON must contain `status=starter-example-completed`; in `result`, look for a smoke dictionary of frozen layers; the real notebook exports a checkpoint and metrics.
- Keep a local learning log with the seed or config, runtime, the lab-specific check, and at least one limitation or failure.
- Answer in your own words: "What does this output prove, and what does it not prove?"

## Terminology oracle

**Expected reasoning:** A real transfer-learning run verifies the pretrained weights and normalization, freezes the backbone, trains the new head, and exports the results.

**Evidence mapping:** The weight source, device, `requires_grad` values, and parameter counts support the backbone claims. The transforms and metric history describe training, while the manifest and checksum identify the checkpoint.

**Misconception check:** The local frozen-layer dictionary is not completed training, and random validation augmentation would weaken the comparison. The starter status remains smoke-only.

## If your result differs

If results differ, check pretrained weights, normalization, seed, data split, and the number of trainable parameters.

This is a self-check, not an assignment to submit. Keep evidence local. Do not commit secrets, personal data, large raw datasets, or paid cloud output.
