# AWS Free Tier - ghi chú nguồn

**Kiểm chứng:** 2026-08-12. Xem các URL trong `docs/sources.yml`; kiểm lại trước mỗi cohort.

- AWS công bố tài khoản mới nhận USD 100 credit và có thể kiếm thêm tối đa USD 100 qua activity.
- Free Plan kết thúc sau sáu tháng hoặc khi hết credit, tùy điều kiện đến trước; account đóng nếu không nâng cấp.
- Always Free có monthly allowance; vượt allowance có thể dùng credit đủ điều kiện.
- AWS Budgets hỗ trợ actual/forecast alert nhưng dữ liệu cập nhật có độ trễ. Budget không phải hard cap.
- SageMaker pricing/free offers biến động; roadmap không dùng SageMaker training/notebook/endpoint trong core path.

**Quyết định:** AWS core path chỉ IAM, S3, Lambda, CloudWatch Logs và Budgets; API Gateway là optional short-lived.

