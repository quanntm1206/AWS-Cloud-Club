# Kết quả tham khảo - lab-18-checkpoint-and-resume

## Oracle

Dừng sau một epoch, load checkpoint rồi chạy tiếp; phân biệt best với last.

## Required receipt

- Chạy `python scripts/run_lab.py --lab 18` từ repository root; PowerShell/Bash đầy đủ nằm trong README.
- JSON phải có `status=starter-example-completed`; trong `result` cần thấy smoke metadata; notebook thật lưu model/optimizer/epoch/config.
- Learning log cục bộ ghi seed/config, runtime, phép kiểm riêng của lab và ít nhất một limitation hoặc failure.
- Tự trả lời: “Output này chứng minh được gì, và chưa chứng minh được gì?”

## Oracle thuật ngữ

- Resume checkpoint giữ optimizer/epoch/history; fine-tuning nếu làm có learning rate riêng; early stopping chỉ nhìn validation set.
- Trả lời câu `Tự giải thích` bằng lời của bạn, trỏ tới evidence trên; không chỉ chép glossary.

## Gợi ý nếu kết quả khác

Nếu load lỗi, so architecture, label mapping, config và optimizer state.

Đây là gợi ý tự kiểm, không phải bài cần gửi. Không commit evidence, secret, dữ liệu cá nhân, raw dataset lớn
hoặc output cloud trả phí.
