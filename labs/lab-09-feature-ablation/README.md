# Lab 09 - Test one feature with ablation

## Goal

A new feature should begin with a hypothesis, not a list of transformations. Ablation helps you identify which change really matters.

## Terms used in this lab

**New terms:** `feature engineering`, `ablation`

**Review:** `feature`, `baseline`, `validation set`, `hyperparameter`

**Use in this lab:** Write a `feature engineering` hypothesis and run an `ablation` that adds or removes one feature. Lock the baseline, validation set, hyperparameter, and data split so the metric delta is meaningful.

**Explain it yourself:** How is feature engineering different from ablation? Why should you change only one factor?


## Apply the concepts

### Feature hypothesis

**Terms:** `feature`, `feature engineering`

**What they mean here:** A `feature` is an input available to the model. `feature engineering` proposes a useful representation, explains why it may help, and defines its availability at prediction time and its missing-value handling.

**Where you will see them:** The hypothesis and feature-group code appear before any metric delta.

**Common mistake:** Inventing a hypothesis after one transformation scores well.

**Evidence to keep:** Keep definition, availability, missing rule, and expected effect.

**Explain after the lab:** Explain why signal is available at inference without future information.

### Single change

**Terms:** `ablation`, `baseline`, `validation set`, `hyperparameter`

**What they mean here:** An `ablation` changes one feature group around a fixed `baseline`; validation data, model `hyperparameter`, split, and seed stay constant.

**Where you will see them:** AUC by group, `single_change`, and `test_set_touched=false` record the comparison.

**Common mistake:** Changing model settings alongside features.

**Evidence to keep:** Keep both lists, AUCs, runtime, unchanged settings, and decision.

**Explain after the lab:** Use the controlled score difference and expected variability to justify whether you keep or drop the feature.

## Before you start

Read `roadmap/weeks/week-10.md`, work from the repository root, and prepare a local place for evidence. Do not put credentials, personal data, or large result files in Git.

## Steps

1. Write the feature hypothesis, its availability at prediction time, and its missing or zero handling.
2. Run the baseline feature set. Keep the model, split, and seed fixed.
3. Remove or add exactly one feature group. Record the validation delta and runtime.
4. Decide whether to keep it. Do not open the test set during ablation.

## Run the smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 9
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 9
```

The result is saved to `.artifacts/lab-09-evidence.json`. In `result`, you will see validation AUC by feature group and `test_set_touched=false`.
`status=starter-example-completed` only confirms that the example code ran. It does **not** mean that you met all acceptance criteria.

## When you are done

- The output contains AUC by feature group, `single_change`, and `test_set_touched=false`.
- The feature decision considers availability, stability, and metric variability.

## When you get stuck

If you are unsure whether a feature is valid, write the data timeline. A feature that appears after prediction time must be removed even when correlation is high.

Predict the output first, then compare it with [`expected/README.md`](expected/README.md) and record what you learned locally. No submission is required.
