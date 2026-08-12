# Tuần 22 - Lambda inference và logging

## Mục tiêu tuần

Triển khai inference serverless có giới hạn.

## Kiến thức cốt lõi

- Lambda handler nhận event/context và trả contract; package chứa code, portable model và runtime-compatible dependencies.
- Core dùng private invoke; concurrency 1, memory/timeout nhỏ để giới hạn blast radius.
- JSON/type errors thành response; exception bất ngờ log correlation ID, không raw payload/secret.
- CloudWatch log retention hữu hạn; log group cũng phải cleanup/scan.
- Estimate, deploy, verify, cleanup chạy liền phiên; không rời stack đang tồn tại.

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

1. Invoke local handler với valid, malformed JSON, wrong types.
2. Deploy guarded stack, private invoke ít lần, kiểm log.
3. Cleanup ngay, residual scan fail-closed, audit billing sau độ trễ.

## Lab

**lab-20:** Private Lambda invoke, logs, cleanup. Môi trường chính: `local, aws`.

## Tự kiểm tra

1. Private invoke bỏ cost/thành phần nào?
2. Concurrency/timeout giảm rủi ro gì?
3. Cleanup chứng minh bằng gì?

## Kết quả hướng tới

deployment manifest + zero residual; kèm config, command, metric, runtime và một failure/limitation.

## Core vs stretch

- **Core:** hoàn thành mini profile, test và kết quả cốt lõi.
- **Stretch:** thử đúng một cải tiến có giả thuyết; không hyperparameter sweep.

## Lỗi thường gặp

- Tạo public endpoint chỉ để demo.
- Xóa stack nhưng bỏ log/bucket ngoài stack.

## AWS cost gate

Không chạy nếu sai account/Region, chưa đọc cost policy, artifact vượt cap hoặc chưa có cleanup path.
Quy trình bắt buộc: `Pre-check -> Estimate -> Dry-run -> Deploy -> Verify -> Cleanup -> Residual scan -> Cost audit`.
AWS Budgets chỉ cảnh báo; dữ liệu billing có thể trễ. Không tạo GPU, NAT Gateway hoặc SageMaker endpoint.

## Nguồn

Xem `docs/sources.yml`; ưu tiên textbook và tài liệu chính thức được ghi trong lab.
