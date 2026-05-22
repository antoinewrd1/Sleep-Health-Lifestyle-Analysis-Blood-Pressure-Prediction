Write-Host "Running full ML pipeline"

python train.py

if ($LASTEXITCODE -ne 0) {
    exit 1
}

python -m pytest

if ($LASTEXITCODE -ne 0) {
    exit 1
}

Write-Host "Pipeline completed successfully"