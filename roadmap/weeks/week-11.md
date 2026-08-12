# Tuần 11 - Interpretability và error analysis

## Mục tiêu tuần

Giải thích model thận trọng; phân tích subgroup/failure.

## Vì sao tuần này quan trọng

Model tốt trung bình vẫn có thể tệ với một nhóm nhỏ. Error analysis biến các lỗi riêng lẻ thành việc tiếp theo có thể kiểm chứng.

**Ví dụ gần gũi:** Accuracy chung ổn nhưng khách hợp đồng tháng có nhiều false negative; đây là tín hiệu cần xem dữ liệu hoặc threshold theo nhóm.

## Kiến thức cốt lõi

- Global importance mô tả trung bình; local explanation mô tả một prediction; không cái nào chứng minh causality.
- Permutation importance bị ảnh hưởng khi feature tương quan.
- Slice metric luôn kèm support để tránh kết luận từ nhóm quá nhỏ; xem chênh lệch như tín hiệu điều tra fairness, không vội kết luận nguyên nhân.
- Khi nhãn đến muộn, theo dõi schema, missing rate, prediction distribution và feature drift trước khi có quality metric.
- Failure taxonomy nhóm lỗi thành data quality, boundary, missing signal, label noise hoặc shift.

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

Bạn báo slice metric kèm support, phân nhóm lỗi và đề xuất một data fix cùng một model fix có phép kiểm.

## Tự kiểm tra

1. Importance khác causality?
2. Support nhỏ gây rủi ro gì?
3. Error analysis cần dẫn tới action nào?

## Kết quả hướng tới

error analysis; lưu kèm lệnh đã chạy, cấu hình, metric, thời gian chạy và một điều còn hạn chế.

## Core vs stretch

- **Cốt lõi:** Báo slice metrics kèm support, review lỗi theo rule và đề xuất next experiment.
- **Mở rộng:** Thêm một subgroup-risk check hoặc một monitoring signal như missing rate/prediction distribution.

## Lỗi thường gặp

- Chọn lỗi thuận mắt.
- Dùng explanation hợp thức hóa lỗi.

## Khi mắc kẹt

Đừng chọn lỗi thuận mắt. Lấy mẫu theo quy tắc cố định và mô tả điều thấy trước khi giải thích nguyên nhân.

## Nguồn

Nguồn nên đọc: scikit-learn permutation importance và model inspection; model-card guidance trong `docs/sources.yml`.
