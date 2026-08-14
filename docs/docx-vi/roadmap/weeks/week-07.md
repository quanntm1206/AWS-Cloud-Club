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

**Áp dụng:** Dùng `validation set` cho `model validation`; chọn `metric` trong `precision / recall / F1`, đặt `threshold` theo `class imbalance`, so với `baseline`, và giữ test set đóng.

## Giải thích khái niệm

### Metric phục vụ quyết định

**Cách hình dung:** `metric`: Con số đo một khía cạnh chất lượng; phải chọn theo mục tiêu và chi phí lỗi. Không metric nào mô tả mọi mặt chất lượng nên phải nêu rõ ý nghĩa của metric đã chọn. `precision / recall / F1`: Precision chú trọng dự đoán dương đúng, recall chú trọng tìm đủ mẫu dương, F1 cân bằng hai phía. Cả ba đều tính từ confusion-matrix count nhưng trả lời những câu hỏi khác nhau.

**Vì sao quan trọng:** Metric phải phản ánh cost của lỗi; precision, recall và F1 cho thấy các trade-off mà accuracy che đi.

**Ví dụ xuyên suốt:** `metric`: Recall đo tỷ lệ khách churn được tìm thấy. `precision / recall / F1`: Bài churn ưu tiên recall nhưng vẫn theo dõi precision.

**Dễ nhầm với:** Metric là thước đo; loss là mục tiêu được tối ưu khi training. Precision hỏi prediction dương có đúng không; recall hỏi đã tìm được bao nhiêu mẫu dương.

**Tự kiểm tra:** Cost của loại lỗi nào khiến recall phù hợp hơn precision cho `metric` đã chọn?

### Threshold đổi trade-off

**Cách hình dung:** `threshold`: Ngưỡng chuyển score hoặc xác suất thành nhãn quyết định. Giảm threshold thường tìm được nhiều positive case hơn nhưng cũng tăng false alarm. `class imbalance`: Tình trạng số mẫu giữa các class chênh lệch lớn. Minority class có thể ảnh hưởng quá ít tới accuracy hoặc quá trình model học.

**Vì sao quan trọng:** Threshold biến score thành action; class imbalance làm thay đổi lượng evidence mỗi class đóng góp.

**Ví dụ xuyên suốt:** `threshold`: Xác suất từ 0.35 trở lên được gắn nhãn churn. `class imbalance`: Chỉ 8% khách churn nên accuracy dễ gây hiểu nhầm.

**Dễ nhầm với:** Threshold đổi quyết định, không đổi predicted probability gốc. Class imbalance mô tả số lượng label, không tự nói lên chi phí kinh doanh.

**Tự kiểm tra:** `Class imbalance` làm quyết định thay đổi ra sao khi di chuyển `threshold`?

## Kết nối kiến thức cũ

`validation set` và quy trình `model validation` giờ hỗ trợ metric cùng threshold theo quyết định thực tế. So sánh với `baseline` cho biết precision-recall trade-off đã chọn có thật sự cải thiện hay không.

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
