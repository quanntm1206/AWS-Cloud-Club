# Kết quả tham khảo - lab-13-ml-testing

## Oracle

Thêm kiểm tra missing column, wrong dtype, unseen category và artifact hỏng.

## Required receipt

- Chạy `python scripts/run_lab.py --lab 13` từ repository root; PowerShell/Bash đầy đủ nằm trong README.
- JSON phải có `status=starter-example-completed`; trong `result` cần thấy `artifact_reload_parity=true` cùng negative cases tự bổ sung.
- Learning log cục bộ ghi seed/config, runtime, phép kiểm riêng của lab và ít nhất một limitation hoặc failure.
- Tự trả lời: “Output này chứng minh được gì, và chưa chứng minh được gì?”

## Gợi ý nếu kết quả khác

Dùng synthetic data nhỏ; tránh assert exact metric khi randomness chưa được khóa.

Đây là gợi ý tự kiểm, không phải bài cần gửi. Không commit evidence, secret, dữ liệu cá nhân, raw dataset lớn
hoặc output cloud trả phí.
