# Tuần 09 - Tree ensembles

## Mục tiêu tuần

So sánh tree, random forest và boosting có giới hạn.

## Vì sao tuần này quan trọng

Tree ensembles cho bạn lựa chọn mạnh với dữ liệu bảng, nhưng mục tiêu vẫn là so sánh công bằng chứ không săn model thắng bằng mọi giá.

**Ví dụ gần gũi:** Random forest giảm dao động bằng nhiều cây; boosting để cây sau tập trung sửa lỗi cây trước.

## Kiến thức cốt lõi

- Tree chia feature để giảm impurity; depth/leaves lớn dễ học nhiễu.
- Random forest bagging tree trên bootstrap/feature subset để giảm variance.
- Gradient boosting thêm learner tuần tự để sửa lỗi; learning_rate tương tác số estimator.
- Giới hạn depth/leaves hoặc thêm regularization giúp model bớt học thuộc nhiễu; kiểm bằng khoảng cách train-validation, không chỉ train score.
- So candidate bằng cùng split, pipeline, metric và runtime budget.

## Từ khóa tuần này

**Thuật ngữ mới hoặc trọng tâm:** `hyperparameter`, `ensemble`, `bagging / boosting`

**Ôn lại:** `baseline`, `validation set`, `metric`, `overfitting`

**Áp dụng:** Giữ cố định dataset, `validation set`, `metric` và budget; so một `ensemble` dùng `bagging / boosting`, chỉ đổi một `hyperparameter`, rồi kiểm mức cải thiện so với `baseline` và dấu hiệu `overfitting`.

## Giải thích khái niệm

### Hyperparameter và ensemble

**Cách hình dung:** `hyperparameter`: Cấu hình do người làm chọn, không phải parameter model tự học. Ví dụ gồm tree depth, regularization strength và số lượng tree. `ensemble`: Model kết hợp nhiều model con để tạo dự đoán chung. Prediction của các model thành viên được gộp bằng voting, averaging hoặc quy tắc khác.

**Vì sao quan trọng:** Hyperparameter điều khiển cách tạo learner; ensemble kết hợp nhiều learner, nên cả hai phải được chọn mà không nhìn test set.

**Ví dụ xuyên suốt:** `hyperparameter`: Số cây và độ sâu tối đa của random forest. `ensemble`: Random forest lấy kết quả từ nhiều decision tree.

**Dễ nhầm với:** Hyperparameter được chọn; parameter được học từ training data. Ensemble là model kết hợp; bagging và boosting là cách xây nó.

**Tự kiểm tra:** Evidence nào phải dùng để chọn `hyperparameter` trước khi kết hợp model thành `ensemble`?

### So sánh bagging với boosting

**Cách hình dung:** `bagging / boosting`: Bagging học nhiều model tương đối độc lập; boosting học tuần tự để sửa lỗi trước. Bagging chủ yếu giảm độ bất ổn; boosting khiến model sau tập trung vào lỗi trước.

**Vì sao quan trọng:** Bagging chủ yếu giảm variance bằng các learner song song; boosting tạo learner tuần tự để sửa lỗi trước đó.

**Ví dụ xuyên suốt:** `bagging / boosting`: Random forest dùng bagging, gradient boosting dùng boosting.

**Dễ nhầm với:** Bagging và boosting là hai chiến lược ensemble khác nhau, không phải tên thay thế nhau.

**Tự kiểm tra:** Vì sao `bagging / boosting` là hai cách kết hợp learner khác nhau?

## Kết nối kiến thức cũ

`baseline`, `validation set` và `metric` vẫn là comparison contract cho mọi ensemble candidate. Khoảng cách train-validation cung cấp evidence `overfitting` trước khi chấp nhận thay đổi hyperparameter.

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


1. Train logistic, random forest, gradient boosting trên một split.
2. So ROC-AUC, F1, runtime, saved-model size.
3. Đổi max_depth đúng một lần và giải thích bias/variance.

## Lab

**lab-08:** Ba candidate, cùng split và metric. Môi trường chính: `local`.

## Dấu hiệu bạn đã hiểu

Bạn so ba candidate trên cùng harness, nêu được đổi chác giữa metric, runtime và saved-model size.

## Tự kiểm tra

1. Bagging khác boosting thế nào?
2. Tree cần preprocessing gì?
3. Depth tác động train/validation ra sao?

## Kết quả hướng tới

model comparison; lưu kèm lệnh đã chạy, cấu hình, metric, thời gian chạy và một điều còn hạn chế.

## Core vs stretch

- **Cốt lõi:** So logistic, random forest và boosting theo cùng harness và runtime budget.
- **Mở rộng:** Đổi đúng một depth/leaf constraint, liên hệ khoảng cách train-validation với regularization.

## Lỗi thường gặp

- Hyperparameter sweep lớn.
- Mỗi model dùng split khác.

## Khi mắc kẹt

Khóa split, seed và metric. Chỉ đổi một tham số như `max_depth`; đừng mở sweep khi chưa hiểu kết quả đầu tiên.

## Nguồn

Nguồn nên đọc: scikit-learn ensemble guide về random forests và gradient boosting.
