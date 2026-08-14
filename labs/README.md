# Lab catalog

This repository contains **21 labs**. Lab 00 checks the environment. Labs 01-19 run offline or on free compute. Lab 20 is the guarded AWS lifecycle reused in weeks 21-24.

## How to work through a lab

1. Read the matching week to understand why the lab appears here.
2. Run the command in the README to see the **smoke demo** and output shape.
3. Complete the practical task. The central code is a reference example, not a scaffold with blanks to fill.
4. Compare your result with `expected/README.md`. Record the result and one meaningful failure in your local learning log.
5. Mark the lab complete only when you can explain the result, not only when the command exits with code 0.

Each lab also includes a terminology loop: read the new terms, recall earlier terms, then use `Apply the concepts` to connect them to the lab's data, code, metric, and output. Keep the named evidence locally and answer `Explain it yourself` from that evidence. In `expected/README.md`, the terminology oracle shows the expected reasoning, maps it to evidence, and checks one lab-specific misconception; it does not ask you to copy definitions.

`status=starter-example-completed` only means that the demo finished. It does not prove that you met the learning goal. Keep evidence local; no submission is required. GitHub is only a source for cloning or downloading the repository. Do not put secrets, personal data, or large output in Git.

| Lab | Topic | Week |
|---|---|---:|
| [00 - Check the environment and reproducibility](lab-00-environment-and-reproducibility/README.md) | environment and reproducibility | 1 |
| [01 - Read NumPy shapes and check vectorization](lab-01-numpy-vectorization/README.md) | numpy vectorization | 2 |
| [02 - Profile data quality before plotting](lab-02-pandas-eda/README.md) | pandas eda | 3 |
| [03 - Check a linear regression gradient](lab-03-linear-regression-from-scratch/README.md) | linear regression from scratch | 4 |
| [04 - Compare a dummy baseline with logistic regression](lab-04-first-classifier/README.md) | first classifier | 5 |
| [05 - Build preprocessing that cannot see the test set](lab-05-leakage-safe-preprocessing/README.md) | leakage safe preprocessing | 6 |
| [06 - Choose a metric and threshold from error costs](lab-06-metrics-and-threshold/README.md) | metrics and threshold | 7 |
| [07 - Measure stability with cross-validation](lab-07-cross-validation/README.md) | cross validation | 8 |
| [08 - Compare tree ensembles fairly](lab-08-tree-ensemble-comparison/README.md) | tree ensemble comparison | 9 |
| [09 - Test one feature with ablation](lab-09-feature-ablation/README.md) | feature ablation | 10 |
| [10 - Turn model errors into the next task](lab-10-error-analysis/README.md) | error analysis | 11 |
| [11 - Combine the tabular pipeline into a mini-project](lab-11-tabular-mini-project/README.md) | tabular mini project | 12 |
| [12 - Move notebook logic into configuration and a CLI](lab-12-notebook-to-package/README.md) | notebook to package | 13 |
| [13 - Test data, models, and artifacts](lab-13-ml-testing/README.md) | ml testing | 14 |
| [14 - Check the local inference API contract](lab-14-local-inference-api/README.md) | local inference api | 15 |
| [15 - Package the service and run a CI smoke test](lab-15-docker-and-ci/README.md) | docker and ci | 16 |
| [16 - Make tensors, gradients, and devices visible](lab-16-device-aware-mlp/README.md) | device aware mlp | 17 |
| [17 - Run real transfer learning on free compute](lab-17-transfer-learning/README.md) | transfer learning | 18 |
| [18 - Save and resume a complete checkpoint](lab-18-checkpoint-and-resume/README.md) | checkpoint and resume | 19 |
| [19 - Evaluate computer vision by class and failure](lab-19-cv-error-analysis/README.md) | cv error analysis | 20 |

Lab 20: [AWS safe lifecycle](lab-20-aws-safe-lifecycle/README.md).
