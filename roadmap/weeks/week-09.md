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


1. Train logistic, random forest, gradient boosting trên một split.
2. So ROC-AUC, F1, runtime, artifact size.
3. Đổi max_depth đúng một lần và giải thích bias/variance.

## Lab

**lab-08:** Ba candidate, cùng split và metric. Môi trường chính: `local`.

## Dấu hiệu bạn đã hiểu

Bạn so ba candidate trên cùng harness, nêu được đổi chác giữa metric, runtime và artifact size.

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
