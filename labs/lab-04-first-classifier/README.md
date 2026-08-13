# Lab 04 - So dummy baseline với logistic regression

## Mục tiêu

Một classifier chỉ đáng quan tâm khi vượt cách đoán đơn giản trên cùng luật chơi. Lab này biến baseline thành điều kiện bắt buộc, không phải dòng phụ trong báo cáo.

## Thuật ngữ trong lab

**Thuật ngữ mới:** `baseline`, `confusion matrix`, `data split`, `fit`, `metric`, `model validation`, `precision / recall / F1`, `test set`, `training set`, `validation set`

**Ôn lại:** `dataset`, `sample`, `feature`, `label / target`, `prediction`

**Áp dụng trong lab:** Tạo `data split` từ `dataset` không trùng sample thành `training set`, `validation set`, `test set`; `fit` baseline trên feature, dùng `metric` precision / recall / F1 và `confusion matrix` để thực hiện `model validation`, so prediction với label / target.

**Tự giải thích:** Data validation, validation set và model validation khác nhau ở điểm nào?

## Trước khi bắt đầu

Đọc `roadmap/weeks/week-05.md`, chạy từ repository root và tạo chỗ lưu evidence cục bộ. Không đưa
credential, dữ liệu cá nhân hoặc file kết quả lớn vào Git.

## Các bước thực hiện

1. Kiểm class balance, chia train/validation/test với stratification và xác nhận ID không trùng.
2. Train dummy classifier; ghi F1 cùng confusion matrix.
3. Train logistic regression trên đúng split và metric đó.
4. Nêu model có vượt baseline không; không đổi ngưỡng quyết định sau khi xem test.

## Chạy smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 4
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 4
```

Kết quả được lưu tại `.artifacts/lab-04-evidence.json`. Trong `result`, bạn sẽ thấy `dummy_f1` và `logistic_f1`.
`status=starter-example-completed` chỉ xác nhận code mẫu chạy; **không** có nghĩa toàn bộ acceptance đã đạt.

## Khi nào xem như hoàn thành?

- JSON có `dummy_f1` và `logistic_f1`; phép so dùng cùng split, seed và metric.
- Bạn giải thích được vì sao accuracy cao chưa chắc hữu ích khi positive hiếm.

## Khi mắc kẹt

Nếu cả hai model gần nhau, kiểm signal và target trước. Đừng thêm model phức tạp chỉ để tìm một số cao hơn.

Sau khi tự dự đoán output, đối chiếu [`expected/README.md`](expected/README.md) và ghi lại điều đã học ở local.
