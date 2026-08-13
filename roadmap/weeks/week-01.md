# Tuần 01 - ML workflow và môi trường tái lập

## Mục tiêu tuần

Mô tả một ML workflow hoàn chỉnh; tạo môi trường tái lập.

## Vì sao tuần này quan trọng

Một workflow rõ ràng giúp bạn biết model phục vụ quyết định nào, thay vì bắt đầu bằng thuật toán rồi mới đi tìm bài toán.

**Ví dụ gần gũi:** Hãy hình dung model churn dự đoán khách nào có thể rời đi vào đầu tháng; đội chăm sóc chỉ hành động sau thời điểm đó.

## Kiến thức cốt lõi

- Tách business question khỏi model output task: xác định đối tượng, nhãn, model output time và hành động sau dự đoán.
- Workflow tối thiểu: validate data, split, simple reference, học, đánh giá, khóa quyết định, test một lần, phân tích lỗi, đóng gói.
- Quy ước dữ liệu khóa schema/target; experiment contract lưu seed, config, code revision, quality measure, runtime và limitation.
- Reproducibility yêu cầu tái tạo input, procedure, environment và tolerance; không hứa mọi phần cứng cho bit-identical result.

## Từ khóa tuần này

**Thuật ngữ mới hoặc trọng tâm:** `dataset`, `sample`, `schema`, `reproducibility`, `seed`

**Ôn lại:** Chưa có - đây là lab đầu tiên.

**Áp dụng:** Mở `dataset` smoke, đếm từng `sample`, đối chiếu `schema`, cố định `seed` rồi chạy hai lần để kiểm `reproducibility`.

## Lịch 8-10 giờ

| Hoạt động | Giờ |
|---|---:|
| Đọc và ghi chú | 2 |
| Guided practice | 2 |
| Lab | 3 |
| Assessment/failure review | 1 |
| Learning log và tự đánh giá | 1 |
| Review/hoàn thiện | 0 |

## Guided practice


1. Viết problem statement cho churn theo mẫu ai-khi nào-để làm gì.
2. Vẽ data -> split -> học -> đánh giá -> test -> saved model bundle; đánh dấu điểm leakage.
3. Chạy lab, lưu environment report và một limitation.

## Lab

**lab-00:** Cài môi trường, chạy kiểm tra, lập learning log. Môi trường chính: `local`.

## Dấu hiệu bạn đã hiểu

Bạn có thể kể lại đường đi từ câu hỏi đến saved model bundle và chỉ ra final holdout được mở khi nào.

## Tự kiểm tra

1. Model output khác quyết định sản phẩm thế nào?
2. Vì sao test không dùng chọn model/decision cutoff?
3. Experiment log tối thiểu gồm gì?

## Kết quả hướng tới

environment report lưu cục bộ; lưu kèm lệnh đã chạy, cấu hình, quality measure, thời gian chạy và một điều còn hạn chế.

## Core vs stretch

- **Cốt lõi:** Chạy lab 00, giữ environment report và vẽ workflow churn bằng lời của bạn.
- **Mở rộng:** Nếu còn thời gian, thử thay đổi seed/input rồi giải thích phần nào nên giữ ổn định.

## Lỗi thường gặp

- Bắt đầu từ thuật toán thay vì câu hỏi.
- Không khóa model output time nên input signal nhìn tương lai.

## Khi mắc kẹt

Nếu các khái niệm còn trừu tượng, lấy một app quen thuộc rồi viết rõ: dự đoán ai, vào lúc nào, để làm gì.

## Nguồn

Nguồn nên đọc: `docs/sources.yml` - mục scikit-learn model persistence và tài liệu tái lập môi trường.
