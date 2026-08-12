#!/usr/bin/env bash
set -euo pipefail
project_id="";owner="";expires_at="";artifact="";region="us-east-1";public="false";budget="false";while [[ $# -gt 0 ]];do case "$1" in --project-id)project_id="$2";shift 2;;--owner)owner="$2";shift 2;;--expires-at)expires_at="$2";shift 2;;--artifact-path)artifact="$2";shift 2;;--region)region="$2";shift 2;;--enable-public-api)public="true";shift;;--acknowledge-budget-configured)budget="true";shift;;*)exit 2;;esac;done
[[ "$budget" == "true" ]] || { echo "Acknowledge actual + forecast Budget alerts explicitly."; exit 2; }
[[ -f "$artifact" ]] || { echo "Artifact missing"; exit 2; }; (( $(wc -c < "$artifact") <= 209715200 )) || { echo "Artifact exceeds 200 MB"; exit 2; }
bash "$(dirname "$0")/cost-check.sh" --project-id "$project_id" --region "$region"
bash "$(dirname "$0")/preflight.sh" --project-id "$project_id" --region "$region" --artifact-path "$artifact" --acknowledge-budget-configured
aws cloudformation validate-template --template-body file://aws/cloudformation/tabular-inference.yml --region "$region" >/dev/null
aws cloudformation deploy --stack-name "ml-roadmap-$project_id" --template-file aws/cloudformation/tabular-inference.yml --capabilities CAPABILITY_NAMED_IAM --region "$region" --parameter-overrides ProjectId="$project_id" Owner="$owner" ExpiresAt="$expires_at" EnablePublicApi="$public" --tags Project="ml-roadmap-$project_id" Owner="$owner" Environment=learning ExpiresAt="$expires_at"
bucket=$(aws cloudformation describe-stacks --stack-name "ml-roadmap-$project_id" --region "$region" --query "Stacks[0].Outputs[?OutputKey=='BucketName'].OutputValue" --output text)
aws s3 cp "$artifact" "s3://$bucket/models/portable_model.json" --region "$region"
