# Tuần 07 - Metrics, imbalance và threshold

## Mục tiêu tuần

Chọn metric và threshold theo chi phí lỗi.

## Vì sao tuần này quan trọng

Metric phải phản ánh loại sai lầm bạn thật sự quan tâm. Threshold là quyết định vận hành, không phải con số mặc định 0.5.

**Ví dụ gần gũi:** Trong sàng lọc rủi ro, bỏ sót một ca có thể đắt hơn cảnh báo nhầm; recall vì thế có thể quan trọng hơn accuracy.

## Kiến thức cốt lõi

- Confusion matrix tách TP/FP/FN/TN; precision đo độ đúng của positive prediction, recall đo positive thật tìm được.
- F1 cân bằng precision/recall nhưng không thay thế cost của FP/FN.
- ROC-AUC đo ranking; PR-AUC thường rõ hơn khi positive hiếm.
- Chọn threshold trên validation, khóa lại, rồi đánh giá test; 0.5 không mặc định tối ưu.
- Log loss phạt dự đoán tự tin nhưng sai; calibration hỏi liệu nhóm được dự đoán khoảng 0.7 có positive gần 70% hay không.

## Từ khóa tuần này

**Thuật ngữ mới hoặc trọng tâm:** `metric`, `precision / recall / F1`, `threshold`, `class imbalance`

**Ôn lại:** `validation set`, `model validation`, `baseline`

**Áp dụng:** Dùng `validation set` cho `model validation`: chọn metric precision / recall / F1 và threshold theo class imbalance, so với baseline; giữ test set đóng đến cuối.

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


1. Lập bảng metric và business cost theo threshold.
2. Chọn threshold thỏa recall tối thiểu bằng validation.
3. Áp threshold đã khóa lên test.

## Lab

**lab-06:** Imbalance, PR/ROC, confusion matrix. Môi trường chính: `local`.

## Dấu hiệu bạn đã hiểu

Bạn chọn threshold trên validation theo chi phí FP/FN, khóa nó rồi mới đánh giá test; giải thích được trade-off.

## Tự kiểm tra

1. Tăng recall ảnh hưởng precision thế nào?
2. AUC cao có đảm bảo calibration?
3. Vì sao không chọn threshold trên test?

## Kết quả hướng tới

metric decision memo; lưu kèm lệnh đã chạy, cấu hình, metric, thời gian chạy và một điều còn hạn chế.

## Core vs stretch

- **Cốt lõi:** Chọn threshold bằng validation theo cost rule; khóa trước khi đánh giá test.
- **Mở rộng:** Vẽ reliability/calibration curve nhỏ hoặc so log loss ở hai model có cùng accuracy.

## Lỗi thường gặp

- Chỉ báo accuracy trên imbalance.
- Sửa threshold sau khi xem test.

## Khi mắc kẹt

Lập confusion matrix bằng số đếm trước. Nếu PR-AUC và ROC-AUC gây rối, quay lại hỏi positive class có hiếm không.

## Nguồn

Nguồn nên đọc: scikit-learn model evaluation về precision-recall, ROC, log loss và calibration.
