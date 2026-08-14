# Tuần 23 - Nối capstone thành một hệ thống nhỏ có thể giải thích

## Mục tiêu tuần

Nối training local/Colab/Kaggle với artifact, manifest và private Lambda inference.

## Vì sao tuần này quan trọng

Một demo đáng tin không phải chuỗi lệnh chạy may mắn. Manifest giúp bạn trả lời: model nào, schema nào,
threshold nào, được train từ run nào và artifact có bị thay đổi hay không.

## Kiến thức cốt lõi

- Training vẫn ở local/Colab/Kaggle. AWS chỉ lưu portable logistic model và chạy inference ngắn.
- Manifest liên kết model version, feature schema, threshold, checksum và source run.
- CloudFormation quản toàn bộ resource của lab; ownership tags hỗ trợ audit, không tự cleanup.
- Learner path chỉ có private `aws lambda invoke`. Public API là chủ đề kiến trúc để đọc, không thực hành.
- Nếu deploy/upload/output lookup lỗi, stack có thể đã tồn tại; recovery cleanup là bắt buộc.

## Từ khóa tuần này

**Thuật ngữ mới hoặc trọng tâm:** `artifact`, `inference`, `residual scan`

**Ôn lại:** `Lambda`, `CloudWatch Logs`, `API contract`

**Áp dụng:** Ghép promoted `artifact` với private `inference`, rồi chạy `residual scan` sau cleanup; review evidence từ `Lambda`, `CloudWatch Logs` và `API contract` cùng nhau.

## Giải thích khái niệm

### Từ artifact đến inference

**Cách hình dung:** `artifact`: File model, config, metric và metadata cần để tái tạo hoặc phục vụ dự đoán. Artifact cần được version và kèm đủ provenance để kiểm chứng cách nó được tạo. `inference`: Dùng model đã train để tạo prediction cho input mới. Nó phải áp đúng preprocessing và feature order đã học khi training.

**Vì sao quan trọng:** Inference chỉ đáng tin khi artifact đã deploy truy được về local training evidence và schema chính xác.

**Ví dụ xuyên suốt:** `artifact`: model.joblib và manifest.json tạo thành artifact. `inference`: Load artifact rồi dự đoán churn cho một khách hàng mới.

**Dễ nhầm với:** Artifact là gói model đã lưu; checkpoint là training state để resume. Inference dùng model đã train; training cập nhật parameter của model.

**Tự kiểm tra:** Mỗi `inference` result có truy được deployed `artifact` về schema và source run không?

### Residual scan sau lần chạy

**Cách hình dung:** `residual scan`: Bước kiểm sau cleanup để tìm tài nguyên project còn sót. Nó phải kiểm mọi service liên quan và chỉ ra phần nào vẫn cần xóa.

**Vì sao quan trọng:** Residual scan là bằng chứng sau cleanup rằng cloud demo ngắn không để lại project resource đã biết.

**Ví dụ xuyên suốt:** `residual scan`: Residual scan kiểm CloudFormation, S3, Lambda, CloudWatch Logs và IAM.

**Dễ nhầm với:** Residual scan xác minh không còn resource; cleanup thực hiện hành động xóa.

**Tự kiểm tra:** `residual scan` phải kiểm những service nào sau cloud run ngắn?

## Kết nối kiến thức cũ

`Lambda` response, `CloudWatch Logs` và `API contract` giờ đi cùng promoted artifact như deployment evidence. Scan sau cleanup khép vòng kiểm bằng cách xác nhận cloud run ngắn không để lại resource đã biết.

## Lịch 8-10 giờ

| Hoạt động | Giờ |
|---|---:|
| Ôn artifact contract và manifest | 2 |
| Train mini profile, kiểm parity | 2 |
| Chạy end-to-end private invoke | 3 |
| Failure drill và cleanup | 1 |
| Learning log và tự đánh giá | 1 |

## Guided practice

1. Train mini profile ngoài AWS; so portable model với sklearn trên cùng known requests.
2. Kiểm checksum, schema và threshold trước upload.
3. Chạy end-to-end private invoke; không load test, không tạo public endpoint.
4. Diễn tập một failure sau deploy và đọc recovery command trước khi cleanup.

## Lab

**lab-20:** capstone end-to-end qua private Lambda. API Gateway chỉ được phân tích trên sơ đồ/pricing.

## Tự kiểm tra

1. Vì sao không ship thẳng `joblib` phụ thuộc runtime?
2. Manifest ngăn loại drift nào?
3. Sau upload lỗi, vì sao vẫn phải kiểm stack?

## Kết quả hướng tới

Bạn demo được luồng train -> portable artifact -> S3 -> private Lambda -> cleanup, đồng thời giải thích
được từng guard thay vì chỉ đọc output xanh.

## Dấu hiệu bạn đã hiểu

Bạn lần ngược được một prediction về đúng artifact, schema, threshold và source run.

## Core vs stretch

- **Core:** end-to-end private invoke, tối đa vài request.
- **Stretch:** vẽ kiến trúc authenticated/throttled API và liệt kê guard cần có; không deploy.

## Lỗi thường gặp

- Train trên SageMaker/EC2 chỉ vì còn credit.
- Thêm public URL để demo trông “thật” hơn.
- Để stack qua đêm vì tin `ExpiresAt` tự xóa.

## Khi mắc kẹt

Quay về handler local và known request. Nếu AWS đã tạo stack, ưu tiên cleanup trước debugging. Một demo
local có giải thích tốt an toàn hơn một stack sống mà bạn không kiểm soát.

## Bạn đã sẵn sàng chuyển tuần khi

- Portable/sklearn parity đạt trên known requests.
- Bạn chứng minh được checksum + schema + source run.
- Residual scan hoàn tất, không có known infrastructure còn sót.

## AWS cost gate

Không nâng Paid Plan để hoàn thành core. Không SageMaker, EC2, NAT Gateway, API Gateway hoặc Bedrock.
Nếu pricing/eligibility không xác minh được, dùng local simulation.

## Nguồn

[AWS Pricing Calculator](https://calculator.aws/) và `docs/sources.yml`.
