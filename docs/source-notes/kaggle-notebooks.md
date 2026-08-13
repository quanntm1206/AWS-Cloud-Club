# Kaggle Notebooks - a free path for Computer Vision

**Verified:** 2026-08-12 against the [Kaggle Notebooks documentation](https://www.kaggle.com/docs/notebooks).

The roadmap does not promise a fixed number of GPU or TPU hours because availability and quotas may change.
The notebook detects the device and uses `cpu-mini` when no accelerator is available.

## Open the notebook

1. Download [`notebooks/kaggle/cv_transfer_learning_kaggle.ipynb`](../../notebooks/kaggle/cv_transfer_learning_kaggle.ipynb).
2. In Kaggle, create a Notebook, then select `File > Import Notebook` to upload the file.
3. Open Settings and enable an accelerator if your account can use one. Run the environment check to confirm the device.
4. Run `cpu-mini` first. With `gpu-free`, the notebook uses a CIFAR10 subset, a frozen backbone, and no more than 5 epochs.
5. Select `Save Version`, wait for the output, then download `artifacts.zip`, metrics, the manifest, and checkpoints.
6. Disable the accelerator or end the session after export. Do not leave the notebook running in the background.

## Data and internet access

To use another dataset, add it with `Add Input`. Data usually appears as read-only files under `/kaggle/input`.
Record the licence and split. Never put credentials or private tokens in a notebook. If internet access is off
or a download fails, use an added input dataset or a FakeData smoke test. Do not report FakeData accuracy as
model quality. If pretrained weights are not cached and internet access is off, the random-weight fallback only
checks the code. It does not pass the transfer-learning gate.

## Quick fixes

- GPU unavailable: run CPU-mini. The core work remains valid.
- File not found: print the working directory and list `/kaggle/input`. Do not hard-code an unverified dataset name.
- Out of memory: reduce the batch, image size, or sample count. Restart the session, then rerun from the start.
- Session stops: create a new notebook version, upload the checkpoint, and confirm the configuration and label mapping before resuming.
- Output disappears: select `Save Version` and download the artifacts before ending the session.

Choose **Kaggle or Colab**. You do not need to run both or buy a paid plan.
