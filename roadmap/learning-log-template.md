# Nhật ký học tập - Tuần NN

Nhật ký này dành cho bạn, không phải bài nộp. Viết ngắn nhưng cụ thể: một command hoặc một quan sát thật hữu
ích hơn câu “đã hiểu bài”.

## Mẫu trống

- **Mục tiêu tuần:** Tôi muốn tự giải thích hoặc tự làm được điều gì?
- **Điều đã chạy:** Command, notebook, config và môi trường nào?
- **Bằng chứng:** Metric, test, biểu đồ hoặc kiểm tra nào hỗ trợ kết luận?
- **Một lỗi đáng nhớ:** Triệu chứng, nguyên nhân, cách tôi kiểm tra và sửa.
- **Điều chưa chắc:** Câu hỏi nào vẫn cần quay lại?
- **Quyết định kỹ thuật:** Tôi giữ hoặc loại cách làm nào? Vì sao?
- **Bước nhỏ tiếp theo:** Việc đầu tiên của tuần sau, đủ cụ thể để làm trong 30 phút.

## Ví dụ ngắn - Tuần 07

- **Mục tiêu tuần:** Chọn threshold theo chi phí bỏ sót churn, không chọn theo F1 cao nhất một cách máy móc.
- **Điều đã chạy:** `python scripts/run_lab.py --lab 6`, seed 42, local CPU.
- **Bằng chứng:** Threshold 0.35 tăng recall từ 0.68 lên 0.81; precision giảm từ 0.74 xuống 0.61.
- **Một lỗi đáng nhớ:** Ban đầu tôi chọn threshold trên test. Tôi phát hiện test metric thay đổi sau mỗi lần thử;
  sửa bằng cách chọn trên validation rồi chỉ đánh giá test một lần.
- **Điều chưa chắc:** Khi chi phí false positive thay đổi theo nhóm khách hàng, một threshold chung có còn hợp lý?
- **Quyết định kỹ thuật:** Giữ threshold 0.35 cho giả định chi phí hiện tại; ghi rõ giả định trong report.
- **Bước nhỏ tiếp theo:** Vẽ confusion matrix theo hai nhóm tenure ở lần chạy sau.
