# Kaggle Notebooks - hướng dẫn free path

**Kiểm chứng:** 2026-08-12 tại `https://www.kaggle.com/docs/notebooks`.

Roadmap không ghi cứng số giờ GPU/TPU vì availability và quota có thể thay đổi. Notebook luôn tự phát hiện
device và chuyển sang `cpu-mini` khi accelerator không có.

## Quy trình

1. Tạo notebook, import từ GitHub hoặc upload file.
2. Add dataset bằng Kaggle Dataset UI; không commit credential hoặc private token.
3. Chọn accelerator nếu tài khoản còn quyền sử dụng; chạy cell kiểm tra device.
4. Chạy frozen-backbone baseline, tối đa 3-5 epoch; không sweep.
5. `Save Version` để giữ output; tải checkpoint, metrics, manifest và model card.
6. Tắt accelerator/chấm dứt session sau khi export.

Chọn **Kaggle hoặc Colab**, không buộc chạy cả hai.

