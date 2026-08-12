# Tuần 16 - Docker, CI và artifact versioning

## Mục tiêu tuần

Đóng gói, CI, version artifact; hiểu image trade-off.

## Kiến thức cốt lõi

- Container đóng runtime/dependency, không bảo đảm model đúng; dùng base nhỏ, non-root user.
- Đặt dependency layer trước source, loại data/artifact/.venv khỏi build context.
- CI chạy lint/type/test/validators offline; roadmap không auto-deploy AWS.
- Artifact manifest có schema/version/checksum/config/metrics; checksum không thay provenance.

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

1. Build image, smoke health/predict, kiểm non-root.
2. Chạy CI commands từ clean checkout.
3. Đổi một byte artifact và xác nhận checksum fail.

## Lab

**lab-15:** Docker/local CI smoke. Môi trường chính: `local`.

## Tự kiểm tra

1. latest tag có rủi ro gì?
2. Image/model cần version riêng vì sao?
3. Checksum chứng minh gì?

## Kết quả hướng tới

mốc năng lực 4; kèm config, command, metric, runtime và một failure/limitation.

## Core vs stretch

- **Core:** hoàn thành mini profile, test và kết quả cốt lõi.
- **Stretch:** thử đúng một cải tiến có giả thuyết; không hyperparameter sweep.

## Lỗi thường gặp

- Đưa secret/data vào image.
- CI tự deploy cloud.

## Nguồn

Xem `docs/sources.yml`; ưu tiên textbook và tài liệu chính thức được ghi trong lab.
