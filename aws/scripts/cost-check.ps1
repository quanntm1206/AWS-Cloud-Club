param([Parameter(Mandatory)][string]$ProjectId,[string]$Region='us-east-1')
$stack="ml-roadmap-$ProjectId"
Write-Host "DRY-RUN bounded estimate: $stack ($Region)"
Write-Host 'Assumptions: artifact <=50 MB stored 24h; <=100 Lambda invokes at 512 MB/<=1s; <=5 MB logs; HTTP API disabled.'
Write-Host 'Planning envelope: USD 0.00-0.10 before tax, assuming no Free Tier/credits. STOP if calculator estimate exceeds USD 0.10.'
Write-Host 'Pricing checked 2026-08-12; recheck current S3, Lambda, CloudWatch Logs prices before every deploy.'
Write-Host 'Sources: https://aws.amazon.com/s3/pricing/ https://aws.amazon.com/lambda/pricing/ https://aws.amazon.com/cloudwatch/pricing/'
Write-Host 'Budget alerts are delayed, not a hard cap. This bound is a planning guard, not a bill guarantee.'
