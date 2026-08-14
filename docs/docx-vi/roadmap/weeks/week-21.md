# Tuần 21 - Bước lên AWS mà vẫn kiểm soát được chi phí

## Mục tiêu tuần

Hiểu account plan, credit, IAM, Budget và S3 trước khi tạo bất kỳ tài nguyên nào.

## Vì sao tuần này quan trọng

Một ML Engineer không chỉ biết deploy; họ còn biết lúc nào **không nên deploy**. Tuần này giúp bạn đọc
màn hình Billing, nhận ra ranh giới Free/Paid Plan và dựng hàng rào an toàn trước khi chạm cloud.

## Kiến thức cốt lõi

- “Up to USD 200” là USD 100 khi đăng ký và có thể kiếm thêm tối đa USD 100 qua activity; không phải
  USD 200 được cấp hết ngay. Free Plan kết thúc sau 6 tháng hoặc khi hết credit.
- Paid Plan là pay-as-you-go. Credit chỉ bù khoản đủ điều kiện; Budget alert không phải hard cap.
- Join AWS Organizations hoặc setup Control Tower có thể làm credit hết hiệu lực và Free Plan tự nâng
  Paid Plan. Không dùng hai tính năng này trong account học tập.
- IAM least privilege, MFA root, không root access key; luôn xác nhận account ID và Region trước lệnh.
- S3 tính theo storage, request và transfer. Artifact nhỏ, block public access, lifecycle ngắn.

Nguồn AWS, kiểm ngày 2026-08-12:
[plans](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans.html),
[FAQ](https://aws.amazon.com/free/free-tier-faqs/) và
[tracking](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/tracking-free-tier-usage.html).

## Từ khóa tuần này

**Thuật ngữ mới hoặc trọng tâm:** `IAM`, `S3`, `Lambda`, `CloudWatch Logs`, `budget alert`, `residual scan`, `idempotent cleanup`

**Ôn lại:** `artifact`, `inference`, `API contract`

**Áp dụng:** Upload `artifact` lên `S3`, cấp quyền tối thiểu bằng `IAM`, gọi `Lambda` để `inference`, rồi đọc `CloudWatch Logs`; tạo `budget alert`, chạy `idempotent cleanup`, và xác nhận bằng `residual scan` theo `API contract`.

## Giải thích khái niệm

### Least privilege và storage

**Cách hình dung:** `IAM`: Dịch vụ AWS quản danh tính và quyền truy cập theo nguyên tắc quyền tối thiểu. Policy gắn action và resource được phép vào user, role hoặc service. `S3`: Dịch vụ object storage của AWS dùng để lưu artifact nhỏ. Mỗi object có một key trong bucket và có thể được bảo vệ bằng IAM cùng encryption.

**Vì sao quan trọng:** IAM theo least privilege giới hạn blast radius; S3 object private giữ model artifact trong boundary dự kiến.

**Ví dụ xuyên suốt:** `IAM`: Lambda role chỉ được đọc đúng model object cần thiết trong S3. `S3`: Upload portable_model.json vào private bucket.

**Dễ nhầm với:** IAM kiểm soát access; security group kiểm soát network traffic. S3 lưu object trong bucket; file system cung cấp directory và file operation.

**Tự kiểm tra:** Lambda role cần cho phép S3 action nào và nên từ chối action không liên quan nào?

### Event-driven execution

**Cách hình dung:** `Lambda`: Dịch vụ chạy hàm serverless theo request mà không quản máy chủ. AWS cấp execution environment và tính phí resource dùng cho mỗi invocation. `CloudWatch Logs`: Nơi lưu log runtime trên AWS; cần tránh dữ liệu nhạy cảm và đặt retention. Log group cần retention, access control và quy tắc không ghi sensitive value.

**Vì sao quan trọng:** Lambda thực hiện event-driven computation; CloudWatch Logs cung cấp operational evidence có giới hạn mà không trở thành nơi lưu payload nhạy cảm.

**Ví dụ xuyên suốt:** `Lambda`: Dùng private invoke để chạy tabular inference. `CloudWatch Logs`: Đặt retention một ngày cho Lambda log group.

**Dễ nhầm với:** Lambda là compute; S3 là object storage. CloudWatch Logs lưu runtime log; CloudWatch metric lưu số đo.

**Tự kiểm tra:** Log field nào chứng minh Lambda load đúng artifact mà không lộ customer payload?

### Observability và cost

**Cách hình dung:** `budget alert`: Cảnh báo khi chi phí thực tế hoặc dự báo chạm ngưỡng; không phải hard cap. Nó theo dõi actual và forecast spending, nhưng resource AWS vẫn chạy cho đến khi có hành động dừng. `residual scan`: Bước kiểm sau cleanup để tìm tài nguyên project còn sót. Nó phải kiểm mọi service liên quan và chỉ ra phần nào vẫn cần xóa.

**Vì sao quan trọng:** Budget alert báo cost threshold; residual scan kiểm tra technical state thực tế sau cleanup.

**Ví dụ xuyên suốt:** `budget alert`: AWS Budget gửi email cảnh báo Actual và Forecasted spending. `residual scan`: Residual scan kiểm CloudFormation, S3, Lambda, CloudWatch Logs và IAM.

**Dễ nhầm với:** Budget alert gửi cảnh báo; nó không tự động dừng chi tiêu AWS. Residual scan xác minh không còn resource; cleanup thực hiện hành động xóa.

**Tự kiểm tra:** Vì sao budget alert có thể im lặng trong khi residual scan vẫn tìm thấy resource?

### Cleanup an toàn

**Cách hình dung:** `idempotent cleanup`: Quy trình dọn có thể chạy lại an toàn và vẫn hướng tới trạng thái sạch. Resource đã không còn được xem là trạng thái thành công thay vì fatal error.

**Vì sao quan trọng:** Idempotent cleanup phục hồi được từ partial failure vì chạy lại vẫn hướng tới cùng clean state.

**Ví dụ xuyên suốt:** `idempotent cleanup`: Xóa resource có đúng project ID rồi scan lại.

**Dễ nhầm với:** Idempotent cleanup chạy lặp an toàn; delete một lần có thể hỏng khi mới hoàn tất một phần.

**Tự kiểm tra:** Kết quả lần chạy thứ hai nào chứng minh cleanup là idempotent?

## Kết nối kiến thức cũ

Local `artifact` giờ đi tới cloud `inference` qua cùng `API contract`. S3 checksum, Lambda response và log có giới hạn cho thấy cloud path giữ đúng model cùng interface dự kiến.

## Lịch 8-10 giờ

| Hoạt động | Giờ |
|---|---:|
| Đọc plans, credits và cost policy | 2 |
| Xem Billing, IAM và Budget có hướng dẫn | 2 |
| Chạy local preflight, checksum và cleanup dry-run | 3 |
| Learning log và tự đánh giá | 2 |

## Guided practice

1. Nếu chưa có account, chỉ tạo ở tuần 20/21 để không lãng phí cửa sổ 6 tháng. Không tạo nhiều account
   để săn credit.
2. Mở Billing; ghi `plan`, credit còn lại, ngày hết hạn và days remaining. Nếu thông tin không rõ hoặc
   console bắt nâng Paid Plan, chọn local-only.
3. Tạo Cost budget với Actual và Forecasted email alerts ở ngưỡng thấp. Không tạo Budget Report hoặc
   Budget Action. Alert có độ trễ, không thay cleanup.
4. Chạy `cost-check` và `preflight` local. Tập đọc lý do dừng thay vì vội bỏ qua guard.

## Lab

**lab-20, phần chuẩn bị:** checksum artifact, cost planning, preflight và cleanup dry-run. Chưa deploy.

## Tự kiểm tra

1. Vì sao “up to USD 200” không phải USD 200 có sẵn?
2. Free Plan khác Paid Plan ở rủi ro charge như thế nào?
3. Vì sao Budget không thể thay cleanup?

## Kết quả hướng tới

Bạn tự giải thích được plan/credit của account, tạo alert đúng loại và nhận ra các điều kiện buộc dừng.

## Dấu hiệu bạn đã hiểu

Bạn phân biệt được credit, Free Plan, Paid Plan và Budget mà không gọi chung tất cả là “miễn phí”.

## Core vs stretch

- **Core:** local preflight + đọc Billing/plan rõ ràng.
- **Stretch:** đọc AWS Pricing Calculator cho S3/Lambda; không deploy thử chỉ để xem.

## Lỗi thường gặp

- Tin credit hoặc Budget tự chặn mọi chi phí.
- Join Organizations/Control Tower vì lời mời của club.
- Tạo account từ đầu lộ trình rồi để Free Plan gần hết hạn trước capstone.

## Khi mắc kẹt

Không đoán trạng thái account. Chụp lại thông tin không nhạy cảm hoặc hỏi người quản lý club; tiếp tục
local-only. Không gửi account ID, email billing hoặc credential.

## Bạn đã sẵn sàng chuyển tuần khi

- Bạn biết account đang ở Free hay Paid Plan và ngày hết hạn.
- Bạn có Actual + Forecasted notifications; hiểu chúng có thể báo muộn.
- Bạn có thể nói “không deploy” khi eligibility, estimate hoặc cleanup path chưa rõ.

## AWS cost gate

Không chạy nếu sai account/Region, chưa đọc `aws/README.md`, chưa có cleanup path hoặc estimate vượt
USD 0.10. Không dùng EC2, NAT Gateway, SageMaker, Bedrock, database, container cluster hay Marketplace.

## Nguồn

Xem `docs/sources.yml` và `docs/source-notes/aws-free-tier.md`.
