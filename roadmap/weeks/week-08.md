# Tuần 08 - Cross-validation và learning curve

## Mục tiêu tuần

Dùng cross-validation và learning curve.

## Kiến thức cốt lõi

- Cross-validation ước lượng biến thiên qua nhiều fold; báo từng score, mean, std và runtime.
- StratifiedKFold cho classification độc lập; GroupKFold/time split cho entity/time.
- Transform phải nằm trong pipeline để fit lại bên trong từng fold.
- Learning curve so train/validation theo lượng data để nhận diện high bias/high variance.

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

## Tự kiểm tra

1. Std giữa fold lớn gợi ý gì?
2. CV có thay final test không?
3. Shuffle time series sai vì sao?

## Kết quả hướng tới

mốc năng lực 2; kèm config, command, metric, runtime và một failure/limitation.

## Core vs stretch

- **Core:** hoàn thành mini profile, test và kết quả cốt lõi.
- **Stretch:** thử đúng một cải tiến có giả thuyết; không hyperparameter sweep.

## Lỗi thường gặp

- Tune rồi báo cùng CV như final test.
- Dùng nhiều fold nhưng không thêm insight.

## Nguồn

Xem `docs/sources.yml`; ưu tiên textbook và tài liệu chính thức được ghi trong lab.
