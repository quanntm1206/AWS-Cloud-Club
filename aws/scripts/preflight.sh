#!/usr/bin/env bash
set -euo pipefail
project_id=""; region="us-east-1"; artifact=""; budget="false"
while [[ $# -gt 0 ]]; do case "$1" in --project-id) project_id="$2";shift 2;;--region) region="$2";shift 2;;--artifact-path) artifact="$2";shift 2;;--acknowledge-budget-configured) budget="true";shift;;*) echo "Unknown argument: $1";exit 2;;esac;done
[[ "$project_id" =~ ^[a-z0-9-]{3,24}$ ]] || { echo "Invalid project id"; exit 2; }
[[ "$region" == "us-east-1" ]] || { echo "Core lab requires us-east-1"; exit 2; }
command -v aws >/dev/null; [[ -f "$artifact" ]] || { echo "Artifact missing"; exit 2; }
[[ "$budget" == "true" ]] || { echo "Create actual + forecast budget alerts, then acknowledge."; exit 2; }
(( $(wc -c < "$artifact") <= 209715200 )) || { echo "Artifact exceeds 200 MB"; exit 2; }
aws sts get-caller-identity --output json
echo "Stack=ml-roadmap-$project_id Region=$region. AWS Budgets is not a hard cap; billing can be delayed."
