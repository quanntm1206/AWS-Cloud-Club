# Tuần 02 - NumPy và vectorization

## Mục tiêu tuần

Dùng vector, matrix, broadcasting; hiểu shape.

## Vì sao tuần này quan trọng

NumPy là ngôn ngữ chung của dữ liệu dạng số. Hiểu shape và axis sớm sẽ giúp bạn tránh nhiều lỗi model chạy được nhưng tính sai.

**Ví dụ gần gũi:** Một hàng là một khách hàng, một cột là một đặc trưng; `X @ w` tạo một điểm số cho từng khách hàng.

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

## Dấu hiệu bạn đã hiểu

Bạn dự đoán được shape trước khi chạy code và giải thích vì sao loop với phép nhân ma trận cho cùng kết quả.

## Tự kiểm tra

1. Shape X, w, X @ w với n mẫu/d feature?
2. Broadcasting khác copy dữ liệu thế nào?
3. Vì sao dùng np.allclose?

## Kết quả hướng tới

tested NumPy module; lưu kèm lệnh đã chạy, cấu hình, metric, thời gian chạy và một điều còn hạn chế.

## Core vs stretch

- **Cốt lõi:** Hoàn thành phép tính loop/vectorized, tự tính một hàng và kiểm shape/boundary.
- **Mở rộng:** Thử một mảng có zero variance hoặc shape sai; dự đoán lỗi trước khi chạy.

## Lỗi thường gặp

- Reshape để code chạy mà không hiểu axis.
- Vectorize bằng mảng trung gian làm hết RAM.

## Khi mắc kẹt

In `shape`, `dtype` sau từng bước. Giảm mảng xuống 2-3 hàng rồi tính tay trước khi sửa `reshape`.

## Nguồn

Nguồn nên đọc: NumPy documentation về broadcasting, `matmul` và floating-point comparison trong `docs/sources.yml`.
