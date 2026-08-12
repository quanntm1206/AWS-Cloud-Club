# AWS capstone: học cloud mà không đánh cược hóa đơn

Phần AWS của lộ trình chỉ làm một việc nhỏ nhưng đủ thật: đưa model tabular đã train ở máy cá nhân,
Colab hoặc Kaggle lên S3 rồi gọi Lambda **riêng tư**. Không có public endpoint. Bạn học được lifecycle
deploy, quan sát và dọn tài nguyên mà không cần dùng AWS để training.

## Hiểu đúng về USD 200 và hai loại account plan

- Tài khoản mới đủ điều kiện nhận **USD 100 khi đăng ký** và **có thể kiếm thêm tối đa USD 100** khi
  hoàn thành các activity AWS chỉ định. Đây không phải USD 200 được cấp hết ngay.
- **Free Plan** kết thúc sau 6 tháng hoặc khi dùng hết credit, tùy điều kiện nào đến trước. AWS mô tả
  plan này không phát sinh charge; khi plan kết thúc, account sẽ đóng nếu bạn không nâng cấp.
- **Paid Plan** là pay-as-you-go. Credit chỉ bù các khoản đủ điều kiện; phần vượt credit hoặc không đủ
  điều kiện vẫn có thể bị tính phí. Budget alert không phải hard cap.
- Credit Free Tier hết hạn 12 tháng từ ngày tạo account. Eligibility, credit và service allowance có
  thể khác theo account; hãy tin màn hình Billing của chính bạn thay vì một con số trong tài liệu.

Nguồn AWS, kiểm ngày 2026-08-12:
[account plans](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans.html),
[Free Tier FAQ](https://aws.amazon.com/free/free-tier-faqs/) và
[tracking Free Tier](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/tracking-free-tier-usage.html).

> Dành cho AWS Cloud Club: đừng join AWS Organizations và đừng bật Control Tower cho account học tập.
> Theo FAQ của AWS, hai thao tác này có thể làm Free Plan tự chuyển sang Paid Plan và credit Free Tier
> hết hiệu lực ngay. Nếu account đã join, dừng AWS lab và dùng local simulation.

## Khi nào nên tạo account

Đừng tạo account từ tuần 1 rồi để đồng hồ 6 tháng chạy trong lúc bạn còn học NumPy. Nếu chưa có account,
hãy đợi đến cuối tuần 20 hoặc đầu tuần 21. Không tạo nhiều account để săn credit. Trước mỗi lần deploy,
mở Billing để kiểm `plan`, credit còn lại, ngày hết hạn và dịch vụ đủ điều kiện. Nếu console buộc nâng
cấp Paid Plan, hoặc thông tin không rõ, bỏ qua deploy; private handler vẫn chạy local để bạn hoàn thành bài.

## Trước khi bấm Deploy

1. Bật MFA cho root; không tạo root access key. Dùng identity có quyền tối thiểu.
2. Xác nhận đúng account và `us-east-1` bằng `aws sts get-caller-identity`.
3. Tạo **Cost budget** với Actual và Forecasted email alerts ở ngưỡng thấp. Chỉ dùng notification thường:
   không tạo Budget Report hoặc Budget Action cho lab này.
4. Đọc `cost-policy.yml`. Không dùng EC2/EBS/Elastic IP, NAT Gateway, SageMaker, Bedrock, RDS/Aurora,
   OpenSearch, Redshift, EMR/Glue, EKS/ECS/Fargate, Marketplace, Savings Plans, Reserved Instances hoặc
   Route 53 domain. Những dịch vụ này chỉ được thảo luận ở mức kiến trúc/pricing.
5. Chạy cost check, tự đối chiếu [AWS Pricing Calculator](https://calculator.aws/), rồi chạy preflight.
   `USD 0.00-0.10` là planning envelope theo giả định nhỏ, không phải báo giá hay cam kết hóa đơn.
6. Đặt timer để cleanup trong cùng phiên. Tag `ExpiresAt` chỉ là lời nhắc; nó **không tự xóa** tài nguyên.

AWS Budgets dùng dữ liệu có độ trễ. AWS cho biết budget cập nhật tối đa ba lần mỗi ngày, thường cách nhau
8-12 giờ. Alert có thể đến sau khi chi phí đã vượt ngưỡng. Xem
[AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)
và [Budget pricing](https://aws.amazon.com/aws-cost-management/aws-budgets/pricing/).

## Lifecycle bắt buộc

```text
Pre-check -> Estimate -> Dry-run -> Deploy -> Verify -> Cleanup -> Residual scan -> Cost audit
```

`aws lambda invoke` là đường học duy nhất. Template không tạo API Gateway hay public URL. Cleanup chỉ
xóa stack exact-name có prefix `ml-roadmap-`; script không quét hoặc xóa tài nguyên ngoài project.
Budget alert được giữ có chủ đích để bảo vệ các buổi sau; cuối khóa bạn tự review rồi xóa trên Console.

## Nếu có gì sai

Nếu deploy lỗi, terminal đóng bất ngờ, hoặc bạn không chắc stack còn sống hay không:

1. Dừng mọi lệnh tạo tài nguyên. Xác nhận lại account, Region và project ID.
2. Chạy cleanup ở chế độ dry-run; đọc từng exact resource name.
3. Chạy cleanup với xác nhận project ID, sau đó chạy residual scan.
4. Nếu scan lỗi vì thiếu quyền, **không** coi đó là sạch. Kiểm thủ công CloudFormation, S3, Lambda,
   CloudWatch Logs và IAM hoặc nhờ người quản lý account hỗ trợ.
5. Kiểm Billing ngay, sau khoảng 12 giờ và vào ngày kế tiếp. Không lấy số 0 ngay sau cleanup làm kết luận.

## Bạn đã an toàn khi

- Stack, bucket, Lambda, log group và IAM role của project không còn.
- Residual scan trả `residual=false`; scan không có lỗi quyền hay lỗi mạng.
- Bạn đã ghi lịch kiểm Billing lại sau độ trễ.
- Budget alert còn lại được ghi rõ là giữ có chủ đích, không bị nhầm với residual infrastructure.

