# Tuần 10 - Feature engineering và ablation

## Mục tiêu tuần

Feature engineering có giả thuyết; ablation một biến.

## Vì sao tuần này quan trọng

Feature engineering biến hiểu biết về bài toán thành tín hiệu model dùng được. Ablation giúp kiểm xem feature mới thật sự có ích hay chỉ trùng với nhiễu.

**Ví dụ gần gũi:** Tỉ lệ chi tiêu trên thời gian gắn bó có thể hữu ích, nhưng phải xử lý mẫu số 0 và chỉ dùng dữ liệu có tại prediction time.

## Kiến thức cốt lõi

- Feature phải tồn tại tại prediction time, ổn định, tái tạo được và có ý nghĩa.
- Ratio/log/interaction cần hypothesis; xử lý zero, missing và range.
- Ablation thay đúng một feature group trong cùng harness.
- Metric delta nhỏ hơn CV variability chưa chứng minh feature có ích.

## Từ khóa tuần này

**Thuật ngữ mới hoặc trọng tâm:** `feature engineering`, `ablation`

**Ôn lại:** `feature`, `baseline`, `validation set`, `hyperparameter`

**Áp dụng:** Viết giả thuyết `feature engineering`, chạy `ablation` thêm/bỏ một feature; khóa baseline, validation set, hyperparameter và data split để metric delta có nghĩa.

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


1. Viết feature hypothesis và availability time.
2. So all-features với without-monthly-charge.
3. Ghi metric/runtime delta và keep/drop decision.

## Lab

**lab-09:** Feature ablation log. Môi trường chính: `local`.

## Dấu hiệu bạn đã hiểu

Mỗi feature có giả thuyết và thời điểm sẵn có; quyết định giữ/bỏ dựa trên cùng harness cùng variability.

## Tự kiểm tra

1. Availability khác correlation thế nào?
2. Ablation vì sao giữ seed/model?
3. Khi nào bỏ feature dù metric tăng?

## Kết quả hướng tới

ablation report; lưu kèm lệnh đã chạy, cấu hình, metric, thời gian chạy và một điều còn hạn chế.

## Core vs stretch

- **Cốt lõi:** Chạy một ablation có giả thuyết, availability time rõ và test chưa bị chạm.
- **Mở rộng:** Thử một feature ratio an toàn với zero/missing rồi đo cả metric lẫn runtime.

## Lỗi thường gặp

- Dùng future/target-proxy feature.
- Đổi feature lẫn hyperparameter cùng lúc.

## Khi mắc kẹt

Viết feature bằng lời trước code. Nếu không nói được nó có sẵn khi nào, tạm loại khỏi model.

## Nguồn

Nguồn nên đọc: phần feature engineering/model inspection trong tài liệu chính thức ở `docs/sources.yml`.
