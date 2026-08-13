# Lab 14 - Kiểm contract của inference API local

## Mục tiêu

API là nơi dữ liệu ngoài hệ thống gặp model. Bạn sẽ làm cho lỗi client, lỗi artifact và response thành công có contract khác nhau, thay vì mọi thứ thành 500.

## Thuật ngữ trong lab

**Thuật ngữ mới:** `API contract`, `latency`

**Ôn lại:** `data contract`, `artifact`, `inference`, `schema`

**Áp dụng trong lab:** Định nghĩa `API contract`, đo `latency`, gửi sample hợp lệ/sai qua inference; data contract chặn schema lỗi trước artifact và response không lộ raw feature.

**Tự giải thích:** API contract khác data contract thế nào; latency đo được chưa chứng minh điều gì?

## Trước khi bắt đầu

Đọc `roadmap/weeks/week-15.md`, chạy từ repository root và tạo chỗ lưu evidence cục bộ. Không đưa
credential, dữ liệu cá nhân hoặc artifact lớn vào Git.

## Các bước thực hiện

1. Gọi `/health` và `/predict` với payload hợp lệ.
2. Thử missing field, wrong type và unknown category; kiểm response 4xx có thông tin vừa đủ.
3. Mô phỏng model chưa sẵn sàng; kiểm 503 mà không lộ stack trace.
4. Đo warm latency mini input group, ghi payload/input group limit và giới hạn phép đo.

## Chạy smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 14
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 14
```

Kết quả được lưu tại `.artifacts/lab-14-evidence.json`. Trong `result`, bạn sẽ thấy contract `/health`, `/predict`, 422 và 503.
`status=starter-example-completed` chỉ xác nhận code mẫu chạy; **không** có nghĩa toàn bộ acceptance đã đạt.

## Khi nào xem như hoàn thành?

- Contract có `/health`, `/predict`, 422 và 503; preprocessing đúng artifact training.
- Log không chứa raw feature nhạy cảm; health không train hoặc sửa model.

## Khi mắc kẹt

Gọi handler với payload tối thiểu trước. Nếu lỗi client thành 500, đưa validation ra boundary và giữ exception nội bộ trong log.

Sau khi tự dự đoán output, đối chiếu [`expected/README.md`](expected/README.md) và ghi lại điều đã học ở local.
