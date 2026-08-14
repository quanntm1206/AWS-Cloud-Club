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

**Use:** Demonstrate `idempotent cleanup`, review the `budget alert`, and verify the final `manifest`; include the `artifact`, `inference`, and `residual scan` evidence in the closing demo.

## Concept walkthrough

### Repeatable cleanup and budget signals

**Mental model:** `idempotent cleanup`: Idempotent cleanup can run repeatedly and still move toward the same clean state. It treats already-absent resources as a successful state rather than a fatal error. `budget alert`: A budget alert sends a notification when actual or forecast AWS cost reaches a threshold. It can watch actual and forecast spending, but AWS resources continue running until something stops them.

**Why it matters:** Idempotent cleanup proves repeatability of the technical state; a budget alert remains a separate delayed cost signal, not proof of deletion.

**Worked example:** `idempotent cleanup`: Delete resources with the exact project ID, then scan again. `budget alert`: An AWS Budget emails alerts for Actual and Forecasted spending.

**Easy to confuse:** Idempotent cleanup is safe to repeat; a one-shot delete may fail when partly completed. A budget alert sends a warning; it does not automatically stop AWS spending.

**Check yourself:** Why are `idempotent cleanup` evidence and a `budget alert` two separate safety signals?

### Manifest for the final handoff

**Mental model:** `manifest`: A manifest lists an artifact's contents, versions, checksums, and origin. Checksums help detect changed files, while metadata explains how those files were created.

**Why it matters:** The manifest ties the final artifact, schema, threshold, checksum, and source run into one auditable handoff.

**Worked example:** `manifest`: The manifest records the seed, feature order, and SHA-256 checksum.

**Easy to confuse:** A manifest describes files and provenance; the artifact contains the actual files.

**Check yourself:** Can the `manifest` identify the final artifact, schema, threshold, checksum, and source run?

## Connect earlier terms

The final `artifact` and its `inference` evidence are accepted only after the `residual scan` reports a clean technical state. The manifest and delayed budget review preserve separate provenance and cost evidence for the handoff.

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