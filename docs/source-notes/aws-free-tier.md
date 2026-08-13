# AWS Free Tier - source notes

**Verified:** 2026-08-12. This information can change. Check it again before each cohort and each deployment.

- Eligible new accounts receive USD 100 after sign-up and may earn up to USD 100 more through activities.
  The phrase "up to USD 200" does not mean that AWS gives the full USD 200 at once.
- The Free Plan ends after 6 months or when its credits are used, whichever comes first. AWS describes this
  plan as having no charges. The account closes when the plan ends unless the user upgrades.
- The Paid Plan is pay-as-you-go. Remaining credits apply only to eligible charges. A Budget is not a hard cap.
- Free Tier credits expire 12 months after account creation. Existing or past customers may not be eligible.
- Joining AWS Organizations or setting up Control Tower may immediately invalidate the credits and move a
  Free Plan to the Paid Plan.
- AWS Budgets updates up to three times per day, usually every 8-12 hours. An alert may arrive after a threshold is exceeded.
- Budget monitoring and notifications are free. Avoid Budget Reports and Budget Actions in the lab because
  they have separate pricing.

## Official sources

- Plans: https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans.html
- FAQ: https://aws.amazon.com/free/free-tier-faqs/
- Tracking: https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/tracking-free-tier-usage.html
- Budgets: https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html
- Budget pricing: https://aws.amazon.com/aws-cost-management/aws-budgets/pricing/

**Decision:** The core path uses only S3, a private Lambda, CloudWatch Logs, IAM, and Budgets. It has no public
API. Training stays on local, Colab, or Kaggle compute. If the account or pricing is unclear, learners use the
local simulation.
