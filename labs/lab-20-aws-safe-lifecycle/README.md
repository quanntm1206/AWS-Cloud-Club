# lab-20: AWS safe lifecycle

## Goal

Triển khai portable tabular model bằng S3 + private Lambda; kiểm valid/invalid contract, logs, cleanup và
zero residual. HTTP API là optional, tắt mặc định. Không dùng EC2, GPU, NAT Gateway hoặc SageMaker runtime.

## 0. Chuẩn bị local artifact

```powershell
.venv\Scripts\python.exe -c "from ml_roadmap.data import make_demo_churn_data; make_demo_churn_data(300,42).to_csv('.artifacts/churn.csv',index=False)"
.venv\Scripts\python.exe -m ml_roadmap.train_tabular --config capstones/tabular-churn/configs/mini.yml --data .artifacts/churn.csv --output .artifacts/churn-model
Get-FileHash .artifacts/churn-model/portable_model.json -Algorithm SHA256
```

## 1. Tạo Budget alerts trên Console

1. Mở **Billing and Cost Management > Budgets > Create budget**.
2. Chọn **Cost budget**, monthly, fixed amount nhỏ phù hợp credit còn lại.
3. Thêm email alert cho **Actual** và **Forecasted** tại ngưỡng thấp do người học tự chọn.
4. Xác nhận email. Ghi screenshot/ID vào evidence; không commit email.

Budget chỉ cảnh báo; dữ liệu billing có thể trễ. Nó không tự chặn mọi chi phí.

## 2. Preflight

```powershell
$project='student01'
$region='us-east-1'
aws sts get-caller-identity
pwsh aws/scripts/preflight.ps1 -ProjectId $project -Region $region -ArtifactPath .artifacts/churn-model/portable_model.json -AcknowledgeBudgetConfigured
pwsh aws/scripts/cost-check.ps1 -ProjectId $project -Region $region
```

Dừng nếu account/Region sai, artifact >200 MB, chưa tạo alert hoặc output liệt kê resource ngoài policy.

## 3. Deploy core path

`ExpiresAt` là ngày kết thúc lab gần nhất. Deploy script gọi lại preflight trước CloudFormation.

```powershell
pwsh aws/scripts/deploy.ps1 -ProjectId $project -Owner 'student01' -ExpiresAt '2026-08-13' -ArtifactPath .artifacts/churn-model/portable_model.json -Region $region -AcknowledgeBudgetConfigured
```

Không thêm `-EnablePublicApi` cho core lab.

## 4. Verify artifact và private Lambda

```powershell
$stack="ml-roadmap-$project"
$bucket=aws cloudformation describe-stacks --stack-name $stack --region $region --query "Stacks[0].Outputs[?OutputKey=='BucketName'].OutputValue" --output text
$function=aws cloudformation describe-stacks --stack-name $stack --region $region --query "Stacks[0].Outputs[?OutputKey=='FunctionName'].OutputValue" --output text
aws s3api head-object --bucket $bucket --key models/portable_model.json --region $region
aws lambda invoke --function-name $function --payload fileb://aws/events/valid.json --region $region .artifacts/lambda-valid.json
aws lambda invoke --function-name $function --payload fileb://aws/events/invalid.json --region $region .artifacts/lambda-invalid.json
Get-Content .artifacts/lambda-valid.json
Get-Content .artifacts/lambda-invalid.json
```

Oracle: valid trả label/probability/threshold; invalid trả `statusCode=422` và danh sách missing fields.

## 5. Kiểm logs, không log raw payload

```powershell
aws logs tail "/aws/lambda/$function" --since 10m --region $region
```

Không được có credential hoặc raw sensitive record trong log. Log group retention phải là một ngày.

## 6. Cleanup trong cùng phiên

```powershell
pwsh aws/scripts/cleanup.ps1 -ProjectId $project -Region $region
# Đọc exact resources. Sau đó:
pwsh aws/scripts/cleanup.ps1 -ProjectId $project -Region $region -Execute -ConfirmProjectId $project
pwsh aws/scripts/residual-scan.ps1 -ProjectId $project -Region $region -Json
```

Cleanup empty bucket, xóa stack, chờ hoàn tất. Residual scan kiểm CloudFormation, S3, Lambda, Logs, IAM,
API Gateway theo exact prefix. Exit khác 0 nghĩa lab chưa sạch.

## 7. Cost audit

1. Mở Billing home/Free Tier/credits; ghi timestamp, credit before/after khi dữ liệu cập nhật.
2. Xác nhận không còn stack/resource theo scan.
3. Lưu `.artifacts/lambda-valid.json`, cleanup output, residual JSON và learning log; không commit account ID.

Giữ toàn bộ evidence cục bộ để tự đánh giá; không gửi các file này cho ai. Xóa credential, account ID và
dữ liệu cá nhân khỏi bản tổng kết.

## Acceptance

- Portable model checksum có trước deploy; private invoke valid/invalid đúng contract.
- Không forbidden resource hoặc public API trong core path.
- Cleanup dry-run được đọc trước execute; residual scan sạch mọi allowlist service.
- Cost audit ghi Budget caveat và billing delay; không tuyên bố “miễn phí tuyệt đối”.


## Bash equivalents (macOS/Linux)

```bash
project="student01"; region="us-east-1"; artifact=".artifacts/churn-model/portable_model.json"
bash aws/scripts/cost-check.sh --project-id "$project" --region "$region"
bash aws/scripts/preflight.sh --project-id "$project" --region "$region" --artifact-path "$artifact" --acknowledge-budget-configured
bash aws/scripts/deploy.sh --project-id "$project" --owner student01 --expires-at 2026-08-13 --artifact-path "$artifact" --region "$region" --acknowledge-budget-configured
bash aws/scripts/cleanup.sh --project-id "$project" --region "$region"
bash aws/scripts/cleanup.sh --project-id "$project" --region "$region" --execute --confirm-project-id "$project"
bash aws/scripts/residual-scan.sh --project-id "$project" --region "$region"
```

Không chạy deploy khi chưa đọc output estimate/preflight. Cleanup và residual scan cùng phiên.
