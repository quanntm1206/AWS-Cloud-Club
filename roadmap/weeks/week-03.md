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

**Use:** Run `data validation` on `dataset`: check `schema`, `missing value`, `outlier`; Use EDA to describe features and labels/targets at the sample level.

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