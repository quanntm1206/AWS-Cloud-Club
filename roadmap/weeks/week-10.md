# Tuần 10 - Feature engineering và ablation

## Mục tiêu tuần

Feature engineering có giả thuyết; ablation một biến.

## Kiến thức cốt lõi

- Feature phải tồn tại tại prediction time, ổn định, tái tạo được và có ý nghĩa.
- Ratio/log/interaction cần hypothesis; xử lý zero, missing và range.
- Ablation thay đúng một feature group trong cùng harness.
- Metric delta nhỏ hơn CV variability chưa chứng minh feature có ích.

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

1. Viết feature hypothesis và availability time.
2. So all-features với without-monthly-charge.
3. Ghi metric/runtime delta và keep/drop decision.

## Lab

**lab-09:** Feature ablation log. Môi trường chính: `local`.

## Tự kiểm tra

1. Availability khác correlation thế nào?
2. Ablation vì sao giữ seed/model?
3. Khi nào bỏ feature dù metric tăng?

## Kết quả hướng tới

ablation report; kèm config, command, metric, runtime và một failure/limitation.

## Core vs stretch

- **Core:** hoàn thành mini profile, test và kết quả cốt lõi.
- **Stretch:** thử đúng một cải tiến có giả thuyết; không hyperparameter sweep.

## Lỗi thường gặp

- Dùng future/target-proxy feature.
- Đổi feature lẫn hyperparameter cùng lúc.

## Nguồn

Xem `docs/sources.yml`; ưu tiên textbook và tài liệu chính thức được ghi trong lab.
