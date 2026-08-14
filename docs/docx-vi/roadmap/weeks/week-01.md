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

**Áp dụng:** Mở smoke `dataset`, đếm các dòng `sample`, kiểm `schema`, cố định `seed`, rồi chạy hai lần để kiểm `reproducibility`.

## Giải thích khái niệm

### Dòng dữ liệu, tập hợp và quy tắc

**Cách hình dung:** `dataset`: Tập dữ liệu gồm nhiều mẫu được gom để phân tích hoặc huấn luyện model. Dataset thường có các hàng là sample và các cột là feature. `sample`: Một đơn vị quan sát trong dataset; thường là một hàng hoặc một ảnh. Mỗi sample có cùng cấu trúc mong đợi nhưng mang các giá trị quan sát khác nhau.

**Vì sao quan trọng:** Dataset cung cấp evidence cho dự án; sample là đơn vị được split, prediction và metric đếm.

**Ví dụ xuyên suốt:** `dataset`: File churn có 300 khách hàng và các cột mô tả từng khách. `sample`: Một khách hàng là một sample trong bảng churn.

**Dễ nhầm với:** Dataset là cả tập; sample là một phần tử bên trong. Sample là một quan sát; feature là một giá trị input hoặc cột mô tả quan sát đó.

**Tự kiểm tra:** Khi đếm evidence churn, một `sample` khác toàn bộ `dataset` như thế nào?

### Schema và lần chạy tái lập

**Cách hình dung:** `schema`: Bản mô tả tên cột, kiểu dữ liệu và quy tắc hợp lệ của input. Schema còn nêu constraint như cột bắt buộc, category hợp lệ và khoảng số cho phép. `reproducibility`: Khả năng chạy lại cùng dữ liệu, code và cấu hình để nhận kết quả tương đương. Cần ghi lại data, code, dependency, configuration và các yếu tố ngẫu nhiên.

**Vì sao quan trọng:** Schema phát hiện structural drift; reproducibility cho biết cùng procedure còn tạo evidence tương đương hay không.

**Ví dụ xuyên suốt:** `schema`: Cột tenure phải là số không âm; churn chỉ nhận 0 hoặc 1. `reproducibility`: Hai terminal dùng cùng seed cho cùng số hàng và metric trong tolerance.

**Dễ nhầm với:** Schema mô tả cấu trúc hợp lệ; data validation kiểm dữ liệu thật theo schema. Cùng seed hỗ trợ reproducibility, nhưng code hoặc package đổi vẫn có thể làm kết quả đổi.

**Tự kiểm tra:** Column type thay đổi sẽ phá `schema`, `reproducibility` hay cả hai?

### Seed kiểm soát randomness

**Cách hình dung:** `seed`: Con số khởi tạo bộ sinh ngẫu nhiên để phép chia hoặc khởi tạo có thể lặp lại. Dùng lại seed sẽ khởi tạo cùng chuỗi giả ngẫu nhiên cho các thao tác có hỗ trợ.

**Vì sao quan trọng:** Seed chỉ kiểm soát một random sequence, nên chỉ hữu ích khi data, code, configuration và environment cũng được ghi lại.

**Ví dụ xuyên suốt:** `seed`: Đặt seed 42 trước khi tạo dữ liệu mẫu.

**Dễ nhầm với:** Seed điều khiển một chuỗi ngẫu nhiên, không kiểm soát mọi nguồn nondeterminism.

**Tự kiểm tra:** Những gì phải giữ nguyên để cùng `seed` giúp hai run so sánh được?

## Kết nối kiến thức cũ

Tuần 01 chưa có thuật ngữ cũ để ôn. Environment report tạo evidence đầu tiên bằng cách ghi `dataset`, `seed` và kết quả chạy lặp để các tuần sau đối chiếu.

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
