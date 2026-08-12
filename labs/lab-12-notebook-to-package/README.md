# Lab 12 - Tách logic khỏi notebook thành config và CLI

## Mục tiêu

Bạn sẽ tháo training logic khỏi notebook mà không thay đổi hành vi. Mục tiêu không phải nhiều file hơn, mà là input/output rõ và một nguồn logic duy nhất.

## Trước khi bắt đầu

Đọc `roadmap/weeks/week-13.md`, chạy từ repository root và tạo chỗ lưu evidence cục bộ. Không đưa
credential, dữ liệu cá nhân hoặc artifact lớn vào Git.

## Các bước thực hiện

1. Đánh dấu cell nào thuộc data, features, train, evaluate và artifact I/O.
2. Di chuyển core logic vào module; notebook chỉ import và gọi.
3. Tạo config có schema cùng CLI nhận config/data/output.
4. Chạy cùng config từ notebook và clean shell, so metric/artifact trong tolerance.

## Chạy smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 12
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 12
```

Kết quả được lưu tại `.artifacts/lab-12-evidence.json`. Trong `result`, bạn sẽ thấy danh sách config keys và `notebook_state_required=false`.
`status=starter-example-completed` chỉ xác nhận code mẫu chạy; **không** có nghĩa toàn bộ acceptance đã đạt.

## Khi nào xem như hoàn thành?

- Output cho thấy config keys rõ và `notebook_state_required=false`.
- Không còn logic training copy ở hai nơi; CLI trả lỗi hữu ích khi config sai.

## Khi mắc kẹt

Restart kernel và mở clean shell. Biến hoặc file chỉ tồn tại sau một cell cũ chính là hidden dependency cần loại.

Sau khi tự dự đoán output, đối chiếu [`expected/README.md`](expected/README.md) và ghi lại điều đã học ở local.
