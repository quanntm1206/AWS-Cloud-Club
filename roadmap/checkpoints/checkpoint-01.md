# Mốc năng lực 01 - Tuần 4

## Mục tiêu

Tự đánh giá nền tảng dữ liệu và toán bằng một bài toán nhỏ chạy được, không cần model phức tạp.

## Bạn đã đạt mốc nếu

- Viết rõ đối tượng dự đoán, nhãn, thời điểm dự đoán và hành động sau dự đoán.
- Kiểm tra được shape, dtype, missing, duplicate và range trước khi tính toán.
- Giải thích bằng lời của bạn dot product, loss và gradient đang làm gì trong ví dụ đã chạy.
- Chạy lại mini path từ môi trường sạch và nhận kết quả trong tolerance đã ghi.

## Minh chứng đạt mốc

- Problem statement và data-quality table lưu cục bộ.
- Notebook/code tính linear regression, gradient check và lệnh chạy lại.
- Environment report, seed, tolerance, test output cùng một ví dụ từng thất bại rồi được sửa.

## Rubric

| Tiêu chí | Điểm |
|---|---:|
| Hiểu dữ liệu và đặt bài toán | 30 |
| Tính đúng và kiểm tra kết quả | 30 |
| Tái lập môi trường | 25 |
| Giải thích giới hạn | 15 |

Điểm đạt: 70/100. Gate: không leakage, không secret, mini run tái lập. Nếu gradient check sai hoặc chưa giải thích được prediction time, quay lại phần cốt lõi.

## Câu hỏi tự nhìn lại

- Nếu đổi scale của feature, loss và gradient thay đổi ra sao?
- Kiểm tra nào đã bắt được lỗi thật thay vì chỉ xác nhận code chạy?
- Phần nào bạn vẫn phải nhìn tài liệu mới giải thích được?
