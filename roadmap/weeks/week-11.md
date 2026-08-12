# Tuần 11 - Interpretability và error analysis

## Mục tiêu tuần

Giải thích model thận trọng; phân tích subgroup/failure.

## Kiến thức cốt lõi

- Global importance mô tả trung bình; local explanation mô tả một prediction; không cái nào chứng minh causality.
- Permutation importance bị ảnh hưởng khi feature tương quan.
- Slice metric luôn kèm support để tránh kết luận từ nhóm quá nhỏ.
- Failure taxonomy nhóm lỗi thành data quality, boundary, missing signal, label noise hoặc shift.

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

1. Lập FP/FN counts theo region/contract.
2. Review tối đa 20 lỗi theo sampling rule.
3. Đề xuất một data fix và một model fix có phép kiểm.

## Lab

**lab-10:** Slice metrics và failure taxonomy. Môi trường chính: `local`.

## Tự kiểm tra

1. Importance khác causality?
2. Support nhỏ gây rủi ro gì?
3. Error analysis cần dẫn tới action nào?

## Kết quả hướng tới

error analysis; kèm config, command, metric, runtime và một failure/limitation.

## Core vs stretch

- **Core:** hoàn thành mini profile, test và kết quả cốt lõi.
- **Stretch:** thử đúng một cải tiến có giả thuyết; không hyperparameter sweep.

## Lỗi thường gặp

- Chọn lỗi thuận mắt.
- Dùng explanation hợp thức hóa lỗi.

## Nguồn

Xem `docs/sources.yml`; ưu tiên textbook và tài liệu chính thức được ghi trong lab.
