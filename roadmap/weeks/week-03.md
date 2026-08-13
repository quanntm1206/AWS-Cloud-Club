# Tuần 03 - pandas, cleaning và EDA

## Mục tiêu tuần

Làm sạch dữ liệu; phân biệt observed và suy diễn.

## Vì sao tuần này quan trọng

EDA không phải cuộc thi vẽ nhiều biểu đồ. Đây là lúc bạn tìm xem dữ liệu có đáng tin để model học hay không.

**Ví dụ gần gũi:** Một cột tuổi âm hoặc customer ID bị lặp có thể làm quality measure đẹp giả, dù biểu đồ trông hoàn toàn bình thường.

## Kiến thức cốt lõi

- EDA bắt đầu bằng schema, row/key, target distribution, missing, duplicate và range; biểu đồ đứng sau quality table.
- Missing có thể mang thông tin; không drop/impute trước khi hiểu cơ chế.
- Observation từ sample không chứng minh causal explanation.
- Thống kê đi vào data operation phải học sau split và chỉ trên train.

## Từ khóa tuần này

**Thuật ngữ mới hoặc trọng tâm:** `data validation`, `EDA`, `missing value`, `outlier`

**Ôn lại:** `dataset`, `sample`, `feature`, `label / target`

**Áp dụng:** Chạy `data validation` trên `dataset`: kiểm `schema`, `missing value`, `outlier`; dùng EDA mô tả feature và label / target ở cấp sample.

## Lịch 8-10 giờ

| Hoạt động | Giờ |
|---|---:|
| Đọc và ghi chú | 2 |
| Guided practice | 2 |
| Lab | 3 |
| Assessment/failure review | 1 |
| Learning log và tự đánh giá | 1 |
| Review/hoàn thiện | 0 |

## Guided practice


1. Tạo data-quality table theo cột.
2. Kiểm duplicate theo khóa nghiệp vụ.
3. Viết ba insight dạng evidence -> hypothesis -> next check.

## Lab

**lab-02:** EDA có data-quality table và ba insight. Môi trường chính: `local`.

## Dấu hiệu bạn đã hiểu

Bạn phân biệt được điều quan sát thấy với giả thuyết cần kiểm tra thêm và không dùng test để thiết kế data operation.

## Tự kiểm tra

1. Dtype suy ra có thể sai nghiệp vụ khi nào?
2. Missing tổng thể che subgroup ra sao?
3. EDA gây target leakage thế nào?

## Kết quả hướng tới

EDA notebook/report; lưu kèm lệnh đã chạy, cấu hình, quality measure, thời gian chạy và một điều còn hạn chế.

## Core vs stretch

- **Cốt lõi:** Tạo data-quality table và ba ghi chú evidence - hypothesis - next check.
- **Mở rộng:** Khảo sát một subgroup hoặc quy tắc duplicate khác; không dùng test để thiết kế cleaning.

## Lỗi thường gặp

- Xóa outlier chỉ vì boxplot.
- Nhìn test để thiết kế data operation.

## Khi mắc kẹt

Bắt đầu bằng bảng schema, missing, duplicate và range. Chỉ vẽ biểu đồ sau khi biết mỗi hàng đại diện cho gì.

## Nguồn

Nguồn nên đọc: pandas documentation về missing data, duplicates và dtypes trong `docs/sources.yml`.
