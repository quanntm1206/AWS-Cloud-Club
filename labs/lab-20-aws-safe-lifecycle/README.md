# Lab 20 - Đưa model lên AWS rồi dọn sạch

## Mục tiêu

Đưa portable tabular model lên S3, gọi Lambda riêng tư với input đúng/sai, xem log, cleanup và chứng minh
không còn infrastructure của project. Không dùng EC2, SageMaker, Bedrock, NAT Gateway hoặc public API.

## Trước khi bắt đầu

- Đọc `aws/README.md`; xác nhận plan, credit, ngày hết hạn và đúng account/Region.
- Tạo Cost budget với Actual + Forecasted email notifications. Không dùng Budget Report/Action.
- Chừa một phiên liền mạch khoảng 45-60 phút; đặt timer cleanup. Không deploy trước khi sắp rời máy.
- Nhớ rằng `ExpiresAt` chỉ là metadata nhắc việc; AWS không tự xóa stack theo tag này.
- Nếu Billing không rõ hoặc console bắt nâng Paid Plan, dừng ở local simulation. Bài vẫn hoàn thành.

## Bạn sẽ làm gì

1. Train artifact local; ghi checksum.
2. Chạy cost planning và preflight.
3. Deploy S3, Lambda, CloudWatch Logs và IAM role bằng CloudFormation.
4. Gọi Lambda riêng tư cho valid/invalid event.
5. Cleanup, residual scan, rồi kiểm Billing theo ba mốc.

### 1. Chuẩn bị artifact local

```powershell
.venv\Scripts\python.exe -c "from ml_roadmap.data import make_demo_churn_data; make_demo_churn_data(300,42).to_csv('.artifacts/churn.csv',index=False)"
.venv\Scripts\python.exe -m ml_roadmap.train_tabular --config capstones/tabular-churn/configs/mini.yml --data .artifacts/churn.csv --output .artifacts/churn-model
Get-FileHash .artifacts/churn-model/portable_model.json -Algorithm SHA256
```

### 2. Budget, estimate và preflight

Trên Console, mở **Billing and Cost Management > Budgets > Create budget**. Chọn monthly Cost budget,
thêm Actual và Forecasted email notifications ở ngưỡng thấp phù hợp account. Budget có thể báo muộn;
nó không phải hard cap.

```powershell
$project = 'student01'
$region = 'us-east-1'
$expiresAt = (Get-Date).AddDays(1).ToString('yyyy-MM-dd')
aws sts get-caller-identity
pwsh aws/scripts/cost-check.ps1 -ProjectId $project -Region $region
pwsh aws/scripts/preflight.ps1 -ProjectId $project -Region $region -ArtifactPath .artifacts/churn-model/portable_model.json -AcknowledgeBudgetConfigured
```

Dừng nếu account/Region sai, artifact vượt 200 MB, estimate vượt USD 0.10, pricing chưa xác minh được hoặc
output nhắc tới resource ngoài policy. Planning envelope không phải live quote hay bill guarantee.

### 3. Deploy private path

```powershell
pwsh aws/scripts/deploy.ps1 -ProjectId $project -Owner 'student01' -ExpiresAt $expiresAt -ArtifactPath .artifacts/churn-model/portable_model.json -Region $region -AcknowledgeBudgetConfigured
```

Template không có API Gateway/Public URL. Nếu deploy, output lookup hoặc upload lỗi, stack có thể đã tồn
tại. Đừng chạy lại ngay; chuyển thẳng sang mục **Khi mắc kẹt**.

### 4. Verify artifact và private Lambda

```powershell
$stack = "ml-roadmap-$project"
$bucket = aws cloudformation describe-stacks --stack-name $stack --region $region --query "Stacks[0].Outputs[?OutputKey=='BucketName'].OutputValue" --output text
$function = aws cloudformation describe-stacks --stack-name $stack --region $region --query "Stacks[0].Outputs[?OutputKey=='FunctionName'].OutputValue" --output text
aws s3api head-object --bucket $bucket --key models/portable_model.json --region $region
aws lambda invoke --function-name $function --payload fileb://aws/events/valid.json --region $region .artifacts/lambda-valid.json
aws lambda invoke --function-name $function --payload fileb://aws/events/invalid.json --region $region .artifacts/lambda-invalid.json
Get-Content .artifacts/lambda-valid.json
Get-Content .artifacts/lambda-invalid.json
```

Valid trả label/probability/threshold. Invalid trả `statusCode=422` và missing fields. Chỉ gọi vài lần;
đây không phải load test.

### 5. Kiểm log

```powershell
aws logs tail "/aws/lambda/$function" --since 10m --region $region
```

Log không được chứa credential hoặc raw sensitive record. Log retention phải là một ngày.

### 6. Cleanup trong cùng phiên

```powershell
pwsh aws/scripts/cleanup.ps1 -ProjectId $project -Region $region
# Đọc exact resource names trước khi execute.
pwsh aws/scripts/cleanup.ps1 -ProjectId $project -Region $region -Execute -ConfirmProjectId $project
pwsh aws/scripts/residual-scan.ps1 -ProjectId $project -Region $region -Json
```

Scan kiểm CloudFormation, S3, Lambda, Logs và IAM. Exit khác 0 hoặc lỗi quyền nghĩa là **chưa chứng minh
được sạch**. Budget alert không nằm trong stack và được giữ có chủ đích; review/xóa thủ công cuối khóa.

### 7. Cost audit

1. Kiểm Billing/Free Tier/credits ngay sau cleanup; ghi timestamp, không lưu account ID.
2. Đặt lịch kiểm lại sau khoảng 12 giờ và vào ngày kế tiếp vì billing có độ trễ.
3. Lưu output local trong `.artifacts/`; xóa credential, email và dữ liệu cá nhân khỏi learning log.

## Khi nào xem như hoàn thành

- Checksum có trước deploy; private invoke valid/invalid đúng contract.
- Không có public endpoint hoặc forbidden service.
- Cleanup dry-run được đọc trước execute; residual scan hoàn tất với `residual=false`.
- Billing được kiểm theo ba mốc; Budget caveat được ghi thật, không tuyên bố “miễn phí tuyệt đối”.

## Khi mắc kẹt

Nếu bất kỳ bước nào sau deploy lỗi:

1. Dừng tạo/thử lại resource; xác nhận account, Region và project ID.
2. Chạy cleanup dry-run, đọc exact names, rồi execute với exact project ID.
3. Chạy residual scan. Nếu scan lỗi, kiểm Console hoặc nhờ quản trị account; không coi lỗi là “sạch”.
4. Dùng handler local để tiếp tục học. Không giữ stack sống chỉ để debug hoặc demo.

## Bash tương đương (macOS/Linux)

```bash
project="student01"; region="us-east-1"; artifact=".artifacts/churn-model/portable_model.json"
expires_at="$(date -d '+1 day' +%F 2>/dev/null || date -v+1d +%F)"
bash aws/scripts/cost-check.sh --project-id "$project" --region "$region"
bash aws/scripts/preflight.sh --project-id "$project" --region "$region" --artifact-path "$artifact" --acknowledge-budget-configured
bash aws/scripts/deploy.sh --project-id "$project" --owner student01 --expires-at "$expires_at" --artifact-path "$artifact" --region "$region" --acknowledge-budget-configured
bash aws/scripts/cleanup.sh --project-id "$project" --region "$region"
bash aws/scripts/cleanup.sh --project-id "$project" --region "$region" --execute --confirm-project-id "$project"
bash aws/scripts/residual-scan.sh --project-id "$project" --region "$region" --json
```

Nguồn AWS kiểm ngày 2026-08-12: [account plans](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans.html),
[Free Tier FAQ](https://aws.amazon.com/free/free-tier-faqs/),
[Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html).
