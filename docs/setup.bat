@echo off
echo ==========================================
echo Konfiguracja srodowiska Python
echo ModulationPSKProject
echo ==========================================
echo.

REM Sprawdzenie wersji Pythona
echo Sprawdzanie wersji Pythona...
python --version

REM Tworzenie wirtualnego srodowiska
echo.
echo Tworzenie wirtualnego srodowiska...
python -m venv venv

REM Aktywacja wirtualnego srodowiska
echo.
echo Aktywacja wirtualnego srodowiska...
call venv\Scripts\activate.bat

REM Aktualizacja pip
echo.
echo Aktualizacja pip...
python -m pip install --upgrade pip

REM Instalacja zaleznosci
echo.
echo Instalacja zaleznosci z requirements.txt...
pip install -r requirements.txt

echo.
echo ==========================================
echo Konfiguracja zakonczona pomyslnie!
echo ==========================================
echo.
echo Aby aktywowac srodowisko uruchom:
echo venv\Scripts\activate.bat
echo.
echo Aby dezaktywowac srodowisko uruchom:
echo deactivate
echo.
pause
