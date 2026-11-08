# MiroFish Localhost Startup Script
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$projectDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $projectDir

Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "              Iniciando MiroFish Localhost              " -ForegroundColor Cyan
Write-Host "========================================================" -ForegroundColor Cyan

if (-not (Test-Path ".env")) {
    Write-Host "[INFO] Criando arquivo .env a partir de .env.example..." -ForegroundColor Yellow
    Copy-Item ".env.example" ".env"
}

$env:PATH = "$env:APPDATA\Python\Python314\Scripts;$env:PATH"

Write-Host ""
Write-Host "[INFO] Endereços de acesso:" -ForegroundColor Green
Write-Host "  - Frontend:  http://localhost:3000" -ForegroundColor White
Write-Host "  - Backend:   http://localhost:5001" -ForegroundColor White
Write-Host ""
Write-Host "Pressione Ctrl+C para encerrar os serviços." -ForegroundColor Gray
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host ""

npm run dev

