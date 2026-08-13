# Tuần 05 - Supervised learning và baseline

## Mục tiêu tuần

Đặt baseline; split train/validation/test đúng.

## Vì sao tuần này quan trọng

Baseline tạo một vạch xuất phát trung thực. Nếu model chưa vượt cách đoán đơn giản, tăng độ phức tạp chưa mang lại giá trị.

**Ví dụ gần gũi:** Dataset có 90% khách không churn sẽ cho dummy accuracy 90%, nhưng gần như vô dụng khi cần tìm người sắp rời đi.

## Kiến thức cốt lõi

- Classification dự đoán class/probability; regression dự đoán giá trị liên tục.
- Dummy baseline đo mức tối thiểu; logistic regression tạo linear logit rồi sigmoid.
- Train để fit, validation để chọn, test chỉ dùng khi quyết định đã khóa.
- Dùng stratified split cho class; dùng group/time split khi mẫu liên quan hoặc có thời gian.

## Từ khóa tuần này

**Thuật ngữ mới hoặc trọng tâm:** `data split`, `training set`, `validation set`, `test set`, `baseline`, `model validation`

**Ôn lại:** `dataset`, `sample`, `feature`, `label / target`, `prediction`

**Áp dụng:** Tạo `data split` từ `dataset` không trùng sample thành `training set`, `validation set`, `test set`; fit `baseline` trên feature, thực hiện `model validation`, so prediction với label / target.

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


1. So dummy và logistic trên đúng cùng split/workflow/quality measure.
2. Kiểm class balance và ID không trùng giữa tập.
3. Viết quality measure gate model phải vượt baseline.

## Lab

**lab-04:** Dummy và logistic classifier. Môi trường chính: `local`.

## Dấu hiệu bạn đã hiểu

Bạn dùng cùng split và quality measure để so dummy với logistic regression; test set vẫn chưa tham gia chọn model.

## Tự kiểm tra

1. Dummy accuracy cao khi nào?
2. Logistic tuyến tính ở không gian nào?
3. Random split gây leakage khi nào?

## Kết quả hướng tới

baseline report; lưu kèm lệnh đã chạy, cấu hình, quality measure, thời gian chạy và một điều còn hạn chế.

## Core vs stretch

- **Cốt lõi:** So dummy với logistic trên cùng split, quality measure và seed; giữ test chưa tham gia lựa chọn.
- **Mở rộng:** Thử group/time split trên một tình huống giả định và nêu vì sao random split có thể sai.

## Lỗi thường gặp

- So model trên split khác nhau.
- Bỏ baseline để chạy model phức tạp.

## Khi mắc kẹt

Kiểm phân bố nhãn, ID trùng và thời gian trước. Khi nghi ngờ split, vẽ sơ đồ các tập thay vì đổi model.

## Nguồn

Nguồn nên đọc: scikit-learn documentation về model selection, train-test split và DummyClassifier.
