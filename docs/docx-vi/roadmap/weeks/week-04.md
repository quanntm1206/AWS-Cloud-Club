# Tuần 04 - Toán trực giác và linear regression

## Mục tiêu tuần

Tự viết linear regression nhỏ; đọc loss curve và dùng xác suất cơ bản để diễn giải kết quả.

## Vì sao tuần này quan trọng

Loss cho model biết đang sai bao nhiêu; gradient cho biết nên đổi tham số theo hướng nào. Nắm trực giác này giúp bạn debug mọi mô hình về sau.

**Ví dụ gần gũi:** Nếu learning rate quá lớn, mỗi bước có thể nhảy qua đáy loss như người xuống dốc nhưng bước dài quá mức.

## Kiến thức cốt lõi

- Linear regression dùng y_hat=Xw+b; MSE phạt sai số theo bình phương và nhạy outlier.
- Gradient chỉ hướng tăng nhanh của loss; gradient descent cập nhật ngược hướng với learning rate.
- Central finite difference kiểm analytic gradient bằng thay đổi nhỏ của tham số.
- Feature scale ảnh hưởng hội tụ; hệ số chỉ diễn giải cùng scale, encoding và assumptions.
- Xác suất nằm trong `[0, 1]`; xác suất có điều kiện luôn gắn với một điều kiện, còn tần suất trên mẫu chỉ là ước lượng có sai số.

## Từ khóa tuần này

**Thuật ngữ mới hoặc trọng tâm:** `prediction`, `loss`, `gradient`, `learning rate`

**Ôn lại:** `feature`, `label / target`, `data validation`

**Áp dụng:** Tính `prediction` và `loss`, theo hướng `gradient`, rồi cập nhật từng parameter bằng `learning rate` đã chọn; giữ lại `feature`, `label / target` và mọi lỗi `data validation`.

## Giải thích khái niệm

### Prediction và error

**Cách hình dung:** `prediction`: Giá trị model tạo ra cho một sample. Với regression, nó có thể là một số; với classification, nó có thể là class hoặc probability. `loss`: Con số model cố giảm trong training để đo sai lệch trên dữ liệu học. Mỗi bài toán dùng loss function phù hợp, như MSE cho regression hoặc cross-entropy cho classification.

**Vì sao quan trọng:** Prediction là output của model; loss cho training một objective dạng số để cải thiện output đó.

**Ví dụ xuyên suốt:** `prediction`: Model dự đoán monthly_charges là 42.5. `loss`: MSE phạt bình phương khoảng cách giữa prediction và target.

**Dễ nhầm với:** Prediction là output; label là đáp án quan sát được. Loss dẫn hướng training; metric báo chất lượng mà con người quan tâm.

**Tự kiểm tra:** Vì sao `loss` thấp hơn có thể cải thiện `prediction` nhưng chưa chắc hữu ích cho sản phẩm?

### Quá trình học di chuyển ra sao

**Cách hình dung:** `gradient`: Hướng và độ lớn cho biết loss thay đổi thế nào khi parameter thay đổi. Dấu của gradient cho biết hướng, còn độ lớn cho biết loss phản ứng mạnh đến đâu. `learning rate`: Độ lớn mỗi bước cập nhật parameter. Optimizer nhân giá trị này với gradient để tạo bước cập nhật.

**Vì sao quan trọng:** Gradient cung cấp hướng update; learning rate kiểm soát parameter di chuyển bao xa theo hướng đó.

**Ví dụ xuyên suốt:** `gradient`: Gradient dương gợi ý giảm parameter theo learning rate. `learning rate`: Learning rate quá lớn làm loss dao động hoặc tăng.

**Dễ nhầm với:** Gradient là hướng thay đổi; learning rate scale độ lớn bước cập nhật. Learning rate là cấu hình bước cập nhật, không phải loss cần giảm.

**Tự kiểm tra:** Update thay đổi thế nào khi `gradient` giữ nguyên nhưng `learning rate` tăng gấp đôi?

## Kết nối kiến thức cũ

Mỗi `feature` giờ đóng góp vào prediction để so với `label / target`; `data validation` vẫn là cổng chặn input sai trước phép tính. Loss log và parameter update làm mối nối này quan sát được.

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


1. Tính forward, MSE, gradient bằng tay trên bốn điểm.
2. So analytic gradient với finite difference qua nhiều epsilon.
3. So loss curve khi learning rate nhỏ, hợp lý, quá lớn.

## Lab

**lab-03:** Linear regression từ đầu và gradient check. Môi trường chính: `local`.

## Dấu hiệu bạn đã hiểu

Bạn tự viết linear regression nhỏ, gradient check khớp và đọc loss curve để nói model đang học hay diverge.

## Tự kiểm tra

1. Gradient bằng 0 nói gì?
2. Epsilon quá nhỏ gây lỗi số nào?
3. MSE khác MAE với outlier ra sao?

## Kết quả hướng tới

mốc năng lực 1; lưu kèm lệnh đã chạy, cấu hình, quality measure, thời gian chạy và một điều còn hạn chế.

## Core vs stretch

- **Cốt lõi:** Tự viết linear regression, gradient check và giải thích ba dạng loss curve.
- **Mở rộng:** Thử MAE thay MSE hoặc đổi feature scale, nhưng giữ nguyên một yếu tố tại mỗi lần chạy.

## Lỗi thường gặp

- Tin gradient đúng chỉ vì loss giảm.
- Tăng training pass để che learning rate quá lớn.

## Khi mắc kẹt

Tính một bước trên bốn điểm bằng tay. Nếu gradient lệch, kiểm dấu, hệ số trung bình và nhiều giá trị `epsilon`.

## Nguồn

Nguồn nên đọc: phần optimization/linear models trong tài liệu scikit-learn và textbook được đăng ký ở `docs/sources.yml`.
