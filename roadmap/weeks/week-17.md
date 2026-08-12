# Tuần 17 - Neural networks và PyTorch

## Mục tiêu tuần

Hiểu tensor, autograd, loop và device.

## Kiến thức cốt lõi

- Tensor có shape, dtype, device; model, input và target phải ở device tương thích. `.to(device)` trả tensor/module cần được gán lại.
- `nn.Module` giữ parameter và `forward`; Linear nhận `[batch, features]`, loss cần prediction/target đúng shape-dtype.
- Autograd dựng graph. Mỗi batch: `zero_grad()` -> forward -> loss -> `backward()` -> `step()`; bỏ zero_grad làm gradient cộng dồn.
- `model.train()` khác `model.eval()`; validation dùng cả `model.eval()` và `torch.no_grad()` để đúng hành vi và tiết kiệm memory.
- Device auto ưu tiên CUDA, fallback CPU-mini. Seed hỗ trợ tái lập nhưng hardware/kernel vẫn có sai khác nhỏ.

## Lịch 8-10 giờ

| Hoạt động | Giờ |
|---|---:|
| Đọc và ghi chú | 2 |
| Guided practice | 2 |
| Lab | 3 |
| Assessment/error analysis | 1 |
| Learning log và tự đánh giá | 1 |
| Review/hoàn thiện | 0 |

## Guided practice

1. In shape/dtype/device của batch và output trước train.
2. Viết loop 3 epoch, lưu train/validation loss.
3. Thử bỏ zero_grad; khôi phục rồi validation bằng eval/no_grad.

## Lab

**lab-16:** MLP device-aware trên mini data. Môi trường chính: `local, colab, kaggle`.

## Tự kiểm tra

1. requires_grad khác grad?
2. eval có thay no_grad không?
3. CrossEntropyLoss cần shape/dtype gì?
4. Device mismatch phát sinh thế nào?

## Kết quả hướng tới

seeded run; kèm config, command, metric, runtime và một failure/limitation.

## Core vs stretch

- **Core:** hoàn thành mini profile, test và kết quả cốt lõi.
- **Stretch:** thử đúng một cải tiến có giả thuyết; không hyperparameter sweep.

## Lỗi thường gặp

- Input lên GPU nhưng model/target ở CPU.
- Validation trong train mode hoặc giữ graph.

## Nguồn

Xem `docs/sources.yml`; ưu tiên textbook và tài liệu chính thức được ghi trong lab.
