# Lab 08 - So sánh tree ensembles công bằng

## Mục tiêu

Tree, random forest và boosting có cách học khác nhau; phép so chỉ có ý nghĩa khi dữ liệu, metric và budget giống nhau.

## Trước khi bắt đầu

Đọc `roadmap/weeks/week-09.md`, chạy từ repository root và tạo chỗ lưu evidence cục bộ. Không đưa
credential, dữ liệu cá nhân hoặc artifact lớn vào Git.

## Các bước thực hiện

1. Train logistic, random forest và gradient boosting trên cùng train/validation split.
2. Ghi validation AUC, runtime và artifact size cho từng candidate.
3. Chọn candidate bằng rule đã viết; chỉ sau đó đánh giá final test.
4. Đổi đúng một giới hạn độ phức tạp, giải thích tác động train-validation.

## Chạy smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 8
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 8
```

Kết quả được lưu tại `.artifacts/lab-08-evidence.json`. Trong `result`, bạn sẽ thấy validation score từng candidate, model được chọn và final test AUC.
`status=starter-example-completed` chỉ xác nhận code mẫu chạy; **không** có nghĩa toàn bộ acceptance đã đạt.

## Khi nào xem như hoàn thành?

- Output nêu validation scores, candidate được chọn, selection split và final test AUC.
- Bạn mô tả được bagging/boosting và không dùng test để chọn hyperparameter.

## Khi mắc kẹt

Khóa split/seed trước, giảm còn hai candidate nếu cần. Chênh lệch nhỏ hơn variability chưa đủ để tuyên bố model thắng.

Sau khi tự dự đoán output, đối chiếu [`expected/README.md`](expected/README.md) và ghi lại điều đã học ở local.
