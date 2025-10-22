@echo off
echo ==========================================
echo ModulationPSKProject - Setup
echo ==========================================
echo.

REM Check Python version
echo Checking Python version...
python --version
if errorlevel 1 (
    echo ERROR: Python not found! Please install Python 3.8 or higher.
    pause
    exit /b 1
)
echo.

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment!
    pause
    exit /b 1
)
echo.

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo.

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip
echo.

REM Install dependencies
echo Installing dependencies from requirements.txt...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies!
    pause
    exit /b 1
)
echo.

REM Create results directory
echo Creating results directory...
if not exist results mkdir results
echo.

echo ==========================================
echo Setup completed successfully!
echo ==========================================
echo.
echo To activate the environment, run:
echo   venv\Scripts\activate.bat
echo.
echo To run the simulation:
echo   cd src
echo   python main.py
echo.
pause