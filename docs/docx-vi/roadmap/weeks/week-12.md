# Tuần 12 - Mini-project tabular

## Mục tiêu tuần

Tổng hợp pipeline tabular có thể tái lập.

## Vì sao tuần này quan trọng

Mini-project là lúc ghép các mảnh thành một quy trình người khác có thể chạy lại, không phải lúc thêm thật nhiều thuật toán.

**Ví dụ gần gũi:** Một model file không đủ nếu thiếu schema, threshold, config và cách tái tạo đúng preprocessing.

## Kiến thức cốt lõi

- Mini-project khóa problem, contract, split, baseline và success criteria trước tối ưu.
- Training xuất model, portable artifact, metrics, manifest và model card.
- Reproduction guide bắt đầu từ clean environment, ghi command/config/seed/input/output.
- Model card nêu intended/out-of-scope use, data, metrics, subgroup, limitation và rollback signal.

## Từ khóa tuần này

**Thuật ngữ mới hoặc trọng tâm:** `artifact`, `manifest`, `inference`

**Ôn lại:** `schema`, `data split`, `pipeline`

**Áp dụng:** Khóa `schema` và `data split`, rồi chạy `pipeline`; lưu `artifact` kèm `manifest`, load trong process mới để `inference`, sau đó so prediction, metric và checksum.

## Giải thích khái niệm

### Artifact và manifest

**Cách hình dung:** `artifact`: File model, config, metric và metadata cần để tái tạo hoặc phục vụ dự đoán. Artifact cần được version và kèm đủ provenance để kiểm chứng cách nó được tạo. `manifest`: Bản kê mô tả nội dung, phiên bản, checksum và nguồn gốc artifact. Checksum giúp phát hiện file bị đổi, còn metadata giải thích cách tạo các file đó.

**Vì sao quan trọng:** Artifact chỉ hữu ích khi manifest xác định đúng schema, configuration, checksum và source run.

**Ví dụ xuyên suốt:** `artifact`: model.joblib và manifest.json tạo thành artifact. `manifest`: Manifest ghi seed, feature order và SHA-256 checksum.

**Dễ nhầm với:** Artifact là gói model đã lưu; checkpoint là training state để resume. Manifest mô tả file và provenance; artifact chứa các file thật.

**Tự kiểm tra:** Reviewer có xác định được mọi file và source run chỉ từ `artifact` và `manifest` không?

### Inference từ state đã lưu

**Cách hình dung:** `inference`: Dùng model đã train để tạo prediction cho input mới. Nó phải áp đúng preprocessing và feature order đã học khi training.

**Vì sao quan trọng:** Inference phải tái tạo preprocessing và feature order lúc training mà không phụ thuộc notebook state.

**Ví dụ xuyên suốt:** `inference`: Load artifact rồi dự đoán churn cho một khách hàng mới.

**Dễ nhầm với:** Inference dùng model đã train; training cập nhật parameter của model.

**Tự kiểm tra:** `inference` có tái tạo cùng preprocessing và feature order mà không dựa vào notebook state không?

## Kết nối kiến thức cũ

`schema`, `data split` và `pipeline` đã lưu giờ trở thành provenance trong artifact manifest. Prediction sau reload cùng checksum khớp cho thấy process mới dùng đúng learned path.

## Lịch 8-10 giờ

| Hoạt động | Giờ |
|---|---:|
| Đọc và ghi chú | 2 |
| Guided practice | 2 |
| Lab | 3 |
| Assessment/error analysis | 1 |
| Learning log và tự đánh giá | 1 |
| Review/hoàn thiện | 0 |

## Guided practice


1. Chạy churn pipeline mini end-to-end.
2. Reload artifact ở process mới và kiểm prediction output agreement.
3. Chạy reproduction guide từ clean shell.

## Lab

**lab-11:** Mini-project tabular end-to-end. Môi trường chính: `local`.

## Dấu hiệu bạn đã hiểu

Từ clean shell, bạn train, lưu, load lại artifact và tạo cùng prediction trong tolerance đã ghi.

## Tự kiểm tra

1. Artifact cần gì ngoài weights?
2. Model card phải nêu misuse nào?
3. Chứng minh run tái lập bằng gì?

## Kết quả hướng tới

mốc năng lực 3 + model card; lưu kèm lệnh đã chạy, cấu hình, metric, thời gian chạy và một điều còn hạn chế.

## Core vs stretch

- **Cốt lõi:** Chạy mini-project từ clean shell; load artifact ở process mới và hoàn thiện model card.
- **Mở rộng:** So config `mini` với đúng một controlled change; ghi cả negative result.

## Lỗi thường gặp

- Chỉ lưu notebook phụ thuộc cell state, thiếu artifact tái lập.
- Thiếu split manifest/config.

## Khi mắc kẹt

Chạy `mini` trước, kiểm từng artifact. Khi output agreement sai, so config và feature order trước khi train lại.

## Nguồn

Nguồn nên đọc: model persistence của scikit-learn và model-card references trong `docs/sources.yml`.
