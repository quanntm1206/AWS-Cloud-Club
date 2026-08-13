# Week 23 - Connect the capstone into a small explainable system

## Weekly goals

Connect training local/Colab/Kaggle with artifact, manifest and private Lambda inference.

## Why this week matters

A reliable demo is not a lucky run of commands. Manifest helps you answer: which model, which schema,
what threshold, what run it was trained from and whether the artifact has been changed or not.

## Core knowledge

- Training is still at local/Colab/Kaggle. AWS only stores the portable logistic model and runs short inference.
- Manifest links model version, feature schema, threshold, checksum and source run.
- CloudFormation manages all lab resources; ownership tags support audit, not self-cleanup.
- Learner path only has private `aws lambda invoke`. Public API is an architecture topic for reading, not practice.
- If deploy/upload/output lookup fails, the stack may already exist; recovery cleanup is required.

## Keywords for this week

**New or focus terms:** `artifact`, `inference`, `residual scan`

**Review:** `Lambda`, `CloudWatch Logs`, `API contract`

**Use:** Pair `artifact` with private `inference`, after cleanup run `residual scan`; Review Lambda, CloudWatch Logs and API contracts.

## 8-10 hour schedule

| Activities | Hours |
|---|---:|
| Review artifact contract and manifest | 2 |
| Train mini profile, check parity | 2 |
| Run end-to-end private invoke | 3 |
| Failure drill and cleanup | 1 |
| Learning log and self-assessment | 1 |

## Guided practice

1. Train mini profile outside AWS; so portable model with sklearn on top of known requests.
2. Check checksum, schema and threshold before uploading.
3. Run end-to-end private invoke; Do not load test, do not create public endpoint.
4. Rehearse a failure after deploying and read the recovery command before cleanup.

## Lab

**lab-20:** end-to-end capstone via private Lambda. API Gateway is only analyzed on the diagram/pricing.

## Test yourself

1. Why not directly ship `joblib` runtime dependencies?
2. What type of drift does Manifest prevent?
3. After uploading an error, why do we still need to check the stack?

## Result oriented

You can demo the train -> portable artifact -> S3 -> private Lambda -> cleanup flow, and explain
get each guard instead of just reading the green output.

## Signs that you understand

You trace back a prediction to the correct artifact, schema, threshold and source run.

## Core vs stretch

- **Core:** end-to-end private invoke, up to several requests.
- **Stretch:** draws the authenticated/throttled API architecture and lists required guards; do not deploy.

## Common errors

- Train on SageMaker/EC2 only for credits.
- Add public URL to make the demo look more "real".
- Leave the stack overnight because the `ExpiresAt` message deletes itself.

## When you get stuck

Return to the local handler and known request. If AWS has created a stack, prioritize cleanup before debugging. A demo
local has a good explanation which is safer than a live stack that you don't control.

## Are you ready to move weeks when

- Portable/sklearn parity reached on known requests.
- You can prove checksum + schema + source run.
- Residual scan completed, no known infrastructure remaining.

## AWS cost gate

Do not raise Paid Plan to complete core. No SageMaker, EC2, NAT Gateway, API Gateway or Bedrock.
If pricing/eligibility cannot be verified, use local simulation.

## Source

[AWS Pricing Calculator](https://calculator.aws/) and `docs/sources.yml`.