# Week 03 - pandas, cleaning and EDA

## Weekly goals

Data cleaning; Distinguish between observed and inferred.

## Why this week matters

EDA is not a drawing contest. This is when you find out if the data is reliable for the model to learn from.

**Close example:** A negative age column or duplicate customer ID can make the quality measure look fake, even though the chart looks completely normal.

## Core knowledge

- EDA starts with schema, row/key, target distribution, missing, duplicate and range; the chart behind the quality table.
- Missing can carry information; Do not drop/impute before understanding the mechanism.
- Observation from sample does not prove causal explanation.
- Statistics that go into data operations must be learned after split and only on train.

## Keywords for this week

**New or focus terms:** `data validation`, `EDA`, `missing value`, `outlier`

**Review:** `dataset`, `sample`, `feature`, `label / target`

**Use:** Run `data validation` on the `dataset` against its `schema`, including `missing value` and `outlier` checks; use `EDA` to describe each `feature` and `label / target` at sample level.

## Concept walkthrough

### Trust before modeling

**Mental model:** `data validation`: Checking that data follows the schema and quality rules before use. Checks can reject or report invalid rows before those rows enter the workflow. `EDA`: Exploring data with statistics and plots to understand quality, distributions, and follow-up questions. It begins with questions, then uses summaries and plots to investigate them.

**Why it matters:** Data validation enforces known rules, while EDA looks for distributions and patterns that may require new rules.

**Worked example:** `data validation`: Find duplicate IDs, negative ages, or a missing target. `EDA`: Compare the overall churn rate with the rate for each contract group.

**Easy to confuse:** Data validation enforces known rules; EDA searches for patterns and new questions. EDA explores and forms hypotheses; model validation evaluates model choices.

**Check yourself:** Which checks belong to `data validation`, and which questions require `EDA`?

### Missingness and unusual values

**Mental model:** `missing value`: A value that is absent or not recorded in the dataset. It may be represented by null, NaN, or another agreed marker, depending on the schema. `outlier`: An observation far from most of the data; investigate it before deleting or changing it. Its cause should be checked with domain knowledge before it is removed or capped.

**Why it matters:** Missing values and outliers can be errors or real signal, so investigate their mechanism before changing them.

**Worked example:** `missing value`: Some samples have no monthly_charges value. `outlier`: An unusually high bill may be an error or a real business customer.

**Easy to confuse:** A missing value is absent; zero can be a valid recorded value. An outlier is unusual, not automatically incorrect.

**Check yourself:** How would you decide whether a `missing value` or `outlier` is an error or useful signal?

## Connect earlier terms

A `dataset` is trustworthy only when each `sample`, `feature`, and `label / target` passes explicit quality checks. Validation results and EDA summaries now provide that evidence instead of relying on row counts alone.

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


1. Create a data-quality table by column.
2. Check duplicates by business key.
3. Write three insights in the form of evidence -> hypothesis -> next check.

## Lab

**lab-02:** EDA has a data-quality table and three insights. Main environment: `local`.

## Signs that you understand

You distinguish observations from hypotheses that need further testing and do not use testing to design data operations.

## Test yourself

1. When can the inferred Dtype be wrong in business?
2. How does overall missingness cover subgroups?
3. How does EDA cause target leakage?

## Result oriented

EDA notebook/report; Saves the executed command, configuration, quality measure, run time and one limitation.

## Core vs stretch

- **Core:** Create data-quality table and three notes evidence - hypothesis - next check.
- **Expand:** Examine another subgroup or duplicate rule; Do not use testing to design cleaning.

## Common errors

- Remove outlier just because of boxplot.
- Look at tests to design data operations.

## When you get stuck

Start with the schema, missing, duplicate and range tables. Only draw a graph after knowing what each row represents.

## Source

Recommended source: pandas documentation on missing data, duplicates and dtypes in `docs/sources.yml`.