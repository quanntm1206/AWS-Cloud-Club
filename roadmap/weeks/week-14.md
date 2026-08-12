# Tuần 14 - Testing cho hệ thống ML

## Mục tiêu tuần

Test schema, transform, model và artifact.

## Kiến thức cốt lõi

- ML tests bao phủ schema, transforms, determinism, metric sanity, reload và API boundary.
- Unit dùng synthetic nhỏ; integration chạy pipeline ngắn.
- Negative cases: thiếu cột, sai dtype, unseen category, NaN/Inf, empty batch, artifact hỏng.
- Metric assertion dùng threshold/tolerance có lý do, không khóa số stochastic mong manh.

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

1. Test valid/invalid schema và unseen category.
2. Fit-save-load-predict, kiểm parity.
3. Kiểm model vượt dummy trên data có signal.

## Lab

**lab-13:** ML tests với edge cases. Môi trường chính: `local`.

## Tự kiểm tra

1. Nguồn randomness nào cần seed?
2. Vì sao exact metric dễ flaky?
3. Test nào bắt train/serve skew?

## Kết quả hướng tới

test evidence; kèm config, command, metric, runtime và một failure/limitation.

## Core vs stretch

- **Core:** hoàn thành mini profile, test và kết quả cốt lõi.
- **Stretch:** thử đúng một cải tiến có giả thuyết; không hyperparameter sweep.

## Lỗi thường gặp

- Chỉ test happy path.
- CI dùng production dataset lớn/nhạy cảm.

## Nguồn

Xem `docs/sources.yml`; ưu tiên textbook và tài liệu chính thức được ghi trong lab.
