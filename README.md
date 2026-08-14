# Machine Learning Engineer Roadmap - AWS Cloud Club

If you can already write code but Machine Learning still feels like a black box, this roadmap will help you
understand it step by step. Over 24 weeks, you will move from reading data and training your first model to
building a small ML system that can be tested, packaged, and run safely. Plan for 8-10 study hours per week.
You do not need a GPU or an AWS account to get started.

## After 24 weeks, what can you do?

- Convert a real-life question into an ML problem with clear data, labels, baseline and metrics.
- Build a tabular pipeline that prevents data leakage and evaluate models with evidence, not one attractive score.
- Turn notebook code into a package, write tests, build an inference API, create a Docker image, and manage artifacts.
- Train a small image model using transfer learning on Colab Free or Kaggle Free.
- Deploy tabular capstone using private Lambda and then clean up AWS resources in the same session.

This roadmap builds a foundation for the ML Engineer path. It does not claim that 24 weeks can replace experience
with real products. The main skill you will gain is the ability to question, verify, and explain your decisions.

## Six stage map

| Week | Stage | You will do it |
|---|---|---|
| [01-04](roadmap/weeks/week-01.md) | Data and Math Foundations | Understand workflow, NumPy, EDA and gradients intuitively |
| [05-08](roadmap/weeks/week-05.md) | Classic ML and Review | Build baseline, prevent leakage, choose metrics and check stability |
| [09-12](roadmap/weeks/week-09.md) | Applied ML | Compare models, design features, analyze errors, complete mini-project |
| [13-16](roadmap/weeks/week-13.md) | ML Engineering | Package code, test it, build an API and Docker image, use CI, and version artifacts |
| [17-20](roadmap/weeks/week-17.md) | Deep Learning and CV | PyTorch, transfer learning, checkpoints and failure analysis |
| [21-24](roadmap/weeks/week-21.md) | AWS secure capstone | S3, private Lambda, cleanup, cost audit and demo |

## How to use repo

GitHub only hosts the course template. Clone it to your own computer:

```text
git clone https://github.com/quanntm1206/AWS-Cloud-Club.git
```

If you do not use Git, download the source archive from `https://github.com/quanntm1206/AWS-Cloud-Club` and extract
it locally. Learners do not need to fork, commit, push, open a pull request, or submit work. Keep your learning log,
lab results, and artifacts on your own computer for self-review; you do not need a public repository.

Set up the environment and then run the boot test:

```powershell
pwsh scripts/setup.ps1 -Profile core
pwsh scripts/check.ps1 -Scope bootstrap
```

```bash
bash scripts/setup.sh --profile core
bash scripts/check.sh --scope bootstrap
```

Read the [getting started guide](roadmap/00-getting-started.md), then open week 01. Each week points to the relevant lab.
After week 24, use the [90-day map](roadmap/sau-24-tuan.md) to choose Model Engineering, ML Platform/MLOps,
or Applied Computer Vision.

## Learn terms without memorizing them by rote

Each lab introduces a small group of terms, brings back terms from earlier labs, and asks you to connect them to
real code, metrics, and outputs. For example, you meet `dataset` in lab 00, reuse it while creating a `data split`
in lab 04, then check for `data leakage` in lab 05. The concept sections ask you to explain each idea in your own
words. Use the [full glossary](roadmap/glossary.md) when you need it; do not try to memorize it in one sitting.
The glossary also separates terms that sound similar:

- `data validation`: checks whether data follows the expected schema and rules;
- `validation set`: the part of the data used to choose settings, not to fit model parameters;
- `model validation`: the wider process of testing whether a model works on data it did not fit.

## Principle of keeping costs low

- Local CPU is the default route; Colab Free or Kaggle Free is only used for the CV section.
- AWS is limited to artifacts, IAM, Lambda, and system observability; it is not used for GPU or heavy training.
- Tabular capstone is the core part; The CV capstone is a fully guided extension.
- Every AWS lab comes complete: pre-check, estimate, dry-run, deploy, verify, cleanup, residual scan, cost audit.
- AWS Budgets only sends alerts, does not block spending. Pricing and eligibility are subject to change.

## What's in the repo?

- [`roadmap/`](roadmap/): 24 weeks, six competency milestones, learning log and self-assessment.
- [`labs/`](labs/): 21 labs, including startup lab 00, lab 01-19 offline/free compute and lab 20 for AWS.
- [`notebooks/`](notebooks/): real notebook running on Colab/Kaggle with fallback CPU.
- `src/ml_roadmap/`: sample code for training, evaluation and inference.
- [`capstones/`](capstones/): capstone churn tabular and image classification.
- `aws/`: cost policy, CloudFormation and preflight/deploy/cleanup scripts.
- `dist/`: complete Word document.

## If slow or stuck

Do not buy more compute to fix an error you do not understand. Return to `cpu-mini`, read the first error message,
then check the shape, dtype, data split, and command. Record each attempt in the learning log. If a week takes longer
than planned, complete the core work and skip `Stretch`; the roadmap does not require every optional task.

## License

MIT. Third-party datasets and models may use different licenses; check each lab and capstone before use.
