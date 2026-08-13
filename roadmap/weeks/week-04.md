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

**Use:** Calculate `prediction`, `loss`, `gradient` and update parameters with `learning rate`; keep feature, label / target and log data validation error if input is wrong.

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