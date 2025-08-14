@echo off
echo ========================================
echo    SUNDAE Crypto Futures Analyst
echo ========================================
echo.
echo Starting the SUNDAE application...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ and try again
    pause
    exit /b 1
)

REM Check if requirements are installed
echo Checking dependencies...
pip show streamlit >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies...
    pip install -r requirements.txt
)

REM Run the application
echo.
echo Starting SUNDAE Streamlit application...
echo The app will open in your browser at: http://localhost:8501
echo Press Ctrl+C to stop the application
echo.
python run_app.py

pause
