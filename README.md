# Machine Learning Engineer Roadmap - AWS Cloud Club

Chương trình tự học 24 tuần, 8-10 giờ/tuần, dành cho người đã biết lập trình nhưng chưa học Machine
Learning. Lộ trình đi từ dữ liệu và ML nền tảng tới software engineering, Computer Vision và capstone
serverless trên AWS.

## Nguyên tắc

- Local CPU trước; Colab Free hoặc Kaggle Free cho training CV.
- AWS dùng cho artifact, IAM, Lambda và observability; không dùng GPU/training nặng.
- Tabular capstone bắt buộc; CV capstone mở rộng nhưng có hướng dẫn đầy đủ.
- Mọi AWS lab: pre-check, cost estimate, dry-run, deploy, verify, cleanup, residual scan, cost audit.
- AWS Budgets là cảnh báo, không phải hard spending cap.

## Bắt đầu

GitHub chỉ là nơi chủ repo phát hành bộ khung. Clone repo mẫu:

```text
git clone https://github.com/quanntm1206/AWS-Cloud-Club.git
```

Nếu không dùng Git, tải source archive từ `https://github.com/quanntm1206/AWS-Cloud-Club` rồi giải nén
cục bộ. Người học không fork, commit, push, mở pull request hoặc nộp bài. Artifact, learning log
và minh chứng test được lưu cục bộ để tự đánh giá; không gửi cho ai và không cần public repository.

```powershell
pwsh scripts/setup.ps1 -Profile core
pwsh scripts/check.ps1 -Scope bootstrap
```

```bash
bash scripts/setup.sh --profile core
bash scripts/check.sh --scope bootstrap
```

Đọc `roadmap/00-getting-started.md`, sau đó học tuần tự trong `roadmap/weeks/`.

## Cấu trúc

- `roadmap/`: 24 tuần, mốc năng lực, learning log và tự đánh giá.
- `labs/`: 20 lab có acceptance criteria.
- `notebooks/`: notebook dùng chung, Colab, Kaggle.
- `src/ml_roadmap/`: code training, evaluation, inference.
- `capstones/`: tabular AWS và CV transfer learning.
- `aws/`: cost policy, CloudFormation, preflight/deploy/cleanup.
- `dist/`: tài liệu Word hoàn chỉnh.

## Cảnh báo AWS

Đường học mặc định nhắm Free Plan, nhưng pricing và eligibility có thể đổi. Luôn đọc `aws/README.md`,
kiểm đúng account/Region, tạo budget alerts, chạy dry-run và cleanup trong cùng phiên lab. Không nâng cấp
Paid Plan chỉ để hoàn thành bài bắt buộc.

## License

MIT. Dataset/model bên thứ ba giữ license riêng; xem từng lab/capstone.
