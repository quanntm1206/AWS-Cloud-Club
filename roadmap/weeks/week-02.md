# Tuần 02 - NumPy và vectorization

## Mục tiêu tuần

Dùng vector, matrix, broadcasting; hiểu shape.

## Kiến thức cốt lõi

- Array có shape, dtype, axis; code chạy nhưng sai axis vẫn sai nghiệp vụ.
- Broadcasting hợp lệ khi kích thước từ phải sang trái bằng nhau hoặc một chiều bằng 1.
- Dot product tạo weighted score; matrix multiplication tính đồng thời nhiều mẫu.
- Float cần tolerance; chú ý chia 0, overflow exp/log và mảng trung gian quá lớn.

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

1. Viết weighted score bằng loop và X @ w; đối chiếu np.allclose.
2. Tính confusion matrix và precision/recall bằng NumPy.
3. In shape từng bước, cố ý gây lỗi broadcasting rồi sửa.

## Lab

**lab-01:** NumPy vectorization và metric từ đầu. Môi trường chính: `local`.

## Tự kiểm tra

1. Shape X, w, X @ w với n mẫu/d feature?
2. Broadcasting khác copy dữ liệu thế nào?
3. Vì sao dùng np.allclose?

## Kết quả hướng tới

tested NumPy module; kèm config, command, metric, runtime và một failure/limitation.

## Core vs stretch

- **Core:** hoàn thành mini profile, test và kết quả cốt lõi.
- **Stretch:** thử đúng một cải tiến có giả thuyết; không hyperparameter sweep.

## Lỗi thường gặp

- Reshape để code chạy mà không hiểu axis.
- Vectorize bằng mảng trung gian làm hết RAM.

## Nguồn

Xem `docs/sources.yml`; ưu tiên textbook và tài liệu chính thức được ghi trong lab.
