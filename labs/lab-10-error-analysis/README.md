# Lab 10 - Biến lỗi model thành việc cần làm tiếp

## Mục tiêu

Error analysis không phải sưu tập vài lỗi thú vị. Bạn sẽ lấy mẫu theo quy tắc rồi biến các lỗi thành giả thuyết có hành động tiếp theo.

## Trước khi bắt đầu

Đọc `roadmap/weeks/week-11.md`, chạy từ repository root và tạo chỗ lưu evidence cục bộ. Không đưa
credential, dữ liệu cá nhân hoặc artifact lớn vào Git.

## Các bước thực hiện

1. Tính FP/FN theo ít nhất hai slice, luôn ghi support.
2. Lấy tối đa 20 failure records theo sampling rule đã viết.
3. Gán taxonomy: data, boundary, missing signal, label noise hoặc shift.
4. Đề xuất một data fix và một model fix; nêu phép kiểm có thể bác bỏ mỗi giả thuyết.

## Chạy smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 10
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 10
```

Kết quả được lưu tại `.artifacts/lab-10-evidence.json`. Trong `result`, bạn sẽ thấy slice metrics, failure records có cap và taxonomy.
`status=starter-example-completed` chỉ xác nhận code mẫu chạy; **không** có nghĩa toàn bộ acceptance đã đạt.

## Khi nào xem như hoàn thành?

- Output có slice metrics, failure cap, records và taxonomy; không chọn mẫu bằng cảm tính.
- Bạn không gọi feature importance là causality và không kết luận fairness từ nhóm quá nhỏ.

## Khi mắc kẹt

Nếu không thấy pattern, đổi sampling để phủ nhiều nhóm/confidence. Mô tả điều quan sát trước, giải thích nguyên nhân sau.

Sau khi tự dự đoán output, đối chiếu [`expected/README.md`](expected/README.md) và ghi lại điều đã học ở local.
