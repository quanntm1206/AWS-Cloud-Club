# Tuần 06 - Preprocessing và chống leakage

## Mục tiêu tuần

Xử lý missing/category bằng pipeline không leakage.

## Kiến thức cốt lõi

- Imputer, scaler, encoder đều học trạng thái và chỉ được fit trên train.
- ColumnTransformer tách numeric/categorical; Pipeline giữ preprocess và model cùng lifecycle.
- OneHotEncoder cần xử lý category chưa thấy để inference không vỡ.
- Schema validation bắt thiếu cột, sai dtype/range và target lẫn vào input trước transform.

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

1. Tạo pipeline impute-scale và impute-one-hot.
2. Inject unseen category vào validation.
3. Test scaler mean không lấy test data.

## Lab

**lab-05:** Leakage-safe preprocessing. Môi trường chính: `local`.

## Tự kiểm tra

1. Vì sao fit_transform trước split là leakage?
2. handle_unknown có trade-off gì?
3. Pipeline giảm train/serve skew thế nào?

## Kết quả hướng tới

pipeline + schema; kèm config, command, metric, runtime và một failure/limitation.

## Core vs stretch

- **Core:** hoàn thành mini profile, test và kết quả cốt lõi.
- **Stretch:** thử đúng một cải tiến có giả thuyết; không hyperparameter sweep.

## Lỗi thường gặp

- Lưu model nhưng quên transformer.
- Impute theo test distribution.

## Nguồn

Xem `docs/sources.yml`; ưu tiên textbook và tài liệu chính thức được ghi trong lab.
