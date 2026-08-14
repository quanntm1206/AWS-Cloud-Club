# Tuần 15 - Inference API và contracts

## Mục tiêu tuần

Thiết kế inference contract và error boundary.

## Vì sao tuần này quan trọng

Inference API là ranh giới giữa model và sản phẩm. Contract tốt giúp lỗi của client, lỗi artifact và giới hạn vận hành được xử lý khác nhau.

**Ví dụ gần gũi:** Payload thiếu cột nên trả 422; model chưa load là lỗi dịch vụ 503, không phải lỗi người gọi.

## Kiến thức cốt lõi

- Inference contract khóa request/response schema, model version, threshold, error codes và limits.
- Validation lỗi client trả 4xx; artifact/service failure trả 5xx, chi tiết nội bộ chỉ vào log an toàn.
- Health/readiness không train; predict dùng đúng preprocessing artifact và không nhận target.
- Input Group/payload/timeout limits là guardrail; không log raw sensitive features.

## Từ khóa tuần này

**Thuật ngữ mới hoặc trọng tâm:** `API contract`, `latency`

**Ôn lại:** `data contract`, `artifact`, `inference`, `schema`

**Áp dụng:** Định nghĩa `API contract`, đo `latency`, rồi gửi sample hợp lệ và sai qua `inference`; thực thi `data contract` trước khi load `artifact` và không đưa raw feature vào response.

## Giải thích khái niệm

### Request và response

**Cách hình dung:** `API contract`: Quy ước rõ về input, output, status code và lỗi của inference service. Client và server cùng dựa vào contract để trao đổi data hợp lệ.

**Vì sao quan trọng:** API contract tách caller error khỏi service failure bằng request, response và error shape ổn định.

**Ví dụ xuyên suốt:** `API contract`: Payload thiếu tenure trả về 422 thay vì 500.

**Dễ nhầm với:** API contract mô tả hành vi; data contract tập trung vào quy tắc input data.

**Tự kiểm tra:** Request, response và error case nào phải được `API contract` giữ ổn định?

### Latency là một distribution

**Cách hình dung:** `latency`: Thời gian từ khi nhận request đến khi trả response. Cần đo trong điều kiện được nêu rõ như trạng thái warm-up và batch size.

**Vì sao quan trọng:** Latency quyết định inference có đáp ứng product deadline hay không; percentile hữu ích hơn một request nhanh đơn lẻ.

**Ví dụ xuyên suốt:** `latency`: Đo warm latency cho mini-batch gồm 16 sample.

**Dễ nhầm với:** Latency đo thời gian; throughput đo lượng công việc hoàn tất mỗi đơn vị thời gian.

**Tự kiểm tra:** Latency percentile nào phản ánh product deadline tốt hơn một request nhanh đơn lẻ?

## Kết nối kiến thức cũ

`data contract` và `schema` bảo vệ request trước khi `artifact` thực hiện `inference`. Status code ổn định cùng latency đã đo cho thấy serving boundary hoạt động đúng contract.

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


1. Gửi valid, missing, wrong-type, unknown-category payload.
2. Kiểm success/422/503 theo contract.
3. Đo warm latency mini input group và ghi giới hạn phép đo.

## Lab

**lab-14:** Local API valid/invalid payload. Môi trường chính: `local`.

## Dấu hiệu bạn đã hiểu

Bạn gửi được payload đúng/sai, nhận status phù hợp và xác nhận API dùng chính preprocessing đã lưu.

## Tự kiểm tra

1. 422 khác 500 thế nào?
2. Health khác readiness?
3. Vì sao không log raw request?

## Kết quả hướng tới

API demo; lưu kèm lệnh đã chạy, cấu hình, metric, thời gian chạy và một điều còn hạn chế.

## Core vs stretch

- **Cốt lõi:** Kiểm valid/invalid API contract, health/readiness và log không chứa raw feature.
- **Mở rộng:** Đo latency mini input group hoặc thêm payload limit với test rõ.

## Lỗi thường gặp

- Lộ stack trace cho client.
- API tự viết preprocessing khác training.

## Khi mắc kẹt

Gọi handler hoặc API với một request tối thiểu. Khi có 500, đọc server log nhưng không đưa stack trace vào response.

## Nguồn

Nguồn nên đọc: FastAPI request validation/error handling và HTTP status semantics trong tài liệu chính thức.
