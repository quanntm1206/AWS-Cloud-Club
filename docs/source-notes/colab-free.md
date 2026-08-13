# Colab Free - run CV without buying compute

**Verified:** 2026-08-12 against the [Google Colab FAQ](https://research.google.com/colaboratory/faq.html).

Colab Free may provide a GPU or TPU, but accelerator types, usage limits, idle timeouts, and VM lifetimes vary
with availability and usage patterns. The roadmap always includes `cpu-mini`, so a missing GPU will not block
you from completing the core work.

## Open the notebook

1. Download or open [`notebooks/colab/cv_transfer_learning_colab.ipynb`](../../notebooks/colab/cv_transfer_learning_colab.ipynb).
2. In Colab, select `File > Upload notebook`. To keep your edits, select `Copy to Drive`.
3. Run the `Environment check` cell. Select `Runtime > Change runtime type > GPU` only when you are ready to train.
4. Run the notebook from top to bottom with `cpu-mini`. Try `gpu-free` later if an accelerator is available.
5. After each epoch, confirm that the checkpoint was updated. Download `artifacts.zip` after the run.
6. Select `Runtime > Disconnect and delete runtime` when you finish.

## If the runtime stops

A runtime is not permanent storage. Create a checkpoint after every epoch and download artifacts early. In a
new session, rerun the environment and configuration sections, upload the checkpoint, confirm the same
architecture and label mapping, then resume. If you only have weights, call the file an inference checkpoint;
do not claim that the optimizer state was restored.

## Quick fixes

- `torch.cuda.is_available()` is `False`: use CPU-mini or try again later. Do not buy Colab Pro for this roadmap.
- CIFAR10 download fails: use the FakeData fallback for a smoke test, record the limitation, and do not use its
  accuracy to support a quality claim.
- Pretrained weights do not download: the random-weight fallback only checks the code. It does not pass the
  transfer-learning gate.
- `CUDA out of memory`: restart the runtime, then reduce the batch size, image size, or sample count.
- Imports still fail after installation: restart the runtime once, then rerun from the environment check.
- A file is missing: check the Files panel and download your output before `Disconnect and delete runtime`.

Do not use SSH, remote desktop, background services, or multiple accounts to bypass quotas. Never store a token
in a cell.
