# Instrukcja instalacji

## Wersja: 1.4.0

Szczegolowy przewodnik instalacji projektu ModulationPSKProject dla roznych systemow operacyjnych.

---

## Spis tresci

1. [Przed instalacja](#przed-instalacja)
2. [Instalacja na Windows](#instalacja-na-windows)
3. [Instalacja na Linux](#instalacja-na-linux)
4. [Instalacja na macOS](#instalacja-na-macos)
5. [Instalacja manualna](#instalacja-manualna)
6. [Weryfikacja instalacji](#weryfikacja-instalacji)
7. [Rozwiazywanie problemow](#rozwiazywanie-problemow)
8. [Dezinstalacja](#dezinstalacja)

---

## Przed instalacja

### Wymagania wstepne

Przed rozpoczeciem instalacji upewnij sie, ze:

✅ Masz zainstalowany Python 3.8 lub nowszy  
✅ Masz stabilne polaczenie z internetem (do pobrania bibliotek)  
✅ Masz ~500 MB wolnego miejsca na dysku  
✅ Masz uprawnienia administratora (jesli wymagane)

### Sprawdzenie Python

**Windows:**

```cmd
python --version
```

**Linux/Mac:**

```bash
python3 --version
```

Powinno wyswietlic wersje Python rowna lub wyzsza niz 3.8, np.: `Python 3.9.7`

Jesli Python nie jest zainstalowany, zobacz: [Wymagania i srodowisko](requirements-and-environment.md#python)

---

## Instalacja na Windows

### Metoda 1: Instalacja automatyczna (zalecana)

#### Krok 1: Pobierz projekt

```cmd
cd C:\Projects
git clone [URL_PROJEKTU] ModulationPSKProject
cd ModulationPSKProject
```

Lub rozpakuj ZIP z projektem.

#### Krok 2: Uruchom skrypt instalacyjny

Kliknij dwukrotnie na plik `setup.bat` lub uruchom w CMD:

```cmd
setup.bat
```

#### Co robi setup.bat?

1. ✅ Sprawdza wersje Python
2. ✅ Tworzy srodowisko wirtualne `venv`
3. ✅ Aktywuje srodowisko
4. ✅ Aktualizuje pip
5. ✅ Instaluje wszystkie zaleznosci z `requirements.txt`
6. ✅ Tworzy katalogi `results` i `docs`
7. ✅ Weryfikuje instalacje bibliotek

#### Krok 3: Weryfikacja

Po zakonczeniu instalacji zobaczysz:

```
============================================================
Setup completed successfully!
============================================================

Next steps:

1. Activate the virtual environment:
   venv\Scripts\activate.bat

2. Navigate to src directory:
   cd src

3. Run the simulation:
   python main.py
```

#### Krok 4: Test instalacji

```cmd
REM Aktywuj srodowisko
venv\Scripts\activate.bat

REM Przetestuj import
python -c "import numpy, scipy, matplotlib; print('OK')"
```

Powinno wyswietlic: `OK`

### Metoda 2: Instalacja przez PowerShell

#### Krok 1: Wlacz wykonywanie skryptow

Uruchom PowerShell jako Administrator:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### Krok 2: Uruchom instalacje

```powershell
.\setup.bat
```

### Typowe problemy na Windows

#### Problem 1: "python nie jest rozpoznawany"

**Rozwiazanie A:** Uzyj `py` zamiast `python`:

```cmd
py --version
py -m venv venv
```

**Rozwiazanie B:** Dodaj Python do PATH:

1. Szukaj "Environment Variables" w menu Start
2. System Properties → Advanced → Environment Variables
3. W "System variables" znajdz "Path"
4. Dodaj: `C:\Users\[User]\AppData\Local\Programs\Python\Python39\`
5. Dodaj: `C:\Users\[User]\AppData\Local\Programs\Python\Python39\Scripts\`

#### Problem 2: Blad uprawnien

**Rozwiazanie:** Uruchom CMD jako Administrator:

1. Prawy klik na CMD
2. "Run as administrator"
3. Uruchom `setup.bat`

#### Problem 3: Antywirus blokuje

**Rozwiazanie:**

1. Tymczasowo wylacz antywirus
2. Dodaj katalog projektu do wyjatkow
3. Uruchom instalacje

---

## Instalacja na Linux

### Metoda 1: Instalacja automatyczna (zalecana)

#### Dla Ubuntu/Debian

##### Krok 1: Zainstaluj wymagania systemowe

```bash
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv python3-dev build-essential
```

##### Krok 2: Pobierz projekt

```bash
cd ~
git clone [URL_PROJEKTU] ModulationPSKProject
cd ModulationPSKProject
```

Lub rozpakuj archiwum.

##### Krok 3: Nadaj uprawnienia i uruchom

```bash
chmod +x setup.sh
./setup.sh
```

#### Dla Fedora/RHEL/CentOS

##### Krok 1: Zainstaluj wymagania

```bash
sudo dnf install python3 python3-pip python3-devel gcc
```

##### Krok 2: Pobierz i uruchom

```bash
cd ~
git clone [URL_PROJEKTU] ModulationPSKProject
cd ModulationPSKProject
chmod +x setup.sh
./setup.sh
```

#### Dla Arch Linux

##### Krok 1: Zainstaluj wymagania

```bash
sudo pacman -S python python-pip
```

##### Krok 2: Pobierz i uruchom

```bash
cd ~
git clone [URL_PROJEKTU] ModulationPSKProject
cd ModulationPSKProject
chmod +x setup.sh
./setup.sh
```

#### Co robi setup.sh?

Skrypt automatycznie:

1. ✅ Sprawdza wersje Python (wymaga 3.8+)
2. ✅ Tworzy srodowisko wirtualne
3. ✅ Aktywuje srodowisko
4. ✅ Aktualizuje pip
5. ✅ Instaluje wszystkie zaleznosci
6. ✅ Tworzy katalogi robocze
7. ✅ Weryfikuje instalacje

#### Weryfikacja instalacji

Po zakonczeniu:

```bash
# Aktywuj srodowisko
source venv/bin/activate

# Test importu
python -c "import numpy, scipy, matplotlib; print('Instalacja OK')"
```

### Typowe problemy na Linux

#### Problem 1: Brak modulu venv

**Rozwiazanie (Ubuntu/Debian):**

```bash
sudo apt-get install python3-venv
```

**Rozwiazanie (Fedora/RHEL):**

```bash
sudo dnf install python3-virtualenv
```

#### Problem 2: Bledy kompilacji (NumPy/SciPy)

**Rozwiazanie:**

```bash
# Ubuntu/Debian
sudo apt-get install python3-dev build-essential gfortran libopenblas-dev liblapack-dev

# Fedora/RHEL
sudo dnf install python3-devel gcc gcc-gfortran openblas-devel lapack-devel
```

#### Problem 3: Uprawnienia

**Rozwiazanie:**

```bash
# Nadaj uprawnienia do katalogu
chmod -R u+rwX ~/ModulationPSKProject

# Lub zmien wlasciciela
sudo chown -R $USER:$USER ~/ModulationPSKProject
```

---

## Instalacja na macOS

### Metoda 1: Instalacja przez Homebrew (zalecana)

#### Krok 1: Zainstaluj Homebrew (jesli nie masz)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### Krok 2: Zainstaluj Python

```bash
brew install python3
```

#### Krok 3: Pobierz projekt

```bash
cd ~
git clone [URL_PROJEKTU] ModulationPSKProject
cd ModulationPSKProject
```

#### Krok 4: Uruchom instalacje

```bash
chmod +x setup.sh
./setup.sh
```

### Metoda 2: Instalacja bez Homebrew

#### Krok 1: Zainstaluj Python

Pobierz instalator ze strony https://www.python.org/downloads/macos/

#### Krok 2: Zainstaluj Xcode Command Line Tools

```bash
xcode-select --install
```

#### Krok 3: Uruchom instalacje

```bash
cd ~/ModulationPSKProject
chmod +x setup.sh
./setup.sh
```

### Typowe problemy na macOS

#### Problem 1: Brak xcode-select

**Rozwiazanie:**

```bash
xcode-select --install
```

#### Problem 2: Bledy SSL/certyfikatu

**Rozwiazanie:**

```bash
# Aktualizuj certyfikaty
/Applications/Python\ 3.9/Install\ Certificates.command
```

#### Problem 3: M1/M2 (Apple Silicon)

**Rozwiazanie:**

Uzyj natywnego Python dla ARM:

```bash
# Sprawdz architekture
uname -m  # Powinno wyswietlic arm64

# Uzyj odpowiedniej wersji Python
which python3
```

Jesli uzywasz Rosetta (x86_64), zainstaluj Python przez Homebrew.

---

## Instalacja manualna

Dla zaawansowanych uzytkownikow lub w przypadku problemow z automatyczna instalacja.

### Krok 1: Utworz srodowisko wirtualne

**Windows:**

```cmd
python -m venv venv
```

**Linux/Mac:**

```bash
python3 -m venv venv
```

### Krok 2: Aktywuj srodowisko

**Windows CMD:**

```cmd
venv\Scripts\activate.bat
```

**Windows PowerShell:**

```powershell
venv\Scripts\Activate.ps1
```

**Linux/Mac:**

```bash
source venv/bin/activate
```

### Krok 3: Aktualizuj pip

```bash
python -m pip install --upgrade pip
```

### Krok 4: Zainstaluj zaleznosci

```bash
pip install -r requirements.txt
```

Lub recznie:

```bash
pip install "numpy>=1.24.0,<2.0.0"
pip install "scipy>=1.10.0,<2.0.0"
pip install "matplotlib>=3.7.0,<4.0.0"
```

### Krok 5: Utworz katalogi

**Windows:**

```cmd
mkdir results
mkdir docs
```

**Linux/Mac:**

```bash
mkdir -p results docs
```

### Krok 6: Weryfikacja

```bash
python -c "import numpy; print('NumPy:', numpy.__version__)"
python -c "import scipy; print('SciPy:', scipy.__version__)"
python -c "import matplotlib; print('Matplotlib:', matplotlib.__version__)"
```

---

## Weryfikacja instalacji

### Test 1: Wersje bibliotek

```bash
pip list
```

Powinny byc widoczne:

- numpy (>= 1.24.0)
- scipy (>= 1.10.0)
- matplotlib (>= 3.7.0)

### Test 2: Import modulow projektu

```bash
cd src
python -c "from GetBytes import gen_bites; print('OK')"
python -c "from Modulator import bpsk_modulation; print('OK')"
python -c "from AddAWGNNoise import add_awgn_noise; print('OK')"
```

### Test 3: Pelna symulacja

```bash
cd src
python main.py
```

Powinno uruchomic symulacje i wygenerowac wykresy w katalogu `results/`.

### Test 4: Skrypt testowy (jesli dostepny)

```bash
python test_environment.py
```

---

## Rozwiazywanie problemow

### Problem: ModuleNotFoundError

**Przyczyna:** Srodowisko nie jest aktywowane lub biblioteki nie sa zainstalowane.

**Rozwiazanie:**

```bash
# Aktywuj srodowisko
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Zainstaluj zaleznosci ponownie
pip install -r requirements.txt
```

### Problem: ImportError: DLL load failed (Windows)

**Przyczyna:** Brak Visual C++ Redistributable.

**Rozwiazanie:**
Zainstaluj Microsoft Visual C++ Redistributable:
https://aka.ms/vs/17/release/vc_redist.x64.exe

### Problem: Permission denied

**Rozwiazanie (Linux/Mac):**

```bash
chmod +x setup.sh
sudo chown -R $USER:$USER .
```

### Problem: pip install fails

**Rozwiazanie:**

```bash
# Aktualizuj pip
python -m pip install --upgrade pip

# Wyczysc cache
pip cache purge

# Sprobuj ponownie
pip install -r requirements.txt
```

### Problem: Slow installation

**Rozwiazanie:**

Uzyj lokalnego cache lub mirrorow:

```bash
pip install -r requirements.txt --cache-dir ~/.cache/pip
```

### Problem: Konflikt wersji

**Rozwiazanie:**

Usun stare srodowisko i utworz nowe:

**Windows:**

```cmd
rmdir /s venv
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**Linux/Mac:**

```bash
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Dezinstalacja

### Usuwanie srodowiska wirtualnego

**Windows:**

```cmd
deactivate  REM Dezaktywuj srodowisko
rmdir /s /q venv
```

**Linux/Mac:**

```bash
deactivate  # Dezaktywuj srodowisko
rm -rf venv
```

### Calkowite usuniecie projektu

**Windows:**

```cmd
cd ..
rmdir /s ModulationPSKProject
```

**Linux/Mac:**

```bash
cd ..
rm -rf ModulationPSKProject
```

---

## Aktualizacja projektu

### Aktualizacja bibliotek

```bash
# Aktywuj srodowisko
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Aktualizuj wszystkie biblioteki
pip install --upgrade -r requirements.txt
```

### Aktualizacja kodu projektu

```bash
git pull origin main
```

---

## Podsumowanie

### Checklist instalacji

#### Przed instalacja

- [ ] Python 3.8+ zainstalowany
- [ ] pip dziala poprawnie
- [ ] Polaczenie z internetem

#### Instalacja

- [ ] Pobrany projekt
- [ ] Uruchomiony setup.bat / setup.sh
- [ ] Srodowisko wirtualne utworzone
- [ ] Biblioteki zainstalowane

#### Weryfikacja

- [ ] Import numpy, scipy, matplotlib dziala
- [ ] Import modulow projektu dziala
- [ ] Symulacja uruchamia sie poprawnie

### Nastepne kroki

Po pomyslnej instalacji:

1. Przeczytaj [glowny README](../README.md) - przyklady uzycia
2. Przejrzyj [strukture projektu](project-structure.md) - organizacja kodu
3. Uruchom pierwsza symulacje: `python src/main.py`

---

## Pomoc

Jesli napotkasz problemy:

1. Sprawdz [Obsluge bledow](error-handling.md)
2. Upewnij sie ze spelniasz [Wymagania](requirements-and-environment.md)
3. Przeczytaj sekcje "Rozwiazywanie problemow" powyzej

---

**Ostatnia aktualizacja:** 2025-10-22  
**Wersja dokumentu:** 1.4.0
