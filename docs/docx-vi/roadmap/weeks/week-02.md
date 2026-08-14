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

## Từ khóa tuần này

**Thuật ngữ mới hoặc trọng tâm:** `feature`, `label / target`, `parameter`, `vectorization`

**Ôn lại:** `dataset`, `sample`, `schema`

**Áp dụng:** Biểu diễn mỗi `sample` thành vector `feature` nhưng giữ riêng `label / target`; dùng `vectorization` để tính output từ các `parameter` đã học, rồi ghi lại `dataset` và `schema` của array.

## Giải thích khái niệm

### Input và outcome

**Cách hình dung:** `feature`: Thông tin đầu vào model dùng để tạo dự đoán. Feature phải có cả khi training lẫn khi hệ thống nhận yêu cầu prediction mới. `label / target`: Kết quả cần dự đoán và dùng để học hoặc đánh giá model. Trong supervised learning, feature của mỗi training sample đi cùng đáp án đã biết này.

**Vì sao quan trọng:** Model chỉ có thể học đúng khi input được tách rõ khỏi outcome cần dự đoán.

**Ví dụ xuyên suốt:** `feature`: Tenure và monthly_charges là hai feature của bài toán churn. `label / target`: Churn=1 là label cho khách đã rời đi.

**Dễ nhầm với:** Feature là input; label hoặc target là đáp án cần dự đoán. Label là truth quan sát được; prediction là đáp án model ước lượng.

**Tự kiểm tra:** Trong bài toán churn, cột nào là `feature` và field nào là `label / target`?

### Parameter đã học và vectorized computation

**Cách hình dung:** `parameter`: Giá trị model học từ dữ liệu trong lúc training. Parameter gồm weight và bias thay đổi khi training giảm loss. `vectorization`: Thực hiện phép tính trên cả mảng thay vì lặp từng phần tử bằng Python. Phép toán trên array giúp thư viện số học tối ưu xử lý nhiều giá trị cùng lúc.

**Vì sao quan trọng:** Parameter lưu phần training học được; vectorization áp dụng phép tính đã học nhất quán trên nhiều sample.

**Ví dụ xuyên suốt:** `parameter`: Các trọng số trong vector w của hồi quy tuyến tính là parameter. `vectorization`: Dùng X @ w để tính score cho mọi sample.

**Dễ nhầm với:** Parameter được học khi fit; hyperparameter được chọn trước hoặc quanh quá trình fit. Vectorization đổi cách biểu diễn phép tính, không đổi mục tiêu toán học.

**Tự kiểm tra:** Training học gì thành `parameter`, còn `vectorization` thực hiện phần việc nào?

## Kết nối kiến thức cũ

`dataset`, `sample` và `schema` từ tuần trước giờ trở thành biểu diễn số: mỗi sample ánh xạ thành một feature vector có shape rõ ràng. Array shape và vectorized output đã lưu cho biết biểu diễn đó có nhất quán hay không.

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


1. Viết weighted score bằng loop và X @ w; đối chiếu np.allclose.
2. Tính error count table và precision/recall bằng NumPy.
3. In shape từng bước, cố ý gây lỗi broadcasting rồi sửa.

## Lab

**lab-01:** NumPy vectorization và quality measure từ đầu. Môi trường chính: `local`.

## Dấu hiệu bạn đã hiểu

Bạn dự đoán được shape trước khi chạy code và giải thích vì sao loop với phép nhân ma trận cho cùng kết quả.

## Tự kiểm tra

1. Shape X, w, X @ w với n mẫu/d feature?
2. Broadcasting khác copy dữ liệu thế nào?
3. Vì sao dùng np.allclose?

## Kết quả hướng tới

tested NumPy module; lưu kèm lệnh đã chạy, cấu hình, quality measure, thời gian chạy và một điều còn hạn chế.

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
