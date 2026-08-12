# Thiết kế chương trình Machine Learning Engineer 24 tuần

**Ngày chốt:** 2026-08-12  
**Đơn vị:** AWS Cloud Club  
**Hình thức:** Tự học cá nhân, có mốc năng lực và artifact local  
**Thời lượng:** 24 tuần, 8-10 giờ/tuần  
**Đối tượng:** Đã biết lập trình, chưa học Machine Learning

## 1. Mục tiêu

Sau 24 tuần, người học có thể:

1. Giải thích quy trình ML từ bài toán, dữ liệu, baseline, huấn luyện, đánh giá đến triển khai.
2. Xây dựng pipeline tabular classification có khả năng tái lập và tránh data leakage.
3. Xây dựng mô hình image classification bằng transfer learning trên Colab hoặc Kaggle miễn phí.
4. Đóng gói model, viết inference API, test đầu vào/đầu ra, logging và theo dõi lỗi cơ bản.
5. Triển khai capstone tabular lên AWS theo mô hình chi phí thấp: S3 + Lambda, API Gateway tùy chọn.
6. Hoàn thiện Tổng kết năng lực local gồm notebook, source code, test, model card, báo cáo thí nghiệm và hướng dẫn tái lập.

## 2. Nguyên tắc thiết kế

- **Local-first:** học thuật toán và huấn luyện trên máy cá nhân trước.
- **Free-compute-first:** bài train nặng chạy trên Colab Free hoặc Kaggle Free; luôn có CPU fallback và mini dataset.
- **AWS for MLOps, not heavy training:** AWS dùng cho artifact storage, serverless inference, IAM, logging và cost hygiene.
- **One primary path:** mỗi lab chỉ yêu cầu một môi trường chính; Colab/Kaggle là hai lựa chọn tương đương, không buộc chạy cả hai.
- **Reproducible by default:** seed, split, dependency lock, config, metric và artifact manifest được lưu cục bộ.
- **Minh chứng tự đánh giá:** mỗi giai đoạn tạo đầu ra để người học tự kiểm tra; không gửi ai và không chỉ đọc lý thuyết.
- **Cost-safe by default:** không GPU AWS, NAT Gateway, SageMaker endpoint chạy nền, hyperparameter sweep hoặc tài nguyên không tag.

## 3. Kiến trúc chương trình

| Giai đoạn | Tuần | Trọng tâm | Sản phẩm chính |
|---|---:|---|---|
| A. Nền tảng dữ liệu và toán | 1-4 | NumPy, pandas, visualization, đại số tuyến tính, xác suất | EDA notebook + bài cài đặt metric |
| B. ML cổ điển | 5-8 | supervised learning, preprocessing, validation, metrics | Pipeline classification tái lập |
| C. ML thực hành | 9-12 | trees, ensembles, tuning có kiểm soát, interpretability | Mini-project tabular |
| D. Engineering nền tảng | 13-16 | package hóa, test, API, Docker, CI | Local inference service |
| E. Deep learning và CV | 17-20 | neural networks, PyTorch, transfer learning, error analysis | CV model + model card |
| F. AWS capstone | 21-24 | IAM, S3, Lambda, observability, cleanup, tổng kết năng lực | Tabular AWS capstone + CV architecture |

## 4. Phân bổ 8-10 giờ mỗi tuần

- 2 giờ: đọc/xem tài liệu và ghi chú câu hỏi.
- 2 giờ: guided notebook hoặc code-along.
- 3-4 giờ: lab độc lập.
- 1 giờ: quiz, error analysis hoặc code review checklist.
- 1 giờ: cập nhật learning log, tự đánh giá, kết quả và retrospective.

Tuần có Mốc năng lực hoặc capstone có thể chuyển 1 giờ lý thuyết sang implementation nhưng không vượt 10 giờ.

## 5. Chiến lược Colab và Kaggle Free

### 5.1 Mặc định

- Tabular: chạy local CPU; Colab/Kaggle chỉ là đường thay thế.
- Computer Vision: người học chọn **một** trong Colab hoặc Kaggle.
- Không ghi cứng loại GPU hoặc quota vì tài nguyên miễn phí thay đổi theo thời điểm.
- Notebook tự phát hiện accelerator, in thiết bị đang dùng, chuyển sang CPU nếu không có GPU.
- Dataset CV có `mini` profile để hoàn thành lab bằng CPU.
- Mỗi run giới hạn 3-5 epoch, frozen backbone trước, early stopping, checkpoint mỗi epoch.
- Không dùng sweep; tối đa ba cấu hình được chọn trước và chạy tuần tự khi còn quota.
- Artifact phải tải về hoặc đồng bộ sau mỗi run; runtime miễn phí không được xem là nơi lưu trữ bền vững.

### 5.2 Notebook contract

Mọi notebook training có cùng thứ tự cell:

1. `Environment check`
2. `Install/verify dependencies`
3. `Configuration and seed`
4. `Data acquisition with mini fallback`
5. `Data validation`
6. `Baseline`
7. `Training`
8. `Evaluation and error analysis`
9. `Save artifacts and manifest`
10. `Export/download instructions`
11. `Release accelerator/runtime`

## 6. AWS cost-safety contract

### 6.1 Dịch vụ bắt buộc

- IAM: least-privilege role/policy cho lab.
- S3: lưu model artifact và test payload nhỏ.
- Lambda: inference tabular CPU, timeout và memory giới hạn.
- CloudWatch Logs: log ngắn, retention một ngày.
- AWS Budgets: cảnh báo actual và forecasted; tài liệu phải nói rõ đây không phải hard cap.

### 6.2 Dịch vụ tùy chọn

- API Gateway HTTP API: chỉ tạo trong lab ngắn, xóa ngay sau verify.
- ECR: chỉ khi chọn container path; ưu tiên ZIP Lambda để giảm surface và storage.
- SageMaker: chỉ mô tả kiến trúc và bài tập ước tính chi phí. Không có bước bắt buộc tạo training job, notebook instance hoặc endpoint.

### 6.3 Dịch vụ bị cấm trong đường học mặc định

- GPU instance trên AWS.
- NAT Gateway.
- SageMaker real-time endpoint.
- OpenSearch domain, RDS, Redshift, EKS hoặc ECS service chạy nền.
- Marketplace AMI hoặc paid subscription.
- Multi-region replication.
- Hyperparameter tuning job.

### 6.4 Giới hạn kỹ thuật

- Region mặc định: `us-east-1`, cho phép override rõ ràng qua `AWS_REGION`.
- Project tag: `Project=ml-roadmap`; thêm `Owner`, `Environment=learning`, `ExpiresAt`.
- Artifact tabular đã nén: mục tiêu dưới 50 MB; hard validation dưới 200 MB.
- Dữ liệu upload S3 cho lab: mục tiêu dưới 100 MB; hard validation dưới 500 MB.
- Lambda: memory 512 MB, timeout 15 giây, reserved concurrency 1 khi hỗ trợ.
- CloudWatch log retention: một ngày.
- S3 lifecycle: xóa object lab sau bảy ngày; bucket versioning tắt cho lab mặc định.
- API public chỉ tồn tại trong phiên lab; không lưu secret trong URL hoặc repository.

### 6.5 Quy trình bắt buộc cho mọi AWS lab

`Pre-check -> Cost estimate -> Dry-run -> Deploy -> Verify -> Cleanup -> Residual scan -> Cost audit`

Không được đánh dấu lab hoàn thành nếu thiếu bằng chứng cleanup và residual scan.

### 6.6 Kill switch

- Cleanup chỉ thao tác trên resource có đủ tag và prefix của project.
- Mặc định `--dry-run`; xóa thật cần `--execute` và xác nhận project ID.
- Script idempotent: chạy lần hai không lỗi khi tài nguyên đã xóa.
- In rõ ARN/name, Region và loại tài nguyên trước khi xóa.
- Không quét hoặc xóa resource ngoài allowlist S3, Lambda, API Gateway, IAM lab role/policy, CloudWatch log group và ECR lab repository.

## 7. Hai capstone

### 7.1 Capstone A - Tabular classification, bắt buộc

**Bài toán:** dự đoán churn hoặc rủi ro trên bộ dữ liệu công khai nhỏ.

**Luồng:** data validation -> split -> preprocessing pipeline -> baseline -> candidate models -> threshold selection -> error analysis -> model card -> export artifact -> S3 -> Lambda inference -> logging -> cleanup.

**Tiêu chí:**

- Pipeline chống leakage, split có lý do, metric phù hợp imbalance.
- Có baseline và so sánh tối đa ba model.
- Test schema đầu vào, missing value, unknown category và response contract.
- AWS deployment không cần nâng cấp Paid Plan theo đường mặc định.
- Cleanup report không còn resource lab trong allowlist.

### 7.2 Capstone B - Image classification, mở rộng có hướng dẫn đầy đủ

**Bài toán:** phân loại ảnh quy mô nhỏ bằng transfer learning.

**Luồng:** train trên Colab hoặc Kaggle -> checkpoint -> error analysis -> model card -> export artifact -> upload S3 tùy chọn -> thiết kế kiến trúc inference AWS trên giấy.

**Tiêu chí:**

- Frozen-backbone baseline; fine-tuning giới hạn là phần mở rộng.
- Có confusion matrix, per-class metric và tối đa 20 ảnh failure cases được phân nhóm; nếu ít hơn thì export toàn bộ và ghi limitation.
- CPU mini profile chạy được khi không có GPU.
- Không triển khai endpoint CV trên AWS trong đường mặc định.
- Bài AWS kết thúc ở artifact integrity, cost estimate và architecture decision record.

## 8. DOCX

File cuối: `dist/ML-Roadmap-24-Tuan-AWS-Cloud-Club.docx`.

Nội dung:

1. Trang bìa và cách dùng tài liệu.
2. Chuẩn đầu vào/đầu ra, lịch học và rubric.
3. Roadmap 24 tuần chi tiết.
4. Hướng dẫn local, Colab Free và Kaggle Free.
5. Hướng dẫn AWS Free Plan, budget, IAM và cost guardrails.
6. Danh mục lab, Mốc năng lực và hai capstone.
7. Hướng dẫn Kết quả hướng tới, Minh chứng đạt mốc và Tổng kết năng lực local.
8. Troubleshooting, glossary và nguồn chính thức có ngày kiểm chứng.

Preset: `compact_reference_guide`; khổ Letter, lề 1 inch, Calibri 11 pt, line spacing 1.25, bảng full-width 9360 DXA. Các cảnh báo chi phí dùng một named override màu vàng nhạt, nhất quán toàn tài liệu.

## 9. Phát hành bộ khung và workflow local

Chủ repo phát hành bộ khung trên GitHub. Người học chỉ clone bằng
`git clone https://github.com/quanntm1206/AWS-Cloud-Club.git` hoặc tải archive. Repository phải setup được trên Windows/macOS/Linux và
chạy quick validation không cần AWS credentials. Workflow người học không có bước đóng góp lại repository,
gửi bài hoặc xuất bản hồ sơ công khai. Artifact, learning log và test evidence lưu local để tự đánh giá.

Các phần chính:

- `roadmap/`: nội dung từng tuần và Mốc năng lực.
- `labs/`: lab guide, starter code, solution notes tách biệt.
- `notebooks/`: notebook local/Colab/Kaggle theo notebook contract.
- `src/`: code tái sử dụng cho data, train, evaluate và serve.
- `capstones/`: yêu cầu, rubric, starter và report template.
- `aws/`: IaC tối giản, policy, cost guard, cleanup.
- `tests/`: unit, integration offline, notebook smoke và AWS template checks.
- `scripts/`: setup, lint, test, validate notebooks, audit cost safety.
- `.github/workflows/`: CI offline; không deploy AWS.

## 10. Definition of done

- DOCX render thành PNG; mọi trang được kiểm tra không clipping, overlap, bảng vỡ hoặc thiếu glyph tiếng Việt.
- Repo không chứa secret, credential, dataset/model lớn hoặc output notebook dư thừa.
- Quickstart chạy từ fresh virtual environment.
- Training smoke test dùng mini data hoàn thành trên CPU.
- Notebook Colab/Kaggle có CPU fallback và export artifact.
- IaC/cost policy vượt qua static checks; CI không tạo AWS resource.
- Cleanup dry-run và mocked idempotency tests pass.
- 24 tuần, Mốc năng lực, lab và capstone trace được tới file cụ thể và tiêu chí tự đánh giá.
- Mọi claim hiện trạng về AWS/Colab/Kaggle có URL chính thức và ngày kiểm chứng.

