# Lab 16 - Nhìn rõ tensor, gradient và device

## Mục tiêu

Lab local này làm lộ vòng học của neural network mà không phụ thuộc GPU. Smoke demo dùng NumPy; bạn dùng nó để kiểm loss trước khi chuyển sang loop PyTorch của tuần 17.

## Thuật ngữ trong lab

**Thuật ngữ mới:** `tensor`, `batch`, `epoch`, `optimizer`, `device`

**Ôn lại:** `parameter`, `gradient`, `loss`, `validation set`

**Áp dụng trong lab:** Tạo `tensor` theo `batch`, chạy nhiều `epoch`; dùng `optimizer` cập nhật parameter từ gradient/loss, kiểm model và input cùng `device`, đánh giá trên validation set.

**Tự giải thích:** Batch, epoch, loss và optimizer tạo thành một vòng training như thế nào?

## Trước khi bắt đầu

Đọc `roadmap/weeks/week-17.md`, chạy từ repository root và tạo chỗ lưu evidence cục bộ. Không đưa
credential, dữ liệu cá nhân hoặc artifact lớn vào Git.

## Các bước thực hiện

1. In shape của input, hidden, logits và target; dự đoán số parameter.
2. Chạy mini MLP có seed, ghi loss qua các bước và xác nhận xu hướng.
3. Thử bỏ bước reset gradient trong loop PyTorch nhỏ, quan sát rồi khôi phục.
4. Chạy validation bằng `eval()` và `no_grad()`; in device/dtype.

## Chạy smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 16
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 16
```

Kết quả được lưu tại `.artifacts/lab-16-evidence.json`. Trong `result`, bạn sẽ thấy losses giảm, device và số parameter.
`status=starter-example-completed` chỉ xác nhận code mẫu chạy; **không** có nghĩa toàn bộ acceptance đã đạt.

## Khi nào xem như hoàn thành?

- Output có loss giảm, device và parameter count; bạn giải thích được từng bước zero-grad/forward/backward/step.
- Loop chạy CPU; model/input/target cùng device và target đúng dtype cho loss.

## Khi mắc kẹt

In shape, dtype, device ngay trước forward/loss. Sửa mismatch đầu tiên; không chuyển GPU để né lỗi logic.

Sau khi tự dự đoán output, đối chiếu [`expected/README.md`](expected/README.md) và ghi lại điều đã học ở local.
