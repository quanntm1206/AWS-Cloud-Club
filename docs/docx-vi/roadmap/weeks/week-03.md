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

**Áp dụng:** Chạy `data validation` trên `dataset` theo `schema`, gồm check `missing value` và `outlier`; dùng `EDA` để mô tả từng `feature` và `label / target` ở cấp sample.

## Giải thích khái niệm

### Tin dữ liệu trước khi modeling

**Cách hình dung:** `data validation`: Kiểm dữ liệu có đúng schema và quy tắc chất lượng trước khi dùng hay không. Các check có thể từ chối hoặc báo row không hợp lệ trước khi row đi vào workflow. `EDA`: Khám phá dữ liệu bằng thống kê và biểu đồ để hiểu chất lượng, phân bố và câu hỏi cần kiểm tiếp. EDA bắt đầu từ câu hỏi rồi dùng summary và plot để điều tra.

**Vì sao quan trọng:** Data validation thực thi rule đã biết; EDA tìm distribution và pattern có thể dẫn tới rule mới.

**Ví dụ xuyên suốt:** `data validation`: Phát hiện ID trùng, tuổi âm hoặc target thiếu. `EDA`: So sánh churn rate tổng với churn rate của từng nhóm hợp đồng.

**Dễ nhầm với:** Data validation áp quy tắc đã biết; EDA tìm pattern và câu hỏi mới. EDA khám phá và tạo giả thuyết; model validation đánh giá lựa chọn model.

**Tự kiểm tra:** Check nào thuộc `data validation`, còn câu hỏi nào cần `EDA`?

### Missingness và giá trị bất thường

**Cách hình dung:** `missing value`: Giá trị bị thiếu hoặc không được ghi nhận trong dataset. Tùy schema, nó có thể được biểu diễn bằng null, NaN hoặc marker đã thống nhất. `outlier`: Quan sát khác xa phần lớn dữ liệu; cần điều tra trước khi xóa hoặc sửa. Cần dùng hiểu biết domain để tìm nguyên nhân trước khi xóa hoặc cap giá trị này.

**Vì sao quan trọng:** Missing value và outlier có thể là lỗi hoặc signal thật, nên phải tìm cơ chế trước khi thay đổi chúng.

**Ví dụ xuyên suốt:** `missing value`: Một số sample không có monthly_charges. `outlier`: Một hóa đơn cao bất thường có thể là lỗi hoặc khách doanh nghiệp thật.

**Dễ nhầm với:** Missing value là không có giá trị; số 0 vẫn có thể là giá trị hợp lệ. Outlier là bất thường, không tự động đồng nghĩa với sai.

**Tự kiểm tra:** Bạn dựa vào evidence nào để biết `missing value` hoặc `outlier` là lỗi hay signal hữu ích?

## Kết nối kiến thức cũ

Một `dataset` chỉ đáng tin khi từng `sample`, `feature` và `label / target` qua quality check rõ ràng. Kết quả validation cùng EDA summary cung cấp evidence thay vì chỉ dựa vào row count.

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
