Write-Host "========================================="
Write-Host "Running Project Health Checks"
Write-Host "========================================="

Write-Host ""
Write-Host "1. Running training pipeline..."
python train.py

if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "Training pipeline failed."
    exit 1
}

Write-Host ""
Write-Host "2. Running pytest suite..."
python -m pytest

if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "Pytest suite failed."
    exit 1
}

Write-Host ""
Write-Host "========================================="
Write-Host "All health checks passed successfully."
Write-Host "========================================="