# Lab 06 - Chọn metric và threshold theo chi phí lỗi

## Mục tiêu

Threshold 0.5 không hiểu chi phí kinh doanh. Bạn sẽ chọn một ngưỡng bằng validation evidence, sau đó khóa quyết định trước khi chạm test.

## Thuật ngữ trong lab

**Thuật ngữ mới:** `class imbalance`, `threshold`

**Ôn lại:** `validation set`, `model validation`, `baseline`, `metric`, `precision / recall / F1`

**Áp dụng trong lab:** Dùng `validation set` cho `model validation`: chọn metric precision / recall / F1 và threshold theo class imbalance, so với baseline; giữ test set đóng đến cuối.

**Tự giải thích:** Metric và threshold nào phù hợp khi class imbalance; validation set được dùng ra sao?

## Trước khi bắt đầu

Đọc `roadmap/weeks/week-07.md`, chạy từ repository root và tạo chỗ lưu evidence cục bộ. Không đưa
credential, dữ liệu cá nhân hoặc file kết quả lớn vào Git.

## Các bước thực hiện

1. Lập confusion matrix ở ít nhất ba threshold và gán chi phí FP/FN.
2. Viết selection rule, chẳng hạn recall tối thiểu rồi chi phí thấp nhất.
3. Chọn threshold trên validation; ghi F1 và PR-AUC.
4. Áp đúng threshold đã khóa lên test, so kết quả nhưng không chỉnh lại.

## Chạy smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 6
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 6
```

Kết quả được lưu tại `.artifacts/lab-06-evidence.json`. Trong `result`, bạn sẽ thấy validation threshold/F1/PR-AUC, FP/FN cost và test metrics.
`status=starter-example-completed` chỉ xác nhận code mẫu chạy; **không** có nghĩa toàn bộ acceptance đã đạt.

## Khi nào xem như hoàn thành?

- Output ghi selection rule, selected threshold, validation/test metrics và FP/FN cost.
- Bạn giải thích được precision-recall trade-off, log loss và câu hỏi calibration kiểm điều gì.

## Khi mắc kẹt

Nếu các metric gây rối, quay về số lượng TP/FP/FN/TN. Chỉ chọn metric sau khi viết loại sai lầm nào đắt hơn.

Sau khi tự dự đoán output, đối chiếu [`expected/README.md`](expected/README.md) và ghi lại điều đã học ở local.
