# Tuần 20 - CV evaluation và failure analysis

## Mục tiêu tuần

Đánh giá per-class và phân nhóm failure.

## Kiến thức cốt lõi

- Overall accuracy che class yếu; báo per-class precision/recall/F1/support và macro/weighted aggregate.
- Confusion matrix normalized theo true class giúp so recall giữa class khác support.
- Failure record có sample ID, truth, prediction, confidence, error type; không publish sensitive data.
- Review theo sampling rule rồi phân nhóm data, label, ambiguity, transform, model hoặc shift.
- Model card gắn metric với dataset/split/config và cấm dùng fallback data để kết luận quality.

## Lịch 8-10 giờ

| Hoạt động | Giờ |
|---|---:|
| Đọc và ghi chú | 2 |
| Guided practice | 2 |
| Lab | 4 |
| Assessment/error analysis | 1 |
| Learning log và tự đánh giá | 1 |
| Review/hoàn thiện | 1 |

## Guided practice

1. Tạo per-class table và confusion matrix.
2. Xuất tối đa 20 failure records, ưu tiên confident-wrong.
3. Viết limitation và next experiment từ taxonomy.

## Lab

**lab-19:** Confusion matrix và tối đa 20 failure examples; nếu ít hơn thì xuất toàn bộ và ghi limitation. Môi trường chính: `local, colab, kaggle`.

## Tự kiểm tra

1. Macro khác weighted F1?
2. Normalize matrix theo hàng trả lời gì?
3. Sampling chỉ theo confidence bias gì?

## Kết quả hướng tới

mốc năng lực 5 + model card; kèm config, command, metric, runtime và một failure/limitation.

## Core vs stretch

- **Core:** hoàn thành mini profile, test và kết quả cốt lõi.
- **Stretch:** thử đúng một cải tiến có giả thuyết; không hyperparameter sweep.

## Lỗi thường gặp

- Chỉ xem aggregate.
- Đưa data không có quyền chia sẻ vào artifact công khai.

## Nguồn

Xem `docs/sources.yml`; ưu tiên textbook và tài liệu chính thức được ghi trong lab.
