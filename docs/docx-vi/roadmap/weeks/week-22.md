# Tuần 22 - Đưa model lên Lambda, giữ mọi thứ riêng tư

## Mục tiêu tuần

Triển khai inference serverless nhỏ, gọi riêng tư, đọc log rồi dọn sạch trong cùng phiên.

## Vì sao tuần này quan trọng

Training model chỉ là nửa đầu công việc. Khi model chạy sau một service boundary, input sai, artifact
lỗi và log nhạy cảm đều trở thành vấn đề engineering. Private invoke cho bạn học đúng phần này mà không
cần mở endpoint ra Internet.

## Kiến thức cốt lõi

- Lambda handler có contract rõ; lỗi JSON/type trả response có chủ đích.
- Artifact portable nằm trong S3; checksum và schema được kiểm trước khi score.
- Memory 512 MB, timeout 15 giây, reserved concurrency 1 giúp thu hẹp blast radius, nhưng không phải
  hard spending cap.
- CloudWatch log không chứa raw payload/secret và có retention một ngày.
- Tag `ExpiresAt` chỉ là metadata nhắc cleanup, không tự xóa stack.

## Từ khóa tuần này

**Thuật ngữ mới hoặc trọng tâm:** `Lambda`, `CloudWatch Logs`, `API contract`

**Ôn lại:** `IAM`, `S3`, `budget alert`

**Áp dụng:** Chạy `inference` trong `Lambda` theo `API contract`, kiểm `CloudWatch Logs` không chứa sample nhạy cảm, rồi review các control `IAM`, `S3` và `budget alert` từ tuần trước.

## Giải thích khái niệm

### Lambda execution và log

**Cách hình dung:** `Lambda`: Dịch vụ chạy hàm serverless theo request mà không quản máy chủ. AWS cấp execution environment và tính phí resource dùng cho mỗi invocation. `CloudWatch Logs`: Nơi lưu log runtime trên AWS; cần tránh dữ liệu nhạy cảm và đặt retention. Log group cần retention, access control và quy tắc không ghi sensitive value.

**Vì sao quan trọng:** Lambda cần input và output rõ ràng; CloudWatch Logs cho biết version nào đã chạy và vì sao request lỗi.

**Ví dụ xuyên suốt:** `Lambda`: Dùng private invoke để chạy tabular inference. `CloudWatch Logs`: Đặt retention một ngày cho Lambda log group.

**Dễ nhầm với:** Lambda là compute; S3 là object storage. CloudWatch Logs lưu runtime log; CloudWatch metric lưu số đo.

**Tự kiểm tra:** `Lambda` result và field nào trong `CloudWatch Logs` chứng minh đúng model version đã chạy?

### API contract tại boundary

**Cách hình dung:** `API contract`: Quy ước rõ về input, output, status code và lỗi của inference service. Client và server cùng dựa vào contract để trao đổi data hợp lệ.

**Vì sao quan trọng:** API contract giữ cloud invocation tương thích với local caller và làm error có thể chẩn đoán.

**Ví dụ xuyên suốt:** `API contract`: Payload thiếu tenure trả về 422 thay vì 500.

**Dễ nhầm với:** API contract mô tả hành vi; data contract tập trung vào quy tắc input data.

**Tự kiểm tra:** Cloud response có còn thỏa cùng `API contract` với local caller không?

## Kết nối kiến thức cũ

Các control `IAM`, `S3` và `budget alert` vẫn hoạt động khi `Lambda` phục vụ request. Response cùng log entry đã redact cho thấy access, storage và cost guardrail vẫn bao quanh deployment.

## Lịch 8-10 giờ

| Hoạt động | Giờ |
|---|---:|
| Đọc handler, template và policy | 2 |
| Test handler local với input đúng/sai | 2 |
| Deploy, private invoke, xem log | 3 |
| Cleanup và residual scan | 1 |
| Learning log và tự đánh giá | 1 |

## Guided practice

1. Gọi handler local với valid JSON, malformed JSON, thiếu field và sai type.
2. Mở terminal riêng, đặt timer cleanup; chạy cost check và preflight trước deploy.
3. Deploy stack, invoke Lambda bằng AWS CLI tối đa vài lần, đọc log.
4. Cleanup ngay; scan phải fail-closed nếu AWS CLI lỗi hoặc thiếu quyền.

## Lab

**lab-20:** S3 + private Lambda invoke + Logs + cleanup. Không tạo API Gateway hay public URL.

## Tự kiểm tra

1. Private invoke loại bỏ rủi ro/thành phần nào?
2. Vì sao concurrency 1 không phải giới hạn tổng chi phí?
3. `ExpiresAt` khác TTL tự động ở điểm nào?

## Kết quả hướng tới

Một inference lifecycle nhỏ nhưng đầy đủ: artifact có checksum, contract chạy đúng, log sạch, residual
scan sạch và có lịch kiểm Billing lại.

## Dấu hiệu bạn đã hiểu

Bạn giải thích được vì sao private invoke vẫn cần contract, logs, giới hạn runtime và cleanup.

## Core vs stretch

- **Core:** private invoke valid/invalid rồi cleanup.
- **Stretch:** giải thích trên giấy cách API Gateway thêm attack surface và request cost; không triển khai.

## Lỗi thường gặp

- Đóng terminal sau deploy rồi quên cleanup.
- Nghĩ tag hết hạn sẽ tự xóa tài nguyên.
- Thấy residual scan lỗi quyền nhưng vẫn kết luận “zero residual”.

## Khi mắc kẹt

Nếu bất kỳ lệnh nào lỗi sau khi deploy bắt đầu, dừng và chạy cleanup dry-run ngay. Đọc exact names, chạy
execute, rồi residual scan. Nếu scan không hoàn tất, kiểm Console hoặc nhờ quản trị account; đừng đoán.

## Bạn đã sẵn sàng chuyển tuần khi

- Private Lambda trả đúng contract cho cả request hợp lệ và không hợp lệ.
- Log không có credential hoặc raw record.
- Stack, bucket, function, log group và role không còn sau cleanup.

## AWS cost gate

Lifecycle bắt buộc: `Pre-check -> Estimate -> Dry-run -> Deploy -> Verify -> Cleanup -> Residual scan -> Cost audit`.
Budget có thể trễ; planning envelope không phải bill guarantee.

## Nguồn

[Lambda pricing](https://aws.amazon.com/lambda/pricing/),
[S3 pricing](https://aws.amazon.com/s3/pricing/) và `docs/sources.yml`.
