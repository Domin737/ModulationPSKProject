@echo off
REM ============================================================
REM ModulationPSKProject - Setup Script for Windows
REM Version: 1.4.0
REM ============================================================

setlocal enabledelayedexpansion

echo.
echo ============================================================
echo ModulationPSKProject - Environment Setup
echo Version: 1.4.0
echo ============================================================
echo.

REM Check if Python is installed
echo [1/6] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH!
    echo.
    echo Please install Python 3.8 or higher from:
    echo https://www.python.org/downloads/
    echo.
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b 1
)

REM Display Python version
for /f "tokens=*" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo SUCCESS: Found %PYTHON_VERSION%
echo.

REM Check if requirements.txt exists
echo [2/6] Checking requirements.txt...
if not exist "requirements.txt" (
    echo ERROR: requirements.txt not found!
    echo.
    echo Please make sure you are running this script from the project root directory.
    pause
    exit /b 1
)
echo SUCCESS: requirements.txt found
echo.

REM Remove old virtual environment if exists
if exist "venv" (
    echo [3/6] Removing old virtual environment...
    rmdir /s /q venv
    echo SUCCESS: Old environment removed
    echo.
)

REM Create virtual environment
echo [3/6] Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment!
    echo.
    echo This might be caused by:
    echo - Insufficient permissions
    echo - Antivirus software blocking the operation
    echo - Corrupted Python installation
    echo.
    echo Try running this script as Administrator.
    pause
    exit /b 1
)
echo SUCCESS: Virtual environment created
echo.

REM Activate virtual environment
echo [4/6] Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment!
    pause
    exit /b 1
)
echo SUCCESS: Virtual environment activated
echo.

REM Upgrade pip
echo [5/6] Upgrading pip...
python -m pip install --upgrade pip --quiet
if errorlevel 1 (
    echo WARNING: Failed to upgrade pip (continuing anyway)
    echo.
) else (
    echo SUCCESS: pip upgraded
    echo.
)

REM Install dependencies
echo [6/6] Installing dependencies...
echo This may take a few minutes...
echo.
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies!
    echo.
    echo Please check your internet connection and try again.
    echo.
    echo If the problem persists, try installing packages manually:
    echo   pip install numpy scipy matplotlib
    pause
    exit /b 1
)
echo SUCCESS: All dependencies installed
echo.

REM Create necessary directories
echo Creating project directories...
if not exist "results" mkdir results
if not exist "docs" mkdir docs
echo SUCCESS: Directories created
echo.

REM Verification
echo ============================================================
echo Verifying installation...
echo ============================================================
echo.

python -c "import numpy; print('  NumPy version:', numpy.__version__)" 2>nul
if errorlevel 1 (
    echo WARNING: NumPy verification failed
) else (
    echo SUCCESS: NumPy verified
)

python -c "import scipy; print('  SciPy version:', scipy.__version__)" 2>nul
if errorlevel 1 (
    echo WARNING: SciPy verification failed
) else (
    echo SUCCESS: SciPy verified
)

python -c "import matplotlib; print('  Matplotlib version:', matplotlib.__version__)" 2>nul
if errorlevel 1 (
    echo WARNING: Matplotlib verification failed
) else (
    echo SUCCESS: Matplotlib verified
)

echo.
echo ============================================================
echo Setup completed successfully!
echo ============================================================
echo.
echo Next steps:
echo.
echo 1. Activate the virtual environment:
echo    venv\Scripts\activate.bat
echo.
echo 2. Navigate to src directory:
echo    cd src
echo.
echo 3. Run the simulation:
echo    python main.py
echo.
echo 4. To deactivate the environment:
echo    deactivate
echo.
echo For more information, see docs\index.md
echo ============================================================
echo.
pause