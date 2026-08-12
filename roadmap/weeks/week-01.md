# Tuần 01 - ML workflow và môi trường tái lập

## Mục tiêu tuần

Mô tả một ML workflow hoàn chỉnh; tạo môi trường tái lập.

## Kiến thức cốt lõi

- Tách business question khỏi prediction task: xác định đối tượng, nhãn, prediction time và hành động sau dự đoán.
- Workflow tối thiểu: validate data, split, baseline, fit, validate, khóa quyết định, test một lần, phân tích lỗi, đóng gói.
- Data contract khóa schema/target; experiment contract lưu seed, config, code revision, metric, runtime và limitation.
- Reproducibility yêu cầu tái tạo input, procedure, environment và tolerance; không hứa mọi phần cứng cho bit-identical result.

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

1. Viết problem statement cho churn theo mẫu ai-khi nào-để làm gì.
2. Vẽ data -> split -> fit -> validate -> test -> artifact; đánh dấu điểm leakage.
3. Chạy lab, lưu environment report và một limitation.

## Lab

**lab-00:** Cài môi trường, chạy kiểm tra, lập learning log. Môi trường chính: `local`.

## Tự kiểm tra

1. Model output khác quyết định sản phẩm thế nào?
2. Vì sao test không dùng chọn model/threshold?
3. Experiment log tối thiểu gồm gì?

## Kết quả hướng tới

environment report lưu cục bộ; kèm config, command, metric, runtime và một failure/limitation.

## Core vs stretch

- **Core:** hoàn thành mini profile, test và kết quả cốt lõi.
- **Stretch:** thử đúng một cải tiến có giả thuyết; không hyperparameter sweep.

## Lỗi thường gặp

- Bắt đầu từ thuật toán thay vì câu hỏi.
- Không khóa prediction time nên feature nhìn tương lai.

## Nguồn

Xem `docs/sources.yml`; ưu tiên textbook và tài liệu chính thức được ghi trong lab.
