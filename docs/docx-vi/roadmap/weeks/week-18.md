# Tuần 18 - CNN và transfer learning

## Mục tiêu tuần

Hiểu CNN và transfer learning.

## Vì sao tuần này quan trọng

Transfer learning tận dụng biểu diễn đã học để giảm dữ liệu và compute. Đây là con đường hợp lý cho người mới dùng free runtime.

**Ví dụ gần gũi:** Giữ backbone cố định giống dùng một bộ trích đặc trưng có sẵn; bạn chỉ dạy classifier head cho lớp mới.

## Kiến thức cốt lõi

- Convolution học kernel cục bộ chia sẻ weight; stride/padding đổi spatial size, downsampling giảm compute.
- Transfer learning dùng pretrained backbone và thay head; frozen-backbone chỉ train head nên nhẹ hơn full fine-tune.
- Input normalization phải khớp pretrained weights; train augmentation khác validation transform deterministic.
- Notebook có CPU-mini và FakeData khi GPU/dataset thiếu; CPU-mini vẫn cố dùng pretrained weights. Nếu weights
  không tải được, random-weight fallback chỉ smoke code và chưa đạt gate transfer learning. FakeData không
  chứng minh accuracy.

## Từ khóa tuần này

**Thuật ngữ mới hoặc trọng tâm:** `augmentation`, `backbone`, `freeze`, `transfer learning`

**Ôn lại:** `tensor`, `batch`, `epoch`, `device`, `overfitting`

**Áp dụng:** Chỉ dùng `augmentation` cho từng training `batch` và giữ validation transform deterministic; đặt pretrained `backbone` lên đúng `device`, `freeze` parameter, rồi chạy `transfer learning` trong khi theo dõi epoch loss để phát hiện `overfitting`.

## Giải thích khái niệm

### Augmentation và backbone

**Cách hình dung:** `augmentation`: Biến đổi ngẫu nhiên hợp lý trên training sample để tăng độ đa dạng mà không đổi label. Biến đổi phải giữ nguyên task label và thường chỉ random trên training data. `backbone`: Phần mạng chính trích xuất đặc trưng trước classifier head. Classifier head nhỏ sẽ đổi các feature đó thành score cho class mới.

**Vì sao quan trọng:** Augmentation đổi training view nhưng không đổi label; backbone biến các view đó thành representation có thể dùng lại.

**Ví dụ xuyên suốt:** `augmentation`: Lật ngang ảnh training; resize ảnh validation theo cách deterministic. `backbone`: ResNet18 pretrained làm backbone.

**Dễ nhầm với:** Augmentation đổi training example; preprocessing còn chuẩn bị validation và inference input. Backbone trích xuất feature; classifier head ánh xạ chúng sang task label.

**Tự kiểm tra:** `augmentation` nào giữ nguyên label, và representation nào đến từ `backbone`?

### Freeze và transfer learning

**Cách hình dung:** `freeze`: Tạm không cập nhật parameter của một phần model trong training. Frozen parameter vẫn tham gia forward pass nhưng không nhận optimizer update. `transfer learning`: Tái sử dụng kiến thức từ model pretrained cho bài toán mới. Có thể train classifier head trước trong khi giữ pretrained backbone ở trạng thái freeze.

**Vì sao quan trọng:** Freeze bảo vệ pretrained weight và giảm compute; transfer learning thích nghi các layer còn trainable cho task mới.

**Ví dụ xuyên suốt:** `freeze`: Đặt requires_grad=False cho backbone. `transfer learning`: Giữ ResNet18 backbone và thay classifier head.

**Dễ nhầm với:** Freeze ngừng cập nhật parameter nhưng data vẫn đi qua layer. Transfer learning là chiến lược reuse tổng thể; fine-tuning là một giai đoạn training sau.

**Tự kiểm tra:** Phần nào không đổi khi `freeze` backbone trong `transfer learning`?

## Kết nối kiến thức cũ

`tensor` và mỗi `batch` phải nằm trên đúng `device`; validation result qua từng `epoch` cho thấy `overfitting`. Các check đó cung cấp evidence để quyết định augmentation và transfer learning có hữu ích hay không.

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


1. Tính conv output size và in shape qua model.
2. Freeze backbone, xác nhận chỉ head trainable.
3. Chạy CIFAR10 subset; ép FakeData fallback rồi ghi limitation.

## Lab

**lab-17:** Frozen-backbone baseline trên một free runtime. Môi trường chính: `colab, kaggle`.

## Dấu hiệu bạn đã hiểu

Bạn chạy notebook thật, xác nhận chỉ head trainable và phân biệt FakeData smoke với kết quả CIFAR10.

## Tự kiểm tra

1. Frozen backbone giảm compute vì sao?
2. Normalization sai ảnh hưởng gì?
3. FakeData chứng minh được gì?

## Kết quả hướng tới

CV baseline; lưu kèm lệnh đã chạy, cấu hình, metric, thời gian chạy và một điều còn hạn chế.

## Core vs stretch

- **Cốt lõi:** Chạy notebook bằng `cpu-mini` với pretrained weights; chỉ báo quality khi dùng dữ liệu thật.
- **Mở rộng:** Nếu có GPU miễn phí, chạy `gpu-free` một lần; không fine-tune hoặc sweep trong tuần này.

## Lỗi thường gặp

- Báo transfer learning dù pretrained weights không tải.
- Báo FakeData accuracy như chất lượng thật.

## Khi mắc kẹt

Mở đúng notebook Colab/Kaggle, chạy `cpu-mini` trước. Nếu data không tải được, dùng FakeData smoke. Nếu
pretrained weights không tải được, random-weight fallback chỉ kiểm code; ghi rõ chưa đạt transfer-learning gate.

## Nguồn

Nguồn nên đọc: PyTorch transfer learning tutorial, torchvision weights/transforms và hướng dẫn Colab/Kaggle của repo.
