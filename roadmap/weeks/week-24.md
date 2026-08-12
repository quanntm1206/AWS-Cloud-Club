# Tuần 24 - Tổng kết năng lực, cost audit và demo

## Mục tiêu tuần

Trình bày tổng kết năng lực; audit chi phí và tài nguyên.

## Kiến thức cốt lõi

- Tổng kết năng lực nêu problem, constraint, baseline, decision, evidence, failure, reproduction; không chỉ accuracy/screenshot.
- Demo 5-7 phút có fallback local, không cần AWS resource sống thường trực.
- Cost audit đối chiếu manifest, stack, residual scan và Billing; kiểm lại vì billing data có độ trễ.
- Incident drill: dừng deploy, xác định owner/tag, cleanup, scan lại, retrospective.
- Done khi tests/validators pass, model card cập nhật, zero known residual, secret scan sạch và limitation được nêu.

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

1. Chạy demo từ clean environment và bấm giờ.
2. Cleanup + residual scan; lưu evidence không chứa account secret.
3. Review theo rubric và viết kế hoạch 90 ngày hướng ML Engineer.

## Lab

**lab-20:** Incident drill, residual scan, retrospective. Môi trường chính: `local, aws`.

## Tự kiểm tra

1. Tổng kết năng lực chứng minh engineering bằng gì?
2. Fallback demo cần gì?
3. Vì sao audit billing sau cleanup?

## Kết quả hướng tới

mốc năng lực 6 + tổng kết năng lực; kèm config, command, metric, runtime và một failure/limitation.

## Core vs stretch

- **Core:** hoàn thành mini profile, test và kết quả cốt lõi.
- **Stretch:** thử đúng một cải tiến có giả thuyết; không hyperparameter sweep.

## Lỗi thường gặp

- Giữ endpoint sống chỉ để trình diễn.
- Đưa account ID/credential/raw billing vào artifact.

## AWS cost gate

Không chạy nếu sai account/Region, chưa đọc cost policy, artifact vượt cap hoặc chưa có cleanup path.
Quy trình bắt buộc: `Pre-check -> Estimate -> Dry-run -> Deploy -> Verify -> Cleanup -> Residual scan -> Cost audit`.
AWS Budgets chỉ cảnh báo; dữ liệu billing có thể trễ. Không tạo GPU, NAT Gateway hoặc SageMaker endpoint.

## Nguồn

Xem `docs/sources.yml`; ưu tiên textbook và tài liệu chính thức được ghi trong lab.
