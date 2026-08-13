# Tuần 17 - Neural networks và PyTorch

## Mục tiêu tuần

Hiểu tensor, autograd, loop và device.

## Vì sao tuần này quan trọng

PyTorch làm rõ điều thư viện cổ điển thường giấu: tensor đi qua model, loss tạo gradient và optimizer cập nhật parameter.

**Ví dụ gần gũi:** Quên `zero_grad()` khiến gradient của batch mới cộng lên batch cũ; quên `eval()` làm validation hành xử khác dự kiến.

## Kiến thức cốt lõi

- Tensor có shape, dtype, device; model, input và target phải ở device tương thích. `.to(device)` trả tensor/module cần được gán lại.
- `nn.Module` giữ parameter và `forward`; Linear nhận `[batch, features]`, loss cần prediction/target đúng shape-dtype.
- Autograd dựng graph. Mỗi batch: `zero_grad()` -> forward -> loss -> `backward()` -> `step()`; bỏ zero_grad làm gradient cộng dồn.
- `model.train()` khác `model.eval()`; validation dùng cả `model.eval()` và `torch.no_grad()` để đúng hành vi và tiết kiệm memory.
- Device auto ưu tiên CUDA, fallback CPU-mini. Seed hỗ trợ tái lập nhưng hardware/kernel vẫn có sai khác nhỏ.

## Từ khóa tuần này

**Thuật ngữ mới hoặc trọng tâm:** `tensor`, `batch`, `epoch`, `optimizer`, `device`

**Ôn lại:** `parameter`, `gradient`, `loss`, `validation set`

**Áp dụng:** Tạo `tensor` theo `batch`, chạy nhiều `epoch`; dùng `optimizer` cập nhật parameter từ gradient/loss, kiểm model và input cùng `device`, đánh giá trên validation set.

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

## Dấu hiệu bạn đã hiểu

Bạn giải thích được shape/dtype/device, viết loop nhỏ và thấy loss giảm mà không phụ thuộc GPU.

## Tự kiểm tra

1. requires_grad khác grad?
2. eval có thay no_grad không?
3. CrossEntropyLoss cần shape/dtype gì?
4. Device mismatch phát sinh thế nào?

## Kết quả hướng tới

seeded run; lưu kèm lệnh đã chạy, cấu hình, metric, thời gian chạy và một điều còn hạn chế.

## Core vs stretch

- **Cốt lõi:** Chạy MLP mini trên CPU, giải thích tensor/device và đúng train/eval loop.
- **Mở rộng:** Thử một learning rate khác hoặc bỏ `zero_grad` có chủ đích rồi khôi phục.

## Lỗi thường gặp

- Input lên GPU nhưng model/target ở CPU.
- Validation trong train mode hoặc giữ graph.

## Khi mắc kẹt

Chạy local one-epoch smoke. Nếu lỗi, in device của model, input, target và kiểm target dtype trước.

## Nguồn

Nguồn nên đọc: PyTorch tutorials về tensors, autograd, optimization và `train`/`eval`.
