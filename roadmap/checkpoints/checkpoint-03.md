# Competency milestone 03 - Week 12

## Target

Evaluate a complete tabular project yourself, from data to error analysis.

## You have reached the if mark

- Pipeline handles schema, missing/category and model in the same contract to prevent leakage.
- Baseline and candidates use the same split, seed, metric and runtime budget.
- Feature engineering has a hypothesis; ablation only changes one decision at a time.
- Error analysis leads to the next action, and also indicates that the subgroup or failure mode is weak.

## Proof of reaching the milestone

- Short data/model card, split manifest, pipeline config and reproduction command saved locally.
- Baseline/candidate/ablation table, including a significant negative result.
- Total metric, appropriate subgroup metric and list of grouped failure cases.
- Artifact manifest with test schema, prediction parity or important invariant.

## Rubric

| Criteria | Score |
|---|---:|
| Pipelines and data contracts | 30 |
| Baseline and controlled experiments | 25 |
| Error analysis | 25 |
| Reconstruction and communication | 20 |

Passing score: 70/100. Gate: no leakage, no secret, mini run re-established; The final test cannot be used to correct the decision.

## Self-reflection question

- Candidate is better than baseline because of real signals or because the evaluation process has changed?
- Which failure cluster is worth addressing first, based on what impact?
- If there were two more hours, what would be the smallest experiment that would reduce uncertainty?