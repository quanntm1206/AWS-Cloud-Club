# Tuần 15 - Inference API và contracts

## Mục tiêu tuần

Thiết kế inference contract và error boundary.

## Kiến thức cốt lõi

- Inference contract khóa request/response schema, model version, threshold, error codes và limits.
- Validation lỗi client trả 4xx; artifact/service failure trả 5xx, chi tiết nội bộ chỉ vào log an toàn.
- Health/readiness không train; predict dùng đúng preprocessing artifact và không nhận target.
- Batch/payload/timeout limits là guardrail; không log raw sensitive features.

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

1. Gửi valid, missing, wrong-type, unknown-category payload.
2. Kiểm success/422/503 theo contract.
3. Đo warm latency mini batch và ghi giới hạn phép đo.

## Lab

**lab-14:** Local API valid/invalid payload. Môi trường chính: `local`.

## Tự kiểm tra

1. 422 khác 500 thế nào?
2. Health khác readiness?
3. Vì sao không log raw request?

## Kết quả hướng tới

API demo; kèm config, command, metric, runtime và một failure/limitation.

## Core vs stretch

- **Core:** hoàn thành mini profile, test và kết quả cốt lõi.
- **Stretch:** thử đúng một cải tiến có giả thuyết; không hyperparameter sweep.

## Lỗi thường gặp

- Lộ stack trace cho client.
- API tự viết preprocessing khác training.

## Nguồn

Xem `docs/sources.yml`; ưu tiên textbook và tài liệu chính thức được ghi trong lab.
