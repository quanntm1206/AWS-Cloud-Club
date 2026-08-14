# Lab 05 - Build preprocessing that cannot see the test set

## Goal

Imputers, scalers, and encoders all learn from data. Keep them in one pipeline so the test set cannot quietly take part in training.

## Terms used in this lab

**New terms:** `data leakage`, `pipeline`, `preprocessing`, `transform`

**Review:** `data split`, `fit`, `training set`, `validation set`, `test set`

**Use in this lab:** Make the `data split` first. Fit every `preprocessing` and `transform` step only on the `training set`, then join them in a `pipeline`. Use the `validation set` and `test set` to show that no `data leakage` reaches either set.

**Explain it yourself:** Why must preprocessing transforms be fit after the data split and only on the training set?


## Apply the concepts

### Learning boundary

**Terms:** `data split`, `fit`, `training set`, `validation set`, `test set`, `data leakage`

**What they mean here:** Every preprocessing value and model parameter must be learned by calling `fit` on the `training set` only. If validation or test data influences those values, you have `data leakage`.

**Where you will see them:** The split precedes every fitted transformer, whose statistics trace to training rows only.

**Common mistake:** Fitting label-free preprocessing on the full table; feature distributions still leak.

**Evidence to keep:** Keep the split sizes and the learned imputer and scaler values beside the training-only calculation that produced them.

**Explain after the lab:** Name every operation that learns state and show where its fit input stops.

### One transform path

**Terms:** `pipeline`, `preprocessing`, `transform`

**What they mean here:** The `pipeline` puts each `preprocessing` operation and the model in one ordered path. The `transform` step applies rules that were already learned, without fitting them again.

**Where you will see them:** The `ColumnTransformer`, unknown validation category, prediction, and `leakage_guard=true` exercise one path.

**Common mistake:** Calling `fit_transform` on validation data to make an unknown category pass.

**Evidence to keep:** Keep pipeline steps, unknown-category prediction, and the guard field.

**Explain after the lab:** Trace the validation row through the pipeline and name the unchanged state.

## Before you start

Read `roadmap/weeks/week-06.md`, work from the repository root, and prepare a local place for evidence. Do not put credentials, personal data, or large result files in Git.

## Steps

1. Identify numeric and categorical columns, then split the data before preprocessing.
2. Build a `ColumnTransformer` for missing values, scaling, and one-hot encoding.
3. Add a validation row with a category that was not seen during training. Predict on it without fitting again.
4. Confirm that scaler and imputer statistics come only from the training set.

## Run the smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 5
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 5
```

The result is saved to `.artifacts/lab-05-evidence.json`. In `result`, you will see a prediction for the unknown category and `leakage_guard=true`.
`status=starter-example-completed` only confirms that the example code ran. It does **not** mean that you met all acceptance criteria.

## When you are done

- The unknown category is handled, and `leakage_guard=true`.
- The pipeline stores both transforms and the model. No `fit` step uses validation or test data.

## When you get stuck

If the encoder fails, check `handle_unknown`. If the metric looks unusually strong, find every `fit` and `fit_transform` call and inspect its input.

Predict the output first, then compare it with [`expected/README.md`](expected/README.md) and record what you learned locally. No submission is required.
