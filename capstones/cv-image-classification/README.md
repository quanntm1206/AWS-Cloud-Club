# Capstone B - Image Classification bằng free compute

Capstone mở rộng này giúp bạn trải nghiệm một vòng Computer Vision thực tế mà không dùng GPU AWS. Bạn chọn
**Colab Free hoặc Kaggle Free**, train frozen-backbone model, phân tích lỗi rồi viết quyết định kiến trúc AWS
trên giấy. Không cần chạy cả hai nền tảng.

## Bạn sẽ tạo ra gì?

- Checkpoint tốt nhất và checkpoint có thể resume; metrics tổng hợp/per-class; confusion matrix.
- Tối đa 20 failure records hoặc toàn bộ nếu ít hơn; experiment report và model card.
- `artifacts.zip`, manifest/checksum và ADR giải thích vì sao core path không deploy CV endpoint.

## File map

- [`notebooks/colab.ipynb`](notebooks/colab.ipynb): notebook chạy thật trên Colab.
- [`notebooks/kaggle.ipynb`](notebooks/kaggle.ipynb): cùng workflow cho Kaggle.
- [`configs/cpu-mini.yml`](configs/cpu-mini.yml): 1 epoch, 160 mẫu; luôn chạy trước.
- [`configs/gpu-free.yml`](configs/gpu-free.yml): tối đa 5 epoch, frozen backbone; chỉ khi có GPU miễn phí.
- [`reports/experiment-report.md`](reports/experiment-report.md), [`reports/model-card.md`](reports/model-card.md)
  và [`reports/aws-adr.md`](reports/aws-adr.md): ba tài liệu cần hoàn thiện.
- [`rubric.yml`](rubric.yml): tiêu chí tự đánh giá.

## Giai đoạn 1 - Chọn runtime

1. Mở một notebook bằng [hướng dẫn Colab/Kaggle](../../notebooks/README.md).
2. Chạy environment check và `cpu-mini`. Notebook vẫn cố tải pretrained ResNet18; FakeData chỉ xác nhận
   pipeline, không chứng minh accuracy.
3. Nếu có GPU miễn phí và internet, chuyển `gpu-free`; notebook dùng CIFAR10 subset và pretrained weights.
4. Không quá 3-5 epoch, không hyperparameter sweep. Notebook ghi `last_checkpoint.pt` sau mỗi epoch và cập
   nhật `best_checkpoint.pt` khi validation loss tốt hơn.

## Giai đoạn 2 - Training có kiểm soát

Giữ pretrained normalization, split seed và validation transform cố định; augmentation chỉ áp dụng cho train.
Train head với frozen backbone trước. Fine-tuning block cuối là phần mở rộng, chỉ làm nếu validation và runtime
budget có lý do. Test không tham gia early stopping. Resume từ last checkpoint; đánh giá best checkpoint. Tải
`artifacts.zip` về máy trước khi đóng runtime.

Khi resume ở runtime mới, upload `last_checkpoint.pt` hoặc `artifacts.zip` vào thư mục làm việc rồi đặt
`RESUME=True`. Notebook tự đưa file về đúng `artifacts/last_checkpoint.pt` và dừng rõ nếu không tìm thấy.

## Giai đoạn 3 - Hiểu model sai ở đâu

Báo macro/weighted và từng class cùng support; confusion matrix normalize theo true class. Review lỗi theo quy
tắc confident-wrong, không chọn ảnh thuận mắt. Notebook để `error_type='unreviewed'`; bạn mở từng ảnh và gán
nhóm lỗi dựa trên evidence trước khi tổng hợp taxonomy. Với mỗi nhóm lỗi, ghi giả thuyết và một next experiment.
Không chia sẻ ảnh nhạy cảm hoặc không có quyền sử dụng.

## Giai đoạn 4 - AWS chỉ ở mức artifact và thiết kế

Có thể upload artifact nhỏ/checksum lên S3 nếu đã qua cost gate. Core path không dùng SageMaker training,
notebook instance, real-time endpoint, GPU AWS hoặc public API. Hoàn thiện `reports/aws-adr.md` để so private
Lambda khi artifact phù hợp, batch inference và managed endpoint theo workload; không triển khai endpoint CV.

## Khi nào xem như hoàn thành?

- Notebook chạy từ đầu với `cpu-mini`; pretrained weights phải tải thành công để đạt gate transfer learning.
  Nếu báo quality, run còn phải dùng dataset thật chứ không phải FakeData.
- Frozen backbone được kiểm; best checkpoint, resume state, config, label mapping và manifest đã export.
- Per-class metrics, confusion matrix, failure taxonomy, report và model card hoàn chỉnh.
- ADR nêu constraint, lựa chọn, trade-off và lý do không dùng AWS training/endpoint trong core path.

## Khi mắc kẹt

- **Không có GPU:** giữ CPU-mini hoặc thử free runtime lúc khác; không mua compute.
- **Download dataset lỗi:** dùng FakeData smoke và ghi limitation; chưa được kết luận model quality.
- **Download pretrained weights lỗi:** random-weight fallback chỉ kiểm tra code, chưa đạt gate transfer learning.
- **Out of memory:** giảm batch, image size và sample count; restart runtime sau OOM.
- **Session bị ngắt:** upload checkpoint, kiểm architecture/config/label mapping rồi resume.
- **Metric một class rất thấp:** kiểm support, split, label và confusion matrix trước khi fine-tune.

Lưu artifact và báo cáo cục bộ để tự đánh giá; không xuất bản hoặc gửi cho ai.
