# Week 20 - CV evaluation and failure analysis

## Weekly goals

Evaluate per-class and failure grouping.

## Why this week matters

The aggregated metric does not indicate where the model is wrong. Failure analysis helps you decide whether to edit data, labels, transforms or models.

**Close example:** A class with few samples may be omitted in weighted F1 but clearly visible in macro F1 and row-by-row confusion matrix.

## Core knowledge

- Overall accuracy covers weak class; report per-class precision/recall/F1/support and macro/weighted aggregate.
- Confusion matrix normalized according to true class helps compare recall between other support classes.
- Failure record has sample ID, truth, prediction, confidence, error type; Do not publish sensitive data.
- Review according to sampling rule and then group data, label, ambiguity, transform, model or shift.
- Model card attaches metrics to dataset/split/config and prohibits using fallback data to conclude quality.

## Keywords for this week

**New or focus terms:** `confusion matrix`, `support`

**Review:** `metric`, `validation set`, `error analysis`, `failure taxonomy`

**Use:** Build a `confusion matrix` with precision, recall, F1, and `support`; perform `error analysis` on real validation predictions, assign each failure to the `failure taxonomy`, and never use FakeData for `model validation`.

## Concept walkthrough

### Counts behind the metric

**Mental model:** `confusion matrix`: A table that counts each combination of true class and predicted class. Its cells separate true positives, false positives, true negatives, and false negatives.

**Why it matters:** A confusion matrix exposes the exact class-to-class mistakes hidden by one aggregate score.

**Worked example:** `confusion matrix`: The row churn=1 indicates how many samples were predicted to be 0.

**Easy to confuse:** A confusion matrix contains counts; precision, recall, and F1 summarize those counts.

**Check yourself:** Which error counts in the `confusion matrix` explain the class-level metric?

### Support gives denominators

**Mental model:** `support`: Support is the number of actual samples in a class or slice. Small support makes an apparently perfect metric uncertain.

**Why it matters:** Support supplies the denominator, so a strong class or slice score can be judged against the amount of evidence behind it.

**Worked example:** `support`: 100% recall on support=2 is not enough for a strong conclusion.

**Easy to confuse:** Support is a count, not a quality score.

**Check yourself:** Is the `support` large enough to trust the reported class or slice score?

## Connect earlier terms

The existing `metric` on the `validation set` is now decomposed into class-level counts and support. `error analysis` and the `failure taxonomy` explain which real examples create each weak class result.

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


1. Create per-class table and confusion matrix.
2. Export up to 20 failure records, confident-wrong priority.
3. Write limitation and next experiment from taxonomy.

## Lab

**lab-19:** Confusion matrix and up to 20 failure examples; If less, export all and write limitation. Main environment: `local, colab, kaggle`.

## Signs that you understand

You create a per-class table, review errors according to the rules, write limitations, and a follow-up experiment can disprove the hypothesis.

## Test yourself

1. Other macros weighted F1?
2. What does normalizing matrix by row answer?
3. Sampling only follows what confidence bias?

## Result oriented

competency milestone 5 + model card; Saves executed commands, configuration, metrics, runtime and one limitation.

## Core vs stretch

- **Core:** Create per-class metrics, confusion matrix, failure taxonomy and model cards from real runtime.
- **Expansion:** Try another sampling rule for failure review; Do not publish photos without permission to share.

## Common errors

- View only aggregates.
- Putting data that does not have sharing rights into the public artifact.

## When you get stuck

Start with 5-10 errors. If the photo is sensitive or doesn't have permission to share, save only the anonymized ID and description.

## Source

Recommended reading: scikit-learn classification metrics/confusion matrix and model-card guidance in `docs/sources.yml`.