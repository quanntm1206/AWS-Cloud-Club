# Tuần 17 - Neural networks và PyTorch

## Mục tiêu tuần

Hiểu tensor, autograd, loop và device.

## Vì sao tuần này quan trọng

PyTorch làm rõ điều thư viện cổ điển thường giấu: tensor đi qua model, loss tạo gradient và optimizer cập nhật parameter.

**Ví dụ gần gũi:** Quên `zero_grad()` khiến gradient của batch mới cộng lên batch cũ; quên `eval()` làm validation hành xử khác dự kiến.

## Kiến thức cốt lõi

- Tensor có shape, dtype, device; model, input và target phải ở device tương thích. `.to(device)` trả tensor/module cần được gán lại.
- `nn.Module` giữ parameter và `forward`; Linear nhận `[batch, features]`, loss cần prediction/target đúng shape-dtype.
- Autograd dựng graph. Mỗi batch: `zero_grad()` -> forward -> loss -> `backward()` -> `step()`; bỏ zero_grad làm gradient cộng dồn.
- `model.train()` khác `model.eval()`; validation dùng cả `model.eval()` và `torch.no_grad()` để đúng hành vi và tiết kiệm memory.
- Device auto ưu tiên CUDA, fallback CPU-mini. Seed hỗ trợ tái lập nhưng hardware/kernel vẫn có sai khác nhỏ.

## Từ khóa tuần này

**Thuật ngữ mới hoặc trọng tâm:** `tensor`, `batch`, `epoch`, `optimizer`, `device`

**Ôn lại:** `parameter`, `gradient`, `loss`, `validation set`

**Áp dụng:** Tạo mỗi `tensor` theo `batch` và train qua nhiều `epoch`; dùng `optimizer` cập nhật từng `parameter` từ `gradient` và `loss`, giữ model cùng input trên một `device`, rồi đánh giá trên `validation set`.

## Giải thích khái niệm

### Tensor và batch

**Cách hình dung:** `tensor`: Mảng nhiều chiều dùng để biểu diễn dữ liệu và phép tính trong neural network. Shape, data type và device quyết định phép toán nào có thể dùng tensor. `batch`: Nhóm sample được xử lý cùng một lần trước khi cập nhật parameter. Training thường thực hiện một forward pass và backward pass cho mỗi batch.

**Vì sao quan trọng:** Tensor shape, dtype và batch size quyết định phép tính có tương thích và vừa memory hay không.

**Ví dụ xuyên suốt:** `tensor`: Batch ảnh có shape [32, 3, 160, 160]. `batch`: Batch size 32 nghĩa là model đọc 32 ảnh mỗi bước.

**Dễ nhầm với:** Tensor là array có shape và dtype, không phải chính neural network. Batch gom sample; epoch đi qua toàn bộ training set.

**Tự kiểm tra:** `tensor` shape và `batch` size có khớp model input và memory hiện có không?

### Epoch và update từ optimizer

**Cách hình dung:** `epoch`: Một lượt model đi qua toàn bộ training set. Số optimizer step trong mỗi epoch phụ thuộc dataset size và batch size. `optimizer`: Thuật toán dùng gradient để cập nhật parameter. Optimizer còn có thể giữ moving average hoặc state khác để tạo cập nhật sau.

**Vì sao quan trọng:** Epoch mô tả mức độ đi qua dataset; optimizer update parameter sau các batch, nên hai khái niệm đếm tiến độ khác nhau.

**Ví dụ xuyên suốt:** `epoch`: Ba epoch dùng mỗi training sample khoảng ba lần. `optimizer`: Adam cập nhật classifier head sau loss.backward().

**Dễ nhầm với:** Epoch là một lượt; nhiều optimizer step có thể xảy ra trong lượt đó. Optimizer áp cập nhật; learning rate là một cấu hình điều khiển cập nhật.

**Tự kiểm tra:** Trong một `epoch` có bao nhiêu optimizer update, và mỗi bước `optimizer` đổi gì?

### Device placement

**Cách hình dung:** `device`: Phần cứng nơi tensor và model thực hiện phép tính. Model và mọi tensor trong cùng phép toán phải nằm trên device tương thích.

**Vì sao quan trọng:** Model, input và target phải ở device tương thích; device đã chọn cũng phải nằm trong run record.

**Ví dụ xuyên suốt:** `device`: Model và input cùng ở CPU hoặc cùng ở CUDA.

**Dễ nhầm với:** Device là hardware tính toán; tensor là data được đặt lên đó.

**Tự kiểm tra:** Model, input và target có cùng `device` tương thích không?

## Kết nối kiến thức cũ

`parameter`, `gradient` và `loss` giờ hoạt động trên tensor batch thông qua optimizer. History đã lưu trên `validation set` cho thấy update ảnh hưởng generalization qua các epoch ra sao.

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


1. In shape/dtype/device của batch và output trước train.
2. Viết loop 3 epoch, lưu train/validation loss.
3. Thử bỏ zero_grad; khôi phục rồi validation bằng eval/no_grad.

## Lab

**lab-16:** MLP device-aware trên mini data. Môi trường chính: `local, colab, kaggle`.

## Dấu hiệu bạn đã hiểu

Bạn giải thích được shape/dtype/device, viết loop nhỏ và thấy loss giảm mà không phụ thuộc GPU.

## Tự kiểm tra

1. requires_grad khác grad?
2. eval có thay no_grad không?
3. CrossEntropyLoss cần shape/dtype gì?
4. Device mismatch phát sinh thế nào?

## Kết quả hướng tới

seeded run; lưu kèm lệnh đã chạy, cấu hình, metric, thời gian chạy và một điều còn hạn chế.

## Core vs stretch

- **Cốt lõi:** Chạy MLP mini trên CPU, giải thích tensor/device và đúng train/eval loop.
- **Mở rộng:** Thử một learning rate khác hoặc bỏ `zero_grad` có chủ đích rồi khôi phục.

## Lỗi thường gặp

- Input lên GPU nhưng model/target ở CPU.
- Validation trong train mode hoặc giữ graph.

## Khi mắc kẹt

Chạy local one-epoch smoke. Nếu lỗi, in device của model, input, target và kiểm target dtype trước.

## Nguồn

Nguồn nên đọc: PyTorch tutorials về tensors, autograd, optimization và `train`/`eval`.
