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
2. Reload artifact ở process mới và kiểm prediction parity.
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

Chạy `mini` trước, kiểm từng artifact. Khi parity sai, so config và feature order trước khi train lại.

## Nguồn

Nguồn nên đọc: model persistence của scikit-learn và model-card references trong `docs/sources.yml`.
