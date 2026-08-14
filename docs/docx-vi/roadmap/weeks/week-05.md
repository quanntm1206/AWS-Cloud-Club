# Tuần 05 - Supervised learning và baseline

## Mục tiêu tuần

Đặt baseline; split train/validation/test đúng.

## Vì sao tuần này quan trọng

Baseline tạo một vạch xuất phát trung thực. Nếu model chưa vượt cách đoán đơn giản, tăng độ phức tạp chưa mang lại giá trị.

**Ví dụ gần gũi:** Dataset có 90% khách không churn sẽ cho dummy accuracy 90%, nhưng gần như vô dụng khi cần tìm người sắp rời đi.

## Kiến thức cốt lõi

- Classification dự đoán class/probability; regression dự đoán giá trị liên tục.
- Dummy baseline đo mức tối thiểu; logistic regression tạo linear logit rồi sigmoid.
- Train để fit, validation để chọn, test chỉ dùng khi quyết định đã khóa.
- Dùng stratified split cho class; dùng group/time split khi mẫu liên quan hoặc có thời gian.

## Từ khóa tuần này

**Thuật ngữ mới hoặc trọng tâm:** `data split`, `training set`, `validation set`, `test set`, `baseline`, `model validation`

**Ôn lại:** `dataset`, `sample`, `feature`, `label / target`, `prediction`

**Áp dụng:** Tạo `data split` không có `sample` trùng giữa `training set`, `validation set` và `test set`; fit `baseline`, thực hiện `model validation`, rồi so từng `prediction` với `label / target`.

## Giải thích khái niệm

### Chia dữ liệu để training

**Cách hình dung:** `data split`: Cách chia dataset thành các phần có vai trò khác nhau và không chồng lặp. Ba vai trò thường gặp là training, validation và test, không có sample dùng chung. `training set`: Phần dữ liệu dùng để model học parameter. Validation và test sample không được ảnh hưởng bất kỳ điều gì học từ tập này.

**Vì sao quan trọng:** Data split gán vai trò trước modeling; chỉ training set được dùng để fit parameter.

**Ví dụ xuyên suốt:** `data split`: Chia 70% train, 15% validation, 15% test. `training set`: Logistic regression gọi fit chỉ với training set.

**Dễ nhầm với:** Data split tạo tập con; cross-validation luân phiên nhiều fold qua các vai trò. Training set dạy model; validation set chỉ hướng dẫn lựa chọn.

**Tự kiểm tra:** Vì sao chỉ `training set` được phép dạy parameter cho model?

### Validation và test chưa đụng tới

**Cách hình dung:** `validation set`: Phần dữ liệu dùng chọn model, threshold hoặc hyperparameter; không dùng fit parameter. Có thể xem nó nhiều lần để ra quyết định, nhưng label của nó không được đi vào fit. `test set`: Phần dữ liệu chỉ mở sau khi đã khóa quyết định để ước lượng kết quả cuối. Không được dùng nó để fit preprocessing, chọn model hoặc tune threshold.

**Vì sao quan trọng:** Validation set hỗ trợ lựa chọn; test set phải đóng cho đến khi các lựa chọn đã khóa.

**Ví dụ xuyên suốt:** `validation set`: Chọn threshold có recall đạt yêu cầu trên validation set. `test set`: Chạy test một lần sau khi chọn logistic regression.

**Dễ nhầm với:** Validation set hướng dẫn lựa chọn; test set kiểm kết quả đã khóa. Test set không phải validation set bổ sung để tuning lặp lại.

**Tự kiểm tra:** Quyết định nào dùng `validation set`, và khi nào mới được mở `test set`?

### Baseline và model validation

**Cách hình dung:** `baseline`: Mốc đơn giản để biết model phức tạp có thực sự cải thiện hay không. Baseline có thể là quy tắc đơn giản, dummy model hoặc learned model hợp lý nhỏ nhất. `model validation`: Quá trình kiểm model trên dữ liệu chưa dùng để fit nhằm đánh giá và chọn quyết định. Quy trình gồm so sánh candidate và threshold trên validation data trước final test.

**Vì sao quan trọng:** Baseline đặt mức hữu ích tối thiểu; model validation kiểm tra cải tiến có giữ được trên dữ liệu chưa thấy hay không.

**Ví dụ xuyên suốt:** `baseline`: Dummy classifier luôn đoán class phổ biến. `model validation`: So sánh F1 trên validation set trước khi mở test set.

**Dễ nhầm với:** Baseline là mốc so sánh, không nhất thiết là model cuối. Validation hướng dẫn lựa chọn; test chỉ ước lượng hệ thống cuối một lần.

**Tự kiểm tra:** Evidence nào cho thấy model vượt `baseline` dưới quy trình `model validation` trung thực?

## Kết nối kiến thức cũ

`dataset` và các dòng `sample` giờ được gán vai trò cố định trước mọi lựa chọn model. Split index đã lưu chứng minh mỗi `feature` và `label / target` chỉ vào một split, còn evidence `prediction` giữ được tính độc lập.

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


1. So dummy và logistic trên đúng cùng split/workflow/quality measure.
2. Kiểm class balance và ID không trùng giữa tập.
3. Viết quality measure gate model phải vượt baseline.

## Lab

**lab-04:** Dummy và logistic classifier. Môi trường chính: `local`.

## Dấu hiệu bạn đã hiểu

Bạn dùng cùng split và quality measure để so dummy với logistic regression; test set vẫn chưa tham gia chọn model.

## Tự kiểm tra

1. Dummy accuracy cao khi nào?
2. Logistic tuyến tính ở không gian nào?
3. Random split gây leakage khi nào?

## Kết quả hướng tới

baseline report; lưu kèm lệnh đã chạy, cấu hình, quality measure, thời gian chạy và một điều còn hạn chế.

## Core vs stretch

- **Cốt lõi:** So dummy với logistic trên cùng split, quality measure và seed; giữ test chưa tham gia lựa chọn.
- **Mở rộng:** Thử group/time split trên một tình huống giả định và nêu vì sao random split có thể sai.

## Lỗi thường gặp

- So model trên split khác nhau.
- Bỏ baseline để chạy model phức tạp.

## Khi mắc kẹt

Kiểm phân bố nhãn, ID trùng và thời gian trước. Khi nghi ngờ split, vẽ sơ đồ các tập thay vì đổi model.

## Nguồn

Nguồn nên đọc: scikit-learn documentation về model selection, train-test split và DummyClassifier.
