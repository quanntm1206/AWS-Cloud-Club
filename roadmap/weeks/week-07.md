# Tuần 07 - Metrics, imbalance và threshold

## Mục tiêu tuần

Chọn metric và threshold theo chi phí lỗi.

## Kiến thức cốt lõi

- Confusion matrix tách TP/FP/FN/TN; precision đo độ đúng của positive prediction, recall đo positive thật tìm được.
- F1 cân bằng precision/recall nhưng không thay thế cost của FP/FN.
- ROC-AUC đo ranking; PR-AUC thường rõ hơn khi positive hiếm.
- Chọn threshold trên validation, khóa lại, rồi đánh giá test; 0.5 không mặc định tối ưu.

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

1. Lập bảng metric và business cost theo threshold.
2. Chọn threshold thỏa recall tối thiểu bằng validation.
3. Áp threshold đã khóa lên test.

## Lab

**lab-06:** Imbalance, PR/ROC, confusion matrix. Môi trường chính: `local`.

## Tự kiểm tra

1. Tăng recall ảnh hưởng precision thế nào?
2. AUC cao có đảm bảo calibration?
3. Vì sao không chọn threshold trên test?

## Kết quả hướng tới

metric decision memo; kèm config, command, metric, runtime và một failure/limitation.

## Core vs stretch

- **Core:** hoàn thành mini profile, test và kết quả cốt lõi.
- **Stretch:** thử đúng một cải tiến có giả thuyết; không hyperparameter sweep.

## Lỗi thường gặp

- Chỉ báo accuracy trên imbalance.
- Sửa threshold sau khi xem test.

## Nguồn

Xem `docs/sources.yml`; ưu tiên textbook và tài liệu chính thức được ghi trong lab.
