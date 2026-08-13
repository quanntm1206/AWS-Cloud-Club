# Kết quả tham khảo - lab-17-transfer-learning

## Oracle

Chọn đúng một notebook Colab hoặc Kaggle, chạy `cpu-mini` trước rồi mới dùng GPU nếu có.

## Required receipt

- Chạy `python scripts/run_lab.py --lab 17` từ repository root; PowerShell/Bash đầy đủ nằm trong README.
- JSON phải có `status=starter-example-completed`; trong `result` cần thấy smoke dict về frozen layers; notebook thật xuất checkpoint và metrics.
- Learning log cục bộ ghi seed/config, runtime, phép kiểm riêng của lab và ít nhất một limitation hoặc failure.
- Tự trả lời: “Output này chứng minh được gì, và chưa chứng minh được gì?”

## Oracle thuật ngữ

- Train dùng augmentation, validation deterministic; backbone freeze đúng; transfer learning dùng pretrained weights; checkpoint được export.
- Trả lời câu `Tự giải thích` bằng lời của bạn, trỏ tới evidence trên; không chỉ chép glossary.

## Gợi ý nếu kết quả khác

FakeData chỉ chứng minh pipeline chạy; không báo accuracy đó như chất lượng model.
Random weights chỉ chứng minh code chạy; chưa được gọi là transfer learning.

Đây là gợi ý tự kiểm, không phải bài cần gửi. Không commit evidence, secret, dữ liệu cá nhân, raw dataset lớn
hoặc output cloud trả phí.
