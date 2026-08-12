#!/usr/bin/env bash
set -euo pipefail
project_id=""; region="us-east-1"; execute="false"; confirm_project_id=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --project-id) project_id="$2"; shift 2;;
    --region) region="$2"; shift 2;;
    --execute) execute="true"; shift;;
    --confirm-project-id) confirm_project_id="$2"; shift 2;;
    --dry-run) shift;;
    *) echo "Unknown argument: $1" >&2; exit 2;;
  esac
done
[[ "$project_id" =~ ^[a-z0-9-]{3,24}$ ]] || { echo "Invalid project id" >&2; exit 2; }
stack="ml-roadmap-$project_id"; echo "Cleanup target: stack=$stack region=$region"
resources=$(aws cloudformation list-stack-resources --stack-name "$stack" --region "$region" --output table)
printf '%s\n' "$resources"
[[ "$execute" == "true" ]] || { echo "DRY-RUN only. Re-run with --execute --confirm-project-id <exact-id>."; exit 0; }
[[ "$confirm_project_id" == "$project_id" ]] || { echo "Confirmation mismatch" >&2; exit 2; }
bucket=$(aws cloudformation describe-stacks --stack-name "$stack" --region "$region" --query "Stacks[0].Outputs[?OutputKey=='BucketName'].OutputValue" --output text)
[[ -z "$bucket" || "$bucket" == "None" ]] || aws s3 rm "s3://$bucket" --recursive --region "$region"
aws cloudformation delete-stack --stack-name "$stack" --region "$region"
aws cloudformation wait stack-delete-complete --stack-name "$stack" --region "$region"
