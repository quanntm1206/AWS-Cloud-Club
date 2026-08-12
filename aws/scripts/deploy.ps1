param(
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9-]{3,24}$')][string]$ProjectId,
    [Parameter(Mandatory)][string]$Owner,
    [Parameter(Mandatory)][string]$ExpiresAt,
    [Parameter(Mandatory)][string]$ArtifactPath,
    [string]$Region = 'us-east-1',
    [switch]$AcknowledgeBudgetConfigured
)
$ErrorActionPreference = 'Stop'
$stack = "ml-roadmap-$ProjectId"
Write-Host 'ExpiresAt is metadata, not automatic deletion. Keep this session open for cleanup.'
if (-not $AcknowledgeBudgetConfigured) {
    throw 'Pass -AcknowledgeBudgetConfigured only after creating actual + forecast alerts.'
}

& "$PSScriptRoot/cost-check.ps1" -ProjectId $ProjectId -Region $Region
& "$PSScriptRoot/preflight.ps1" -ProjectId $ProjectId -Region $Region -ArtifactPath $ArtifactPath `
    -AcknowledgeBudgetConfigured:$AcknowledgeBudgetConfigured

aws cloudformation validate-template --template-body file://aws/cloudformation/tabular-inference.yml `
    --region $Region | Out-Null
if ($LASTEXITCODE -ne 0) { throw "CloudFormation template validation failed: exit $LASTEXITCODE" }

aws cloudformation deploy --stack-name $stack --template-file aws/cloudformation/tabular-inference.yml `
    --capabilities CAPABILITY_NAMED_IAM --region $Region `
    --parameter-overrides ProjectId=$ProjectId Owner=$Owner ExpiresAt=$ExpiresAt `
    --tags Project=$stack Owner=$Owner Environment=learning ExpiresAt=$ExpiresAt
if ($LASTEXITCODE -ne 0) {
    Write-Error "RECOVERY REQUIRED: deploy may have left a stack. Run: pwsh aws/scripts/cleanup.ps1 -ProjectId $ProjectId -Region $Region"
    throw "CloudFormation deploy failed: exit $LASTEXITCODE"
}

$bucket = aws cloudformation describe-stacks --stack-name $stack --region $Region `
    --query "Stacks[0].Outputs[?OutputKey=='BucketName'].OutputValue" --output text
if ($LASTEXITCODE -ne 0) {
    Write-Error "RECOVERY REQUIRED: output lookup failed. Run: pwsh aws/scripts/cleanup.ps1 -ProjectId $ProjectId -Region $Region"
    throw "CloudFormation output lookup failed: exit $LASTEXITCODE"
}
if ([string]::IsNullOrWhiteSpace($bucket) -or $bucket -eq 'None') { throw 'Stack did not return BucketName' }

aws s3 cp $ArtifactPath "s3://$bucket/models/portable_model.json" --region $Region
if ($LASTEXITCODE -ne 0) {
    Write-Error "RECOVERY REQUIRED: stack may exist. Run: pwsh aws/scripts/cleanup.ps1 -ProjectId $ProjectId -Region $Region"
    throw "Artifact upload failed: exit $LASTEXITCODE"
}
