# Week 19 - Fine-tuning saves and checkpoints

## Weekly goals

Checkpoint/resume; fine-tune savings.

## Why this week matters

Free runtime can be interrupted at any time. A good checkpoint turns a break into a small interruption instead of losing the entire training session.

**Close example:** Best checkpoint holds the best epoch validation; last checkpoint only reflects the most recent update and may be inferior.

## Core knowledge

- Train head first; Only unfreeze the last block if validation and runtime budget justify it.
- Pretrained layers often use a lower learning rate than head; As a policy, do not scan GPU for free.
- Resumable checkpoint needs model, optimizer, epoch, best metric, config, seed, label mapping.
- Early stopping according to validation with patience; best checkpoint else last; test does not participate in every epoch.
- Free runtime can be interrupted/quota changed; export persistent ZIP before release session.

## Keywords for this week

**New or focus terms:** `fine-tuning`, `checkpoint`, `early stopping`

**Review:** `transfer learning`, `freeze`, `optimizer`, `epoch`, `validation set`

**Use:** Start from the frozen `transfer learning` baseline, then optionally run `fine-tuning`; save a `checkpoint` with optimizer and epoch state, apply `early stopping` on the `validation set`, and resume once to verify the saved state.

## Concept walkthrough

### Fine-tuning checkpoints

**Mental model:** `fine-tuning`: Fine-tuning continues training some pretrained layers with a small learning rate for the new problem. It commonly follows frozen-head training and uses a lower learning rate for unfrozen layers. `checkpoint`: A checkpoint saves training state so a run can continue after interruption. It often contains model parameters, optimizer state, epoch number, and training history.

**Why it matters:** A checkpoint preserves model and optimizer state so a fine-tuning decision can be reproduced or safely resumed.

**Worked example:** `fine-tuning`: Unfreeze layer4 after frozen-head baseline. `checkpoint`: Last checkpoint contains model, optimizer, epoch and history.

**Easy to confuse:** Fine-tuning updates pretrained layers; frozen-head training leaves them unchanged. A checkpoint may resume training; a final artifact is prepared for evaluation or serving.

**Check yourself:** What state must a `checkpoint` preserve so the `fine-tuning` run can resume exactly?

### Early stopping

**Mental model:** `early stopping`: Early stopping ends training after validation performance has not improved for a chosen number of epochs. A patience setting defines how many non-improving epochs are tolerated.

**Why it matters:** Early stopping uses validation evidence to stop before extra epochs mostly memorize training noise.

**Worked example:** `early stopping`: Stop after validation loss fails to improve for two epochs.

**Easy to confuse:** Early stopping is a training rule, not a guarantee against all overfitting.

**Check yourself:** Which validation signal and patience rule trigger `early stopping`?

## Connect earlier terms

The frozen `transfer learning` baseline and `freeze` policy remain the comparison point. Restored `optimizer` and `epoch` state plus unchanged `validation set` rules show whether fine-tuning genuinely improves the model.

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


1. Train maximum 3-5 epochs, save best validation checkpoint.
2. Stop-load-resume for another epoch.
3. Create self-contained ZIP, manifest and checksum right in the notebook.

## Lab

**lab-18:** 3-5 epochs, early stopping, export artifact. Main environment: `colab, kaggle`.

## Signs that you understand

You save all models, optimizers, epochs, config and label mapping; stop and then resume another successful epoch.

## Test yourself

1. Why is Optimizer state needed?
2. When is best different from last?
3. Does the test participate in early stopping?

## Result oriented

checkpoint artifact; Saves executed commands, configuration, metrics, runtime and one limitation.

## Core vs stretch

- **Core:** Save checkpoints with enough state, proactively stop/resume and export artifacts before closing runtime.
- **Extension:** Unfreeze the last block only if validation/runtime has a reason; Use a learning rate lower than head.

## Common errors

- Only save weights but call resumable.
- Keep the accelerator session running after the lab.

## When you get stuck

Reduce data and epoch first. If the resume is wrong, compare architecture, label mapping and optimizer state instead of just load weights.

## Source

Recommended sources: PyTorch saving/loading checkpoint tutorial and notebook contract in the repo.