# Lab 17 - Chạy transfer learning thật trên free runtime

## Mục tiêu

Smoke local chỉ minh họa layer nào được freeze. Bài chính là notebook PyTorch thật: dùng pretrained backbone như bộ trích đặc trưng và chỉ train classifier head.

## Trước khi bắt đầu

Đọc `roadmap/weeks/week-18.md`, chạy từ repository root và tạo chỗ lưu evidence cục bộ. Không đưa
credential, dữ liệu cá nhân hoặc artifact lớn vào Git.

## Các bước thực hiện

1. Chạy local smoke, giải thích `requires_grad` của backbone và head.
2. Chọn một notebook Colab hoặc Kaggle; chạy `cpu-mini` từ đầu và xác nhận pretrained weights đã tải.
3. Xác nhận pretrained normalization, frozen parameters và trainable head.
4. Nếu GPU miễn phí có sẵn, chạy `gpu-free`; export checkpoint, metrics và manifest.

## Chạy smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 17
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 17
```

Kết quả được lưu tại `.artifacts/lab-17-evidence.json`. Trong `result`, bạn sẽ thấy smoke dict về frozen layers; notebook thật xuất checkpoint và metrics.
`status=starter-example-completed` chỉ xác nhận code mẫu chạy; **không** có nghĩa toàn bộ acceptance đã đạt.


## Bài thực hành đầy đủ trên PyTorch

Command local ở trên chỉ là smoke demo nhanh. Phần training/evaluation thật nằm trong notebook:

- Colab: [`notebooks/colab/cv_transfer_learning_colab.ipynb`](../../notebooks/colab/cv_transfer_learning_colab.ipynb)
- Kaggle: [`notebooks/kaggle/cv_transfer_learning_kaggle.ipynb`](../../notebooks/kaggle/cv_transfer_learning_kaggle.ipynb)

Chọn **một** nền tảng. Chạy `cpu-mini` trước; chỉ chuyển sang `gpu-free` khi accelerator có sẵn. Tải
`artifacts.zip` về máy trước khi kết thúc session.

## Khi nào xem như hoàn thành?

- Smoke output chỉ head trainable; notebook thật hoàn tất ít nhất CPU-mini và xuất artifact local.
- Nếu dùng FakeData, kết quả được gọi là pipeline smoke, không phải model quality.
- Nếu notebook phải dùng random weights, kết quả chỉ là execution smoke và chưa đạt gate transfer learning.

## Khi mắc kẹt

Nếu data không tải, dùng FakeData fallback và ghi limitation. Nếu pretrained weights không tải, chỉ kiểm luồng
chạy rồi thử lại khi có internet/cache. Nếu loss không đổi, kiểm trainable parameters, optimizer và normalization.

Sau khi tự dự đoán output, đối chiếu [`expected/README.md`](expected/README.md) và ghi lại điều đã học ở local.
