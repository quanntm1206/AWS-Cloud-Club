# ADR - do not deploy a CV endpoint in the core path

## Context

A CV model is larger than a tabular model, has higher cold-start and memory needs, and an endpoint may create
ongoing costs. Learners need to understand MLOps, but the main constraints are the Free Plan and avoiding
surprise costs.

## Decision

Train on Colab or Kaggle, export the artifact, and verify its checksum. Uploading it to S3 is optional. Design
the AWS deployment only:

- Use Lambda only if the measured artifact and runtime fit within the limits and requests are small.
- Batch inference suits workloads that do not need real-time responses.
- A managed endpoint suits production latency and scaling needs, but the core path excludes it because of its ongoing cost.

## Consequence

The capstone demonstrates experiment discipline and architecture reasoning. It does not demonstrate production CV serving.
