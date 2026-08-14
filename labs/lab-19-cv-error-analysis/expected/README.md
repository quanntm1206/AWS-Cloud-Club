# Reference result - lab-19-cv-error-analysis

## Oracle

Use real notebook output to create the confusion matrix, review no more than 20 errors, and record a limitation.

## Required receipt

- Run `python scripts/run_lab.py --lab 19` from the repository root. The full PowerShell and Bash commands are in the lab README.
- The JSON must contain `status=starter-example-completed`; in `result`, look for per-class metrics and failure records.
- Keep a local learning log with the seed or config, runtime, the lab-specific check, and at least one limitation or failure.
- Answer in your own words: "What does this output prove, and what does it not prove?"

## Terminology oracle

**Expected reasoning:** Per-class metrics need support and confusion-matrix context. The failure taxonomy must come from real validation images that were actually reviewed.

**Evidence mapping:** The class table and raw and normalized matrices explain the macro and weighted averages. The confident-wrong record IDs, reviewed categories, and next experiment provide the error-analysis evidence.

**Misconception check:** FakeData or records still marked `unreviewed` do not complete model validation. A weighted average can also hide weak performance on a smaller class.

## If your result differs

If there are few errors, use all of them. For sensitive images, store only an ID and a safe description.

This is a self-check, not an assignment to submit. Keep evidence local. Do not commit secrets, personal data, large raw datasets, or paid cloud output.
