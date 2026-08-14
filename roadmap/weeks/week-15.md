# Week 15 - Inference API and contracts

## Weekly goals

Design inference contract and error boundary.

## Why this week matters

Inference API is the boundary between model and product. Good contracts help client errors, artifact errors, and operational limitations be handled differently.

**Close example:** Payload is missing a column so returns 422; Model not loaded is a 503 service error, not a caller error.

## Core knowledge

- Inference contract locks request/response schema, model version, threshold, error codes and limits.
- Validation error, client returns 4xx; artifact/service failure pays 5xx, internal details point to safe log.
- Health/readiness does not train; predict uses the correct preprocessing artifact and does not recognize the target.
- Input Group/payload/timeout limits are guardrail; do not log raw sensitive features.

## Keywords for this week

**New or focus terms:** `API contract`, `latency`

**Review:** `data contract`, `artifact`, `inference`, `schema`

**Use:** Define the `API contract`, measure `latency`, and send valid and invalid samples through `inference`; enforce the `data contract` before loading the `artifact`, and keep raw features out of responses.

## Concept walkthrough

### Requests and responses

**Mental model:** `API contract`: An API contract defines an inference service's inputs, outputs, status codes, and errors. Both client and server rely on the same contract to exchange valid data.

**Why it matters:** An API contract separates caller errors from service failures through stable request, response, and error shapes.

**Worked example:** `API contract`: A payload missing tenure returns 422 instead of 500.

**Easy to confuse:** An API contract describes behavior; a data contract focuses on input data rules.

**Check yourself:** Which request, response, and error cases must the `API contract` keep stable?

### Latency as a distribution

**Mental model:** `latency`: Latency is the elapsed time between receiving a request and returning its response. It should be measured under stated conditions such as warm-up state and batch size.

**Why it matters:** Latency determines whether inference can serve the product deadline; a percentile is more informative than one fast request.

**Worked example:** `latency`: Measure warm latency for a mini-batch of 16 samples.

**Easy to confuse:** Latency measures elapsed time; throughput measures how much work finishes per unit time.

**Check yourself:** Which latency percentile represents the product deadline better than one fast request?

## Connect earlier terms

The `data contract` and `schema` now protect requests before the `artifact` performs `inference`. Stable status codes plus measured latency show that the serving boundary behaves as specified.

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


1. Send valid, missing, wrong-type, unknown-category payload.
2. Check success/422/503 according to contract.
3. Measure warm latency mini input group and record measurement limits.

## Lab

**lab-14:** Local API valid/invalid payload. Main environment: `local`.

## Signs that you understand

You can send the correct/wrong payload, receive the appropriate status and confirm the API using the saved preprocessing.

## Test yourself

1. How is 422 different from 500?
2. Health readiness differs?
3. Why not log raw requests?

## Result oriented

Demo API; Saves executed commands, configuration, metrics, runtime and one limitation.

## Core vs stretch

- **Core:** Check valid/invalid API contract, health/readiness and log do not contain raw features.
- **Expansion:** Measure mini input group latency or add payload limit with explicit testing.

## Common errors

- Reveal the stack trace to the client.
- Self-written API for preprocessing other than training.

## When you get stuck

Call a handler or API with a minimal request. When there is 500, read the server log but do not include the stack trace in the response.

## Source

Recommended source: FastAPI request validation/error handling and HTTP status semantics in the official documentation.