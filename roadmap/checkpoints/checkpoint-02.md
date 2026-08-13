# Competency milestone 02 - Week 8

## Target

Self-assess your ability to choose a reliable way to measure and test your model.

## You have reached the if mark

- Split the data before any transform that learns parameters and explain why the pipeline does not leak.
- Compare the model with a simple baseline on the metric associated with false positive/false negative costs.
- Select threshold on validation, only open test after locking decision.
- Use cross-validation or learning curve to describe stability, not just a score.

## Proof of reaching the milestone

- Split manifest, pipeline config and baseline report saved locally.
- The metric/threshold table has at least one trade-off explained.
- Cross-validation or learning curve results with mean, dispersion and runtime.
- A leakage test or intentionally false experiment shows that the guardrail is working.

## Rubric

| Criteria | Score |
|---|---:|
| Split data and prevent leakage | 30 |
| Choose the metric according to the problem | 30 |
| Cross-validation and stability | 25 |
| Conclusion with evidence | 15 |

Passing score: 70/100. Gate: no leakage, no secret, test set is not used to select model or threshold.

## Self-reflection question

- Which metric can be beautiful but lead to bad business decisions?
- What does the difference between folds tell you about the data?
- If the cost of false negatives doubles, how should the threshold be revised?