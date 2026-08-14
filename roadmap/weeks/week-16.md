# Week 16 - Docker, CI and artifact versioning

## Weekly goals

Packaging, CI, version artifact; understand image trade-off.

## Why this week matters

Docker encapsulates the runtime; CI checks the rules every time the code changes. Both help the model run consistently but do not replace data quality checks.

**Close example:** Image with correct checksum may still contain wrong model; manifest and test answer two different questions.

## Core knowledge

- Container closes runtime/dependency, does not guarantee correct model; Use a small base, non-root user.
- Place dependency layer before source, remove data/artifact/.venv from build context.
- CI runs lint/type/test/validators offline; roadmap does not auto-deploy AWS.
- Artifact manifest has schema/version/checksum/config/metrics; checksum does not replace provenance.
- Production monitoring needs both service signals (latency/error) and ML signals (schema, drift, prediction distribution); drift is an investigative warning, not self-proving that the model is wrong.

## Keywords for this week

**New or focus terms:** `container`, `CI`

**Review:** `API contract`, `artifact`, `reproducibility`, `latency`

**Use:** Package the service and its `API contract` in a `container`; use `CI` to run data validation, parity, and artifact tests, measure `latency`, then remove the container while retaining reproducibility evidence.

## Concept walkthrough

### Environment in a container

**Mental model:** `container`: A container bundles an application with its dependencies and runtime configuration in an isolated environment. Its image should contain only what the service needs and should run as a non-root user.

**Why it matters:** A container fixes the runtime boundary, but it still needs a small image, a non-root user, and an explicit health check.

**Worked example:** `container`: A Docker image runs the API as a non-root user.

**Easy to confuse:** A container is a runnable package, not a full virtual machine.

**Check yourself:** What runtime assumptions does the `container` fix, and which risks remain outside it?

### CI as repeatable judgment

**Mental model:** `CI`: Continuous integration (CI) automatically runs checks and tests when code changes. Typical CI checks include tests, linting, and type checking, but not an automatic production deployment.

**Why it matters:** CI reruns agreed checks from a clean state so a build is judged by evidence rather than by one developer's machine.

**Worked example:** `CI`: A CI pipeline runs pytest, Ruff, and mypy without deploying to AWS.

**Easy to confuse:** CI validates changes; deployment releases them to an environment.

**Check yourself:** Which clean-state checks must `CI` repeat before accepting a change?

## Connect earlier terms

The existing `API contract`, `artifact`, `reproducibility`, and `latency` expectations now run inside a clean container. CI output and a fresh container test prove that the result is not tied to one workstation.

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


1. Build image, smoke health/predict, non-root check.
2. Run CI commands from clean checkout.
3. Change an artifact byte and confirm checksum failure.

## Lab

**lab-15:** Docker/local CI smoke. Main environment: `local`.

## Signs that you understand

You build a non-root image, smoke `/health` and `/predict`, then detect the altered artifact using checksum.

## Test yourself

1. What are the risks of latest tag?
2. Why does the image/model need a separate version?
3. What does Checksum prove?

## Result oriented

competency milestone 4; Saves executed commands, configuration, metrics, runtime and one limitation.

## Core vs stretch

- **Core:** Build non-root image, smoke service, check checksum and run CI offline.
- **Expand:** Measure image size/startup time or try artifact checksum failure; Do not add auto-deploy cloud.

## Common errors

- Put secret/data into image.
- CI self-deploys to cloud.

## When you get stuck

If Docker takes time, run local tests first. Check `.dockerignore`, build context and container log in order.

## Source

Recommended resources: Dockerfile best practices, non-root containers and GitHub Actions documentation.