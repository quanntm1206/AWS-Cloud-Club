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

**Use:** Pack the package/API contract into `container`, use `CI` to run data validation, parity and test artifact; Measure low latency and then cleanup the container to maintain reproducibility.

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