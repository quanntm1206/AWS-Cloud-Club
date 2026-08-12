# ADR - Không triển khai CV endpoint trong core path

## Context

Model CV lớn hơn tabular, cold start/memory cao hơn và endpoint có thể tạo chi phí nền. Người học cần hiểu
MLOps nhưng constraint ưu tiên Free Plan và tránh surprise cost.

## Decision

Train trên Colab/Kaggle; export và kiểm checksum; S3 upload là optional. AWS deployment chỉ thiết kế:

- Lambda chỉ nếu artifact/runtime nằm trong limit đã đo và request nhỏ.
- Batch inference phù hợp workload không cần realtime.
- Managed endpoint phù hợp production latency/scale nhưng bị loại khỏi core vì chi phí nền.

## Consequence

Capstone chứng minh experiment discipline và architecture reasoning, không chứng minh production serving CV.

