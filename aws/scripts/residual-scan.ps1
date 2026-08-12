param([Parameter(Mandatory)][ValidatePattern('^[a-z0-9-]{3,24}$')][string]$ProjectId,[string]$Region='us-east-1',[switch]$Json)
$ErrorActionPreference='Stop';$stack="ml-roadmap-$ProjectId";$findings=@()
function Invoke-AwsText([string[]]$Arguments,[switch]$NotFoundIsEmpty){
    $output=& aws @Arguments 2>&1;$code=$LASTEXITCODE
    if($code -ne 0){
        $message=($output|Out-String)
        if($NotFoundIsEmpty -and $message -match 'does not exist|not exist'){return ''}
        throw "AWS scan error: aws $($Arguments -join ' ') :: $message"
    }
    return ($output|Out-String).Trim()
}
$stackJson=Invoke-AwsText @('cloudformation','describe-stacks','--stack-name',$stack,'--region',$Region,'--output','json') -NotFoundIsEmpty
if($stackJson){$findings += [pscustomobject]@{service='cloudformation';resource=$stack}}
$queries=@(
    @{service='s3';args=@('s3api','list-buckets','--query',"Buckets[?starts_with(Name, 'ml-roadmap-$ProjectId')].Name",'--output','text')},
    @{service='lambda';args=@('lambda','list-functions','--region',$Region,'--query',"Functions[?starts_with(FunctionName, 'ml-roadmap-$ProjectId')].FunctionName",'--output','text')},
    @{service='logs';args=@('logs','describe-log-groups','--region',$Region,'--log-group-name-prefix',"/aws/lambda/ml-roadmap-$ProjectId",'--query','logGroups[].logGroupName','--output','text')},
    @{service='iam';args=@('iam','list-roles','--query',"Roles[?starts_with(RoleName, 'ml-roadmap-$ProjectId')].RoleName",'--output','text')},
    @{service='apigateway';args=@('apigatewayv2','get-apis','--region',$Region,'--query',"Items[?starts_with(Name, 'ml-roadmap-$ProjectId')].ApiId",'--output','text')}
)
foreach($query in $queries){
    $output=Invoke-AwsText $query.args
    foreach($name in ($output -split '\s+'|Where-Object{$_ -and $_ -ne 'None'})){$findings += [pscustomobject]@{service=$query.service;resource=$name}}
}
$result=[pscustomobject]@{project=$ProjectId;region=$Region;scan_status='complete';residual=($findings.Count -gt 0);resources=$findings}
if($Json){$result|ConvertTo-Json -Depth 4 -Compress}else{$result|Format-List}
if($findings.Count -gt 0){exit 1}

