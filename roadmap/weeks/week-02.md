# Week 02 - NumPy and vectorization

## Weekly goals

Use vector, matrix, broadcasting; understand shapes.

## Why this week matters

NumPy is the lingua franca of numerical data. Understanding shape and axis early will help you avoid many mistakes where the model works but calculates incorrectly.

**Close example:** One row is a customer, one column is a feature; `X @ w` generates a score for each customer.

## Core knowledge

- Array has shape, dtype, axis; The code runs but the axis is wrong but the business is still wrong.
- Broadcasting is valid when the size from right to left is equal or one-way is equal to 1.
- Dot product creates weighted score; matrix multiplication calculates multiple samples simultaneously.
- Float requires tolerance; Pay attention to division by 0, overflow exp/log and the intermediate array is too large.

## Keywords for this week

**New or focus terms:** `feature`, `label / target`, `parameter`, `vectorization`

**Review:** `dataset`, `sample`, `schema`

**Use:** Represent each `sample` as a `feature` vector while keeping the `label / target` separate; use `vectorization` to compute outputs from learned `parameter` values, then record the array `dataset` and `schema`.

## Concept walkthrough

### Inputs and outcomes

**Mental model:** `feature`: Input information the model uses to make a prediction. A feature must be available both during training and when a new prediction is requested. `label / target`: The outcome to predict, used to train or evaluate a model. During supervised learning, each training sample pairs its features with this known answer.

**Why it matters:** The model can only learn from inputs that are clearly separated from the outcome it must predict.

**Worked example:** `feature`: Tenure and monthly_charges are two features in the churn problem. `label / target`: Churn=1 is the label for a customer who left.

**Easy to confuse:** A feature is an input; the label or target is the answer to predict. A label is observed truth; a prediction is the model's estimated answer.

**Check yourself:** For churn prediction, which columns are `feature` inputs and which field is the `label / target`?

### Learned parameters and vectorized computation

**Mental model:** `parameter`: A value the model learns from data during training. Parameters include weights and biases that change as training reduces loss. `vectorization`: Computing on a whole array instead of looping through elements in Python. Array operations let optimized numerical libraries process many values together.

**Why it matters:** Parameters store what training learns; vectorization applies that learned computation consistently across many samples.

**Worked example:** `parameter`: The weights in the linear-regression vector w are parameters. `vectorization`: Use X @ w to calculate scores for every sample.

**Easy to confuse:** A parameter is learned during fit; a hyperparameter is chosen before or around fit. Vectorization changes how computation is expressed, not the mathematical objective.

**Check yourself:** What does training learn as a `parameter`, and what work does `vectorization` perform?

## Connect earlier terms

The earlier `dataset`, `sample`, and `schema` now become a numerical representation: every sample maps to a feature vector with a known shape. The saved array shape and vectorized output show whether that representation is consistent.

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


1. Write weighted score using loop and X @ w; compare np.allclose.
2. Calculate error count table and precision/recall using NumPy.
3. Print the shape step by step, intentionally causing a broadcasting error and then fix it.

## Lab

**lab-01:** NumPy vectorization and quality measure from scratch. Main environment: `local`.

## Signs that you understand

You predict the shape before running the code and explain why loop and matrix multiplication give the same result.

## Test yourself

1. Shape X, w, X @ w with n samples/d features?
2. How is Broadcasting different from copying data?
3. Why use np.allclose?

## Result oriented

tested NumPy module; Saves the executed command, configuration, quality measure, run time and one limitation.

## Core vs stretch

- **Core:** Complete loop/vectorized calculations, calculate a row and check shape/boundary.
- **Expansion:** Try an array with zero variance or wrong shape; Predict errors before running.

## Common errors

- Reshape to let the code run without understanding the axis.
- Vectorize using an intermediate array runs out of RAM.

## When you get stuck

Print `shape`, `dtype` after each step. Reduce the array by 2-3 rows and then calculate it by hand before editing `reshape`.

## Source

Recommended source: NumPy documentation on broadcasting, `matmul` and floating-point comparison in `docs/sources.yml`.