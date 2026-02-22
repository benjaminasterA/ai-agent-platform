@echo off
echo ========================================
echo AI Agent Platform - Clean Installation
echo ========================================
echo.

cd /d "%~dp0"

echo [1/5] Removing old virtual environment...
cd backend
if exist venv (
    rmdir /s /q venv
    echo [OK] Old venv removed
)

echo.
echo [2/5] Creating new virtual environment...
python -m venv venv
echo [OK] New venv created

echo.
echo [3/5] Activating virtual environment...
call venv\Scripts\activate.bat
echo [OK] Activated

echo.
echo [4/5] Upgrading pip to latest version...
python -m pip install --upgrade pip
echo [OK] Pip upgraded

echo.
echo [5/5] Installing packages...
pip install -r requirements.txt
echo [OK] All packages installed

cd ..

echo.
echo ========================================
echo Clean Installation Complete!
echo ========================================
echo.
echo Next: Run start.bat
echo.
pause
