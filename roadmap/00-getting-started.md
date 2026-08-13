# Start roadmap

You don't need to prepare a powerful machine. If you're familiar with variables, functions, loops, and data structures, you have it
enough background to get started. Math will be learned right when it appears in the lesson, instead of becoming a door to overcome
pass first.

## Before the first class

- Python 3.11-3.13; The device has at least 8 GB of RAM. The CPU is enough for the core learning curve.
- Know how to run commands in the terminal and read a basic Python error. Git only needs to be at the clone level.
- No need for an AWS, Colab or Kaggle account before week 17.

GitHub is only used to clone/download sample repos released by the repo owner. Learners do not fork, do not commit/push,
do not create PR and do not submit work.

```text
git clone https://github.com/quanntm1206/AWS-Cloud-Club.git
cd AWS-Cloud-Club
```

Choose the correct command for the operating system:

```powershell
pwsh scripts/setup.ps1 -Profile core
pwsh scripts/check.ps1 -Scope bootstrap
.venv\Scripts\python.exe scripts/run_lab.py --lab 0
```

```bash
bash scripts/setup.sh --profile core
bash scripts/check.sh --scope bootstrap
.venv/bin/python scripts/run_lab.py --lab 0
```

If the last command prints the path `.artifacts/lab-00-evidence.json`, the sample environment is already running. This is just a smoke demo;
You still need to read [lab 00](../labs/lab-00-environment-and-reproducibility/README.md) to understand and check the results yourself.

## Suggested learning rhythm

- 2 hours of reading and explaining in your own words.
- 2 hours of guided practice.
- 3-4 hours of lab work and error observation.
- 1 hour self-test; 1 hour of learning log recording or completion.

The `Stretch` section does not count towards 8-10 hours. Busy for a week? Keep core readings, run mini profile and record one
what is understood; Move the extension to next week.

## Four habits you should keep

1. Run baseline before complex models; If the baseline is not clear, a complex model will only make errors harder to see.
2. Split the data before any transformation that learns the state from the data.
3. Record config, seed, metrics, runtime and even unexpected results.
4. With AWS, only mark done after cleanup and residual scan. Do not purchase Colab/Kaggle or AWS Paid upgrades
   Plan is just to complete the required part.

## How to learn terminology

There is no need to recite the glossary before week 01. In each lab, follow the four lines `New Terminology`, `Review`,
`Lab Applicable`, `Self-explanatory`. When recording your learning log, choose at least one new word and one review word and connect them
with the command, metric or error you just observed. If you just copy the definition without indicating where it appears in the text
lab, let's see if that concept is not really solid.

## What will you save?

Create a convenient local folder for learning logs, notes, charts, and artifacts. Each week keep:

- command was run and environment;
- most important metric or test;
- an error encountered, the cause and how to fix it;
- one thing is still uncertain;
- Decide whether to keep or change in the next run.

Use [`learning-log-template.md`](learning-log-template.md) if you don't know where to start recording. Do not send these
Who is this file for? they are journals that help you see yourself progress.

## When the command does not run

1. Confirm you are at the root repository and the virtual environment has been created.
2. Read the error first, not just the last line; Check Python version and dependencies.
3. Run `scripts/check` again with the scope `bootstrap`.
4. If the error is due to GPU, internet or quota, return to local/`cpu-mini`; no need to pay fees.
5. If you can't solve the problem, write down the commands, errors, and things you tried in the learning log before asking for help.

Now open [Week 01](weeks/week-01.md). No need to read 24 weeks in advance.

When completing week 24, open [`sau-24-tuan.md`](sau-24-tuan.md) to choose a direction to deepen for the next 90 days.
