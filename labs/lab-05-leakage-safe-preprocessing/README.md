# Lab 05 - Dựng preprocessing không nhìn test

## Mục tiêu

Imputer, scaler và encoder đều học từ dữ liệu. Lab này buộc chúng sống trong cùng pipeline để test set không âm thầm tham gia training.

## Trước khi bắt đầu

Đọc `roadmap/weeks/week-06.md`, chạy từ repository root và tạo chỗ lưu evidence cục bộ. Không đưa
credential, dữ liệu cá nhân hoặc artifact lớn vào Git.

## Các bước thực hiện

1. Xác định numeric/categorical columns và chia dữ liệu trước preprocessing.
2. Dựng `ColumnTransformer` cho missing, scaling và one-hot encoding.
3. Thêm một validation row có category chưa từng thấy; chạy inference mà không fit lại.
4. Kiểm statistic của scaler/imputer chỉ đến từ train.

## Chạy smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 5
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 5
```

Kết quả được lưu tại `.artifacts/lab-05-evidence.json`. Trong `result`, bạn sẽ thấy prediction cho unknown category và `leakage_guard=true`.
`status=starter-example-completed` chỉ xác nhận code mẫu chạy; **không** có nghĩa toàn bộ acceptance đã đạt.

## Khi nào xem như hoàn thành?

- Unknown category vẫn được xử lý và `leakage_guard=true`.
- Pipeline lưu cả transform lẫn model; không có bước `fit` nào dùng validation/test.

## Khi mắc kẹt

Nếu encoder vỡ, kiểm `handle_unknown`. Nếu metric đẹp bất thường, tìm mọi `fit`/`fit_transform` và dữ liệu chúng nhận.

Sau khi tự dự đoán output, đối chiếu [`expected/README.md`](expected/README.md) và ghi lại điều đã học ở local.
