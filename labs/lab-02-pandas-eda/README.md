# Lab 02 - Profile data quality before plotting

## Goal

Good EDA begins with 'Can I trust each row?', not 'Which chart looks best?'. Create an inventory that is detailed enough to decide what the data needs before modeling.

## Terms used in this lab

**New terms:** `data validation`, `EDA`, `missing value`, `outlier`

**Review:** `dataset`, `sample`, `feature`, `label / target`

**Use in this lab:** Run `data validation` on the `dataset`: check its schema, each `missing value`, and each `outlier`. Use `EDA` to describe each `feature`, the `label / target`, and the `sample` count.

**Explain it yourself:** How is data validation different from EDA? Why is an outlier not always an error?

## Before you start

Read `roadmap/weeks/week-03.md`, work from the repository root, and prepare a local place for evidence. Do not put credentials, personal data, or large result files in Git.

## Steps

1. Create a table of schema, missing values, duplicates, ranges, and target distribution.
2. Choose one business key. Check duplicate rows and describe the impact of keeping them.
3. Compare the overall churn rate with at least one group. Separate observations from explanations.
4. Write three notes in this form: evidence - hypothesis - next check.

## Run the smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 2
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 2
```

The result is saved to `.artifacts/lab-02-evidence.json`. In `result`, you will see the missing count, duplicate count, churn rate, and mean by target.
`status=starter-example-completed` only confirms that the example code ran. It does **not** mean that you met all acceptance criteria.

## When you are done

- The report includes missing count, duplicate count, target rate, and one group comparison.
- You do not remove an outlier or missing value just because of a chart. Every cleaning decision has a reason and an expected impact.

## When you get stuck

Return to five questions: What is one row? What is the key? What is the target? Which values are impossible? When was the data recorded?

Predict the output first, then compare it with [`expected/README.md`](expected/README.md) and record what you learned locally. No submission is required.
