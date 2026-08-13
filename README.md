# Machine Learning Engineer Roadmap - AWS Cloud Club

If you've written code but Machine Learning still feels like a black box, this roadmap will help you open it
each class. In 24 weeks, you go from reading data and training your first model to having a small ML system
can be tested, packaged, and run safely. Expected study schedule is 8-10 hours per week; No GPU or AWS needed to get started.

## After 24 weeks, what can you do?

- Convert a real-life question into an ML problem with clear data, labels, baseline and metrics.
- Build a tabular pipeline to avoid data leakage; Evaluate the model by evidence instead of a pretty number.
- Split notebooks into packages, write tests, build inference API, package Docker and manage artifacts.
- Train a small image model using transfer learning on Colab Free or Kaggle Free.
- Deploy tabular capstone using private Lambda and then clean up AWS resources in the same session.

This is the foundation for moving forward in the ML Engineer direction, not a promise that 24 weeks will replace experience
Make real products. The most important thing you take away is the ability to question, verify, and explain your decisions.

## Six stage map

| Week | Stage | You will do it |
|---|---|---|
| [01-04](roadmap/weeks/week-01.md) | Data and Math Foundations | Understand workflow, NumPy, EDA and gradients intuitively |
| [05-08](roadmap/weeks/week-05.md) | Classic ML and Review | Build baseline, prevent leakage, choose metrics and check stability |
| [09-12](roadmap/weeks/week-09.md) | Applied ML | Compare models, design features, analyze errors, complete mini-project |
| [13-16](roadmap/weeks/week-13.md) | ML Engineering | Package, test, API, Docker, CI and version artifact |
| [17-20](roadmap/weeks/week-17.md) | Deep Learning and CV | PyTorch, transfer learning, checkpoints and failure analysis |
| [21-24](roadmap/weeks/week-21.md) | AWS secure capstone | S3, private Lambda, cleanup, cost audit and demo |

## How to use repo

GitHub is just where the repo master releases the framework. Clone sample repo:

```text
git clone https://github.com/quanntm1206/AWS-Cloud-Club.git
```

If not using Git, download the source archive from `https://github.com/quanntm1206/AWS-Cloud-Club` and extract it
local. Learners do not fork, commit, push, open pull requests, or submit assignments. Learning log, lab results and
The artifact is saved locally for you to review for yourself; no need for public repository.

Set up the environment and then run the boot test:

```powershell
pwsh scripts/setup.ps1 -Profile core
pwsh scripts/check.ps1 -Scope bootstrap
```

```bash
bash scripts/setup.sh --profile core
bash scripts/check.sh --scope bootstrap
```

Read the [getting started guide](roadmap/00-getting-started.md), then open week 01. Each week will point you to the correct lab.
After week 24, use [90-day map](roadmap/sau-24-tuan.md) to choose the direction Model Engineering, ML Platform/MLOps
or Applied Computer Vision.

## Learn terms without memorizing them by rote

Each lab introduces a new group of words, recalls words used in the previous lab and asks you to apply them
real operations and output. For example, you encounter `dataset` in lab 00, use it again when creating `data split` in lab 04, and then continue
Continue checking `data leakage` in lab 05. The `Self-explanation` section helps you repeat it in your own words; glossary at the end of the document
This is a place to look up, not a list that needs to be memorized right away. Three easily confused clusters are clearly separated:

- `data validation`: check whether the data has the correct schema/rules or not;
- `validation set`: the data part is used for decision selection, not fit parameter;
- `model validation`: the process of evaluating the model on data that has not yet been used for fitting.

## Principle of keeping costs low

- Local CPU is the default route; Colab Free or Kaggle Free is only used for the CV section.
- AWS for artifacts, IAM, Lambda, and system observability; Does not use GPU or heavy training.
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

Don't buy more compute to fix an error you don't understand. Go back to `cpu-mini`, read the first error message, check the shape,
dtype, data split and command are running. Record what you try in the learning log. If a week lasts longer than expected
ant, complete the core then skip `Stretch`; The roadmap doesn't require you to run every option.

## License

MIT. Third-party datasets and models hold separate licenses; View each lab and capstone before use.
