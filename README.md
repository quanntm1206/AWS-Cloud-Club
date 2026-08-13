# Machine Learning Engineer Roadmap - AWS Cloud Club

Nếu bạn đã viết code nhưng Machine Learning vẫn giống một chiếc hộp đen, lộ trình này sẽ giúp bạn mở nó
từng lớp. Trong 24 tuần, bạn đi từ cách đọc dữ liệu và huấn luyện model đầu tiên đến một hệ thống ML nhỏ có
thể kiểm thử, đóng gói và chạy an toàn. Nhịp học dự kiến 8-10 giờ mỗi tuần; không cần GPU hay AWS để bắt đầu.

## Sau 24 tuần, bạn có thể làm gì?

- Chuyển một câu hỏi thực tế thành bài toán ML có dữ liệu, nhãn, baseline và metric rõ ràng.
- Xây pipeline tabular tránh data leakage; đánh giá model bằng bằng chứng thay vì một con số đẹp.
- Tách notebook thành package, viết test, dựng inference API, đóng gói Docker và quản lý artifact.
- Train một model ảnh nhỏ bằng transfer learning trên Colab Free hoặc Kaggle Free.
- Triển khai capstone tabular bằng private Lambda rồi dọn sạch tài nguyên AWS trong cùng phiên học.

Đây là nền móng để đi tiếp theo hướng ML Engineer, không phải lời hứa rằng 24 tuần sẽ thay thế kinh nghiệm
làm sản phẩm thật. Điều quan trọng nhất bạn mang đi là khả năng tự đặt câu hỏi, kiểm chứng và giải thích quyết định.

## Bản đồ sáu chặng

| Tuần | Chặng | Bạn sẽ làm được |
|---|---|---|
| [01-04](roadmap/weeks/week-01.md) | Nền tảng dữ liệu và toán | Hiểu workflow, NumPy, EDA và gradient bằng trực giác |
| [05-08](roadmap/weeks/week-05.md) | ML cổ điển và đánh giá | Dựng baseline, chống leakage, chọn metric và kiểm tra độ ổn định |
| [09-12](roadmap/weeks/week-09.md) | ML ứng dụng | So sánh model, thiết kế feature, phân tích lỗi, hoàn thành mini-project |
| [13-16](roadmap/weeks/week-13.md) | ML Engineering | Package, test, API, Docker, CI và version artifact |
| [17-20](roadmap/weeks/week-17.md) | Deep Learning và CV | PyTorch, transfer learning, checkpoint và failure analysis |
| [21-24](roadmap/weeks/week-21.md) | AWS capstone an toàn | S3, private Lambda, cleanup, cost audit và demo |

## Cách dùng repo

GitHub chỉ là nơi chủ repo phát hành bộ khung. Clone repo mẫu:

```text
git clone https://github.com/quanntm1206/AWS-Cloud-Club.git
```

Nếu không dùng Git, tải source archive từ `https://github.com/quanntm1206/AWS-Cloud-Club` rồi giải nén
cục bộ. Người học không fork, commit, push, mở pull request hoặc nộp bài. Learning log, kết quả lab và
artifact được lưu cục bộ để bạn tự nhìn lại; không cần public repository.

Thiết lập môi trường rồi chạy kiểm tra khởi động:

```powershell
pwsh scripts/setup.ps1 -Profile core
pwsh scripts/check.ps1 -Scope bootstrap
```

```bash
bash scripts/setup.sh --profile core
bash scripts/check.sh --scope bootstrap
```

Đọc [hướng dẫn bắt đầu](roadmap/00-getting-started.md), sau đó mở tuần 01. Mỗi tuần sẽ chỉ bạn đến đúng lab.
Sau tuần 24, dùng [bản đồ 90 ngày](roadmap/sau-24-tuan.md) để chọn hướng Model Engineering, ML Platform/MLOps
hoặc Applied Computer Vision.

## Học thuật ngữ mà không cần học vẹt

Mỗi lab giới thiệu một nhóm từ mới, gọi lại những từ đã dùng ở lab trước rồi yêu cầu bạn áp dụng chúng vào
thao tác và output thật. Ví dụ, bạn gặp `dataset` ở lab 00, dùng lại khi tạo `data split` ở lab 04, rồi tiếp
tục kiểm `data leakage` ở lab 05. Mục `Tự giải thích` giúp bạn nói lại bằng lời của mình; glossary cuối tài liệu
là chỗ tra cứu, không phải danh sách cần thuộc ngay. Ba cụm dễ nhầm được tách rõ:

- `data validation`: kiểm dữ liệu có đúng schema/quy tắc hay không;
- `validation set`: phần dữ liệu dùng chọn quyết định, không dùng fit parameter;
- `model validation`: quá trình đánh giá model trên dữ liệu chưa dùng để fit.

## Nguyên tắc giữ chi phí thấp

- Local CPU là đường mặc định; Colab Free hoặc Kaggle Free chỉ dùng cho phần CV.
- AWS dành cho artifact, IAM, Lambda và quan sát hệ thống; không dùng GPU hoặc training nặng.
- Tabular capstone là phần cốt lõi; CV capstone là phần mở rộng có hướng dẫn đầy đủ.
- Mọi AWS lab đi đủ: pre-check, estimate, dry-run, deploy, verify, cleanup, residual scan, cost audit.
- AWS Budgets chỉ gửi cảnh báo, không tự khóa chi tiêu. Pricing và eligibility có thể thay đổi.

## Trong repo có gì?

- [`roadmap/`](roadmap/): 24 tuần, sáu mốc năng lực, learning log và cách tự đánh giá.
- [`labs/`](labs/): 21 lab, gồm lab 00 khởi động, lab 01-19 offline/free compute và lab 20 cho AWS.
- [`notebooks/`](notebooks/): notebook chạy thật trên Colab/Kaggle cùng CPU fallback.
- `src/ml_roadmap/`: code mẫu cho training, evaluation và inference.
- [`capstones/`](capstones/): capstone churn tabular và image classification.
- `aws/`: cost policy, CloudFormation và script preflight/deploy/cleanup.
- `dist/`: tài liệu Word hoàn chỉnh.

## Nếu bị chậm hoặc mắc kẹt

Đừng mua thêm compute để chữa một lỗi chưa hiểu. Quay về `cpu-mini`, đọc thông báo lỗi đầu tiên, kiểm shape,
dtype, data split và command đang chạy. Ghi lại điều đã thử trong learning log. Nếu một tuần kéo dài hơn dự
kiến, hoàn thành phần cốt lõi rồi bỏ qua `Stretch`; roadmap không yêu cầu bạn chạy mọi tùy chọn.

## License

MIT. Dataset và model bên thứ ba giữ license riêng; xem từng lab và capstone trước khi sử dụng.
