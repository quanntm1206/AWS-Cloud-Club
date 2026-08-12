param(
    [Parameter(Mandatory)][ValidatePattern('^[a-z0-9-]{3,24}$')][string]$ProjectId,
    [string]$Region = 'us-east-1',
    [Parameter(Mandatory)][string]$ArtifactPath,
    [switch]$AcknowledgeBudgetConfigured
)
$ErrorActionPreference = 'Stop'
if (-not (Get-Command aws -ErrorAction SilentlyContinue)) { throw 'AWS CLI not found.' }
if ($Region -ne 'us-east-1') { throw 'Core lab requires us-east-1 unless curriculum owner approves another region.' }
if (-not $AcknowledgeBudgetConfigured) { throw 'Create actual + forecast budget alerts, then pass -AcknowledgeBudgetConfigured.' }
$identityJson = aws sts get-caller-identity --output json
if ($LASTEXITCODE -ne 0) { throw "AWS identity lookup failed; preflight stopped: exit $LASTEXITCODE" }
try { $identity = $identityJson | ConvertFrom-Json } catch { throw 'AWS identity response was not valid JSON.' }
if ([string]::IsNullOrWhiteSpace($identity.Account) -or [string]::IsNullOrWhiteSpace($identity.Arn)) {
    throw 'AWS identity response is missing Account or Arn.'
}
$size = (Get-Item -LiteralPath $ArtifactPath).Length
if ($size -gt 200MB) { throw 'Artifact exceeds hard limit 200 MB.' }
$stack = "ml-roadmap-$ProjectId"
[pscustomobject]@{Account=$identity.Account;Arn=$identity.Arn;Region=$Region;Stack=$stack;ArtifactMB=[math]::Round($size/1MB,2);BudgetCaveat='AWS Budgets is not a hard cap; billing can be delayed.'} | Format-List
