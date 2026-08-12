# Tuần 08 - Cross-validation và learning curve

## Mục tiêu tuần

Dùng cross-validation và learning curve.

## Vì sao tuần này quan trọng

Một lần chia dữ liệu có thể may hoặc rủi. Cross-validation giúp bạn thấy model ổn định đến đâu, còn learning curve gợi ý nên thêm dữ liệu hay đổi cách học.

**Ví dụ gần gũi:** Mean CV giống điểm trung bình; độ lệch giữa các fold cho biết kết quả phụ thuộc mạnh đến mức nào vào cách chia.

## Kiến thức cốt lõi

- Cross-validation ước lượng biến thiên qua nhiều fold; báo từng score, mean, std và runtime.
- StratifiedKFold cho classification độc lập; GroupKFold/time split cho entity/time.
- Transform phải nằm trong pipeline để fit lại bên trong từng fold.
- Learning curve so train/validation theo lượng data: cùng thấp gợi ý underfitting/high bias; train cao nhưng validation thấp gợi ý overfitting/high variance.
- Fold score là mẫu hữu hạn, không phải sự thật tuyệt đối; luôn báo độ phân tán và tránh kết luận mạnh từ chênh lệch nhỏ.

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


1. Chạy 3-fold CV fixed seed.
2. So pipeline đúng với preprocessing ngoài CV.
3. Vẽ learning curve ba train sizes.

## Lab

**lab-07:** Evaluation harness có mean/std/runtime. Môi trường chính: `local`.

## Dấu hiệu bạn đã hiểu

Bạn báo từng fold, mean, std, runtime và biết chọn split theo entity hoặc thời gian khi cần.

## Tự kiểm tra

1. Std giữa fold lớn gợi ý gì?
2. CV có thay final test không?
3. Shuffle time series sai vì sao?

## Kết quả hướng tới

mốc năng lực 2; lưu kèm lệnh đã chạy, cấu hình, metric, thời gian chạy và một điều còn hạn chế.

## Core vs stretch

- **Cốt lõi:** Chạy 3-fold CV cùng pipeline; báo từng fold, mean, std và learning curve.
- **Mở rộng:** So StratifiedKFold với GroupKFold trên một grouping giả định; không tăng fold chỉ để có thêm số.

## Lỗi thường gặp

- Tune rồi báo cùng CV như final test.
- Dùng nhiều fold nhưng không thêm insight.

## Khi mắc kẹt

Giảm còn 3 fold và mini data. Nếu score dao động, kiểm class/group theo fold trước khi tune model.

## Nguồn

Nguồn nên đọc: scikit-learn cross-validation và learning curve documentation.
