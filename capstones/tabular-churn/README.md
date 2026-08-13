# Capstone A - churn prediction from start to private Lambda

This capstone brings together the full core path: define the problem, build a baseline, prevent leakage, select
a threshold, package artifacts, then invoke a private Lambda on AWS. Training stays on a local CPU. AWS receives
only the small logistic model.

## What will you produce?

- A churn pipeline with a dummy baseline, preprocessing, and logistic regression.
- `model.joblib`, a portable model, manifest and checksum, metrics, an experiment report, and a model card.
- Local test evidence. If you choose the AWS section, also produce a deployment manifest, cleanup evidence,
  and a residual scan.

## File map

- [`configs/mini.yml`](configs/mini.yml): the quick configuration to run first.
- [`configs/full.yml`](configs/full.yml): a second configuration for a controlled comparison, not a sweep.
- [`reports/experiment-report.md`](reports/experiment-report.md): a template for the question, results, and negative results.
- [`reports/model-card.md`](reports/model-card.md): intended use, metrics, subgroup behaviour, and limitations.
- [`rubric.yml`](rubric.yml): self-assessment criteria.
- [`../../labs/lab-20-aws-safe-lifecycle/README.md`](../../labs/lab-20-aws-safe-lifecycle/README.md): the safe deployment path.

## Stage 1 - run locally first

Create demo data with no personal information:

```powershell
.venv\Scripts\python.exe -c "from pathlib import Path; from ml_roadmap.data import make_demo_churn_data; p=Path('.artifacts/churn.csv'); p.parent.mkdir(exist_ok=True); make_demo_churn_data(300,42).to_csv(p,index=False); print(p)"
.venv\Scripts\python.exe -m ml_roadmap.train_tabular --config capstones/tabular-churn/configs/mini.yml --data .artifacts/churn.csv --output .artifacts/churn-model
```

```bash
.venv/bin/python -c "from pathlib import Path; from ml_roadmap.data import make_demo_churn_data; p=Path('.artifacts/churn.csv'); p.parent.mkdir(exist_ok=True); make_demo_churn_data(300,42).to_csv(p,index=False); print(p)"
.venv/bin/python -m ml_roadmap.train_tabular --config capstones/tabular-churn/configs/mini.yml --data .artifacts/churn.csv --output .artifacts/churn-model
```

Open the metrics and manifest. Confirm that the model beats the dummy baseline on the chosen metric, the
threshold comes from validation, and the artifact can be loaded again. Use the test set only after you lock the
candidate and threshold.

## Stage 2 - report and self-check

1. Complete the experiment report: question, schema and licence, split, baseline, candidate, threshold, test,
   and failure slices.
2. Complete the model card: intended and out-of-scope use, data, metrics, privacy, operational limits, and rollback signals.
3. Run tests and checks from a clean shell. Record the command, environment, and local limitations.
4. Score your work with `rubric.yml`. Required gates: no leakage, no secrets, and reproducible artifacts.

## Stage 3 - optional AWS work, depending on your account

Read all of lab 20 before you begin. The only workflow is a private invoke:
`Pre-check -> Estimate -> Dry-run -> Deploy -> Verify -> Cleanup -> Residual scan -> Cost audit`.
Do not enable a public HTTP API. If the plan, credits, Region, or estimate is unclear, stop at the local
capstone. You still complete the core ML skills. After deployment, clean up in the same session whether
verification succeeds or fails.

## When is the capstone complete?

- The local pipeline runs again from a clean shell, the model beats the baseline, and all model-selection decisions use validation.
- The artifact checksum is valid, and predictions before and after loading match within tolerance.
- The report and model card describe at least one failure, one limitation, and one next experiment.
- If you used AWS: the private invoke handles valid and invalid events, cleanup leaves zero known residuals,
  and you check Billing again after its reporting delay.

## If you get stuck

- **No `.artifacts/churn.csv`:** run the demo-data command first from the repository root.
- **Configuration rejected:** check valid keys in `src/ml_roadmap/config.py`. Do not guess the schema.
- **Metric does not beat the baseline:** check the split, target, leakage, and data signal before changing the model.
- **Artifact does not load:** check the checksum, feature order, dependencies, and output directory.
- **Any AWS step fails:** stop deployment and run cleanup plus the residual scan. Do not fix it by opening more resources.

Store all results locally for self-assessment. Do not publish or submit them to anyone.
