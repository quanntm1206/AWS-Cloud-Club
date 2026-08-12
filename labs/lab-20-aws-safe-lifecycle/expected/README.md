# Expected evidence - lab-20-aws-safe-lifecycle

## Oracle

Triển khai portable tabular model bằng S3 + private Lambda; kiểm valid/invalid contract, logs, cleanup và
zero residual. HTTP API là optional, tắt mặc định. Không dùng EC2, GPU, NAT Gateway hoặc SageMaker runtime.

## Required receipt

- Command: `AWS lifecycle commands in the lab guide`.
- Evidence must include the lab-specific metric/oracle, seed/config, runtime, and at least one limitation or failure.
- `status=starter-example-completed` proves only that the starter ran; acceptance remains a manual/rubric gate.
- Store this evidence locally for self-assessment; do not commit or send it. Exclude secrets, personal data, large raw datasets, and paid-cloud output.
