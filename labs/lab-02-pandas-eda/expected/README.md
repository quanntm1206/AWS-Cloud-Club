# Reference result - lab-02-pandas-eda

## Oracle

Write three findings in this form: observation - hypothesis - next check.

## Required receipt

- Run `python scripts/run_lab.py --lab 2` from the repository root. The full PowerShell and Bash commands are in the lab README.
- The JSON must contain `status=starter-example-completed`; in `result`, look for the missing count, duplicate count, churn rate, and mean by target.
- Keep a local learning log with the seed or config, runtime, the lab-specific check, and at least one limitation or failure.
- Answer in your own words: "What does this output prove, and what does it not prove?"

## Terminology oracle

**Expected reasoning:** Data validation checks whether the table follows known rules. EDA then uses the checked summaries to form hypotheses, not to claim causes.

**Evidence mapping:** The schema and duplicate checks describe dataset integrity. Missing counts and ranges show possible quality issues, while the churn rate and group summaries support the three evidence-hypothesis-next-check notes.

**Misconception check:** A missing value or outlier is not automatically bad data. The starter status only confirms that the sample report was generated.

## If your result differs

If a dtype is misleading, check its business meaning instead of trusting pandas inference.

This is a self-check, not an assignment to submit. Keep evidence local. Do not commit secrets, personal data, large raw datasets, or paid cloud output.
