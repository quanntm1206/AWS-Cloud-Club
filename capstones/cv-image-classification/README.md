# Capstone B - image classification with free compute

This extension capstone gives you a realistic Computer Vision cycle without an AWS GPU. Choose **Colab Free or
Kaggle Free**, train a frozen-backbone model, analyse its errors, then write an AWS architecture decision. You
do not need to use both platforms.

## What will you produce?

- The best checkpoint and a resumable checkpoint; overall and per-class metrics; a confusion matrix.
- Up to 20 failure records, or all records if there are fewer; an experiment report and a model card.
- `artifacts.zip`, a manifest and checksum, and an ADR explaining why the core path does not deploy a CV endpoint.

## File map

- [`notebooks/colab.ipynb`](notebooks/colab.ipynb): the working Colab notebook.
- [`notebooks/kaggle.ipynb`](notebooks/kaggle.ipynb): the same workflow for Kaggle.
- [`configs/cpu-mini.yml`](configs/cpu-mini.yml): 1 epoch and 160 samples; always run this first.
- [`configs/gpu-free.yml`](configs/gpu-free.yml): up to 5 epochs with a frozen backbone; use only with a free GPU.
- [`reports/experiment-report.md`](reports/experiment-report.md), [`reports/model-card.md`](reports/model-card.md),
  and [`reports/aws-adr.md`](reports/aws-adr.md): the three documents to complete.
- [`rubric.yml`](rubric.yml): self-assessment criteria.

## Stage 1 - choose a runtime

1. Open one notebook by following the [Colab/Kaggle guide](../../notebooks/README.md).
2. Run the environment check and `cpu-mini`. The notebook still tries to download pretrained ResNet18.
   FakeData only confirms the pipeline; it does not prove accuracy.
3. If a free GPU and internet access are available, switch to `gpu-free`. The notebook uses a CIFAR10 subset
   and pretrained weights.
4. Run no more than 3-5 epochs and do not run a hyperparameter sweep. The notebook writes
   `last_checkpoint.pt` after each epoch and updates `best_checkpoint.pt` when validation loss improves.

## Stage 2 - controlled training

Keep pretrained normalization, the split seed, and validation transforms fixed. Apply augmentation only to
the training data. Train the head with a frozen backbone first. Fine-tuning the final block is an extension;
do it only when validation evidence and the runtime budget support it. Do not use the test set for early
stopping. Resume from the last checkpoint and evaluate the best checkpoint. Download `artifacts.zip` before
closing the runtime.

To resume in a new runtime, upload `last_checkpoint.pt` or `artifacts.zip` to the working directory and set
`RESUME=True`. The notebook places the file at `artifacts/last_checkpoint.pt` and stops with a clear error if
it cannot find it.

## Stage 3 - understand the model's errors

Report macro, weighted, and per-class metrics with support. Normalize the confusion matrix by true class.
Review errors using the confident-wrong rule instead of choosing convenient images. The notebook sets
`error_type='unreviewed'`. Open each image and assign an evidence-based error group before you summarise the
taxonomy. For each group, record a hypothesis and one next experiment. Do not share sensitive images or any
image that you do not have permission to use.

## Stage 4 - AWS for artifacts and design only

You may upload a small artifact or checksum to S3 after passing the cost gate. The core path does not use
SageMaker training, notebook instances, real-time endpoints, AWS GPUs, or a public API. Complete
`reports/aws-adr.md` to compare a private Lambda when the artifact fits, batch inference, and a managed
endpoint for different workloads. Do not deploy a CV endpoint.

## When is the capstone complete?

- The notebook runs from the start with `cpu-mini`. Pretrained weights must download successfully to pass the
  transfer-learning gate. A model-quality claim also requires a real dataset, not FakeData.
- The frozen backbone is verified; the best checkpoint, resume state, configuration, label mapping, and manifest are exported.
- Per-class metrics, the confusion matrix, failure taxonomy, report, and model card are complete.
- The ADR states the constraints, options, trade-offs, and reasons for excluding AWS training and endpoints from the core path.

## If you get stuck

- **No GPU:** keep CPU-mini or try another free runtime later. Do not buy compute.
- **Dataset download fails:** use the FakeData smoke test and record the limitation. Do not make a model-quality claim.
- **Pretrained weights do not download:** the random-weight fallback only checks the code. It does not pass the transfer-learning gate.
- **Out of memory:** reduce the batch size, image size, and sample count. Restart the runtime after an OOM.
- **Session stops:** upload the checkpoint, confirm the architecture, configuration, and label mapping, then resume.
- **One class has a very low metric:** check its support, the split, labels, and confusion matrix before fine-tuning.

Store artifacts and reports locally for self-assessment. Do not publish or submit them to anyone.
