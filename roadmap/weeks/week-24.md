# Week 24 - Closing the capstone as an ML Engineer

## Weekly goals

Present technical decisions, resource/cost audits, and planning for the next 90 days.

## Why this week matters

Good ML Engineers do not keep cloud resources alive just for beautiful slides. A good ending must show the model
It's reproducible, the limits are stated, the demo has fallbacks, and the system is cleaned up.

## Core knowledge

- Summarize according to problem, constraint, baseline, decision, evidence, failure and reproduction; not just accuracy.
- 5-7 minute demo using local fallback. No need for permanent AWS resources.
- Residual scan proves technical state; Billing justifies the cost but the data has latency.
- Budget alerts are intentionally kept, not residual infrastructure. Review or delete manually at the end of the course.
- “Done” means tests pass, card model updated, secret scan clean, limitations clear and zero known residual.

## Keywords for this week

**New or focus terms:** `idempotent cleanup`, `budget alert`, `manifest`

**Review:** `artifact`, `inference`, `residual scan`

**Use:** Demonstrate `idempotent cleanup`, reread `budget alert`, compare `manifest`; Review artifact, inference and residual scan in the final demo.

## 8-10 hour schedule

| Activities | Hours |
|---|---:|
| Rerun from clean environment | 2 |
| Prepare demo and fallback | 2 |
| Cleanup, residual scan, cost audit | 2 |
| Rubric, retrospective and 90-day plan | 2 |
| Learning log and self-assessment | 1 |

## Guided practice

1. Demo from clean environment, timer; Turn off AWS then try fallback locally.
2. Run cleanup dry-run, execute, residual scan. If there is an error in the scan, handle the error before concluding.
3. Check Billing immediately, schedule to check again after about 12 hours and the next day.
4. Review Budget alerts; Keep it if you're still learning AWS, delete it manually if you no longer need it.

## Lab

**lab-20:** incident drill, cleanup, residual scan and cost retrospective.

## Test yourself

1. Summarize engineering capabilities using what other than metrics?
2. Why is the number 0 right after cleanup not the last cost evidence?
3. How is the remaining budget different from residual infrastructure?

## Result oriented

Competency milestone 6: reset capstone, demo with fallback, audit with timestamp and 90-day plan for ML Engineer.

## Signs that you understand

You don't call a project "done" before reproduction, cleanup, residual scan and limitations are all clear.

## Core vs stretch

- **Core:** local demo + completed cleanup/audit.
- **Stretch:** architect the production path on paper, with auth, rate limit, monitoring and cost controls.

## Common errors

- Keep the endpoint alive for demonstration only.
- Insert account ID, credential or raw billing into the artifact.
- Seeing that Budget has not reported yet, it is concluded that there are no costs.

## When you get stuck

Prioritize safety: stop AWS demo, cleanup, use local fallback. If Billing has not been updated, record timestamp and
review schedule; Don't make up conclusions to complete the report.

## You are ready to end the route when

- Demo can run from clean environment and has local fallback.
- Residual scan completed with `residual=false`; Budget is reviewed separately.
- You checked Billing in three milestones: right after cleanup, about 12 hours, the next day.

## AWS cost gate

AWS Budgets updates up to three times a day, usually every 8-12 hours. Budget is not a hard cap. Source:
[AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html).

## Source

See `docs/sources.yml` and `aws/README.md`.