# Colab Free - chạy CV mà không cần mua compute

**Kiểm chứng:** 2026-08-12 tại [Google Colab FAQ](https://research.google.com/colaboratory/faq.html).

Colab Free có thể cấp GPU/TPU, nhưng loại accelerator, giới hạn sử dụng, idle timeout và tuổi thọ VM thay
đổi theo availability và usage pattern. Roadmap luôn có `cpu-mini`, vì vậy việc không được cấp GPU không
chặn bạn hoàn thành phần cốt lõi.

## Mở notebook

1. Tải hoặc mở [`notebooks/colab/cv_transfer_learning_colab.ipynb`](../../notebooks/colab/cv_transfer_learning_colab.ipynb).
2. Trong Colab, dùng `File > Upload notebook`; nếu muốn giữ bản chỉnh sửa, chọn `Copy to Drive`.
3. Chạy cell `Environment check`. Chỉ chọn `Runtime > Change runtime type > GPU` khi bạn chuẩn bị train.
4. Chạy từ trên xuống với `cpu-mini`; sau đó mới thử `gpu-free` nếu accelerator có sẵn.
5. Sau mỗi epoch, xác nhận checkpoint được cập nhật. Tải `artifacts.zip` về máy sau run.
6. Chọn `Runtime > Disconnect and delete runtime` khi xong.

## Khi runtime bị ngắt

Runtime không phải ổ lưu trữ bền vững. Tạo checkpoint mỗi epoch và download artifact sớm. Khi mở phiên mới,
chạy lại environment/config, upload checkpoint, kiểm cùng architecture/label mapping rồi resume. Nếu chỉ có
weights, gọi đó là inference checkpoint; không khẳng định optimizer đã được khôi phục.

## Khắc phục nhanh

- `torch.cuda.is_available()` là `False`: dùng CPU-mini hoặc thử lại lúc khác; không mua Colab Pro cho roadmap.
- CIFAR10 tải lỗi: dùng FakeData fallback để smoke, ghi limitation, không dùng accuracy để kết luận.
- Pretrained weights tải lỗi: random-weight fallback chỉ kiểm code; chưa đạt gate transfer learning.
- `CUDA out of memory`: restart runtime rồi giảm batch size/image size/sample count.
- Cài package xong vẫn import lỗi: restart runtime một lần và chạy lại từ environment check.
- Không thấy file: kiểm panel Files; download trước khi `Disconnect and delete runtime`.

Không dùng SSH/remote desktop, background service hoặc nhiều account để lách quota. Không lưu token trong cell.
