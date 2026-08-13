# Competency milestone 06 - Week 24

## Target

Self-assess AWS end-to-end capstone, presentation, and cost security.

## You have reached the if mark

- Demo from input to prediction using local fallback; AWS only uses private Lambda in controlled sessions.
- Manifest connects model version, schema, threshold, checksum and source run; The handler rejects the wrong contract.
- Complete cost check, preflight, deploy, verify, cleanup, residual scan and cost audit.
- Present the problem, constraint, baseline, decision, failure, limitation and how to re-establish it in 5-7 minutes.

## Proof of reaching the milestone

- Capstone README, architecture note, model card, reproduction command and demo outline saved locally.
- Test report for valid/invalid inference with local/portable parity.
- Cost manifest, deployment manifest, cleanup output and zero-residual report; Does not save account ID or raw billing.
- Retrospective records an incident drill or what would have been different if it were actually deployed.

## Rubric

| Criteria | Score |
|---|---:|
| End-to-end integration | 25 |
| Testing and reproducibility | 25 |
| AWS cost safety and cleanup | 30 |
| Demo and retrospective | 20 |

Passing score: 75/100. Gate: no leakage/secret, private-only, mini run reestablishment; cleanup and residual scan must be clean. If AWS is not secure or the credit/plan is unclear, use local fallback and do not grade the deployed AWS part.

## Self-reflection question

- What evidence shows that the system is clean of resources, instead of just seeing that the cleanup command returned successfully?
- If the billing update is late, when will you check and how will you record it?
- Which technical decision best represents your ML Engineer mindset?