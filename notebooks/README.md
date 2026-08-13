# Run notebooks for free

The tabular work runs well on a local CPU. From week 18, choose **one** of the two free platforms for Computer
Vision. You do not need to use both Colab and Kaggle, and you do not need a paid plan.

## Five-minute quick start

| Platform | Notebook |
|---|---|
| Colab Free | [`colab/cv_transfer_learning_colab.ipynb`](colab/cv_transfer_learning_colab.ipynb) |
| Kaggle Free | [`kaggle/cv_transfer_learning_kaggle.ipynb`](kaggle/cv_transfer_learning_kaggle.ipynb) |
| Shared environment check | [`shared/00_environment_check.ipynb`](shared/00_environment_check.ipynb) |

1. Open or upload the correct notebook for your chosen platform.
2. Run `Environment check`, then read the printed `device` and `profile` values.
3. Keep `cpu-mini` for your first run. This profile still tries to use pretrained ResNet18, but FakeData is
   only a smoke test. It does not prove model quality.
4. If a GPU is available, run again with `gpu-free`. The notebook uses a CIFAR10 subset, pretrained weights,
   and no more than 5 epochs.
5. Wait for the export cell to create `artifacts.zip`. Download it **before** you close the runtime.
6. Release the runtime or accelerator as soon as you finish.

The notebook includes an environment check, seed and configuration, separate training augmentation,
deterministic validation, a frozen-backbone baseline, training, evaluation, error analysis, best and last
checkpoints, a manifest, and artifact export. On your first run, execute the cells in order.

The evaluation cell exports accuracy, macro and weighted F1, per-class metrics, and confusion matrices with
counts and true-class normalization. The notebook selects up to 20 high-confidence errors. Open each image and
replace `error_type='unreviewed'` with the error group you observe before writing the model card. Do not infer
an error taxonomy automatically from the labels.

## If the session stops

Open a new runtime, rerun the environment and configuration sections, upload `last_checkpoint.pt` or
`artifacts.zip`, set `RESUME=True`, then run the training cell. `RUN_EPOCHS` is the number of **additional**
epochs for the current session. CPU-mini trains for one epoch by default, and a resumed session adds one more
epoch. The notebook saves `last_checkpoint.pt` after every epoch for resuming and uses only
`best_checkpoint.pt` for evaluation. A valid resume state includes the model, optimizer, epoch, best metric,
configuration, seed, and label mapping. Model weights alone cannot restore the optimizer correctly.

Place the uploaded file in the notebook working directory as `last_checkpoint.pt` or `artifacts.zip`. When
`RESUME=True`, the notebook copies or extracts it into `artifacts/`. If it cannot find a checkpoint, the cell
stops with a clear error instead of silently training again from epoch 0.

## Common issues

- **No GPU:** continue with `cpu-mini`. You can still practise with a frozen pretrained backbone on CPU. For
  model-quality evidence, also run on a real dataset when a runtime is available.
- **CIFAR10 download fails:** the notebook falls back to FakeData. Record that this is a pipeline smoke test;
  do not report its accuracy as model quality.
- **Pretrained weights do not download:** the random-weight fallback only checks that the code runs. It does
  not pass the transfer-learning gate. Try again with internet access or cached weights; do not call this
  result transfer learning.
- **Out of memory:** reduce `BATCH_SIZE`, `IMAGE_SIZE`, or `SAMPLES`. Do not upgrade to a paid runtime.
- **torch/torchvision import fails:** use a compatible version pair for the runtime, then restart it. Do not
  reinstall the packages in every cell.
- **Files disappear after disconnecting:** the runtime is temporary. Always download `artifacts.zip` before
  ending the session.

Platform guides: [Colab Free](../docs/source-notes/colab-free.md) and
[Kaggle Free](../docs/source-notes/kaggle-notebooks.md).
