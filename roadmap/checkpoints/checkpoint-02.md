# Mốc năng lực 02 - Tuần 8

## Mục tiêu

Tự đánh giá khả năng chọn cách đo và kiểm tra model đáng tin cậy.

## Bạn đã đạt mốc nếu

- Split dữ liệu trước mọi transform có học tham số và giải thích vì sao pipeline không leakage.
- So model với baseline đơn giản trên metric gắn với chi phí false positive/false negative.
- Chọn threshold trên validation, chỉ mở test sau khi khóa quyết định.
- Dùng cross-validation hoặc learning curve để mô tả độ ổn định, không chỉ báo một điểm số.

## Minh chứng đạt mốc

- Split manifest, pipeline config và baseline report lưu cục bộ.
- Bảng metric/threshold có ít nhất một trade-off được giải thích.
- Kết quả cross-validation hoặc learning curve kèm mean, độ phân tán và runtime.
- Một leakage test hoặc thí nghiệm cố ý sai cho thấy guardrail hoạt động.

## Rubric

| Tiêu chí | Điểm |
|---|---:|
| Chia dữ liệu và chống leakage | 30 |
| Chọn metric theo bài toán | 30 |
| Cross-validation và độ ổn định | 25 |
| Kết luận có bằng chứng | 15 |

Điểm đạt: 70/100. Gate: không leakage, không secret, test set không dùng để chọn model hoặc threshold.

## Câu hỏi tự nhìn lại

- Metric nào có thể đẹp nhưng dẫn tới quyết định nghiệp vụ tệ?
- Độ lệch giữa các fold cho bạn biết điều gì về dữ liệu?
- Nếu chi phí false negative tăng gấp đôi, threshold nên được xem lại thế nào?
