# Kết quả tham khảo - lab-15-docker-and-ci

## Oracle

Chạy đủ build/start/log/health/predict/stop theo hướng dẫn riêng trong lab.

## Required receipt

- Chạy `python scripts/run_lab.py --lab 15` từ repository root; PowerShell/Bash đầy đủ nằm trong README.
- JSON phải có `status=starter-example-completed`; trong `result` cần thấy non-root user, health/predict smoke và CI không deploy AWS.
- Learning log cục bộ ghi seed/config, runtime, phép kiểm riêng của lab và ít nhất một limitation hoặc failure.
- Tự trả lời: “Output này chứng minh được gì, và chưa chứng minh được gì?”

## Gợi ý nếu kết quả khác

Nếu build chậm hoặc image lớn, kiểm `.dockerignore` và thứ tự dependency layer.

Đây là gợi ý tự kiểm, không phải bài cần gửi. Không commit evidence, secret, dữ liệu cá nhân, raw dataset lớn
hoặc output cloud trả phí.
