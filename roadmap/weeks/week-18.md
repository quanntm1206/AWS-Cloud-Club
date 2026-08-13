# Week 18 - CNN and transfer learning

## Weekly goals

Understand CNN and transfer learning.

## Why this week matters

Transfer learning leverages learned representations for data reduction and compute. This is a reasonable path for new users of free runtime.

**Close example:** Keeping the backbone fixed is like using an existing feature extractor; you only teach classifier head to the new class.

## Core knowledge

- Convolution learns a local kernel with shared weights; stride/padding changes spatial size, downsampling reduces compute.
- Transfer learning uses pretrained backbone and head replacement; frozen-backbone only trains head so it's lighter than full fine-tune.
- Input normalization must match pretrained weights; train augmentation other validation transform deterministic.
- Notebook has CPU-mini and FakeData when GPU/dataset is lacking; CPU-mini still tries to use pretrained weights. If weights
  Unable to load, random-weight fallback only smoke code and does not pass gate transfer learning. FakeData does not
  prove accuracy.

## Keywords for this week

**New or focus terms:** `augmentation`, `backbone`, `freeze`, `transfer learning`

**Review:** `tensor`, `batch`, `epoch`, `device`, `overfitting`

**Use:** Use `augmentation` only for training `batch`, keep validation transform deterministic; upload the pretrained `backbone` to the correct `device`, `freeze` parameters and then run `transfer learning` on the tensor, monitoring epoch/loss to detect overfitting.

## 8-10 hour schedule

| Activities | Hours |
|---|---:|
| Read and take notes | 2 |
| Guided practice | 2 |
| Lab | 3 |
| Assessment/error analysis | 1 |
| Learning log and self-assessment | 1 |
| Review/complete | 0 |

## Guided practice


1. Calculate conv output size and print shape via model.
2. Freeze backbone, confirm head trainable only.
3. Run CIFAR10 subset; Force FakeData fallback then write limitation.

## Lab

**lab-17:** Frozen-backbone baseline on a free runtime. Main environment: `colab, kaggle`.

## Signs that you understand

You run the real notebook, confirm only head trainable and distinguish FakeData smoke from CIFAR10 results.

## Test yourself

1. Why does Frozen backbone reduce compute?
2. What are the effects of incorrect normalization?
3. What can FakeData prove?

## Result oriented

CV baseline; Saves executed commands, configuration, metrics, runtime and one limitation.

## Core vs stretch

- **Core:** Run notebook using `cpu-mini` with pretrained weights; quality indicator when using real data.
- **Extension:** If there is a free GPU, run `gpu-free` once; no fine-tune or sweep this week.

## Common errors

- Report transfer learning even though pretrained weights do not load.
- Report FakeData accuracy as real quality.

## When you get stuck

Open the correct Colab/Kaggle notebook, run `cpu-mini` first. If the data cannot be downloaded, use FakeData smoke. If
pretrained weights cannot be loaded, random-weight fallback only checks the code; clearly state that transfer-learning gate has not been passed.

## Source

Recommended reading: PyTorch transfer learning tutorial, torchvision weights/transforms, and the repo's Colab/Kaggle tutorial.