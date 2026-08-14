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

**Use:** Create each `tensor` in a `batch` and train for several `epoch` passes; use the `optimizer` to update each `parameter` from its `gradient` and `loss`, keep model and input on the same `device`, then evaluate on the `validation set`.

## Concept walkthrough

### Tensor and batch

**Mental model:** `tensor`: A tensor is a multidimensional array used to represent data and computations in a neural network. Its shape, data type, and device determine how operations can use it. `batch`: A batch is a group of samples processed together before a parameter update. Training normally performs one forward and backward pass for each batch.

**Why it matters:** Tensor shape, dtype, and batch size determine whether a computation is compatible and fits in memory.

**Worked example:** `tensor`: A batch of images has shape [32, 3, 160, 160]. `batch`: Batch size 32 means the model reads 32 images per step.

**Easy to confuse:** A tensor is an array with shape and dtype, not the neural network itself. A batch groups samples; an epoch covers the entire training set.

**Check yourself:** Do the `tensor` shape and `batch` size match the model input and available memory?

### Epochs and optimizer updates

**Mental model:** `epoch`: An epoch is one complete pass through the training set. The number of optimizer steps per epoch depends on dataset size and batch size. `optimizer`: An optimizer is an algorithm that uses gradients to update model parameters. It may also keep moving averages or other state used to form later updates.

**Why it matters:** An epoch describes data coverage; the optimizer updates parameters after batches, so the two count different progress.

**Worked example:** `epoch`: Three epochs use each training sample about three times. `optimizer`: Adam updates the classifier head after loss.backward().

**Easy to confuse:** An epoch is one pass; an optimizer step may happen many times within that pass. The optimizer applies updates; the learning rate is one setting that controls them.

**Check yourself:** How many optimizer updates occur within one `epoch`, and what does each `optimizer` step change?

### Device placement

**Mental model:** `device`: A device is the hardware, such as a CPU or GPU, where tensors and models perform computations. The model and every tensor used in one operation must be on compatible devices.

**Why it matters:** Model, input, and target must share a compatible device, and the selected device belongs in the run record.

**Worked example:** `device`: The model and input are both on CPU or both on CUDA.

**Easy to confuse:** A device is compute hardware; a tensor is the data placed on it.

**Check yourself:** Are the model, input, and target on a compatible `device`?

## Connect earlier terms

The earlier `parameter`, `gradient`, and `loss` concepts now operate on tensor batches through an optimizer. A saved history on the `validation set` shows how those updates affect generalization across epochs.

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