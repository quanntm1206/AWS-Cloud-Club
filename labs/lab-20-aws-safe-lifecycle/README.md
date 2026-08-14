# Lab 20 - Deploy a model to AWS, then clean it up

## Goal

Upload a portable tabular model to S3, invoke a private Lambda with valid and invalid input, inspect logs, run cleanup, and prove that no project infrastructure remains. Do not use EC2, SageMaker, Bedrock, NAT Gateway, or a public API.

## Terms used in this lab

**New terms:** `IAM`, `S3`, `Lambda`, `CloudWatch Logs`, `budget alert`, `residual scan`, `idempotent cleanup`

**Review:** `artifact`, `inference`, `API contract`

**Use in this lab:** Upload the `artifact` to `S3`, grant least-privilege access with `IAM`, call inference through `Lambda`, and read `CloudWatch Logs`. Create a `budget alert`, run `idempotent cleanup`, and complete a `residual scan` against the API contract.

**Explain it yourself:** A budget alert is not a hard cap. What do idempotent cleanup and a residual scan protect?


## Apply the concepts

### Private inference path

**Terms:** `artifact`, `S3`, `IAM`, `Lambda`, `inference`, `API contract`

**What they mean here:** Upload the local `artifact` to `S3`. Least-privilege `IAM` allows the private `Lambda` function to load it and run `inference` for valid and invalid events defined by the `API contract`.

**Where you will see them:** You will see this path in the local SHA-256 checksum, the S3 object, the IAM role policy, the stack outputs, and the two Lambda response files.

**Common mistake:** Retrying a failed deploy or adding a public endpoint when the private path is enough.

**Evidence to keep:** Keep sanitized checksum, output names, policy summary, and response shapes locally.

**Explain after the lab:** Trace model access and justify each permission while identifying what stays private.

### Delayed signals

**Terms:** `CloudWatch Logs`, `budget alert`

**What they mean here:** `CloudWatch Logs` records execution evidence; a `budget alert` sends delayed notifications, not a hard cap or zero-spend proof.

**Where you will see them:** The evidence includes sanitized log events, Actual and Forecasted budget notifications, and Billing checks at three different times.

**Common mistake:** Logging secrets or treating a quiet alert as a live billing guarantee.

**Evidence to keep:** Keep sanitized log summary, budget settings, and immediate, ~12-hour, and next-day timestamps.

**Explain after the lab:** Explain what logs and alerts establish and why later billing checks remain.

### Verified teardown

**Terms:** `idempotent cleanup`, `residual scan`

**What they mean here:** `idempotent cleanup` can be repeated safely for the exact project ID. After deletion, the `residual scan` checks whether any governed resources remain.

**Where you will see them:** Dry-run names precede execution, then the scan reports `residual=false` without permission errors.

**Common mistake:** Calling the project clean because deletion was requested.

**Evidence to keep:** Keep the dry-run, cleanup result, residual-scan result, account and Region confirmation without the account ID, and the decision to keep or delete the budget alert.

**Explain after the lab:** Use scan evidence to say clean or not clean and explain safe repetition.

## Before you start

- Read `aws/README.md`. Confirm your plan, credits, expiry date, account, and Region.
- Create a Cost budget with Actual and Forecasted email notifications. Do not use Budget Report or Budget Action.
- Reserve one uninterrupted 45-60 minute session and set a cleanup timer. Do not deploy just before leaving your computer.
- `ExpiresAt` is only reminder metadata; AWS does not delete a stack automatically from this tag.
- If Billing is unclear or the console asks you to upgrade to a Paid Plan, stop at the local simulation. The lab is still complete.

## What you will do

1. Train the local artifact and record its checksum.
2. Run cost planning and preflight.
3. Deploy S3, Lambda, CloudWatch Logs, and an IAM role with CloudFormation.
4. Invoke the private Lambda with valid and invalid events.
5. Clean up, run a residual scan, and check Billing at three checkpoints.

### 1. Prepare the local artifact

```powershell
.venv\Scripts\python.exe -c "from ml_roadmap.data import make_demo_churn_data; make_demo_churn_data(300,42).to_csv('.artifacts/churn.csv',index=False)"
.venv\Scripts\python.exe -m ml_roadmap.train_tabular --config capstones/tabular-churn/configs/mini.yml --data .artifacts/churn.csv --output .artifacts/churn-model
Get-FileHash .artifacts/churn-model/portable_model.json -Algorithm SHA256
```

### 2. Budget, estimate, and preflight

In the Console, open **Billing and Cost Management > Budgets > Create budget**. Choose a monthly Cost budget, then add Actual and Forecasted email notifications at a low threshold suitable for your account. Budgets can report late; they are not hard caps.

```powershell
$project = 'student01'
$region = 'us-east-1'
$expiresAt = (Get-Date).AddDays(1).ToString('yyyy-MM-dd')
aws sts get-caller-identity
pwsh aws/scripts/cost-check.ps1 -ProjectId $project -Region $region
pwsh aws/scripts/preflight.ps1 -ProjectId $project -Region $region -ArtifactPath .artifacts/churn-model/portable_model.json -AcknowledgeBudgetConfigured
```

Stop if the account or Region is wrong, the artifact exceeds 200 MB, the estimate exceeds USD 0.10, pricing cannot be verified, or output mentions a resource outside policy. The planning envelope is not a live quote or billing guarantee.

### 3. Deploy the private path

```powershell
pwsh aws/scripts/deploy.ps1 -ProjectId $project -Owner 'student01' -ExpiresAt $expiresAt -ArtifactPath .artifacts/churn-model/portable_model.json -Region $region -AcknowledgeBudgetConfigured
```

The template has no API Gateway or public URL. If deployment, output lookup, or upload fails, the stack may already exist. Do not retry immediately; go to **When you get stuck**.

### 4. Verify the artifact and private Lambda

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

A valid event returns label, probability, and threshold. An invalid event returns `statusCode=422` and missing fields. Invoke only a few times; this is not a load test.

### 5. Check logs

```powershell
aws logs tail "/aws/lambda/$function" --since 10m --region $region
```

Logs must not contain credentials or raw sensitive records. Log retention must be one day.

### 6. Clean up in the same session

```powershell
pwsh aws/scripts/cleanup.ps1 -ProjectId $project -Region $region
# Read the exact resource names before executing.
pwsh aws/scripts/cleanup.ps1 -ProjectId $project -Region $region -Execute -ConfirmProjectId $project
pwsh aws/scripts/residual-scan.ps1 -ProjectId $project -Region $region -Json
```

The scan checks CloudFormation, S3, Lambda, Logs, and IAM. A non-zero exit or a permission error means **clean status is not proven**. A budget alert is not in the stack and may be kept deliberately; review or delete it manually at the end of the course.

### 7. Cost audit

1. Check Billing, Free Tier, and credits immediately after cleanup. Record a timestamp, not the account ID.
2. Check again after about 12 hours and on the next day because billing can be delayed.
3. Keep local output in `.artifacts/`. Remove credentials, email addresses, and personal data from the learning log.

## When you are done

- The checksum exists before deployment. Private valid and invalid invokes follow the contract.
- No public endpoint or forbidden service exists.
- You read the cleanup dry-run before executing it. The residual scan finishes with `residual=false`.
- Billing is checked at all three checkpoints. Record the budget caveat honestly; do not claim that the run is absolutely free.

## When you get stuck

If any step fails after deployment:

1. Stop creating or retrying resources. Confirm the account, Region, and project ID.
2. Run cleanup in dry-run mode, read the exact names, then execute with the exact project ID.
3. Run the residual scan. If the scan fails, check the Console or ask the account administrator; do not call the project clean.
4. Use the local handler to continue learning. Do not keep a stack alive for debugging or demonstration.

## Bash equivalent (macOS/Linux)

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

AWS sources checked on 2026-08-12: [account plans](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans.html), [Free Tier FAQ](https://aws.amazon.com/free/free-tier-faqs/), and [Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html).
