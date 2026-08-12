# Tuần 14 - Testing cho hệ thống ML

## Mục tiêu tuần

Test schema, transform, model và artifact.

## Vì sao tuần này quan trọng

Hệ thống ML hỏng không chỉ vì model kém. Schema đổi, category lạ hoặc artifact lỗi thường xuất hiện trước khi metric tụt.

**Ví dụ gần gũi:** Một API nhận tuổi dạng chuỗi nên bị từ chối rõ ràng, thay vì âm thầm biến đổi rồi trả prediction khó tin.

## Kiến thức cốt lõi

- ML tests bao phủ schema, transforms, determinism, metric sanity, reload và API boundary.
- Unit dùng synthetic nhỏ; integration chạy pipeline ngắn.
- Negative cases: thiếu cột, sai dtype, unseen category, NaN/Inf, empty batch, artifact hỏng.
- Metric assertion dùng threshold/tolerance có lý do, không khóa số stochastic mong manh.

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


1. Test valid/invalid schema và unseen category.
2. Fit-save-load-predict, kiểm parity.
3. Kiểm model vượt dummy trên data có signal.

## Lab

**lab-13:** ML tests với edge cases. Môi trường chính: `local`.

## Dấu hiệu bạn đã hiểu

Bạn có test cho happy path lẫn missing, wrong dtype, unseen category, NaN/Inf và save-load parity.

## Tự kiểm tra

1. Nguồn randomness nào cần seed?
2. Vì sao exact metric dễ flaky?
3. Test nào bắt train/serve skew?

## Kết quả hướng tới

test evidence; lưu kèm lệnh đã chạy, cấu hình, metric, thời gian chạy và một điều còn hạn chế.

## Core vs stretch

- **Cốt lõi:** Test schema, negative cases, reload parity và model-vượt-dummy trên data synthetic nhỏ.
- **Mở rộng:** Thêm test artifact checksum hỏng hoặc batch rỗng; tránh exact metric dễ flaky.

## Lỗi thường gặp

- Chỉ test happy path.
- CI dùng production dataset lớn/nhạy cảm.

## Khi mắc kẹt

Dùng synthetic data nhỏ và sửa một test mỗi lần. Tránh khóa exact metric nếu thuật toán có ngẫu nhiên.

## Nguồn

Nguồn nên đọc: pytest documentation và scikit-learn guidance về common pitfalls/reproducibility.
