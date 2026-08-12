# Tuần 05 - Supervised learning và baseline

## Mục tiêu tuần

Đặt baseline; split train/validation/test đúng.

## Kiến thức cốt lõi

- Classification dự đoán class/probability; regression dự đoán giá trị liên tục.
- Dummy baseline đo mức tối thiểu; logistic regression tạo linear logit rồi sigmoid.
- Train để fit, validation để chọn, test chỉ dùng khi quyết định đã khóa.
- Dùng stratified split cho class; dùng group/time split khi mẫu liên quan hoặc có thời gian.

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

1. So dummy và logistic trên đúng cùng split/pipeline/metric.
2. Kiểm class balance và ID không trùng giữa tập.
3. Viết metric gate model phải vượt baseline.

## Lab

**lab-04:** Dummy và logistic classifier. Môi trường chính: `local`.

## Tự kiểm tra

1. Dummy accuracy cao khi nào?
2. Logistic tuyến tính ở không gian nào?
3. Random split gây leakage khi nào?

## Kết quả hướng tới

baseline report; kèm config, command, metric, runtime và một failure/limitation.

## Core vs stretch

- **Core:** hoàn thành mini profile, test và kết quả cốt lõi.
- **Stretch:** thử đúng một cải tiến có giả thuyết; không hyperparameter sweep.

## Lỗi thường gặp

- So model trên split khác nhau.
- Bỏ baseline để chạy model phức tạp.

## Nguồn

Xem `docs/sources.yml`; ưu tiên textbook và tài liệu chính thức được ghi trong lab.
