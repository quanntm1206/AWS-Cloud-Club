# Capstone A - Tabular Churn Classification

## Goal

Xây pipeline churn có baseline, leakage-safe preprocessing, threshold decision, error analysis, model card,
artifact integrity và serverless inference an toàn trên AWS.

## Core sequence

1. Validate license/schema/target; chia train/validation/test trước preprocessing.
2. Dummy baseline; tối đa ba candidate; chọn theo validation và constraint, không theo test.
3. Freeze pipeline; đánh giá test đúng một lần; slice/error analysis.
4. Export `model.joblib`, `manifest.json`, `metrics.json`, model card.
5. Chạy AWS preflight/cost check; upload S3; deploy private Lambda; invoke valid/invalid event.
6. Cleanup; residual scan; lưu evidence không còn resource allowlist.

## Gates

Không leakage, secret hoặc forbidden AWS resource. AWS Budget không phải hard cap. Public HTTP API tắt mặc
định; không cần nâng cấp Paid Plan để hoàn thành core path.

## Tổng kết năng lực

Lưu source code, test evidence, report, model card, artifact checksum và AWS cleanup evidence trong thư mục
local do bạn chọn. Dùng rubric để tự đánh giá; không xuất bản hoặc gửi các file này cho ai.
