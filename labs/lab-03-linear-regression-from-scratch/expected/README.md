# Kết quả tham khảo - lab-03-linear-regression-from-scratch

## Oracle

Thử nhiều `epsilon`; hai gradient phải gần nhau trong tolerance đã ghi.

## Required receipt

- Chạy `python scripts/run_lab.py --lab 3` từ repository root; PowerShell/Bash đầy đủ nằm trong README.
- JSON phải có `status=starter-example-completed`; trong `result` cần thấy analytic gradient, finite-difference gradient và `gradient_check=true`.
- Learning log cục bộ ghi seed/config, runtime, phép kiểm riêng của lab và ít nhất một limitation hoặc failure.
- Tự trả lời: “Output này chứng minh được gì, và chưa chứng minh được gì?”

## Oracle thuật ngữ

- History cho thấy `loss`; gradient check so `gradient`; learning log giải thích `learning rate` cập nhật parameter và tác động prediction.
- Trả lời câu `Tự giải thích` bằng lời của bạn, trỏ tới evidence trên; không chỉ chép glossary.

## Gợi ý nếu kết quả khác

Nếu lệch, kiểm dấu, phép lấy trung bình và công thức central difference.

Đây là gợi ý tự kiểm, không phải bài cần gửi. Không commit evidence, secret, dữ liệu cá nhân, raw dataset lớn
hoặc output cloud trả phí.
