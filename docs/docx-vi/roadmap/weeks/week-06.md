# Tuần 06 - Preprocessing và chống leakage

## Mục tiêu tuần

Xử lý missing/category bằng pipeline không leakage.

## Vì sao tuần này quan trọng

Preprocessing cũng học từ dữ liệu. Đặt nó trong pipeline giữ ranh giới train/validation sạch và tránh model chạy khác lúc tạo dự đoán mới.

**Ví dụ gần gũi:** Giá trị trung bình dùng để điền missing phải đến từ train, không được nhìn trước khách hàng trong test.

## Kiến thức cốt lõi

- Imputer, scaler, encoder đều học trạng thái và chỉ được fit trên train.
- ColumnTransformer tách numeric/categorical; Pipeline giữ preprocess và model cùng lifecycle.
- OneHotEncoder cần xử lý category chưa thấy để dự đoán input mới không vỡ.
- Schema validation bắt thiếu cột, sai dtype/range và target lẫn vào input trước transform.

## Từ khóa tuần này

**Thuật ngữ mới hoặc trọng tâm:** `preprocessing`, `transform`, `pipeline`, `data leakage`, `fit`

**Ôn lại:** `data split`, `training set`, `validation set`, `test set`, `schema`

**Áp dụng:** Chia bằng `data split` trước, fit từng bước `preprocessing`/`transform` chỉ trên `training set`, ghép thành `pipeline`; dùng schema để chứng minh không có `data leakage` sang validation set/test set.

## Lịch 8-10 giờ

| Hoạt động | Giờ |
|---|---:|
| Đọc và ghi chú | 2 |
| Guided practice | 2 |
| Lab | 3 |
| Assessment/failure review | 1 |
| Learning log và tự đánh giá | 1 |
| Review/hoàn thiện | 0 |

## Guided practice


1. Tạo pipeline impute-scale và impute-one-hot.
2. Inject unseen category vào validation.
3. Test scaler mean không lấy test data.

## Lab

**lab-05:** Leakage-safe preprocessing. Môi trường chính: `local`.

## Dấu hiệu bạn đã hiểu

Bạn xử lý được missing và category chưa từng thấy, đồng thời chứng minh scaler không học từ test.

## Tự kiểm tra

1. Vì sao fit_transform trước split là leakage?
2. handle_unknown có trade-off gì?
3. Pipeline giảm train/serve skew thế nào?

## Kết quả hướng tới

pipeline + schema; lưu kèm lệnh đã chạy, cấu hình, metric, thời gian chạy và một điều còn hạn chế.

## Core vs stretch

- **Cốt lõi:** Dựng pipeline impute/scale/encode chỉ fit train; kiểm category chưa thấy.
- **Mở rộng:** Thêm một schema failure như thiếu cột hoặc sai dtype và biến nó thành test.

## Lỗi thường gặp

- Lưu model nhưng quên transformer.
- Impute theo test distribution.

## Khi mắc kẹt

Tạo một validation row có category lạ. Nếu pipeline vỡ, sửa encoder và thêm kiểm tra trước khi train lại.

## Nguồn

Nguồn nên đọc: scikit-learn Pipeline, ColumnTransformer, SimpleImputer và OneHotEncoder.
