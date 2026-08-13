# AWS capstone: learn cloud skills without risking a surprise bill

The AWS section of the roadmap does one small but realistic job. Upload a tabular model trained on your local
machine, Colab, or Kaggle to S3, then invoke Lambda **privately**. There is no public endpoint. You learn the
deployment lifecycle, monitoring, and cleanup without using AWS for training.

## Understand USD 200 and the two account plans

- Eligible new accounts receive **USD 100 at sign-up** and **may earn up to USD 100 more** by completing
  activities chosen by AWS. AWS does not provide the full USD 200 at once.
- The **Free Plan** ends after 6 months or when its credits are used, whichever comes first. AWS describes this
  plan as having no charges. When it ends, the account closes unless you upgrade.
- The **Paid Plan** is pay-as-you-go. Credits cover only eligible charges; charges beyond the credits or outside
  their terms may still be billed. A Budget alert is not a hard cap.
- Free Tier credits expire 12 months after account creation. Eligibility, credits, and service allowances may
  vary by account. Trust the Billing page for your account rather than a number in this guide.

AWS sources, checked on 2026-08-12:
[account plans](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans.html),
[Free Tier FAQ](https://aws.amazon.com/free/free-tier-faqs/), and
[tracking Free Tier](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/tracking-free-tier-usage.html).

> AWS Cloud Club learners: do not join AWS Organizations or enable Control Tower for a learning account.
> According to the AWS FAQ, either action may move a Free Plan to the Paid Plan and immediately invalidate
> Free Tier credits. If the account has already joined, stop the AWS lab and use the local simulation.

## When to create an account

Do not create an account in week 1 and let the six-month clock run while you are still learning NumPy. If you
do not have an account, wait until the end of week 20 or the start of week 21. Do not create multiple accounts
to collect credits. Before each deployment, open Billing and check the `plan`, remaining credits, expiry date,
and eligible services. If the console requires the Paid Plan or the information is unclear, skip deployment.
The private handler still runs locally, so you can complete the work.

## Before you select Deploy

1. Enable MFA for the root user. Do not create a root access key. Use a least-privilege identity.
2. Confirm the correct account and `us-east-1` with `aws sts get-caller-identity`.
3. Create a **Cost budget** with low Actual and Forecasted email-alert thresholds. Use standard notifications
   only. Do not create a Budget Report or Budget Action for this lab.
4. Read `cost-policy.yml`. Do not use EC2/EBS/Elastic IP, NAT Gateway, SageMaker, Bedrock, RDS/Aurora,
   OpenSearch, Redshift, EMR/Glue, EKS/ECS/Fargate, Marketplace, Savings Plans, Reserved Instances, or a
   Route 53 domain. Discuss these services only as architecture or pricing options.
5. Run the cost check, compare it with the [AWS Pricing Calculator](https://calculator.aws/), then run preflight.
   `USD 0.00-0.10` is a planning envelope based on small-use assumptions, not a quote or billing promise.
6. Set a timer to clean up during the same session. The `ExpiresAt` tag is only a reminder. It **does not delete** resources.

AWS Budgets uses delayed data. AWS says a budget updates up to three times per day, usually every 8-12 hours.
An alert may arrive after spending has crossed its threshold. See
[AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)
and [Budget pricing](https://aws.amazon.com/aws-cost-management/aws-budgets/pricing/).

## Required lifecycle

```text
Pre-check -> Estimate -> Dry-run -> Deploy -> Verify -> Cleanup -> Residual scan -> Cost audit
```

`aws lambda invoke` is the only learning path. The template creates no API Gateway or public URL. Cleanup
deletes only an exact-name stack with the `ml-roadmap-` prefix. The script does not scan or delete resources
outside the project. The Budget alert remains intentionally to protect later sessions. At the end of the
course, review it and delete it in the Console yourself.

## If something goes wrong

If deployment fails, the terminal closes unexpectedly, or you are not sure whether the stack is still active:

1. Stop all resource-creation commands. Confirm the account, Region, and project ID again.
2. Run cleanup in dry-run mode. Read every exact resource name.
3. Run cleanup with project ID confirmation, then run the residual scan.
4. If the scan fails because of missing permissions, **do not** treat the account as clean. Check
   CloudFormation, S3, Lambda, CloudWatch Logs, and IAM manually, or ask the account administrator for help.
5. Check Billing now, after about 12 hours, and again the next day. A zero immediately after cleanup is not final evidence.

## You are safe when

- The project stack, bucket, Lambda, log group, and IAM role no longer exist.
- The residual scan returns `residual=false` without permission or network errors.
- You have scheduled another Billing check after the reporting delay.
- The remaining Budget alert is recorded as intentional, not mistaken for residual infrastructure.
