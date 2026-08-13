# Tuần 16 - Docker, CI và artifact versioning

## Mục tiêu tuần

Đóng gói, CI, version artifact; hiểu image trade-off.

## Vì sao tuần này quan trọng

Docker đóng gói runtime; CI kiểm các quy tắc mỗi lần code đổi. Cả hai giúp model chạy nhất quán nhưng không thay thế kiểm tra chất lượng dữ liệu.

**Ví dụ gần gũi:** Image có checksum đúng vẫn có thể chứa model sai; manifest và test trả lời hai câu hỏi khác nhau.

## Kiến thức cốt lõi

- Container đóng runtime/dependency, không bảo đảm model đúng; dùng base nhỏ, non-root user.
- Đặt dependency layer trước source, loại data/artifact/.venv khỏi build context.
- CI chạy lint/type/test/validators offline; roadmap không auto-deploy AWS.
- Artifact manifest có schema/version/checksum/config/metrics; checksum không thay provenance.
- Production monitoring cần cả service signals (latency/error) và ML signals (schema, drift, prediction distribution); drift là cảnh báo điều tra, không tự chứng minh model đã sai.

## Từ khóa tuần này

**Thuật ngữ mới hoặc trọng tâm:** `container`, `CI`

**Ôn lại:** `API contract`, `artifact`, `reproducibility`, `latency`

**Áp dụng:** Đóng package/API contract vào `container`, dùng `CI` chạy data validation, parity và test artifact; đo latency nhỏ rồi cleanup container để giữ reproducibility.

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


1. Build image, smoke health/predict, kiểm non-root.
2. Chạy CI commands từ clean checkout.
3. Đổi một byte artifact và xác nhận checksum fail.

## Lab

**lab-15:** Docker/local CI smoke. Môi trường chính: `local`.

## Dấu hiệu bạn đã hiểu

Bạn build image non-root, smoke `/health` và `/predict`, rồi phát hiện artifact bị đổi bằng checksum.

## Tự kiểm tra

1. latest tag có rủi ro gì?
2. Image/model cần version riêng vì sao?
3. Checksum chứng minh gì?

## Kết quả hướng tới

mốc năng lực 4; lưu kèm lệnh đã chạy, cấu hình, metric, thời gian chạy và một điều còn hạn chế.

## Core vs stretch

- **Cốt lõi:** Build image non-root, smoke service, kiểm checksum và chạy CI offline.
- **Mở rộng:** Đo image size/startup time hoặc thử artifact checksum failure; không thêm auto-deploy cloud.

## Lỗi thường gặp

- Đưa secret/data vào image.
- CI tự deploy cloud.

## Khi mắc kẹt

Nếu Docker tốn thời gian, chạy test local trước. Kiểm `.dockerignore`, build context và log container theo thứ tự.

## Nguồn

Nguồn nên đọc: Dockerfile best practices, non-root containers và GitHub Actions documentation.
