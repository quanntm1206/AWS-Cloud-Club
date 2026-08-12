# Kết quả tham khảo - lab-14-local-inference-api

## Oracle

Gửi payload đúng, thiếu cột và sai kiểu; không log raw feature nhạy cảm.

## Required receipt

- Chạy `python scripts/run_lab.py --lab 14` từ repository root; PowerShell/Bash đầy đủ nằm trong README.
- JSON phải có `status=starter-example-completed`; trong `result` cần thấy contract `/health`, `/predict`, 422 và 503.
- Learning log cục bộ ghi seed/config, runtime, phép kiểm riêng của lab và ít nhất một limitation hoặc failure.
- Tự trả lời: “Output này chứng minh được gì, và chưa chứng minh được gì?”

## Gợi ý nếu kết quả khác

Nếu nhận 500 cho lỗi client, đưa validation ra boundary trước khi gọi model.

Đây là gợi ý tự kiểm, không phải bài cần gửi. Không commit evidence, secret, dữ liệu cá nhân, raw dataset lớn
hoặc output cloud trả phí.
