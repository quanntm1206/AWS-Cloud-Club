# Colab Free - hướng dẫn an toàn tài nguyên

**Kiểm chứng:** 2026-08-12 tại `https://research.google.com/colaboratory/faq.html`.

Colab cung cấp notebook hosted miễn phí, có thể có GPU/TPU. Resource không được đảm bảo; usage limit,
idle timeout, maximum VM lifetime và accelerator type thay đổi. Free notebook có thể chạy tối đa 12 giờ
phụ thuộc availability/usage pattern, nhưng roadmap không dựa vào con số này để hoàn thành lab.

## Quy trình

1. Mở notebook từ GitHub hoặc upload `.ipynb`; chọn **Copy to Drive** nếu muốn lưu bản riêng.
2. Chạy `Environment check`; chỉ chọn GPU khi notebook thực sự dùng GPU.
3. Chạy `cpu-mini` trước; sau đó mới chọn `gpu-free` nếu accelerator có sẵn.
4. Lưu checkpoint mỗi epoch; tải `artifacts.zip` sau run.
5. Dùng `Runtime > Disconnect and delete runtime` khi xong; không xem VM là storage bền vững.

Không dùng SSH/remote desktop, không chạy background service và không tạo nhiều account để lách quota.

