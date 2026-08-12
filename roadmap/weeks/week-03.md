# Tuần 03 - pandas, cleaning và EDA

## Mục tiêu tuần

Làm sạch dữ liệu; phân biệt observed và suy diễn.

## Kiến thức cốt lõi

- EDA bắt đầu bằng schema, row/key, target distribution, missing, duplicate và range; biểu đồ đứng sau quality table.
- Missing có thể mang thông tin; không drop/impute trước khi hiểu cơ chế.
- Observation từ sample không chứng minh causal explanation.
- Thống kê đi vào transform phải học sau split và chỉ trên train.

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

1. Tạo data-quality table theo cột.
2. Kiểm duplicate theo khóa nghiệp vụ.
3. Viết ba insight dạng evidence -> hypothesis -> next check.

## Lab

**lab-02:** EDA có data-quality table và ba insight. Môi trường chính: `local`.

## Tự kiểm tra

1. Dtype suy ra có thể sai nghiệp vụ khi nào?
2. Missing tổng thể che subgroup ra sao?
3. EDA gây target leakage thế nào?

## Kết quả hướng tới

EDA notebook/report; kèm config, command, metric, runtime và một failure/limitation.

## Core vs stretch

- **Core:** hoàn thành mini profile, test và kết quả cốt lõi.
- **Stretch:** thử đúng một cải tiến có giả thuyết; không hyperparameter sweep.

## Lỗi thường gặp

- Xóa outlier chỉ vì boxplot.
- Nhìn test để thiết kế transform.

## Nguồn

Xem `docs/sources.yml`; ưu tiên textbook và tài liệu chính thức được ghi trong lab.
