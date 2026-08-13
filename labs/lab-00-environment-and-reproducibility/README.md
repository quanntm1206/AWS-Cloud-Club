# Lab 00 - Kiểm tra môi trường và khả năng tái lập

## Mục tiêu

Buổi đầu chưa cần train model. Mục tiêu là tạo một điểm xuất phát đáng tin: cùng code, cùng seed và cùng môi trường phải cho cùng một báo cáo nhỏ.

## Thuật ngữ trong lab

**Thuật ngữ mới:** `dataset`, `sample`, `schema`, `reproducibility`, `seed`

**Ôn lại:** Chưa có - đây là lab đầu tiên.

**Áp dụng trong lab:** Mở `dataset` smoke, đếm từng `sample`, đối chiếu `schema`, cố định `seed` rồi chạy hai lần để kiểm `reproducibility`.

**Tự giải thích:** Dataset khác sample thế nào; schema và seed giúp reproducibility đến đâu?

## Trước khi bắt đầu

Đọc `roadmap/weeks/week-01.md`, chạy từ repository root và tạo chỗ lưu evidence cục bộ. Không đưa
credential, dữ liệu cá nhân hoặc file kết quả lớn vào Git.

## Các bước thực hiện

1. Chạy bootstrap check, ghi Python version, dependency và hệ điều hành đang dùng.
2. Mở JSON smoke demo; đối chiếu số hàng, dtype và seed với dữ liệu mẫu.
3. Chạy lại từ một terminal mới, so hai báo cáo và ghi tolerance hoặc khác biệt quan sát được.
4. Tạo learning log tuần 01, ghi một giới hạn của phép kiểm hiện tại.

## Chạy smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 0
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 0
```

Kết quả được lưu tại `.artifacts/lab-00-evidence.json`. Trong `result`, bạn sẽ thấy `rows`, `dtypes`, `seed`.
`status=starter-example-completed` chỉ xác nhận code mẫu chạy; **không** có nghĩa toàn bộ acceptance đã đạt.

## Khi nào xem như hoàn thành?

- Hai lần chạy cho cùng số hàng, schema và seed; khác biệt môi trường được ghi rõ.
- Bạn giải thích được vì sao seed hỗ trợ tái lập nhưng không bảo đảm bit-identical trên mọi phần cứng.

## Khi mắc kẹt

Nếu import lỗi, xác nhận terminal đang dùng Python trong `.venv`, rồi chạy lại bootstrap check. Nếu hai run khác nhau, so version và input trước khi đổi code.

Sau khi tự dự đoán output, đối chiếu [`expected/README.md`](expected/README.md) và ghi lại điều đã học ở local.
