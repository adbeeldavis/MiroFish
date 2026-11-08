@echo off
chcp 65001 >nul
title MiroFish - Localhost Server

cd /d "%~dp0"

echo ========================================================
echo               Iniciando MiroFish Localhost
echo ========================================================
echo.

if not exist ".env" (
    echo [INFO] Criando arquivo .env a partir de .env.example...
    copy .env.example .env >nul
)

set "PATH=%APPDATA%\Python\Python314\Scripts;%LOCALAPPDATA%\Programs\Python\Python314\Scripts;%PATH%"

echo [INFO] Enderecos de acesso:
echo   - Frontend:  http://localhost:3000
echo   - Backend:   http://localhost:5001
echo.
echo Pressione Ctrl+C para encerrar o servidor.
echo ========================================================
echo.

npm run dev
pause

