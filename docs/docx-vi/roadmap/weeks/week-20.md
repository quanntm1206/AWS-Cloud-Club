# Tuần 20 - CV evaluation và failure analysis

## Mục tiêu tuần

Đánh giá per-class và phân nhóm failure.

## Vì sao tuần này quan trọng

Metric tổng hợp không cho biết model sai ở đâu. Failure analysis giúp bạn quyết định nên sửa dữ liệu, nhãn, transform hay model.

**Ví dụ gần gũi:** Một class ít mẫu có thể bị bỏ qua trong weighted F1 nhưng hiện rõ trong macro F1 và confusion matrix theo hàng.

## Kiến thức cốt lõi

- Overall accuracy che class yếu; báo per-class precision/recall/F1/support và macro/weighted aggregate.
- Confusion matrix normalized theo true class giúp so recall giữa class khác support.
- Failure record có sample ID, truth, prediction, confidence, error type; không publish sensitive data.
- Review theo sampling rule rồi phân nhóm data, label, ambiguity, transform, model hoặc shift.
- Model card gắn metric với dataset/split/config và cấm dùng fallback data để kết luận quality.

## Từ khóa tuần này

**Thuật ngữ mới hoặc trọng tâm:** `confusion matrix`, `support`

**Ôn lại:** `metric`, `validation set`, `error analysis`, `failure taxonomy`

**Áp dụng:** Tạo `confusion matrix` kèm precision, recall, F1 và `support`; chạy `error analysis` trên validation prediction thật, gán mỗi failure vào `failure taxonomy`, và không dùng FakeData cho `model validation`.

## Giải thích khái niệm

### Số đếm phía sau metric

**Cách hình dung:** `confusion matrix`: Bảng đếm truth và prediction để thấy model nhầm class nào với class nào. Các ô tách riêng true positive, false positive, true negative và false negative.

**Vì sao quan trọng:** Confusion matrix cho thấy đúng loại nhầm lẫn giữa các class mà một aggregate score che đi.

**Ví dụ xuyên suốt:** `confusion matrix`: Hàng churn=1 cho biết bao nhiêu mẫu bị đoán thành 0.

**Dễ nhầm với:** Confusion matrix chứa số đếm; precision, recall và F1 tóm tắt các số đếm đó.

**Tự kiểm tra:** Error count nào trong `confusion matrix` giải thích class-level metric?

### Support cho biết mẫu số

**Cách hình dung:** `support`: Số sample thật của một class hoặc slice dùng để đọc metric có ngữ cảnh. Support nhỏ làm một metric có vẻ hoàn hảo trở nên thiếu chắc chắn.

**Vì sao quan trọng:** Support cung cấp mẫu số để đánh giá một class hoặc slice score dựa trên lượng evidence phía sau.

**Ví dụ xuyên suốt:** `support`: Recall 100% trên support=2 chưa đủ kết luận mạnh.

**Dễ nhầm với:** Support là số đếm, không phải score chất lượng.

**Tự kiểm tra:** `support` có đủ lớn để tin score của class hoặc slice này không?

## Kết nối kiến thức cũ

`metric` trên `validation set` giờ được tách thành count và support theo class. `error analysis` cùng `failure taxonomy` giải thích sample thật nào tạo ra kết quả yếu của từng class.

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


1. Tạo per-class table và confusion matrix.
2. Xuất tối đa 20 failure records, ưu tiên confident-wrong.
3. Viết limitation và next experiment từ taxonomy.

## Lab

**lab-19:** Confusion matrix và tối đa 20 failure examples; nếu ít hơn thì xuất toàn bộ và ghi limitation. Môi trường chính: `local, colab, kaggle`.

## Dấu hiệu bạn đã hiểu

Bạn tạo bảng per-class, review lỗi theo quy tắc, viết limitation và một thí nghiệm tiếp theo có thể bác bỏ giả thuyết.

## Tự kiểm tra

1. Macro khác weighted F1?
2. Normalize matrix theo hàng trả lời gì?
3. Sampling chỉ theo confidence bias gì?

## Kết quả hướng tới

mốc năng lực 5 + model card; lưu kèm lệnh đã chạy, cấu hình, metric, thời gian chạy và một điều còn hạn chế.

## Core vs stretch

- **Cốt lõi:** Tạo per-class metrics, confusion matrix, failure taxonomy và model card từ run thật.
- **Mở rộng:** Thử một sampling rule khác cho failure review; không công bố ảnh không có quyền chia sẻ.

## Lỗi thường gặp

- Chỉ xem aggregate.
- Đưa data không có quyền chia sẻ vào artifact công khai.

## Khi mắc kẹt

Bắt đầu với 5-10 lỗi. Nếu ảnh nhạy cảm hoặc không có quyền chia sẻ, chỉ lưu ID và mô tả đã ẩn danh.

## Nguồn

Nguồn nên đọc: scikit-learn classification metrics/confusion matrix và model-card guidance trong `docs/sources.yml`.
