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

**Áp dụng:** Tạo `data split` trước, chỉ fit từng bước `preprocessing` và `transform` trên `training set`, rồi ghép thành `pipeline`; dùng `schema` và split lineage để loại trừ `data leakage` sang validation hoặc test data.

## Giải thích khái niệm

### Học một transformation

**Cách hình dung:** `preprocessing`: Các bước chuẩn bị dữ liệu trước model như điền thiếu, scale hoặc encode. Có bước cố định, có bước học median, danh sách category hoặc scaling statistic. `transform`: Phép biến đổi input; một số transform phải học trạng thái chỉ từ training set. Sau đó phải dùng lại cùng fitted transform cho validation, test và inference data.

**Vì sao quan trọng:** Mọi preprocessing rule có học statistic chỉ được học từ training data.

**Ví dụ xuyên suốt:** `preprocessing`: Điền median rồi one-hot encode cột hợp đồng. `transform`: StandardScaler học mean và std từ train rồi áp sang validation.

**Dễ nhầm với:** Preprocessing có thể học trạng thái nên không phải lúc nào cũng là cleanup cố định vô hại. transform áp quy tắc; fit học trạng thái mà quy tắc cần.

**Tự kiểm tra:** `preprocessing` có thể học state nào, và cùng `transform` phải được áp dụng ra sao cho dữ liệu sau?

### Thứ tự pipeline và leakage

**Cách hình dung:** `pipeline`: Chuỗi preprocessing và model chạy theo thứ tự cố định để giảm lỗi và leakage. Khi fit pipeline, mỗi bước preprocessing cần học chỉ được thấy training data. `data leakage`: Thông tin không hợp lệ từ validation, test hoặc tương lai lọt vào training. Leakage có thể đến từ future data, feature suy ra từ target, khách trùng hoặc preprocessing trước split.

**Vì sao quan trọng:** Pipeline giữ đúng thứ tự operation; boundary đó ngăn thông tin từ validation hoặc test data bị leakage.

**Ví dụ xuyên suốt:** `pipeline`: ColumnTransformer nối với logistic regression trong một Pipeline. `data leakage`: Fit scaler trên toàn dataset trước split làm rò thông tin test.

**Dễ nhầm với:** Pipeline là container theo thứ tự; preprocessing chỉ là phần chuẩn bị dữ liệu. Leakage có thể xảy ra mà không có row trùng, như fit scaler trước split.

**Tự kiểm tra:** `data leakage` có thể lọt vào đâu khi `pipeline` được fit sai thứ tự?

### Fit học state

**Cách hình dung:** `fit`: Bước học parameter hoặc trạng thái transform từ training data. Với scaler, fit học statistic; với model, fit học predictive parameter.

**Vì sao quan trọng:** Fit làm thay đổi state của object, nên phải ghi rõ fit cái gì và trên những dòng nào để bảo đảm reproducibility.

**Ví dụ xuyên suốt:** `fit`: Gọi pipeline.fit(X_train, y_train).

**Dễ nhầm với:** Fit học state; transform áp dụng transformation cố định hoặc đã học.

**Tự kiểm tra:** Những dòng nào được phép ảnh hưởng state trong lúc `fit`?

## Kết nối kiến thức cũ

`data split`, `training set`, `validation set`, `test set` và `schema` xác định nơi preprocessing được phép học state. Metadata của fitted state và các dòng held-out không đổi cho thấy pipeline giữ đúng boundary.

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
