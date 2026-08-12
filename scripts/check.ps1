param(
    [ValidateSet('bootstrap', 'curriculum', 'capstone-tabular', 'capstone-cv', 'all')][string]$Scope = 'all',
    [ValidateSet('mini', 'ci', 'release')][string]$Profile = 'mini'
)
$ErrorActionPreference = 'Stop'
$python = if (Test-Path '.venv/Scripts/python.exe') { '.venv/Scripts/python.exe' } else { 'python' }
function Invoke-Checked {
  param([Parameter(Mandatory)][string[]]$Arguments)
  & $python @Arguments
  if ($LASTEXITCODE -ne 0) { throw "Check failed: python $($Arguments -join ' ') (exit $LASTEXITCODE)" }
}
if ($Scope -eq 'bootstrap') { Invoke-Checked @('-c', 'import ml_roadmap; print(ml_roadmap.__version__)'); exit 0 }
Invoke-Checked @('scripts/validate_curriculum.py')
Invoke-Checked @('scripts/validate_learner_docs.py')
Invoke-Checked @('scripts/validate_sources.py')
Invoke-Checked @('scripts/validate_notebooks.py')
Invoke-Checked @('scripts/validate_aws_safety.py')
Invoke-Checked @('-m', 'pytest', '-q')
if ($Scope -eq 'all') {
  Invoke-Checked @('-m', 'ruff', 'check', '.')
}
if ($Profile -in @('ci', 'release')) {
  Invoke-Checked @('-m', 'mypy')
}
