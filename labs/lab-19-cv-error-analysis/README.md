# Lab 19 - Đánh giá CV theo từng class và failure

## Mục tiêu

Lab cuối phần CV chuyển metric thành hiểu biết về failure. Smoke local cho format; phân tích có ý nghĩa phải dùng prediction từ notebook thật.

## Thuật ngữ trong lab

**Thuật ngữ mới:** `macro average`, `weighted average`

**Ôn lại:** `confusion matrix`, `support`, `metric`, `validation set`, `error analysis`, `failure taxonomy`

**Áp dụng trong lab:** Tạo confusion matrix, `macro average`, `weighted average` và metric theo class với support; làm error analysis trên prediction ở validation set, gán failure taxonomy cho sample thật, không dùng FakeData làm model validation.

**Tự giải thích:** Macro average khác weighted average thế nào; confusion matrix và support giúp đọc chênh lệch đó ra sao?

## Trước khi bắt đầu

Đọc `roadmap/weeks/week-20.md`, chạy từ repository root và tạo chỗ lưu evidence cục bộ. Không đưa
credential, dữ liệu cá nhân hoặc artifact lớn vào Git.

## Các bước thực hiện

1. Chạy smoke để xem cấu trúc per-class metrics và failure records.
2. Từ run thật, tạo precision/recall/F1/support từng class và macro/weighted aggregate.
3. Vẽ confusion matrix normalize theo true class; review tối đa 20 lỗi theo sampling rule confident-wrong.
4. Notebook để `error_type='unreviewed'`; mở từng ảnh, gán nhóm lỗi dựa trên evidence, rồi viết limitation và
   một next experiment có thể kiểm chứng. Placeholder chưa phải taxonomy hoàn thành.

## Chạy smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 19
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 19
```

Kết quả được lưu tại `.artifacts/lab-19-evidence.json`. Trong `result`, bạn sẽ thấy per-class metrics và failure records.
`status=starter-example-completed` chỉ xác nhận code mẫu chạy; **không** có nghĩa toàn bộ acceptance đã đạt.


## Bài thực hành đầy đủ trên PyTorch

Command local ở trên chỉ là smoke demo nhanh. Phần training/evaluation thật nằm trong notebook:

- Colab: [`notebooks/colab/cv_transfer_learning_colab.ipynb`](../../notebooks/colab/cv_transfer_learning_colab.ipynb)
- Kaggle: [`notebooks/kaggle/cv_transfer_learning_kaggle.ipynb`](../../notebooks/kaggle/cv_transfer_learning_kaggle.ipynb)

Chọn **một** nền tảng. Chạy `cpu-mini` trước; chỉ chuyển sang `gpu-free` khi accelerator có sẵn. Tải
`artifacts.zip` về máy trước khi kết thúc session.

## Khi nào xem như hoàn thành?

- Bảng per-class, confusion matrix và failure taxonomy liên kết đúng dataset/split/config.
- FakeData không được dùng kết luận quality; ảnh nhạy cảm chỉ lưu ID/mô tả an toàn local.

## Khi mắc kẹt

Bắt đầu với 5-10 lỗi và kiểm label mapping. Nếu một class kém, xem support/split/transform trước khi fine-tune.

Sau khi tự dự đoán output, đối chiếu [`expected/README.md`](expected/README.md) và ghi lại điều đã học ở local.
