# Lab 11 - Ghép pipeline tabular thành mini-project

## Mục tiêu

Mini-project này kiểm xem toàn bộ đường đi từ dữ liệu đến artifact có chạy lại được hay không. Model tốt nhưng chỉ sống trong notebook chưa phải sản phẩm tái lập.

## Trước khi bắt đầu

Đọc `roadmap/weeks/week-12.md`, chạy từ repository root và tạo chỗ lưu evidence cục bộ. Không đưa
credential, dữ liệu cá nhân hoặc artifact lớn vào Git.

## Các bước thực hiện

1. Khóa problem, schema, split, baseline và success criteria trước training.
2. Chạy pipeline churn mini end-to-end; lưu metrics, model và manifest.
3. Load artifact ở process mới, kiểm prediction parity và checksum.
4. Điền model card/experiment report với misuse, failure và limitation.

## Chạy smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 11
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 11
```

Kết quả được lưu tại `.artifacts/lab-11-evidence.json`. Trong `result`, bạn sẽ thấy metrics và artifact contract.
`status=starter-example-completed` chỉ xác nhận code mẫu chạy; **không** có nghĩa toàn bộ acceptance đã đạt.

## Khi nào xem như hoàn thành?

- Pipeline chạy từ clean shell; artifact contract gồm model, feature names, threshold và checksum.
- Prediction trước/sau load khớp; report ghi command, config, seed và negative result.

## Khi mắc kẹt

Nếu parity sai, so feature order, preprocessing và threshold. Nếu clean shell thất bại, tìm hidden state hoặc đường dẫn tương đối.

Sau khi tự dự đoán output, đối chiếu [`expected/README.md`](expected/README.md) và ghi lại điều đã học ở local.
