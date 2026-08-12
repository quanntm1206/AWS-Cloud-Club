# Tuần 21 - Bước lên AWS mà vẫn kiểm soát được chi phí

## Mục tiêu tuần

Hiểu account plan, credit, IAM, Budget và S3 trước khi tạo bất kỳ tài nguyên nào.

## Vì sao tuần này quan trọng

Một ML Engineer không chỉ biết deploy; họ còn biết lúc nào **không nên deploy**. Tuần này giúp bạn đọc
màn hình Billing, nhận ra ranh giới Free/Paid Plan và dựng hàng rào an toàn trước khi chạm cloud.

## Kiến thức cốt lõi

- “Up to USD 200” là USD 100 khi đăng ký và có thể kiếm thêm tối đa USD 100 qua activity; không phải
  USD 200 được cấp hết ngay. Free Plan kết thúc sau 6 tháng hoặc khi hết credit.
- Paid Plan là pay-as-you-go. Credit chỉ bù khoản đủ điều kiện; Budget alert không phải hard cap.
- Join AWS Organizations hoặc setup Control Tower có thể làm credit hết hiệu lực và Free Plan tự nâng
  Paid Plan. Không dùng hai tính năng này trong account học tập.
- IAM least privilege, MFA root, không root access key; luôn xác nhận account ID và Region trước lệnh.
- S3 tính theo storage, request và transfer. Artifact nhỏ, block public access, lifecycle ngắn.

Nguồn AWS, kiểm ngày 2026-08-12:
[plans](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans.html),
[FAQ](https://aws.amazon.com/free/free-tier-faqs/) và
[tracking](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/tracking-free-tier-usage.html).

## Lịch 8-10 giờ

| Hoạt động | Giờ |
|---|---:|
| Đọc plans, credits và cost policy | 2 |
| Xem Billing, IAM và Budget có hướng dẫn | 2 |
| Chạy local preflight, checksum và cleanup dry-run | 3 |
| Learning log và tự đánh giá | 2 |

## Guided practice

1. Nếu chưa có account, chỉ tạo ở tuần 20/21 để không lãng phí cửa sổ 6 tháng. Không tạo nhiều account
   để săn credit.
2. Mở Billing; ghi `plan`, credit còn lại, ngày hết hạn và days remaining. Nếu thông tin không rõ hoặc
   console bắt nâng Paid Plan, chọn local-only.
3. Tạo Cost budget với Actual và Forecasted email alerts ở ngưỡng thấp. Không tạo Budget Report hoặc
   Budget Action. Alert có độ trễ, không thay cleanup.
4. Chạy `cost-check` và `preflight` local. Tập đọc lý do dừng thay vì vội bỏ qua guard.

## Lab

**lab-20, phần chuẩn bị:** checksum artifact, cost planning, preflight và cleanup dry-run. Chưa deploy.

## Tự kiểm tra

1. Vì sao “up to USD 200” không phải USD 200 có sẵn?
2. Free Plan khác Paid Plan ở rủi ro charge như thế nào?
3. Vì sao Budget không thể thay cleanup?

## Kết quả hướng tới

Bạn tự giải thích được plan/credit của account, tạo alert đúng loại và nhận ra các điều kiện buộc dừng.

## Dấu hiệu bạn đã hiểu

Bạn phân biệt được credit, Free Plan, Paid Plan và Budget mà không gọi chung tất cả là “miễn phí”.

## Core vs stretch

- **Core:** local preflight + đọc Billing/plan rõ ràng.
- **Stretch:** đọc AWS Pricing Calculator cho S3/Lambda; không deploy thử chỉ để xem.

## Lỗi thường gặp

- Tin credit hoặc Budget tự chặn mọi chi phí.
- Join Organizations/Control Tower vì lời mời của club.
- Tạo account từ đầu lộ trình rồi để Free Plan gần hết hạn trước capstone.

## Khi mắc kẹt

Không đoán trạng thái account. Chụp lại thông tin không nhạy cảm hoặc hỏi người quản lý club; tiếp tục
local-only. Không gửi account ID, email billing hoặc credential.

## Bạn đã sẵn sàng chuyển tuần khi

- Bạn biết account đang ở Free hay Paid Plan và ngày hết hạn.
- Bạn có Actual + Forecasted notifications; hiểu chúng có thể báo muộn.
- Bạn có thể nói “không deploy” khi eligibility, estimate hoặc cleanup path chưa rõ.

## AWS cost gate

Không chạy nếu sai account/Region, chưa đọc `aws/README.md`, chưa có cleanup path hoặc estimate vượt
USD 0.10. Không dùng EC2, NAT Gateway, SageMaker, Bedrock, database, container cluster hay Marketplace.

## Nguồn

Xem `docs/sources.yml` và `docs/source-notes/aws-free-tier.md`.
