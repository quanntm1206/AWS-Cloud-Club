# Week 21 - Step up to AWS while keeping costs under control

## Weekly goals

Understand account plans, credits, IAM, Budget, and S3 before creating any resources.

## Why this week matters

An ML Engineer not only knows how to deploy; They also know when **not to deploy**. This week's reading help
Billing screen, recognize Free/Paid Plan boundaries and set up safety fences before touching the cloud.

## Core knowledge

- “Up to USD 200” is USD 100 when registering and can earn up to USD 100 more through activities; no
  USD 200 will be issued immediately. Free Plan ends after 6 months or when credits run out.
- Paid Plan is pay-as-you-go. Credit only offsets qualifying amounts; Budget alert is not a hard cap.
- Joining AWS Organizations or setting up Control Tower may cause credits to expire and Free Plan to automatically increase
  Paid Plan. Do not use these two features in your learning account.
- IAM least privilege, MFA root, no root access key; Always confirm account ID and Region before ordering.
- S3 is calculated by storage, request and transfer. Small artifact, block public access, short lifecycle.

Source AWS, checked on 2026-08-12:
[plans](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans.html),
[FAQ](https://aws.amazon.com/free/free-tier-faqs/) and
[tracking](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/tracking-free-tier-usage.html).

## Keywords for this week

**New or focus terms:** `IAM`, `S3`, `Lambda`, `CloudWatch Logs`, `budget alert`, `residual scan`, `idempotent cleanup`

**Review:** `artifact`, `inference`, `API contract`

**Use:** Upload the `artifact` to `S3`, grant least-privilege access with `IAM`, invoke `Lambda` for `inference`, and inspect `CloudWatch Logs`; create a `budget alert`, perform `idempotent cleanup`, then confirm the result with a `residual scan` against the `API contract`.

## Concept walkthrough

### Least privilege and storage

**Mental model:** `IAM`: AWS Identity and Access Management (IAM) controls identities and permissions using least privilege. Policies attach allowed actions and resources to users, roles, or services. `S3`: Amazon S3 is an object storage service used here for small model artifacts. Each object has a key inside a bucket and can be protected with IAM and encryption.

**Why it matters:** Least-privilege IAM limits the blast radius, while a private S3 object keeps the model artifact inside the intended boundary.

**Worked example:** `IAM`: The Lambda role may read only the intended model object in S3. `S3`: Upload portable_model.json to a private bucket.

**Easy to confuse:** IAM controls access; security groups control network traffic. S3 stores objects in buckets; a file system exposes directories and file operations.

**Check yourself:** Which S3 action must the Lambda role allow, and which unrelated actions should it deny?

### Event-driven execution

**Mental model:** `Lambda`: AWS Lambda runs functions on request without requiring users to manage servers. AWS provisions the execution environment and charges for the resources used by each invocation. `CloudWatch Logs`: CloudWatch Logs stores runtime logs on AWS, where sensitive data and retention require deliberate controls. Log groups need explicit retention, access control, and rules that prevent sensitive values from being written.

**Why it matters:** Lambda performs the event-driven computation; CloudWatch Logs provide bounded operational evidence without becoming a store for sensitive payloads.

**Worked example:** `Lambda`: Use a private invoke to run tabular inference. `CloudWatch Logs`: Set the Lambda log group retention to one day.

**Easy to confuse:** Lambda is compute; S3 is object storage. CloudWatch Logs stores runtime logs; CloudWatch metrics store numeric measurements.

**Check yourself:** Which log fields prove that Lambda loaded the intended artifact without exposing a customer payload?

### Observability and cost

**Mental model:** `budget alert`: A budget alert sends a notification when actual or forecast AWS cost reaches a threshold. It can watch actual and forecast spending, but AWS resources continue running until something stops them. `residual scan`: A residual scan checks for project resources that remain after cleanup. It should check every relevant service and identify anything that still needs removal.

**Why it matters:** A budget alert reports a cost threshold, while a residual scan inspects the actual technical state after cleanup.

**Worked example:** `budget alert`: An AWS Budget emails alerts for Actual and Forecasted spending. `residual scan`: The scan checks CloudFormation, S3, Lambda, CloudWatch Logs, and IAM.

**Easy to confuse:** A budget alert sends a warning; it does not automatically stop AWS spending. A residual scan verifies absence; cleanup performs the deletion actions.

**Check yourself:** Why can a budget alert be quiet while a residual scan still finds a resource?

### Safe cleanup

**Mental model:** `idempotent cleanup`: Idempotent cleanup can run repeatedly and still move toward the same clean state. It treats already-absent resources as a successful state rather than a fatal error.

**Why it matters:** Idempotent cleanup can recover from partial failure because rerunning it still targets the same clean state.

**Worked example:** `idempotent cleanup`: Delete resources with the exact project ID, then scan again.

**Easy to confuse:** Idempotent cleanup is safe to repeat; a one-shot delete may fail when partly completed.

**Check yourself:** What second-run result demonstrates that cleanup is idempotent?

## Connect earlier terms

The local `artifact` now reaches cloud `inference` through the same `API contract`. S3 checksums, Lambda responses, and bounded logs show that the cloud path preserves the intended model and interface.

## 8-10 hour schedule

| Activities | Hours |
|---|---:|
| Read plans, credits and cost policy | 2 |
| See Billing, IAM and Budget with instructions | 2 |
| Run local preflight, checksum and cleanup dry-run | 3 |
| Learning log and self-assessment | 2 |

## Guided practice

1. If you don't have an account, only create it in week 20/21 so as not to waste the 6 month window. Do not create multiple accounts
   to hunt for credits.
2. Open Billing; Enter `plan`, remaining credits, expiration date and days remaining. If the information is unclear or
   Console starts to upgrade Paid Plan, select local-only.
3. Create Cost budget with Actual and Forecasted email alerts at low thresholds. Do not create a Budget Report either
   Budget Action. Alert has a delay, does not replace cleanup.
4. Run `cost-check` and `preflight` locally. Practice reading the reason for stopping instead of quickly ignoring the guard.

## Lab

**lab-20, preparation:** checksum artifact, cost planning, preflight and cleanup dry-run. Not deployed yet.

## Test yourself

1. Why is “up to USD 200” not available USD 200?
2. How is the Free Plan different from the Paid Plan in terms of charge risk?
3. Why can't Budget replace cleanup?

## Result oriented

You can explain your account's plan/credit, create the right type of alert and recognize the stopping conditions.

## Signs that you understand

You can distinguish between credit, Free Plan, Paid Plan and Budget without calling them all "free".

## Core vs stretch

- **Core:** local preflight + read Billing/plan clearly.
- **Stretch:** reads AWS Pricing Calculator for S3/Lambda; Don't try deploying just to see.

## Common errors

- Tin credit or Budget automatically blocks all costs.
- Join Organizations/Control Tower because of the club's invitation.
- Create an account from the beginning of the route and let the Free Plan expire before the capstone.

## When you get stuck

Do not guess account status. Capture non-sensitive information or ask the club manager; continue
local-only. Do not send account ID, billing email or credential.

## Are you ready to move weeks when

- You know whether your account is in Free or Paid Plan and the expiration date.
- You have Actual + Forecasted notifications; understand that they may report late.
- You can say “don't deploy” when eligibility, estimate or cleanup path is unclear.

## AWS cost gate

Do not run if account/Region is wrong, `aws/README.md` has not been read, there is no cleanup path or the estimate has been exceeded
USD 0.10. Do not use EC2, NAT Gateway, SageMaker, Bedrock, database, container cluster or Marketplace.

## Source

See `docs/sources.yml` and `docs/source-notes/aws-free-tier.md`.