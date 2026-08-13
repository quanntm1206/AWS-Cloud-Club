# Week 07 - Metrics, imbalance and threshold

## Weekly goals

Choose metric and threshold according to error cost.

## Why this week matters

Metrics should reflect the type of errors you truly care about. Threshold is an operational decision, not the default number of 0.5.

**Close example:** In risk screening, missing a case can be more expensive than a false alarm; Recall may therefore be more important than accuracy.

## Core knowledge

- Confusion matrix separates TP/FP/FN/TN; precision measures the accuracy of positive prediction, recall measures the true positive found.
- F1 balances precision/recall but does not replace the cost of FP/FN.
- ROC-AUC measures ranking; PR-AUC is often more obvious when positives are rare.
- Select threshold on validation, lock it, then evaluate the test; 0.5 is not the optimal default.
- Log loss penalizes confident but wrong predictions; calibration asks whether the predicted group of about 0.7 is close to 70% positive.

## Keywords for this week

**New or focus terms:** `metric`, `precision / recall / F1`, `threshold`, `class imbalance`

**Review:** `validation set`, `model validation`, `baseline`

**Use:** Use `validation set` for `model validation`: select metrics precision / recall / F1 and threshold according to class imbalance, compared to baseline; keep the test set closed until the end.

## 8-10 hour schedule

| Activities | Hours |
|---|---:|
| Read and take notes | 2 |
| Guided practice | 2 |
| Lab | 3 |
| Assessment/failure review | 1 |
| Learning log and self-assessment | 1 |
| Review/complete | 0 |

## Guided practice


1. Create a table of metrics and business costs based on threshold.
2. Choose a threshold that satisfies minimum recall using validation.
3. Apply the locked threshold to the test.

## Lab

**lab-06:** Imbalance, PR/ROC, confusion matrix. Main environment: `local`.

## Signs that you understand

You choose the threshold on validation according to the FP/FN cost, lock it and then evaluate the test; Explain trade-off.

## Test yourself

1. How does increasing recall affect precision?
2. Does high AUC warrant calibration?
3. Why not choose threshold on test?

## Result oriented

metric decision memo; Saves executed commands, configuration, metrics, runtime and one limitation.

## Core vs stretch

- **Core:** Choose threshold using validation according to cost rule; locked before evaluating the test.
- **Expand:** Draw a small reliability/calibration curve or compare log loss for two models with the same accuracy.

## Common errors

- Accuracy indicator on imbalance.
- Fix threshold after viewing test.

## When you get stuck

Set up a confusion matrix by pre-counting. If PR-AUC and ROC-AUC cause trouble, go back to asking if positive class is rare.

## Source

Recommended source: scikit-learn model evaluation on precision-recall, ROC, log loss and calibration.