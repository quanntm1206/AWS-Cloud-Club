# Tuần 08 - Cross-validation và learning curve

## Mục tiêu tuần

Dùng cross-validation và learning curve.

## Vì sao tuần này quan trọng

Một lần chia dữ liệu có thể may hoặc rủi. Cross-validation giúp bạn thấy model ổn định đến đâu, còn learning curve gợi ý nên thêm dữ liệu hay đổi cách học.

**Ví dụ gần gũi:** Mean CV giống điểm trung bình; độ lệch giữa các fold cho biết kết quả phụ thuộc mạnh đến mức nào vào cách chia.

## Kiến thức cốt lõi

- Cross-validation ước lượng biến thiên qua nhiều fold; báo từng score, mean, std và runtime.
- StratifiedKFold cho classification độc lập; GroupKFold/time split cho entity/time.
- Transform phải nằm trong pipeline để fit lại bên trong từng fold.
- Learning curve so train/validation theo lượng data: cùng thấp gợi ý underfitting/high bias; train cao nhưng validation thấp gợi ý overfitting/high variance.
- Fold score là mẫu hữu hạn, không phải sự thật tuyệt đối; luôn báo độ phân tán và tránh kết luận mạnh từ chênh lệch nhỏ.

## Từ khóa tuần này

**Thuật ngữ mới hoặc trọng tâm:** `cross-validation`, `fold`, `overfitting`, `bias / variance`

**Ôn lại:** `data split`, `pipeline`, `metric`

**Áp dụng:** Đặt toàn bộ `pipeline` trong `cross-validation`; đọc từng `fold`, mean, standard deviation và learning curve để phân biệt `overfitting` với `bias / variance`, trong khi giữ cố định `metric` và `data split`.

## Giải thích khái niệm

### Luân phiên vai trò validation

**Cách hình dung:** `cross-validation`: Đánh giá lặp qua nhiều fold để ước lượng độ ổn định của model. Mỗi sample làm validation ở một fold và làm training ở các fold còn lại. `fold`: Một phần dữ liệu lần lượt làm validation trong cross-validation. Fold nên giữ cấu trúc quan trọng như class balance hoặc customer group.

**Vì sao quan trọng:** Cross-validation cho biết kết quả có ổn định qua nhiều fold hợp lý hay chỉ may mắn ở một split.

**Ví dụ xuyên suốt:** `cross-validation`: 3-fold CV tạo ba validation score. `fold`: Ở fold 2, nhóm thứ hai được giữ lại để đánh giá.

**Dễ nhầm với:** Cross-validation ước lượng độ dao động, không tạo thêm independent data. Fold là tập con trong cross-validation, không phải test set cuối.

**Tự kiểm tra:** Độ biến thiên giữa các `fold` cho biết gì mà mean `cross-validation` che đi?

### Overfitting qua bias và variance

**Cách hình dung:** `overfitting`: Model nhớ training data nhưng hoạt động kém trên dữ liệu mới. Nó xuất hiện dưới dạng khoảng cách giữa performance trên training và data chưa thấy. `bias / variance`: Bias cao thường do model quá đơn giản; variance cao do model quá nhạy với training data. Bias gây underfitting có hệ thống, còn variance làm model thiếu ổn định giữa các dataset.

**Vì sao quan trọng:** Khoảng cách và độ biến thiên giữa các fold giúp phân biệt overfitting với model có bias quá lớn.

**Ví dụ xuyên suốt:** `overfitting`: Train score tăng còn validation score giảm. `bias / variance`: Learning curve có cả train và validation thấp gợi ý bias cao.

**Dễ nhầm với:** Overfitting là generalization gap, không chỉ là model có nhiều parameter. Bias và variance là xu hướng lỗi, không phải demographic bias của protected attribute.

**Tự kiểm tra:** Pattern nào trên learning curve gợi ý `overfitting`, bias cao hoặc variance cao?

## Kết nối kiến thức cũ

Giữ nguyên `data split`, `pipeline` và `metric` trong khi các fold luân phiên vai trò validation. Score của từng fold và độ phân tán cho thấy độ ổn định mà một split không thể hiện được.

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


1. Chạy 3-fold CV fixed seed.
2. So pipeline đúng với preprocessing ngoài CV.
3. Vẽ learning curve ba train sizes.

## Lab

**lab-07:** Evaluation harness có mean/std/runtime. Môi trường chính: `local`.

## Dấu hiệu bạn đã hiểu

Bạn báo từng fold, mean, std, runtime và biết chọn split theo entity hoặc thời gian khi cần.

## Tự kiểm tra

1. Std giữa fold lớn gợi ý gì?
2. CV có thay final test không?
3. Shuffle time series sai vì sao?

## Kết quả hướng tới

mốc năng lực 2; lưu kèm lệnh đã chạy, cấu hình, metric, thời gian chạy và một điều còn hạn chế.

## Core vs stretch

- **Cốt lõi:** Chạy 3-fold CV cùng pipeline; báo từng fold, mean, std và learning curve.
- **Mở rộng:** So StratifiedKFold với GroupKFold trên một grouping giả định; không tăng fold chỉ để có thêm số.

## Lỗi thường gặp

- Tune rồi báo cùng CV như final test.
- Dùng nhiều fold nhưng không thêm insight.

## Khi mắc kẹt

Giảm còn 3 fold và mini data. Nếu score dao động, kiểm class/group theo fold trước khi tune model.

## Nguồn

Nguồn nên đọc: scikit-learn cross-validation và learning curve documentation.
