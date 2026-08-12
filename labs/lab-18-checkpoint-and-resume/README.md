# Lab 18 - Lưu và resume checkpoint đúng nghĩa

## Mục tiêu

Checkpoint tốt là hợp đồng để tiếp tục training, không chỉ là file weights. Bạn sẽ chủ động dừng một run rồi khôi phục đủ trạng thái.

## Trước khi bắt đầu

Đọc `roadmap/weeks/week-19.md`, chạy từ repository root và tạo chỗ lưu evidence cục bộ. Không đưa
credential, dữ liệu cá nhân hoặc artifact lớn vào Git.

## Các bước thực hiện

1. Chạy smoke local để đọc best epoch, resume epoch và patience.
2. Trong notebook thật, train 1 epoch rồi lưu model, optimizer, epoch, best metric, config, seed và label mapping.
3. Tạo runtime/process mới, upload `last_checkpoint.pt` hoặc `artifacts.zip` vào thư mục làm việc, đặt
   `RESUME=True`; giữ `RUN_EPOCHS=1` để load checkpoint epoch 1 và chạy thêm epoch 2. Thiếu file thì notebook
   phải dừng, không được âm thầm train lại từ đầu.
4. So best với last; export ZIP và checksum trước khi đóng session.

## Chạy smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 18
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 18
```

Kết quả được lưu tại `.artifacts/lab-18-evidence.json`. Trong `result`, bạn sẽ thấy smoke metadata; notebook thật lưu model/optimizer/epoch/config.
`status=starter-example-completed` chỉ xác nhận code mẫu chạy; **không** có nghĩa toàn bộ acceptance đã đạt.


## Bài thực hành đầy đủ trên PyTorch

Command local ở trên chỉ là smoke demo nhanh. Phần training/evaluation thật nằm trong notebook:

- Colab: [`notebooks/colab/cv_transfer_learning_colab.ipynb`](../../notebooks/colab/cv_transfer_learning_colab.ipynb)
- Kaggle: [`notebooks/kaggle/cv_transfer_learning_kaggle.ipynb`](../../notebooks/kaggle/cv_transfer_learning_kaggle.ipynb)

Chọn **một** nền tảng. Chạy `cpu-mini` trước; chỉ chuyển sang `gpu-free` khi accelerator có sẵn. Tải
`artifacts.zip` về máy trước khi kết thúc session. `RUN_EPOCHS` là số epoch chạy thêm trong mỗi phiên, không
phải tổng epoch tính từ đầu.

## Khi nào xem như hoàn thành?

- Resume bắt đầu đúng epoch, giữ optimizer state/history và không dùng test cho early stopping.
- Bạn phân biệt inference weights với resumable checkpoint và tải artifact về local.

## Khi mắc kẹt

Nếu load lỗi, so architecture/config/label mapping trước. Nếu optimizer không load, kiểm parameter groups thay vì bỏ state âm thầm.

Sau khi tự dự đoán output, đối chiếu [`expected/README.md`](expected/README.md) và ghi lại điều đã học ở local.
