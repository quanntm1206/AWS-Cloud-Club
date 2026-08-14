# Week 01 - ML workflow and reproducible environment

## Weekly goals

Describes a complete ML workflow; create a regenerative environment.

## Why this week matters

A clear workflow helps you know which decision the model serves, instead of starting with the algorithm and then finding the problem.

**Close example:** Imagine a churn model that predicts which customers are likely to leave at the beginning of the month; The care team only takes action after that point.

## Core knowledge

- Separate the business question from the model output task: define objects, labels, model output time and actions after prediction.
- Minimum workflow: validate data, split, simple reference, learn, evaluate, lock decision, test once, analyze errors, package.
- Schema/target key data convention; The experiment contract saves seed, config, code revision, quality measure, runtime and limitation.
- Reproducibility requires regenerating input, procedures, environment and tolerance; does not promise every hardware for bit-identical result.

## Keywords for this week

**New or focus terms:** `dataset`, `sample`, `schema`, `reproducibility`, `seed`

**Review:** None - this is the first lab.

**Use:** Inspect the smoke `dataset`, count its `sample` rows, validate the `schema`, fix the `seed`, then run twice to check `reproducibility`.

## Concept walkthrough

### Rows, collections, and rules

**Mental model:** `dataset`: A collection of samples used for analysis or model training. It usually has rows of samples and columns of features. `sample`: One observation in a dataset, usually one row or one image. Every sample has the same expected structure but different observed values.

**Why it matters:** A dataset gives the project its evidence, while samples define the units counted by splits, predictions, and metrics.

**Worked example:** `dataset`: A churn file has 300 customers, with columns describing each customer. `sample`: One customer is a sample in the churn table.

**Easy to confuse:** A dataset is the whole collection; a sample is one item inside it. A sample is one observation, while a feature is one input value or column describing it.

**Check yourself:** When counting churn evidence, how does a `sample` differ from the `dataset`?

### Schema rules and repeatable runs

**Mental model:** `schema`: A description of input column names, data types, and valid rules. It also states constraints such as required columns, allowed categories, and numeric ranges. `reproducibility`: The ability to rerun the same data, code, and settings and get comparable results. It requires recording data, code, dependencies, configuration, and random controls.

**Why it matters:** A schema detects structural drift; reproducibility shows whether the same procedure still gives comparable evidence.

**Worked example:** `schema`: The tenure column must be non-negative; churn accepts only 0 or 1. `reproducibility`: Two terminals use the same seed and produce the same row count and metric within tolerance.

**Easy to confuse:** A schema describes allowed structure; data validation checks actual data against it. The same seed helps reproducibility, but changed code or packages can still change results.

**Check yourself:** Would a changed column type break the `schema`, `reproducibility`, or both?

### Seed controls randomness

**Mental model:** `seed`: A starting number for random generation so splits or initialization can be repeated. Reusing it starts the same pseudorandom sequence in supported operations.

**Why it matters:** A seed controls one random sequence, so it is useful only when data, code, configuration, and environment are also recorded.

**Worked example:** `seed`: Set seed 42 before creating demo data.

**Easy to confuse:** A seed controls a random sequence, not every source of nondeterminism.

**Check yourself:** What must stay fixed before the same `seed` makes two runs comparable?

## Connect earlier terms

There are no earlier course terms to review in Week 01. The environment report establishes the first evidence by recording the `dataset`, `seed`, and repeated-run result for later comparison.

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


1. Write a problem statement for churn in the form of who-when-for what.
2. Draw data -> split -> learn -> evaluate -> test -> saved model bundle; Mark the leakage point.
3. Run the lab, save the environment report and a limitation.

## Lab

**lab-00:** Set up the environment, run tests, create learning log. Main environment: `local`.

## Signs that you understand

Can you recount the path from the question to the saved model bundle and indicate when the final holdout is opened.

## Test yourself

1. How does a different output model determine the product?
2. Why don't tests use model selection/decision cutoff?
3. What does the minimum experimental log include?

## Result oriented

environment report saved locally; Saves the executed command, configuration, quality measure, run time and one limitation.

## Core vs stretch

- **Core:** Run lab 00, keep the environment report and draw the churn workflow in your own words.
- **Expansion:** If you have time, try changing the seed/input and then explain which part should stay stable.

## Common errors

- Start from the algorithm instead of the question.
- Do not lock model output time so input signal looks into the future.

## When you get stuck

If the concepts are still abstract, take a familiar app and write clearly: predict who, when, and for what purpose.

## Source

Recommended source: `docs/sources.yml` - scikit-learn model persistence section and environment reconstruction documentation.