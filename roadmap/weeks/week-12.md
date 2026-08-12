# Tuần 12 - Mini-project tabular

## Mục tiêu tuần

Tổng hợp pipeline tabular có thể tái lập.

## Kiến thức cốt lõi

- Mini-project khóa problem, contract, split, baseline và success criteria trước tối ưu.
- Training xuất model, portable artifact, metrics, manifest và model card.
- Reproduction guide bắt đầu từ clean environment, ghi command/config/seed/input/output.
- Model card nêu intended/out-of-scope use, data, metrics, subgroup, limitation và rollback signal.

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

1. Chạy churn pipeline mini end-to-end.
2. Reload artifact ở process mới và kiểm prediction parity.
3. Chạy reproduction guide từ clean shell.

## Lab

**lab-11:** Mini-project tabular end-to-end. Môi trường chính: `local`.

## Tự kiểm tra

1. Artifact cần gì ngoài weights?
2. Model card phải nêu misuse nào?
3. Chứng minh run tái lập bằng gì?

## Kết quả hướng tới

mốc năng lực 3 + model card; kèm config, command, metric, runtime và một failure/limitation.

## Core vs stretch

- **Core:** hoàn thành mini profile, test và kết quả cốt lõi.
- **Stretch:** thử đúng một cải tiến có giả thuyết; không hyperparameter sweep.

## Lỗi thường gặp

- Chỉ lưu notebook phụ thuộc cell state, thiếu artifact tái lập.
- Thiếu split manifest/config.

## Nguồn

Xem `docs/sources.yml`; ưu tiên textbook và tài liệu chính thức được ghi trong lab.

