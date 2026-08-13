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

**Áp dụng:** Dùng `Lambda` thực hiện inference theo `API contract`, kiểm `CloudWatch Logs` không lộ sample nhạy cảm; ôn IAM và S3 từ tuần trước.

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
