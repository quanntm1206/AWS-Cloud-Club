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

**Use:** Apply `augmentation` only to each training `batch` and keep validation transforms deterministic; place the pretrained `backbone` on the correct `device`, `freeze` its parameters, then run `transfer learning` while monitoring epoch loss for `overfitting`.

## Concept walkthrough

### Augmentation and backbone

**Mental model:** `augmentation`: Augmentation applies valid random changes to training samples to add diversity without changing their labels. The transformation must preserve the task label and is normally random only for training. `backbone`: A backbone is the main network section that extracts features before the task-specific classifier head. A small classifier head converts those features into scores for the new classes.

**Why it matters:** Augmentation changes training views without changing the label; the backbone turns those views into reusable representations.

**Worked example:** `augmentation`: Flip training images horizontally; resize validation images deterministically. `backbone`: Use a pretrained ResNet18 as the backbone.

**Easy to confuse:** Augmentation changes training examples; preprocessing also prepares validation and inference inputs. The backbone extracts features; the classifier head maps them to task labels.

**Check yourself:** Which `augmentation` preserves the label, and which representation comes from the `backbone`?

### Freeze and transfer learning

**Mental model:** `freeze`: To freeze a model section means temporarily preventing its parameters from being updated during training. Frozen parameters still take part in the forward pass but receive no optimizer updates. `transfer learning`: Transfer learning reuses knowledge from a pretrained model for a new problem. The classifier head can be trained first while the pretrained backbone remains frozen.

**Why it matters:** Freezing protects pretrained weights and lowers compute, while transfer learning adapts the remaining trainable layers to the task.

**Worked example:** `freeze`: Set requires_grad=False for backbone. `transfer learning`: Keep the ResNet18 backbone and replace the classifier head.

**Easy to confuse:** Freeze stops parameter updates but still allows data to pass through the layer. Transfer learning is the overall reuse strategy; fine-tuning is one later training stage.

**Check yourself:** What stays unchanged when you `freeze` the backbone during `transfer learning`?

## Connect earlier terms

The `tensor` and every `batch` must remain on the correct `device`, while validation results across each `epoch` expose `overfitting`. Those checks provide the evidence for deciding whether augmentation and transfer learning help.

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