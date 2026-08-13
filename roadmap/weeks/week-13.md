# Week 13 - Notebook to Python package

## Weekly goals

Separate notebook into module, config and CLI.

## Why this week matters

Notebooks help with quick discovery; package helps logic have clear inputs, is reusable and easy to test. ML Engineers need to know how to move from the former to the latter.

**Close example:** Cell runs correctly thanks to variables while in memory it will fail when opening a new notebook; CLI forces dependencies to be visible.

## Core knowledge

- Notebook to explore; production path is the module with explicit input/output and CLI.
- Split data, feature, train, evaluate, artifact I/O; notebook just calls package.
- Config has schema; The CLI returns a useful exit code and error message.
- Place file/network side effects at the boundary, keeping core functions easy to test.

## Keywords for this week

**New or focus terms:** `package`, `configuration`

**Review:** `reproducibility`, `pipeline`, `artifact`

**Use:** Split pipeline into `package`; put seed and hyperparameter in `configuration`, rerun to keep reproducibility, artifact and inference independent of notebook state.

## 8-10 hour schedule

| Activities | Hours |
|---|---:|
| Read and take notes | 2 |
| Guided practice | 2 |
| Lab | 3 |
| Assessment/error analysis | 1 |
| Learning log and self-assessment | 1 |
| Review/complete | 0 |

## Guided practice


1. Move train logic into src but keep output agreement.
2. Add CLI to receive config/output/seed.
3. Run the same config twice, so manifest and metric tolerance.

## Lab

**lab-12:** Notebook-to-package refactor. Main environment: `local`.

## Signs that you understand

You run the same logic from CLI and notebook, don't copy two versions, and have config instead of global state.

## Test yourself

1. What logic is in the notebook/package?
2. How do Globals destroy reproducibility?
3. What does CLI contract include?

## Result oriented

installable package; Saves executed commands, configuration, metrics, runtime and one limitation.

## Core vs stretch

- **Core:** Keep a source of training logic in the package; notebook and CLI give equivalent results.
- **Extension:** Add a useful validation config or error message for incorrect input.

## Common errors

- Copying logic in two places causes drift.
- Hide input in working directory.

## When you get stuck

Restart the kernel or open a clean shell. If only the old notebook is running, trace the hidden variable and dependency path to the working directory.

## Source

Recommended source reading: Python packaging/argparse and project structure references listed in `docs/sources.yml`.