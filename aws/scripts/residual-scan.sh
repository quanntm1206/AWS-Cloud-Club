#!/usr/bin/env bash
set -euo pipefail
project_id="";region="us-east-1";json="false";while [[ $# -gt 0 ]];do case "$1" in --project-id)project_id="$2";shift 2;;--region)region="$2";shift 2;;--json)json="true";shift;;*)exit 2;;esac;done
[[ "$project_id" =~ ^[a-z0-9-]{3,24}$ ]] || { echo "Invalid project id";exit 2; }
stack="ml-roadmap-$project_id";findings=()
tmp=$(mktemp);trap 'rm -f "$tmp"' EXIT
if aws cloudformation describe-stacks --stack-name "$stack" --region "$region" --output json >"$tmp" 2>&1;then findings+=("cloudformation:$stack");else grep -Eqi 'does not exist|not exist' "$tmp" || { echo "AWS scan error: $(cat "$tmp")";exit 3; };fi
scan(){ local service="$1";shift;local output;if ! output=$(aws "$@" 2>&1);then echo "AWS scan error ($service): $output";exit 3;fi;while read -r name;do [[ -z "$name" || "$name" == "None" ]]||findings+=("$service:$name");done < <(printf '%s' "$output"|tr '\t' '\n');}
scan s3 s3api list-buckets --query "Buckets[?starts_with(Name, 'ml-roadmap-$project_id')].Name" --output text
scan lambda lambda list-functions --region "$region" --query "Functions[?starts_with(FunctionName, 'ml-roadmap-$project_id')].FunctionName" --output text
scan logs logs describe-log-groups --region "$region" --log-group-name-prefix "/aws/lambda/ml-roadmap-$project_id" --query 'logGroups[].logGroupName' --output text
scan iam iam list-roles --query "Roles[?starts_with(RoleName, 'ml-roadmap-$project_id')].RoleName" --output text
residual=false;[[ ${#findings[@]} -gt 0 ]]&&residual=true
budget_note="Budget alerts are kept intentionally; review or delete them manually after the course."
if [[ "$json" == "true" ]];then printf '{"project":"%s","region":"%s","scan_status":"complete","residual":%s,"resources":"%s","budget_note":"%s"}\n' "$project_id" "$region" "$residual" "${findings[*]-}" "$budget_note";else printf 'project=%s region=%s scan_status=complete residual=%s resources=%s budget_note=%s\n' "$project_id" "$region" "$residual" "${findings[*]-}" "$budget_note";fi
[[ "$residual" == "false" ]]
