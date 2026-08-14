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

**Use:** Lock the `schema` and `data split`, then run the `pipeline`; save the `artifact` with its `manifest`, load it in a new process for `inference`, and compare predictions, metrics, and checksums.

## Concept walkthrough

### Artifact and manifest

**Mental model:** `artifact`: An artifact is the set of model, configuration, metric, and metadata files needed to reproduce or serve predictions. It should be versioned and accompanied by enough provenance to verify how it was produced. `manifest`: A manifest lists an artifact's contents, versions, checksums, and origin. Checksums help detect changed files, while metadata explains how those files were created.

**Why it matters:** An artifact is useful only when its manifest identifies the exact schema, configuration, checksum, and source run.

**Worked example:** `artifact`: model.joblib and manifest.json make up the artifact. `manifest`: The manifest records the seed, feature order, and SHA-256 checksum.

**Easy to confuse:** An artifact is the saved model package; a checkpoint is training state used to resume. A manifest describes files and provenance; the artifact contains the actual files.

**Check yourself:** Could a reviewer identify every file and source run from the `artifact` and `manifest` alone?

### Inference from saved state

**Mental model:** `inference`: Inference uses a trained model to produce predictions for new input. It must apply exactly the preprocessing and feature order learned during training.

**Why it matters:** Inference must reproduce training-time preprocessing and feature order without relying on notebook state.

**Worked example:** `inference`: Load the artifact, then predict churn for an unseen customer.

**Easy to confuse:** Inference uses a trained model; training updates its parameters.

**Check yourself:** Does `inference` reproduce the same preprocessing and feature order without notebook state?

## Connect earlier terms

The saved `schema`, `data split`, and `pipeline` now become provenance inside the artifact manifest. Reloaded predictions and matching checksums show that the new process uses the same learned path.

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
