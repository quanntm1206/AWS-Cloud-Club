# Tuần 04 - Toán trực giác và linear regression

## Mục tiêu tuần

Hiểu dot product, loss, gradient và xác suất cơ bản.

## Kiến thức cốt lõi

- Linear regression dùng y_hat=Xw+b; MSE phạt sai số theo bình phương và nhạy outlier.
- Gradient chỉ hướng tăng nhanh của loss; gradient descent cập nhật ngược hướng với learning rate.
- Central finite difference kiểm analytic gradient bằng thay đổi nhỏ của tham số.
- Feature scale ảnh hưởng hội tụ; hệ số chỉ diễn giải cùng scale, encoding và assumptions.

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

1. Tính forward, MSE, gradient bằng tay trên bốn điểm.
2. So analytic gradient với finite difference qua nhiều epsilon.
3. So loss curve khi learning rate nhỏ, hợp lý, quá lớn.

## Lab

**lab-03:** Linear regression từ đầu và gradient check. Môi trường chính: `local`.

## Tự kiểm tra

1. Gradient bằng 0 nói gì?
2. Epsilon quá nhỏ gây lỗi số nào?
3. MSE khác MAE với outlier ra sao?

## Kết quả hướng tới

mốc năng lực 1; kèm config, command, metric, runtime và một failure/limitation.

## Core vs stretch

- **Core:** hoàn thành mini profile, test và kết quả cốt lõi.
- **Stretch:** thử đúng một cải tiến có giả thuyết; không hyperparameter sweep.

## Lỗi thường gặp

- Tin gradient đúng chỉ vì loss giảm.
- Tăng epoch để che learning rate quá lớn.

## Nguồn

Xem `docs/sources.yml`; ưu tiên textbook và tài liệu chính thức được ghi trong lab.
