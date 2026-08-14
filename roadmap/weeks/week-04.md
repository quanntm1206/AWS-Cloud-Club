# Week 04 - Intuitive math and linear regression

## Weekly goals

Write your own small linear regression; Read the loss curve and use basic probability to interpret the results.

## Why this week matters

Loss tells the model how much it is wrong; The gradient indicates which direction the parameter should be changed. Grasping this intuition will help you debug any model later.

**Close example:** If the learning rate is too large, each step can jump over the bottom of the loss like a person going downhill but taking steps that are too long.

## Core knowledge

- Linear regression uses y_hat=Xw+b; MSE penalizes the squared error and is outlier sensitive.
- Gradient indicates the direction of rapid increase of loss; The gradient updates in the opposite direction of the learning rate descent.
- Central finite difference checks analytic gradient by small changes of parameters.
- Feature scale influences convergence; The coefficients are only interpreted along with scale, encoding and assumptions.
- Probability within `[0, 1]`; Conditional probability is always associated with a condition, while sample frequency is only an estimate with error.

## Keywords for this week

**New or focus terms:** `prediction`, `loss`, `gradient`, `learning rate`

**Review:** `feature`, `label / target`, `data validation`

**Use:** Compute a `prediction` and `loss`, follow the `gradient`, then update each parameter with the chosen `learning rate`; retain the `feature`, `label / target`, and any `data validation` error.

## Concept walkthrough

### Prediction and error

**Mental model:** `prediction`: The value a model produces for one sample. For regression it may be a number; for classification it may be a class or probability. `loss`: The number a model tries to reduce during training to measure error on learning data. Different tasks use different loss functions, such as MSE for regression or cross-entropy for classification.

**Why it matters:** A prediction is the model output; loss gives training a numerical objective for improving that output.

**Worked example:** `prediction`: The model predicts monthly_charges of 42.5. `loss`: MSE penalizes the squared distance between prediction and target.

**Easy to confuse:** A prediction is an output value; a label is the observed answer. Loss guides training; a metric reports the quality people care about.

**Check yourself:** Why can a lower `loss` improve a `prediction` without making it useful for the product?

### How learning moves

**Mental model:** `gradient`: The direction and size showing how loss changes when a parameter changes. Its sign gives direction, and its magnitude shows how strongly the loss responds. `learning rate`: The size of each parameter update. The optimizer multiplies this value by the gradient when forming an update.

**Why it matters:** The gradient supplies update direction, while the learning rate controls how far parameters move in that direction.

**Worked example:** `gradient`: A positive gradient suggests lowering the parameter by the learning rate. `learning rate`: A learning rate that is too large makes loss oscillate or grow.

**Easy to confuse:** A gradient is a direction of change; the learning rate scales the update size. The learning rate is an update setting, not the loss being minimized.

**Check yourself:** What happens to an update when the `gradient` stays fixed but the `learning rate` doubles?

## Connect earlier terms

Each `feature` now contributes to a prediction that can be compared with the `label / target`; `data validation` remains the gate that keeps malformed inputs out of the calculation. Logged loss and parameter updates make the connection observable.

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


1. Calculate forward, MSE, gradient manually on four points.
2. So analytic gradient with finite difference over many epsilons.
3. So loss curve when learning rate is small, reasonable, too large.

## Lab

**lab-03:** Linear regression from the beginning and gradient check. Main environment: `local`.

## Signs that you understand

You write your own small linear regression, check gradient matching and read the loss curve to tell whether the model is learning or diverging.

## Test yourself

1. What does a gradient of 0 say?
2. What number error does Epsilon too small cause?
3. How is MSE different from MAE and outlier?

## Result oriented

competency milestone 1; Saves the executed command, configuration, quality measure, run time and one limitation.

## Core vs stretch

- **Core:** Write your own linear regression, gradient check and explain three types of loss curves.
- **Extension:** Try MAE instead of MSE or change the feature scale, but keep the same factor at each run.

## Common errors

- Believe the gradient is correct only because the loss is reduced.
- Increase training pass to cover learning rate that is too high.

## When you get stuck

Calculate one step per four points by hand. If the gradient is skewed, check the sign, mean coefficient and multiple `epsilon` values.

## Source

Recommended source: the optimization/linear models section in the scikit-learn documentation and textbook is registered in `docs/sources.yml`.