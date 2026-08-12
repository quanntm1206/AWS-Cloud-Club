# Tuần 21 - AWS Free Plan, IAM, Budgets và S3

## Mục tiêu tuần

Hiểu Free Plan, IAM least privilege, Budget caveat, S3.

## Kiến thức cốt lõi

- Account plan, credit và Free Tier eligibility có thể đổi; kiểm trực tiếp Billing/Free Tier trước lab. Credit không phải hard spending cap.
- AWS Budgets chỉ cảnh báo; billing/alert có thể trễ nên cleanup và residual scan vẫn bắt buộc.
- Dùng IAM least privilege, MFA root, không root access key; xác nhận account ID/Region trước lệnh.
- S3 có storage/request/transfer cost; chỉ upload artifact nhỏ, checksum, lifecycle ngắn, block public access.
- Preflight fail-closed nếu thiếu acknowledgment, tag/expiry, allowlist hoặc cleanup path.

## Lịch 8-10 giờ

| Hoạt động | Giờ |
|---|---:|
| Đọc và ghi chú | 2 |
| Guided practice | 2 |
| Lab | 3 |
| Assessment/error analysis | 1 |
| Learning log và tự đánh giá | 1 |
| Review/hoàn thiện | 0 |

## Guided practice

1. Xác nhận plan/credit/Region; dừng nếu màn hình billing chưa rõ.
2. Chạy local preflight/dry-run, tạo checksum và manifest.
3. Tạo alert nhỏ nếu phù hợp; diễn tập cleanup không resource.

## Lab

**lab-20:** Preflight, artifact checksum và cleanup thử. Môi trường chính: `local, aws`.

## Tự kiểm tra

1. Vì sao 200 USD không đồng nghĩa miễn phí?
2. Budget có thể báo muộn vì sao?
3. Điều kiện nào buộc dừng deploy?

## Kết quả hướng tới

AWS preflight evidence; kèm config, command, metric, runtime và một failure/limitation.

## Core vs stretch

- **Core:** hoàn thành mini profile, test và kết quả cốt lõi.
- **Stretch:** thử đúng một cải tiến có giả thuyết; không hyperparameter sweep.

## Lỗi thường gặp

- Tin Free Tier tự chặn bill.
- Sai account/Region hoặc thiếu tag.

## AWS cost gate

Không chạy nếu sai account/Region, chưa đọc cost policy, artifact vượt cap hoặc chưa có cleanup path.
Quy trình bắt buộc: `Pre-check -> Estimate -> Dry-run -> Deploy -> Verify -> Cleanup -> Residual scan -> Cost audit`.
AWS Budgets chỉ cảnh báo; dữ liệu billing có thể trễ. Không tạo GPU, NAT Gateway hoặc SageMaker endpoint.

## Nguồn

Xem `docs/sources.yml`; ưu tiên textbook và tài liệu chính thức được ghi trong lab.
