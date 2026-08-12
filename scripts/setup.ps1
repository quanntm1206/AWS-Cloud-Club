param(
    [ValidateSet('core', 'serve', 'cv', 'all')][string]$Profile = 'core',
    [string]$Python = 'python'
)
$ErrorActionPreference = 'Stop'
if (-not (Test-Path '.venv')) { & $Python -m venv .venv }
$venvPython = Join-Path '.venv' 'Scripts/python.exe'
& $venvPython -m pip install --upgrade pip
& $venvPython -m pip install -r requirements.lock
if ($Profile -in @('cv', 'all')) {
    Write-Host 'CV dependencies are environment-specific. Follow notebooks/README.md.'
}
& $venvPython -m pip install -e . --no-deps

