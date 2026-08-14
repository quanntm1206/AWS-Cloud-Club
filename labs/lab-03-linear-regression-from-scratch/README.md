# Lab 03 - Check a linear regression gradient

## Goal

Do not trust a gradient only because the loss decreases. Check it with an independent approximation. This debugging habit becomes more important as models grow.

## Terms used in this lab

**New terms:** `prediction`, `loss`, `gradient`, `learning rate`

**Review:** `feature`, `label / target`, `data validation`

**Use in this lab:** Calculate the `prediction`, `loss`, and `gradient`, then update the parameter with the `learning rate`. Keep the `feature` and `label / target` visible, and record any data validation error for invalid input.

**Explain it yourself:** How are loss, gradient, and learning rate connected when a parameter is updated?


## Apply the concepts

### One gradient update

**Terms:** `feature`, `label / target`, `prediction`, `loss`, `gradient`, `learning rate`, `data validation`

**What they mean here:** Features and targets produce a `prediction`. The `loss` summarizes its error, the `gradient` gives the local update direction, and the `learning rate` controls the size of the update. `data validation` rejects invalid shapes or values before this calculation starts.

**Where you will see them:** Follow the arrays for four samples through MSE, the analytic and finite-difference gradients, one parameter update, and the loss history.

**Common mistake:** Reading decreasing loss as proof that the derivative is correct without checking sign and scale.

**Evidence to keep:** Keep one hand calculation, both gradients for several epsilon values, `gradient_check=true`, the loss path, and one intentional validation error.

**Explain after the lab:** Walk from a feature and target to the next parameter value, then state what the gradient check does not prove.

## Before you start

Read `roadmap/weeks/week-04.md`, work from the repository root, and prepare a local place for evidence. Do not put credentials, personal data, or large result files in Git.

## Steps

1. Calculate predictions, MSE, and the analytic gradient for four points by hand.
2. Implement gradient descent. Record the loss at every step with a small learning rate.
3. Calculate central finite differences for several `epsilon` values and compare them with the analytic gradient.
4. Try a learning rate that is too large. Describe the loss path, then restore stable settings.

## Run the smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 3
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 3
```

The result is saved to `.artifacts/lab-03-evidence.json`. In `result`, you will see the analytic gradient, finite-difference gradient, and `gradient_check=true`.
`status=starter-example-completed` only confirms that the example code ran. It does **not** mean that you met all acceptance criteria.

## When you are done

- The analytic and finite-difference gradients are close within tolerance, and `gradient_check=true`.
- You can distinguish slow convergence, divergence, and an incorrect gradient formula.

## When you get stuck

Check the sign, the `2/n` factor, and whether you update the parameter after calculating the gradient. For finite differences, try `epsilon` values at several orders of magnitude.

Predict the output first, then compare it with [`expected/README.md`](expected/README.md) and record what you learned locally. No submission is required.
