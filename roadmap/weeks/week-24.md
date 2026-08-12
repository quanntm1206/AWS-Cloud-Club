# Tuần 24 - Khép lại capstone như một ML Engineer

## Mục tiêu tuần

Trình bày quyết định kỹ thuật, audit tài nguyên/chi phí và lập kế hoạch 90 ngày tiếp theo.

## Vì sao tuần này quan trọng

ML Engineer giỏi không giữ cloud resource sống chỉ để slide đẹp. Một phần kết tốt phải cho thấy model
tái lập được, giới hạn được nói thật, demo có fallback và hệ thống đã được dọn sạch.

## Kiến thức cốt lõi

- Tổng kết theo problem, constraint, baseline, decision, evidence, failure và reproduction; không chỉ accuracy.
- Demo 5-7 phút dùng local fallback. Không cần AWS resource sống thường trực.
- Residual scan chứng minh state kỹ thuật; Billing chứng minh chi phí nhưng dữ liệu có độ trễ.
- Budget alert được giữ có chủ đích không phải residual infrastructure. Review hoặc xóa thủ công cuối khóa.
- “Done” nghĩa tests pass, model card cập nhật, secret scan sạch, limitation rõ và zero known residual.

## Lịch 8-10 giờ

| Hoạt động | Giờ |
|---|---:|
| Chạy lại từ clean environment | 2 |
| Chuẩn bị demo và fallback | 2 |
| Cleanup, residual scan, cost audit | 2 |
| Rubric, retrospective và kế hoạch 90 ngày | 2 |
| Learning log và tự đánh giá | 1 |

## Guided practice

1. Demo từ clean environment, bấm giờ; tắt AWS rồi thử fallback local.
2. Chạy cleanup dry-run, execute, residual scan. Nếu scan lỗi, xử lý lỗi trước khi kết luận.
3. Kiểm Billing ngay, đặt lịch kiểm lại sau khoảng 12 giờ và ngày kế tiếp.
4. Review Budget alerts; giữ nếu còn học AWS, xóa thủ công nếu không cần nữa.

## Lab

**lab-20:** incident drill, cleanup, residual scan và cost retrospective.

## Tự kiểm tra

1. Tổng kết năng lực chứng minh engineering bằng gì ngoài metric?
2. Vì sao số 0 ngay sau cleanup chưa phải cost evidence cuối?
3. Budget còn lại khác residual infrastructure như thế nào?

## Kết quả hướng tới

Mốc năng lực 6: capstone tái lập, demo có fallback, audit có timestamp và kế hoạch 90 ngày hướng ML Engineer.

## Dấu hiệu bạn đã hiểu

Bạn không gọi dự án là “xong” trước khi reproduction, cleanup, residual scan và limitation đều rõ.

## Core vs stretch

- **Core:** local demo + completed cleanup/audit.
- **Stretch:** kiến trúc hóa production path trên giấy, kèm auth, rate limit, monitoring và cost controls.

## Lỗi thường gặp

- Giữ endpoint sống chỉ để trình diễn.
- Đưa account ID, credential hoặc raw billing vào artifact.
- Thấy Budget chưa báo rồi kết luận không có chi phí.

## Khi mắc kẹt

Ưu tiên an toàn: dừng demo AWS, cleanup, dùng local fallback. Nếu Billing chưa cập nhật, ghi timestamp và
lịch kiểm lại; đừng bịa kết luận để hoàn thành báo cáo.

## Bạn đã sẵn sàng kết thúc lộ trình khi

- Demo chạy được từ clean environment và có fallback local.
- Residual scan hoàn tất với `residual=false`; Budget được review riêng.
- Bạn đã kiểm Billing theo ba mốc: ngay sau cleanup, khoảng 12 giờ, ngày kế tiếp.

## AWS cost gate

AWS Budgets cập nhật tối đa ba lần/ngày, thường cách 8-12 giờ. Budget không phải hard cap. Nguồn:
[AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html).

## Nguồn

Xem `docs/sources.yml` và `aws/README.md`.
