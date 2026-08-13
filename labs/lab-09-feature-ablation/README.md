# Lab 09 - Kiểm một feature bằng ablation

## Mục tiêu

Feature mới nên bắt đầu bằng một giả thuyết, không phải bằng danh sách phép biến đổi. Ablation giúp bạn biết thay đổi nào thật sự tạo khác biệt.

## Thuật ngữ trong lab

**Thuật ngữ mới:** `feature engineering`, `ablation`

**Ôn lại:** `feature`, `baseline`, `validation set`, `hyperparameter`

**Áp dụng trong lab:** Viết giả thuyết `feature engineering`, chạy `ablation` thêm/bỏ một feature; khóa baseline, validation set, hyperparameter và data split để metric delta có nghĩa.

**Tự giải thích:** Feature engineering khác ablation thế nào; vì sao chỉ thay một yếu tố?

## Trước khi bắt đầu

Đọc `roadmap/weeks/week-10.md`, chạy từ repository root và tạo chỗ lưu evidence cục bộ. Không đưa
credential, dữ liệu cá nhân hoặc file kết quả lớn vào Git.

## Các bước thực hiện

1. Viết feature hypothesis, prediction-time availability và cách xử lý missing/zero.
2. Chạy baseline feature set; giữ model, split và seed.
3. Bỏ hoặc thêm đúng một feature group, ghi validation delta và runtime.
4. Ra quyết định giữ/bỏ; không mở test trong phép ablation.

## Chạy smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 9
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 9
```

Kết quả được lưu tại `.artifacts/lab-09-evidence.json`. Trong `result`, bạn sẽ thấy validation AUC theo feature group và `test_set_touched=false`.
`status=starter-example-completed` chỉ xác nhận code mẫu chạy; **không** có nghĩa toàn bộ acceptance đã đạt.

## Khi nào xem như hoàn thành?

- Output có AUC theo feature group, `single_change` và `test_set_touched=false`.
- Quyết định feature xét cả availability, stability và metric variability.

## Khi mắc kẹt

Nếu không biết feature có hợp lệ, viết timeline dữ liệu. Feature xuất hiện sau prediction time phải bị loại dù correlation cao.

Sau khi tự dự đoán output, đối chiếu [`expected/README.md`](expected/README.md) và ghi lại điều đã học ở local.
