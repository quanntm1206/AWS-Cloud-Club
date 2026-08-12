# Kết quả tham khảo - lab-08-tree-ensemble-comparison

## Oracle

Mọi candidate dùng cùng split, metric và runtime budget; test chỉ mở sau khi chọn.

## Required receipt

- Chạy `python scripts/run_lab.py --lab 8` từ repository root; PowerShell/Bash đầy đủ nằm trong README.
- JSON phải có `status=starter-example-completed`; trong `result` cần thấy validation score từng candidate, model được chọn và final test AUC.
- Learning log cục bộ ghi seed/config, runtime, phép kiểm riêng của lab và ít nhất một limitation hoặc failure.
- Tự trả lời: “Output này chứng minh được gì, và chưa chứng minh được gì?”

## Gợi ý nếu kết quả khác

Nếu model thắng rất ít, so độ biến thiên CV và artifact size trước khi kết luận.

Đây là gợi ý tự kiểm, không phải bài cần gửi. Không commit evidence, secret, dữ liệu cá nhân, raw dataset lớn
hoặc output cloud trả phí.
