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

**Use:** Open smoke `dataset`, count each `sample`, compare `schema`, fix `seed` then run twice to check `reproducibility`.

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