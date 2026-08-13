# Week 17 - Neural networks and PyTorch

## Weekly goals

Understand tensor, autograd, loop and device.

## Why this week matters

PyTorch makes clear what classic libraries often hide: tensors pass through the model, losses create gradients, and optimizers update parameters.

**Close example:** Forgetting `zero_grad()` causes the gradient of the new batch to be added to the old batch; Forgetting `eval()` causes validation to behave differently than expected.

## Core knowledge

- Tensor has shape, dtype, device; model, input and target must be on a compatible device. `.to(device)` returns the tensor/module that needs to be reassigned.
- `nn.Module` holds parameters and `forward`; Linear receives `[batch, features]`, loss needs prediction/target of correct shape-dtype.
- Autograd graph construction. Each batch: `zero_grad()` -> forward -> loss -> `backward()` -> `step()`; remove zero_grad as cumulative gradient.
- `model.train()` is different from `model.eval()`; Validation uses both `model.eval()` and `torch.no_grad()` to correct behavior and save memory.
- Device auto prioritizes CUDA, fallback CPU-mini. Seed supports reconfiguration but the hardware/kernel still has minor differences.

## Keywords for this week

**New or focus terms:** `tensor`, `batch`, `epoch`, `optimizer`, `device`

**Review:** `parameter`, `gradient`, `loss`, `validation set`

**Use:** Create `tensor` in `batch`, run multiple `epoch`; Use `optimizer` to update parameters from gradient/loss, check model and input with `device`, evaluate on validation set.

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


1. Print shape/dtype/device of batch and output before training.
2. Write a 3-epoch loop, save the training/validation loss.
3. Try removing zero_grad; Restore then validate using eval/no_grad.

## Lab

**lab-16:** MLP device-aware on mini data. Main environment: `local, colab, kaggle`.

## Signs that you understand

You can explain the shape/dtype/device, write a small loop and see the loss decrease without depending on the GPU.

## Test yourself

1. requires_grad is different from grad?
2. Does eval replace no_grad?
3. What shape/dtype does CrossEntropyLoss need?
4. How does Device mismatch arise?

## Result oriented

seeded run; Saves executed commands, configuration, metrics, runtime and one limitation.

## Core vs stretch

- **Core:** Run mini MLP on CPU, explain tensor/device and correct train/eval loop.
- **Expansion:** Try a different learning rate or intentionally drop `zero_grad` and restore.

## Common errors

- Input to GPU but model/target to CPU.
- Validation in train mode or keep graph.

## When you get stuck

Run local one-epoch smoke. If error, print device of model, input, target and check target dtype first.

## Source

Recommended source: PyTorch tutorials on tensors, autograd, optimization and `train`/`eval`.