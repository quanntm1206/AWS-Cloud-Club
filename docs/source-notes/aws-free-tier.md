# AWS Free Tier - ghi chú nguồn

**Kiểm chứng:** 2026-08-12. Đây là thông tin dễ thay đổi; kiểm lại trước mỗi cohort và trước mỗi deploy.

- Account mới đủ điều kiện nhận USD 100 sau khi tạo và có thể kiếm thêm tối đa USD 100 qua activities.
  Cụm “up to USD 200” không có nghĩa USD 200 được cấp toàn bộ ngay.
- Free Plan kết thúc sau 6 tháng hoặc khi credit hết, tùy điều kiện nào đến trước. AWS mô tả plan này
  không phát sinh charge; account đóng khi plan kết thúc nếu người dùng không nâng cấp.
- Paid Plan là pay-as-you-go. Credit còn lại được áp dụng cho khoản đủ điều kiện; Budget không chặn cứng.
- Credit Free Tier hết hạn 12 tháng từ ngày tạo account. Existing/past customer có thể không đủ điều kiện.
- Join AWS Organizations hoặc setup Control Tower có thể làm credit hết hiệu lực ngay và Free Plan tự
  chuyển sang Paid Plan.
- AWS Budgets cập nhật tối đa ba lần/ngày, thường cách 8-12 giờ. Alert có thể đến sau khi đã vượt ngưỡng.
- Budget monitoring/notification không tính phí. Tránh Budget Reports và Budget Actions trong lab;
  chúng có pricing riêng.

## Nguồn chính thức

- Plans: https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans.html
- FAQ: https://aws.amazon.com/free/free-tier-faqs/
- Tracking: https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/tracking-free-tier-usage.html
- Budgets: https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html
- Budget pricing: https://aws.amazon.com/aws-cost-management/aws-budgets/pricing/

**Quyết định:** Core chỉ dùng S3, private Lambda, CloudWatch Logs, IAM và Budgets. Không có public API.
Training giữ local/Colab/Kaggle. Nếu account hoặc pricing không rõ, học viên dùng local simulation.
