param(
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9-]{3,24}$')][string]$ProjectId,
    [string]$Region = 'us-east-1',
    [switch]$Execute,
    [string]$ConfirmProjectId
)
$ErrorActionPreference = 'Stop'
$stack = "ml-roadmap-$ProjectId"
Write-Host "Cleanup target: stack=$stack region=$Region"

$resources = aws cloudformation list-stack-resources --stack-name $stack --region $Region --output json 2>$null
if ($LASTEXITCODE -ne 0) { throw "Cannot list stack resources; cleanup stopped: exit $LASTEXITCODE" }
Write-Host $resources
if (-not $Execute) {
    Write-Host 'DRY-RUN only. Re-run with -Execute -ConfirmProjectId <exact-id> after reading exact resources.'
    exit 0
}
if ($ConfirmProjectId -ne $ProjectId) { throw 'Confirmation mismatch; nothing deleted.' }

$bucket = aws cloudformation describe-stacks --stack-name $stack --region $Region `
    --query "Stacks[0].Outputs[?OutputKey=='BucketName'].OutputValue" --output text
if ($LASTEXITCODE -ne 0) { throw "Cannot read BucketName; cleanup stopped: exit $LASTEXITCODE" }
if (-not [string]::IsNullOrWhiteSpace($bucket) -and $bucket -ne 'None') {
    aws s3 rm "s3://$bucket" --recursive --region $Region
    if ($LASTEXITCODE -ne 0) { throw "Bucket cleanup failed; stack deletion stopped: exit $LASTEXITCODE" }
}
aws cloudformation delete-stack --stack-name $stack --region $Region
if ($LASTEXITCODE -ne 0) { throw "Stack delete request failed: exit $LASTEXITCODE" }
aws cloudformation wait stack-delete-complete --stack-name $stack --region $Region
if ($LASTEXITCODE -ne 0) { throw "Stack delete wait failed: exit $LASTEXITCODE" }
