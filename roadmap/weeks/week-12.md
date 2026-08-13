# Week 12 - Mini-project tabular

## Weekly goals

Synthesize reproducible tabular pipelines.

## Why this week matters

Mini-projects are the time to assemble the pieces into a process that others can run again, not the time to add lots of algorithms.

**Close example:** A model file is not enough without schema, threshold, config and how to properly reproduce preprocessing.

## Core knowledge

- Mini-project locks problem, contract, split, baseline and success criteria before optimization.
- Training exports models, portable artifacts, metrics, manifest and model cards.
- Reproduction guide starts from clean environment, writes command/config/seed/input/output.
- Model card states intended/out-of-scope use, data, metrics, subgroup, limitation and rollback signal.

## Keywords for this week

**New or focus terms:** `artifact`, `manifest`, `inference`

**Review:** `schema`, `data split`, `pipeline`

**Use:** Lock schema and data split, run pipeline; Save `artifact` with `manifest`, load in new process for inference, then compare baseline/metric and checksum.

## 8-10 hour schedule

| Activities | Hours |
|---|---:|
| Read and take notes | 2 |
| Guided practice | 2 |
| Lab | 3 |
| Assessment/error analysis | 1 |
| Learning log and self-assessment | 1 |
| Review/complete | 0 |

## Guided practice


1. Run mini churn pipeline end-to-end.
2. Reload the artifact in the new process and check the prediction output agreement.
3. Run reproduction guide from clean shell.

## Lab

**lab-11:** Mini-project tabular end-to-end. Main environment: `local`.

## Signs that you understand

From the clean shell, you train, save, reload the artifact and create the same prediction within the recorded tolerance.

## Test yourself

1. What does Artifact need besides weights?
2. What abuse must be mentioned on the card model?
3. What can be used to prove tremor re-establishment?

## Result oriented

competency milestone 3 + model card; Saves executed commands, configuration, metrics, runtime and one limitation.

## Core vs stretch

- **Core:** Run mini-project from clean shell; Load the artifact in the new process and complete the card model.
- **Expansion:** So config `mini` with exactly one controlled change; Record the negative result as well.

## Common errors

- Only saves notebooks depending on cell state, lacks reproducible artifacts.
- Missing split manifest/config.

## When you get stuck

Run `mini` first, checking each artifact. When output agreement is wrong, compare config and feature order before retraining.

## Source

Recommended source: scikit-learn's model persistence and model-card references in `docs/sources.yml`.