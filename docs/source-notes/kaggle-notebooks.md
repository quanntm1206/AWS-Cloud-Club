# Kaggle Notebooks - free path cho Computer Vision

**Kiểm chứng:** 2026-08-12 tại [Kaggle Notebooks documentation](https://www.kaggle.com/docs/notebooks).

Roadmap không ghi cứng số giờ GPU/TPU vì availability và quota có thể thay đổi. Notebook tự phát hiện device
và dùng `cpu-mini` khi accelerator không có.

## Mở notebook

1. Tải [`notebooks/kaggle/cv_transfer_learning_kaggle.ipynb`](../../notebooks/kaggle/cv_transfer_learning_kaggle.ipynb).
2. Trong Kaggle, tạo Notebook rồi chọn `File > Import Notebook` để upload file.
3. Mở Settings, bật accelerator nếu tài khoản còn quyền sử dụng; chạy environment check để xác nhận device.
4. Chạy `cpu-mini` trước. Với `gpu-free`, notebook dùng CIFAR10 subset, frozen backbone và tối đa 5 epoch.
5. Chọn `Save Version`, chờ output hoàn tất, rồi tải `artifacts.zip`, metrics, manifest và checkpoint.
6. Tắt accelerator/kết thúc session sau khi export; không để notebook chạy nền.

## Dữ liệu và internet

Nếu dùng dataset khác, thêm bằng `Add Input`; dữ liệu thường xuất hiện read-only dưới `/kaggle/input`. Ghi rõ
license và split. Không đưa credential/private token vào notebook. Nếu internet bị tắt hoặc download lỗi,
chuyển sang input dataset đã thêm hoặc FakeData smoke; không dùng FakeData accuracy để báo chất lượng. Nếu
pretrained weights không có trong cache và internet bị tắt, random-weight fallback chỉ kiểm code, chưa đạt gate
transfer learning.

## Khắc phục nhanh

- Không chọn được GPU: chạy CPU-mini; phần cốt lõi vẫn hợp lệ.
- Không tìm thấy file: in working directory và liệt kê `/kaggle/input`; tránh hardcode tên dataset chưa kiểm.
- Hết memory: giảm batch/image/sample, restart session rồi chạy lại từ đầu.
- Session dừng: tạo notebook version mới, upload checkpoint và kiểm config/label mapping trước resume.
- Output biến mất: phải `Save Version` và download artifact trước khi kết thúc session.

Chọn **Kaggle hoặc Colab**, không buộc chạy cả hai và không cần gói trả phí.
