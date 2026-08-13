# Competency milestone 05 - Week 20

## Target

Evaluate yourself with Computer Vision with transfer learning and limited compute for free.

## You have reached the if mark

- Use correct pretrained weights/normalization, have frozen-backbone baseline and mini CPU fallback. If pretrained
  weights cannot be loaded, random-weight run is just execution smoke and has not passed gate transfer learning.
- Checkpoint stores all models, optimizers, epochs, best metrics, history, config, seeds and class mapping.
- Resume continues from the correct epoch; Do not silently retrain from the beginning when the runtime is interrupted.
- Report macro/per-class metrics, confusion matrix and grouping failure cases instead of just accuracy.

## Proof of reaching the milestone

- Notebook Colab or Kaggle can run with device check, mini profile and locally saved command/config.
- Checkpoint manifest, checksum and log prove the resume path works.
- The frozen/unfreeze table has runtime, metrics and quota/compute limits.
- Confusion matrix, per-class report and up to 20 failure examples; If less, save all and clearly state.

## Rubric

| Criteria | Score |
|---|---:|
| Transfer learning is correct | 25 |
| Checkpoint and resume | 25 |
| Per-class evaluation | 30 |
| Failure analysis and limits | 20 |

Passing score: 70/100. Gate: pretrained weights and normalization correct, best/last checkpoint loadable, CPU mini path
recreated, no tokens in notebook/output. FakeData can demonstrate the pipeline; Quality evidence requires real data.

## Self-reflection question

- Is improving metrics worth the runtime and quota used?
- Which image class or condition is the most commonly mistaken model, and why?
- Which results are just execution smoke, not proving model quality?