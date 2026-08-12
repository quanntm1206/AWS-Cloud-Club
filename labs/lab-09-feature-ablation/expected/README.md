# Kết quả tham khảo - lab-09-feature-ablation

## Oracle

Chỉ thay một nhóm feature; ghi giả thuyết, metric delta và quyết định giữ/bỏ.

## Required receipt

- Chạy `python scripts/run_lab.py --lab 9` từ repository root; PowerShell/Bash đầy đủ nằm trong README.
- JSON phải có `status=starter-example-completed`; trong `result` cần thấy validation AUC theo feature group và `test_set_touched=false`.
- Learning log cục bộ ghi seed/config, runtime, phép kiểm riêng của lab và ít nhất một limitation hoặc failure.
- Tự trả lời: “Output này chứng minh được gì, và chưa chứng minh được gì?”

## Gợi ý nếu kết quả khác

Nếu kết quả khó giải thích, khóa seed/model rồi kiểm availability time và missing handling.

Đây là gợi ý tự kiểm, không phải bài cần gửi. Không commit evidence, secret, dữ liệu cá nhân, raw dataset lớn
hoặc output cloud trả phí.
