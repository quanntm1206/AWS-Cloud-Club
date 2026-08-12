# Kết quả tham khảo - lab-06-metrics-and-threshold

## Oracle

Viết rule chọn threshold trước khi xem test; so ít nhất ba threshold.

## Required receipt

- Chạy `python scripts/run_lab.py --lab 6` từ repository root; PowerShell/Bash đầy đủ nằm trong README.
- JSON phải có `status=starter-example-completed`; trong `result` cần thấy validation threshold/F1/PR-AUC, FP/FN cost và test metrics.
- Learning log cục bộ ghi seed/config, runtime, phép kiểm riêng của lab và ít nhất một limitation hoặc failure.
- Tự trả lời: “Output này chứng minh được gì, và chưa chứng minh được gì?”

## Gợi ý nếu kết quả khác

Nếu chưa hiểu AUC, quay về confusion matrix và số lượng FP/FN ở từng threshold.

Đây là gợi ý tự kiểm, không phải bài cần gửi. Không commit evidence, secret, dữ liệu cá nhân, raw dataset lớn
hoặc output cloud trả phí.
