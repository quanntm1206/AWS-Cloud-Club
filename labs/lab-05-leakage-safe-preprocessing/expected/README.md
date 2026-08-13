# Kết quả tham khảo - lab-05-leakage-safe-preprocessing

## Oracle

Thêm một category chưa thấy; pipeline vẫn predict được mà không fit lại.

## Required receipt

- Chạy `python scripts/run_lab.py --lab 5` từ repository root; PowerShell/Bash đầy đủ nằm trong README.
- JSON phải có `status=starter-example-completed`; trong `result` cần thấy prediction cho unknown category và `leakage_guard=true`.
- Learning log cục bộ ghi seed/config, runtime, phép kiểm riêng của lab và ít nhất một limitation hoặc failure.
- Tự trả lời: “Output này chứng minh được gì, và chưa chứng minh được gì?”

## Oracle thuật ngữ

- Evidence chứng minh preprocessing/transform chỉ fit training set trong pipeline; category mới không vỡ; không có data leakage.
- Trả lời câu `Tự giải thích` bằng lời của bạn, trỏ tới evidence trên; không chỉ chép glossary.

## Gợi ý nếu kết quả khác

Nếu vỡ ở encoder, kiểm `handle_unknown`; nếu score đẹp bất thường, tìm bước fit trước split.

Đây là gợi ý tự kiểm, không phải bài cần gửi. Không commit evidence, secret, dữ liệu cá nhân, raw dataset lớn
hoặc output cloud trả phí.
