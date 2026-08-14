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

**Use:** Pair the promoted `artifact` with private `inference`, then run a `residual scan` after cleanup; review the `Lambda`, `CloudWatch Logs`, and `API contract` evidence together.

## Concept walkthrough

### From artifact to inference

**Mental model:** `artifact`: An artifact is the set of model, configuration, metric, and metadata files needed to reproduce or serve predictions. It should be versioned and accompanied by enough provenance to verify how it was produced. `inference`: Inference uses a trained model to produce predictions for new input. It must apply exactly the preprocessing and feature order learned during training.

**Why it matters:** Inference is trustworthy only when the deployed artifact can be traced to its local training evidence and exact schema.

**Worked example:** `artifact`: model.joblib and manifest.json make up the artifact. `inference`: Load the artifact, then predict churn for an unseen customer.

**Easy to confuse:** An artifact is the saved model package; a checkpoint is training state used to resume. Inference uses a trained model; training updates its parameters.

**Check yourself:** Can the deployed `artifact` be traced from each `inference` result back to its schema and source run?

### Residual scan after the run

**Mental model:** `residual scan`: A residual scan checks for project resources that remain after cleanup. It should check every relevant service and identify anything that still needs removal.

**Why it matters:** A residual scan is the post-cleanup proof that the short cloud demonstration did not leave known project resources behind.

**Worked example:** `residual scan`: The scan checks CloudFormation, S3, Lambda, CloudWatch Logs, and IAM.

**Easy to confuse:** A residual scan verifies absence; cleanup performs the deletion actions.

**Check yourself:** Which services must the `residual scan` inspect after the short cloud run?

## Connect earlier terms

The `Lambda` response, `CloudWatch Logs`, and `API contract` now accompany the promoted artifact as deployment evidence. The post-cleanup scan closes the loop by checking that the short cloud run left no known resources.

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
