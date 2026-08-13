# Reference result - lab-17-transfer-learning

## Oracle

Choose exactly one Colab or Kaggle notebook. Run `cpu-mini` before using a GPU, if one is available.

## Required receipt

- Run `python scripts/run_lab.py --lab 17` from the repository root. The full PowerShell and Bash commands are in the lab README.
- The JSON must contain `status=starter-example-completed`; in `result`, look for a smoke dictionary of frozen layers; the real notebook exports a checkpoint and metrics.
- Keep a local learning log with the seed or config, runtime, the lab-specific check, and at least one limitation or failure.
- Answer in your own words: "What does this output prove, and what does it not prove?"

## Terminology oracle

- The receipt records augmentation, the pretrained backbone, frozen parameters, the device, and a checkpoint. The training history can be checked for overfitting.
- Answer the `Explain it yourself` question in your own words and point to the evidence. Do not only copy a glossary.

## If your result differs

If results differ, check pretrained weights, normalization, seed, data split, and the number of trainable parameters.

This is a self-check, not an assignment to submit. Keep evidence local. Do not commit secrets, personal data, large raw datasets, or paid cloud output.
