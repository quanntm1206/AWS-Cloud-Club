# Kết quả tham khảo - lab-16-device-aware-mlp

## Oracle

Smoke demo là NumPy CPU; sau đó viết/chạy loop PyTorch nhỏ của tuần 17.

## Required receipt

- Chạy `python scripts/run_lab.py --lab 16` từ repository root; PowerShell/Bash đầy đủ nằm trong README.
- JSON phải có `status=starter-example-completed`; trong `result` cần thấy losses giảm, device và số parameter.
- Learning log cục bộ ghi seed/config, runtime, phép kiểm riêng của lab và ít nhất một limitation hoặc failure.
- Tự trả lời: “Output này chứng minh được gì, và chưa chứng minh được gì?”

## Oracle thuật ngữ

- Receipt ghi tensor shape, batch, epoch, optimizer, device; loss giảm và parameter count đúng.
- Trả lời câu `Tự giải thích` bằng lời của bạn, trỏ tới evidence trên; không chỉ chép glossary.

## Gợi ý nếu kết quả khác

In shape/dtype/device của model, input và target; kiểm `zero_grad`, `eval`, `no_grad`.

Đây là gợi ý tự kiểm, không phải bài cần gửi. Không commit evidence, secret, dữ liệu cá nhân, raw dataset lớn
hoặc output cloud trả phí.
