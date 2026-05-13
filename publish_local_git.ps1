$ErrorActionPreference = "Stop"

Set-Location -LiteralPath $PSScriptRoot

Write-Host "Preparing local Git repository for Induced Dependence v0.1.0..."

if (-not (Test-Path -LiteralPath ".git")) {
    git init
}

git add .
git commit -m "Initial v0.1.0 research package"
git branch -M main

Write-Host ""
Write-Host "Done. Local Git repository is ready on branch main."
Write-Host ""
Write-Host "Next steps:"
Write-Host "1. Create a GitHub repository, recommended name: induced-dependence"
Write-Host "2. Then run:"
Write-Host "   git remote add origin https://github.com/YOUR_USERNAME/induced-dependence.git"
Write-Host "   git push -u origin main"
Write-Host ""
Write-Host "After GitHub upload, create release v0.1.0 and connect Zenodo."

