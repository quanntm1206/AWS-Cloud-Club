# Reference result - `lab-20-aws-safe-lifecycle`

There is no single output to copy.

## Oracle

A satisfactory run shows all of the following:

- A portable artifact is created locally and has a SHA-256 checksum before upload.
- Cost planning and preflight finish on the correct account and `us-east-1`.
- CloudFormation creates only S3, a private Lambda, CloudWatch Logs, and an IAM role.
- A valid event returns label, probability, and threshold. An invalid event returns an intentional contract error.
- You read the cleanup dry-run before execution. The residual scan returns `residual=false` without a permission error.
- The budget alert is deliberately kept or manually deleted at the end; it is not misclassified as an infrastructure residual.
- Billing is checked immediately after cleanup, after about 12 hours, and on the next day.

## Required receipt

Keep the checksum, valid and invalid responses, cleanup output, residual JSON, and three cost-audit timestamps locally. Do not commit or send the account ID, billing email, or credentials.

## Terminology oracle

- The evidence connects IAM, S3, Lambda, CloudWatch Logs, and the budget alert. Idempotent cleanup and the residual scan prove that the project is clean or that a safe local fallback was used.
- Answer the `Explain it yourself` question in your own words and point to the evidence. Do not only copy the glossary.
