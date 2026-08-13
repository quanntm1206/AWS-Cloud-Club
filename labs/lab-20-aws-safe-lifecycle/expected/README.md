# Kết quả tham khảo - `lab-20-aws-safe-lifecycle`

Không có một output cố định để chép lại.

## Oracle

Một lần làm đạt yêu cầu có các dấu hiệu sau:

- Portable artifact được tạo local, có SHA-256 trước khi upload.
- Cost planning và preflight hoàn tất trên đúng account/`us-east-1`.
- CloudFormation chỉ tạo S3, private Lambda, CloudWatch Logs và IAM role.
- Valid event trả label/probability/threshold; invalid event trả lỗi contract có chủ đích.
- Cleanup dry-run được đọc trước execute; residual scan trả `residual=false` và không lỗi quyền.
- Budget alert được giữ có chủ đích hoặc xóa thủ công cuối khóa, không bị gọi nhầm là infrastructure residual.
- Billing được kiểm ngay sau cleanup, khoảng 12 giờ và ngày kế tiếp.

## Required receipt

Giữ cục bộ checksum, valid/invalid response, cleanup output, residual JSON và ba timestamp cost audit.
Không commit hoặc gửi account ID, billing email hay credential.

## Oracle thuật ngữ

- Evidence nối IAM, S3, Lambda, CloudWatch Logs, budget alert; idempotent cleanup và residual scan chứng minh project sạch hoặc local fallback an toàn.
- Trả lời câu `Tự giải thích` bằng lời của bạn, trỏ tới evidence trên; không chỉ chép glossary.
