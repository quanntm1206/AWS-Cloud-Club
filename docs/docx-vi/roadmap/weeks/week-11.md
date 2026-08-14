# Tuần 11 - Interpretability và error analysis

## Mục tiêu tuần

Giải thích model thận trọng; phân tích subgroup/failure.

## Vì sao tuần này quan trọng

Model tốt trung bình vẫn có thể tệ với một nhóm nhỏ. Error analysis biến các lỗi riêng lẻ thành việc tiếp theo có thể kiểm chứng.

**Ví dụ gần gũi:** Accuracy chung ổn nhưng khách hợp đồng tháng có nhiều false negative; đây là tín hiệu cần xem dữ liệu hoặc threshold theo nhóm.

## Kiến thức cốt lõi

- Global importance mô tả trung bình; local explanation mô tả một prediction; không cái nào chứng minh causality.
- Permutation importance bị ảnh hưởng khi feature tương quan.
- Slice metric luôn kèm sample count để tránh kết luận từ nhóm quá nhỏ; xem chênh lệch như tín hiệu điều tra fairness, không vội kết luận nguyên nhân.
- Khi nhãn đến muộn, theo dõi schema, missing rate, prediction distribution và feature drift trước khi có quality metric.
- Failure taxonomy nhóm lỗi thành data quality, boundary, missing signal, label noise hoặc shift.

## Từ khóa tuần này

**Thuật ngữ mới hoặc trọng tâm:** `error analysis`, `slice`, `failure taxonomy`

**Ôn lại:** `metric`, `validation set`, `feature engineering`

**Áp dụng:** Chạy `error analysis` cho từng `slice` và ghi sample count; tạo `failure taxonomy` từ prediction sai, rồi nối từng category với `feature engineering` và `metric` trên `validation set`.

## Giải thích khái niệm

### Từ score đến failure slice

**Cách hình dung:** `error analysis`: Phân tích có hệ thống các dự đoán sai để tạo giả thuyết và bước kiểm tiếp. Người phân tích xem false positive và false negative theo từng example và group. `slice`: Nhóm sample có đặc điểm chung được tách ra để kiểm hành vi model. Cần so kết quả slice với kết quả tổng và luôn báo kèm support.

**Vì sao quan trọng:** Error analysis biến aggregate metric thành thông tin hành động được bằng cách tìm slice nơi failure tập trung.

**Ví dụ xuyên suốt:** `error analysis`: Xem false negative theo loại hợp đồng. `slice`: Slice khách mới có tenure dưới ba tháng.

**Dễ nhầm với:** Error analysis nghiên cứu failure thật; metric chỉ tóm tắt chúng. Slice là subgroup có ý nghĩa; data split giao vai trò training hoặc evaluation.

**Tự kiểm tra:** `slice` nào tập trung các lỗi tìm thấy trong `error analysis`?

### Đặt tên failure pattern

**Cách hình dung:** `failure taxonomy`: Cách phân nhóm lỗi theo nguyên nhân quan sát được thay vì gom mọi lỗi chung. Category hữu ích phải đủ cụ thể để đếm và nối với một hướng xử lý.

**Vì sao quan trọng:** Failure taxonomy biến triệu chứng lặp lại thành category có tên để đếm, ưu tiên và retest.

**Ví dụ xuyên suốt:** `failure taxonomy`: Gắn lỗi vào data, boundary, missing signal hoặc label noise.

**Dễ nhầm với:** Failure taxonomy đặt tên nhóm lỗi; confusion matrix chỉ nhóm lỗi theo class label.

**Tự kiểm tra:** Mọi failure quan sát được có gán vào một category hành động được trong `failure taxonomy` không?

## Kết nối kiến thức cũ

Aggregate `metric` trên `validation set` giờ dẫn tới từng failure và slice cụ thể. Nối mỗi category về `feature engineering` biến lỗi đã thấy thành thay đổi có thể kiểm chứng.

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


1. Lập FP/FN counts theo region/contract.
2. Review tối đa 20 lỗi theo sampling rule.
3. Đề xuất một data fix và một model fix có phép kiểm.

## Lab

**lab-10:** Slice metrics và failure taxonomy. Môi trường chính: `local`.

## Dấu hiệu bạn đã hiểu

Bạn báo slice metric kèm sample count, phân nhóm lỗi và đề xuất một data fix cùng một model fix có phép kiểm.

## Tự kiểm tra

1. Importance khác causality?
2. Sample Count nhỏ gây rủi ro gì?
3. Error analysis cần dẫn tới action nào?

## Kết quả hướng tới

error analysis; lưu kèm lệnh đã chạy, cấu hình, metric, thời gian chạy và một điều còn hạn chế.

## Core vs stretch

- **Cốt lõi:** Báo slice metrics kèm sample count, review lỗi theo rule và đề xuất next experiment.
- **Mở rộng:** Thêm một subgroup-risk check hoặc một monitoring signal như missing rate/prediction distribution.

## Lỗi thường gặp

- Chọn lỗi thuận mắt.
- Dùng explanation hợp thức hóa lỗi.

## Khi mắc kẹt

Đừng chọn lỗi thuận mắt. Lấy mẫu theo quy tắc cố định và mô tả điều thấy trước khi giải thích nguyên nhân.

## Nguồn

Nguồn nên đọc: scikit-learn permutation importance và model inspection; model-card guidance trong `docs/sources.yml`.
