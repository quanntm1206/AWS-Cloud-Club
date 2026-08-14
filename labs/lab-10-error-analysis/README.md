# Lab 10 - Turn model errors into the next task

## Goal

Error analysis is not a collection of interesting mistakes. Sample by a written rule, then turn the errors into hypotheses with clear next actions.

## Terms used in this lab

**New terms:** `error analysis`, `slice`, `failure taxonomy`, `support`

**Review:** `metric`, `validation set`, `feature engineering`

**Use in this lab:** Run `error analysis` for each `slice` and always record support. Build a `failure taxonomy` from wrong predictions, then connect it to feature engineering and the metric on the validation set.

**Explain it yourself:** How do slice, support, and a failure taxonomy prevent subjective error analysis?


## Apply the concepts

### Slice evidence

**Terms:** `slice`, `support`, `metric`, `validation set`

**What they mean here:** A `slice` is a rule-defined validation subset; `support` gives the denominator for every slice `metric`.

**Where you will see them:** FP, FN, metric, and support appear together for at least two groups.

**Common mistake:** Treating a perfect tiny slice as stronger than a large, slightly weaker one.

**Evidence to keep:** Keep slice rule, support, FP/FN, metric, and sampling rule.

**Explain after the lab:** Compare slices using rate and support, then limit the conclusion.

### Failures into tests

**Terms:** `error analysis`, `failure taxonomy`, `feature engineering`

**What they mean here:** `error analysis` reviews mistakes selected by a written rule. A `failure taxonomy` groups the observed causes so you can test the next data or `feature engineering` change.

**Where you will see them:** The capped failure records receive evidence-based categories, followed by one data experiment and one model experiment.

**Common mistake:** Browsing memorable mistakes and calling anecdotes a taxonomy.

**Evidence to keep:** Keep IDs, safe descriptions, categories, and rejection tests.

**Explain after the lab:** Trace one record from the observed evidence to its category and proposed change, then describe a result that would disprove your hypothesis.

## Before you start

Read `roadmap/weeks/week-11.md`, work from the repository root, and prepare a local place for evidence. Do not put credentials, personal data, or large result files in Git.

## Steps

1. Calculate FP and FN for at least two slices. Always record support.
2. Select no more than 20 failure records using a written sampling rule.
3. Assign a taxonomy: data, boundary, missing signal, label noise, or shift.
4. Propose one data fix and one model fix. Give a test that could reject each hypothesis.

## Run the smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 10
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 10
```

The result is saved to `.artifacts/lab-10-evidence.json`. In `result`, you will see slice metrics, capped failure records, and a taxonomy.
`status=starter-example-completed` only confirms that the example code ran. It does **not** mean that you met all acceptance criteria.

## When you are done

- The output includes slice metrics, a failure cap, records, and a taxonomy. Sampling is rule-based, not subjective.
- You do not call feature importance causality or draw a fairness conclusion from a very small group.

## When you get stuck

If no pattern appears, change the sampling rule to cover more groups and confidence levels. Describe the observation before explaining its cause.

Predict the output first, then compare it with [`expected/README.md`](expected/README.md) and record what you learned locally. No submission is required.
