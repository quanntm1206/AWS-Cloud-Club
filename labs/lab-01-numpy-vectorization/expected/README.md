# Kết quả tham khảo - lab-01-numpy-vectorization

## Oracle

Tự tính một hàng, so loop với `X @ w` bằng `np.allclose`.

## Required receipt

- Chạy `python scripts/run_lab.py --lab 1` từ repository root; PowerShell/Bash đầy đủ nằm trong README.
- JSON phải có `status=starter-example-completed`; trong `result` cần thấy `vectorization_matches_loop=true` và năm score đầu.
- Learning log cục bộ ghi seed/config, runtime, phép kiểm riêng của lab và ít nhất một limitation hoặc failure.
- Tự trả lời: “Output này chứng minh được gì, và chưa chứng minh được gì?”

## Gợi ý nếu kết quả khác

Nếu shape không khớp, in `X.shape`, `w.shape`; không sửa bằng `reshape` khi chưa biết axis.

Đây là gợi ý tự kiểm, không phải bài cần gửi. Không commit evidence, secret, dữ liệu cá nhân, raw dataset lớn
hoặc output cloud trả phí.
