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

**Use:** Use the `validation set` for `model validation`; choose a `metric` from `precision / recall / F1`, select a `threshold` that reflects `class imbalance`, compare with the `baseline`, and keep the test set closed.

## Concept walkthrough

### Metrics answer decisions

**Mental model:** `metric`: A number that measures one aspect of model quality and should match the goal and cost of errors. No single metric describes every kind of quality, so its meaning must be stated. `precision / recall / F1`: Precision focuses on correct positive predictions, recall focuses on finding enough positive samples, and F1 balances both sides. All three come from confusion-matrix counts but answer different questions.

**Why it matters:** A metric must reflect the error cost; precision, recall, and F1 expose different trade-offs hidden by accuracy.

**Worked example:** `metric`: Recall measures the rate at which customer churn is found. `precision / recall / F1`: A churn team prioritizes recall but still tracks precision.

**Easy to confuse:** A metric is a measurement; loss is the objective optimized during training. Precision asks whether positive predictions are right; recall asks whether positives were found.

**Check yourself:** Which error cost makes recall more useful than precision for the chosen `metric`?

### Thresholds change trade-offs

**Mental model:** `threshold`: Threshold converts scores or probabilities into decision labels. Lowering it usually finds more positive cases but also creates more false alarms. `class imbalance`: There is a large difference in the number of samples between classes. The minority class can have too little influence on accuracy or model training.

**Why it matters:** A threshold turns scores into actions, while class imbalance changes how much evidence each class contributes.

**Worked example:** `threshold`: Probabilities of 0.35 or higher are labeled churn. `class imbalance`: Only 8% of customers churn so accuracy is easily misleading.

**Easy to confuse:** A threshold changes decisions, not the underlying predicted probability. Class imbalance describes label counts, not unequal business costs by itself.

**Check yourself:** How can `class imbalance` change the decision when the `threshold` moves?

## Connect earlier terms

The `validation set` and `model validation` process now support a decision-specific metric and threshold. Comparing them with the `baseline` shows whether the chosen precision-recall trade-off is a real improvement.

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