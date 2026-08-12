# Tuần 23 - Capstone integration

## Mục tiêu tuần

Kết nối capstone với lifecycle an toàn.

## Kiến thức cốt lõi

- Training giữ local/Colab/Kaggle; AWS chỉ phục vụ portable logistic inference.
- Manifest liên kết model version, schema, threshold, checksum và source run; handler từ chối contract sai.
- CloudFormation quản allowlisted resources và ownership tags.
- HTTP API optional, tắt mặc định; bật ngắn khi hiểu thêm resource/log/request cost.
- Lifecycle bắt buộc: Pre-check -> Estimate -> Dry-run -> Deploy -> Verify -> Cleanup -> Residual scan -> Cost audit.

## Lịch 8-10 giờ

| Hoạt động | Giờ |
|---|---:|
| Đọc và ghi chú | 2 |
| Guided practice | 2 |
| Lab | 4 |
| Assessment/error analysis | 1 |
| Learning log và tự đánh giá | 1 |
| Review/hoàn thiện | 1 |

## Guided practice

1. Train local và kiểm portable/sklearn parity.
2. End-to-end private invoke bằng known request.
3. Nếu bật HTTP API, không load test, cleanup cùng phiên; nếu không ghi skipped có chủ đích.

## Lab

**lab-20:** End-to-end; HTTP API chỉ optional. Môi trường chính: `local, aws`.

## Tự kiểm tra

1. Vì sao không ship sklearn joblib?
2. Manifest ngăn drift nào?
3. HTTP optional cần guard nào?

## Kết quả hướng tới

capstone demo; kèm config, command, metric, runtime và một failure/limitation.

## Core vs stretch

- **Core:** hoàn thành mini profile, test và kết quả cốt lõi.
- **Stretch:** thử đúng một cải tiến có giả thuyết; không hyperparameter sweep.

## Lỗi thường gặp

- Train SageMaker/EC2 vì có credit.
- Để stack qua đêm.

## AWS cost gate

Không chạy nếu sai account/Region, chưa đọc cost policy, artifact vượt cap hoặc chưa có cleanup path.
Quy trình bắt buộc: `Pre-check -> Estimate -> Dry-run -> Deploy -> Verify -> Cleanup -> Residual scan -> Cost audit`.
AWS Budgets chỉ cảnh báo; dữ liệu billing có thể trễ. Không tạo GPU, NAT Gateway hoặc SageMaker endpoint.

## Nguồn

Xem `docs/sources.yml`; ưu tiên textbook và tài liệu chính thức được ghi trong lab.
