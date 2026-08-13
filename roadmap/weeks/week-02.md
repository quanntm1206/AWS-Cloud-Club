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

**Use:** Represent each `sample` into a `feature` vector, keep `label / target` to explain the problem, use vectorization to calculate model output from `parameter`; write `dataset` and `schema` of the array.

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