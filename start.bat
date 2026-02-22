@echo off
echo ========================================
echo AI Agent Platform - Server Start
echo ========================================
echo.

cd /d "%~dp0"

echo [Check] Checking API Key...
if defined ANTHROPIC_API_KEY (
    echo [OK] ANTHROPIC_API_KEY found
    goto :start_servers
)
if defined OPENAI_API_KEY (
    echo [OK] OPENAI_API_KEY found (will be used for Anthropic)
    goto :start_servers
)

echo [ERROR] API Key not found
echo.
echo Set one of these environment variables:
echo   - ANTHROPIC_API_KEY (recommended)
echo   - OPENAI_API_KEY (fallback)
echo.
echo You already have OPENAI_API_KEY set!
echo The system will use it automatically.
echo.
pause
exit /b 1

:start_servers
echo.
echo [1/2] Starting Backend...
cd backend
if exist venv\Scripts\activate.bat (
    start "Backend" cmd /k "venv\Scripts\activate & python app.py"
) else (
    start "Backend" cmd /k "python app.py"
)
cd ..

echo Waiting 5 seconds...
timeout /t 5 /nobreak > nul

echo [2/2] Starting Frontend...
cd frontend
start "Frontend" cmd /k "python -m http.server 8080"
cd ..

echo.
echo [OK] Servers started!
echo Backend:  http://localhost:5000
echo Frontend: http://localhost:8080
echo.

timeout /t 3 /nobreak > nul
start http://localhost:8080

echo.
echo Servers are running.
echo Close server windows to stop.
pause
