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

Nếu AWS account không đủ điều kiện hoặc buộc nâng Paid Plan, kết quả local handler + artifact contract +
cleanup dry-run là đường hoàn thành an toàn. Không cần mua dịch vụ để đạt lab.
