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

**Expected reasoning:** A satisfactory lifecycle verifies the local artifact, deploys only the guarded private path, checks valid and invalid events, reviews logs and costs, and proves cleanup.

**Evidence mapping:** The checksum, S3 object, IAM policy, Lambda responses, and CloudWatch logs describe inference. The budget settings and three Billing timestamps describe costs. The cleanup dry-run, execution result, and `residual=false` scan describe teardown.

**Misconception check:** A budget alert is not a spending cap, `ExpiresAt` does not delete resources, and requesting stack deletion does not prove cleanup. If a guard fails, stop cloud work and continue with the local fallback.
