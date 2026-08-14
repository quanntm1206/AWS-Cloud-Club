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

**Áp dụng:** Viết hypothesis `feature engineering` và chạy `ablation` chỉ thêm hoặc bỏ một feature; giữ cố định `baseline`, `validation set`, `hyperparameter` và data split để metric delta chỉ có một cách giải thích.

## Giải thích khái niệm

### Feature là hypothesis

**Cách hình dung:** `feature engineering`: Tạo hoặc biến đổi feature dựa trên hiểu biết bài toán và thời điểm dự đoán. Feature tốt mã hóa cấu trúc hữu ích mà không dùng future information hoặc target information.

**Vì sao quan trọng:** Feature phải tồn tại tại prediction time và biểu diễn hypothesis hợp lý, không phải thông tin tương lai vô tình lọt vào.

**Ví dụ xuyên suốt:** `feature engineering`: Tạo tenure_bucket từ tenure nếu dùng được lúc inference.

**Dễ nhầm với:** Feature engineering tạo input; feature selection chỉ giữ hoặc bỏ input có sẵn.

**Tự kiểm tra:** Rule `feature engineering` này có tái tạo được từ thông tin có sẵn tại prediction time không?

### Ablation là controlled test

**Cách hình dung:** `ablation`: Thí nghiệm thêm hoặc bỏ đúng một thành phần để đo tác động của nó. Mọi data, code và setting khác phải giữ nguyên để so sánh công bằng.

**Vì sao quan trọng:** Ablation cô lập giá trị của một thay đổi feature, biến trực giác thành evidence dưới cùng validation protocol.

**Ví dụ xuyên suốt:** `ablation`: Bỏ nhóm feature hành vi rồi so validation AUC.

**Dễ nhầm với:** Ablation đổi một thành phần; tuning thông thường có thể đổi nhiều cấu hình.

**Tự kiểm tra:** Một `ablation` phải cô lập đúng thay đổi nào để kết quả đáng tin?

## Kết nối kiến thức cũ

Mỗi `feature` mới phải cải thiện `baseline` đã khóa trên cùng `validation set` với cùng lựa chọn `hyperparameter`. Ablation delta là evidence cô lập đóng góp của feature đó.

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
