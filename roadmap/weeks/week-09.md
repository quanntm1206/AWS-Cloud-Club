# Tuần 09 - Tree ensembles

## Mục tiêu tuần

So sánh tree, random forest và boosting có giới hạn.

## Kiến thức cốt lõi

- Tree chia feature để giảm impurity; depth/leaves lớn dễ học nhiễu.
- Random forest bagging tree trên bootstrap/feature subset để giảm variance.
- Gradient boosting thêm learner tuần tự để sửa lỗi; learning_rate tương tác số estimator.
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

## Tự kiểm tra

1. Bagging khác boosting thế nào?
2. Tree cần preprocessing gì?
3. Depth tác động train/validation ra sao?

## Kết quả hướng tới

model comparison; kèm config, command, metric, runtime và một failure/limitation.

## Core vs stretch

- **Core:** hoàn thành mini profile, test và kết quả cốt lõi.
- **Stretch:** thử đúng một cải tiến có giả thuyết; không hyperparameter sweep.

## Lỗi thường gặp

- Hyperparameter sweep lớn.
- Mỗi model dùng split khác.

## Nguồn

Xem `docs/sources.yml`; ưu tiên textbook và tài liệu chính thức được ghi trong lab.
