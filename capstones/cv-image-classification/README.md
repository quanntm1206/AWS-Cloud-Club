# Capstone B - Image Classification

Chọn **Colab Free hoặc Kaggle Free**, không chạy cả hai. Chạy `cpu-mini` trước. Core: frozen backbone,
3-5 epoch tối đa nếu có GPU, early stopping, checkpoint mỗi epoch, macro/per-class metrics, confusion matrix,
tối đa 20 failure images; nếu ít hơn thì export toàn bộ và ghi count/limitation và model card. Fine-tuning là stretch.

AWS core chỉ dừng ở artifact upload/checksum và architecture/cost decision. Không SageMaker training,
notebook instance, real-time endpoint hoặc GPU AWS.

## Tổng kết năng lực

Sau khi tải artifact khỏi runtime, lưu model checkpoint, metric, failure images, report, model card và ADR
trong thư mục local do bạn chọn. Dùng rubric để tự đánh giá; không xuất bản hoặc gửi các file này cho ai.

