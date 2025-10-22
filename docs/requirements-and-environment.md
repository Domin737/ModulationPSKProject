# Wymagania i srodowisko

## Wersja: 1.4.0

Ten dokument opisuje wszystkie wymagania systemowe, softwarowe i konfiguracyjne dla projektu ModulationPSKProject.

---

## Spis tresci

1. [Wymagania systemowe](#wymagania-systemowe)
2. [Wymagania softwarowe](#wymagania-softwarowe)
3. [Biblioteki Python](#biblioteki-python)
4. [Srodowisko wirtualne](#srodowisko-wirtualne)
5. [Konfiguracja srodowiska](#konfiguracja-srodowiska)
6. [Weryfikacja instalacji](#weryfikacja-instalacji)
7. [Wymagania opcjonalne](#wymagania-opcjonalne)

---

## Wymagania systemowe

### Minimalne wymagania

| Komponent                | Minimalne wymaganie     | Zalecane                   |
| ------------------------ | ----------------------- | -------------------------- |
| **Procesor**             | Intel/AMD x86-64, 1 GHz | 2 GHz lub szybszy          |
| **RAM**                  | 2 GB                    | 4 GB lub wiecej            |
| **Miejsce na dysku**     | 500 MB                  | 1 GB (z danymi i wynikami) |
| **System operacyjny**    | Zobacz ponizej          | Najnowsza wersja           |
| **Rozdzielczosc ekranu** | 1024x768                | 1920x1080 lub wyzsza       |

### Wspierane systemy operacyjne

#### Windows

- ✅ **Windows 10** (64-bit) - wersja 1809 lub nowsza
- ✅ **Windows 11** (64-bit) - wszystkie wersje
- ⚠️ Windows 8.1 - moze dzialac, ale nie jest oficjalnie wspierany
- ❌ Windows 7 i starsze - nie wspierane

**Uwagi dla Windows:**

- Zalecane jest zainstalowanie wszystkich aktualizacji systemu
- Wymagane Microsoft Visual C++ Redistributable (instalowane z Python)

#### Linux

- ✅ **Ubuntu** 20.04 LTS, 22.04 LTS, 24.04 LTS
- ✅ **Debian** 11 (Bullseye), 12 (Bookworm)
- ✅ **Fedora** 38, 39, 40
- ✅ **CentOS Stream** 9
- ✅ **RHEL** 9
- ✅ **Arch Linux** (rolling release)
- ✅ Inne dystrybucje z Python 3.8+

**Wymagane pakiety systemowe (Linux):**

```bash
# Ubuntu/Debian
sudo apt-get install python3 python3-pip python3-venv python3-dev

# Fedora/RHEL/CentOS
sudo dnf install python3 python3-pip python3-devel

# Arch Linux
sudo pacman -S python python-pip
```

#### macOS

- ✅ **macOS 12 (Monterey)** lub nowszy
- ✅ **macOS 13 (Ventura)**
- ✅ **macOS 14 (Sonoma)**
- ⚠️ macOS 11 (Big Sur) - moze dzialac
- ❌ macOS 10.x - nie wspierany

**Uwagi dla macOS:**

- Wymagane Xcode Command Line Tools
- Zalecana instalacja przez Homebrew

---

## Wymagania softwarowe

### Python

#### Wymagana wersja

- **Minimalna:** Python 3.8
- **Zalecana:** Python 3.9 lub nowszy (3.11, 3.12)
- **Testowana:** Python 3.9, 3.10, 3.11, 3.12
- **Nie wspierana:** Python 3.7 i starsze, Python 2.x

#### Weryfikacja wersji Python

**Windows:**

```cmd
python --version
```

**Linux/Mac:**

```bash
python3 --version
```

**Oczekiwany wynik:**

```
Python 3.9.x  (lub wyzsza wersja 3.x)
```

#### Instalacja Python

**Windows:**

1. Pobierz instalator ze strony: https://www.python.org/downloads/
2. Uruchom instalator
3. ✅ **WAZNE:** Zaznacz "Add Python to PATH"
4. Wybierz "Install Now"

**Linux (Ubuntu/Debian):**

```bash
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv
```

**Linux (Fedora/RHEL):**

```bash
sudo dnf install python3 python3-pip
```

**macOS:**

```bash
# Przez Homebrew (zalecane)
brew install python3

# Lub pobierz instalator z python.org
```

### pip (menadzer pakietow Python)

#### Wymagana wersja

- **Minimalna:** pip 21.0
- **Zalecana:** najnowsza wersja

#### Weryfikacja pip

```bash
pip --version
# lub
python -m pip --version
```

#### Aktualizacja pip

**Windows:**

```cmd
python -m pip install --upgrade pip
```

**Linux/Mac:**

```bash
python3 -m pip install --upgrade pip
```

---

## Biblioteki Python

### Wymagane biblioteki

Wszystkie biblioteki sa automatycznie instalowane przez `setup.bat` / `setup.sh` lub recznie przez `requirements.txt`.

#### 1. NumPy

**Wersja:** >= 1.24.0, < 2.0.0

**Opis:** Biblioteka do obliczen numerycznych, operacji na macierzach i tablicach.

**Zastosowanie w projekcie:**

- Operacje na tablicach bitow
- Obliczenia modulacji
- Generowanie szumu
- Przetwarzanie sygnalow

**Instalacja:**

```bash
pip install "numpy>=1.24.0,<2.0.0"
```

**Weryfikacja:**

```python
import numpy as np
print(np.__version__)  # Powinno wyswietlic np. 1.26.4
```

#### 2. SciPy

**Wersja:** >= 1.10.0, < 2.0.0

**Opis:** Biblioteka do zaawansowanych obliczen naukowych i inzynierskich.

**Zastosowanie w projekcie:**

- Funkcje specjalne (erfc dla BER)
- Przetwarzanie sygnalow
- Statystyka i rozklady prawdopodobienstwa

**Instalacja:**

```bash
pip install "scipy>=1.10.0,<2.0.0"
```

**Weryfikacja:**

```python
import scipy
print(scipy.__version__)  # Powinno wyswietlic np. 1.11.4
```

#### 3. Matplotlib

**Wersja:** >= 3.7.0, < 4.0.0

**Opis:** Biblioteka do tworzenia wykresow i wizualizacji.

**Zastosowanie w projekcie:**

- Wykresy BER vs Eb/N0
- Diagramy konstelacji
- Wizualizacja wynikow

**Instalacja:**

```bash
pip install "matplotlib>=3.7.0,<4.0.0"
```

**Weryfikacja:**

```python
import matplotlib
print(matplotlib.__version__)  # Powinno wyswietlic np. 3.8.2
```

### Plik requirements.txt

Wszystkie zaleznosci sa zdefiniowane w pliku `requirements.txt`:

```txt
# ModulationPSKProject Dependencies
# Version: 1.4.0
# Python 3.8+

# Core numerical computing
numpy>=1.24.0,<2.0.0

# Scientific computing and signal processing
scipy>=1.10.0,<2.0.0

# Plotting and visualization
matplotlib>=3.7.0,<4.0.0
```

### Instalacja wszystkich zaleznosci

```bash
pip install -r requirements.txt
```

---

## Srodowisko wirtualne

### Dlaczego srodowisko wirtualne?

Srodowisko wirtualne (venv) izoluje zaleznosci projektu od systemowego Python. Zalety:

✅ Brak konfliktow z innymi projektami  
✅ Latwiejsze zarzadzanie wersjami bibliotek  
✅ Mozliwosc tworzenia identycznych srodowisk na roznych maszynach  
✅ Bezpieczenstwo systemowego Python

### Tworzenie srodowiska wirtualnego

#### Automatycznie (zalecane)

**Windows:**

```cmd
setup.bat
```

**Linux/Mac:**

```bash
chmod +x setup.sh
./setup.sh
```

#### Recznie

**Windows:**

```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**Linux/Mac:**

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Aktywacja srodowiska wirtualnego

#### Windows

**CMD:**

```cmd
venv\Scripts\activate.bat
```

**PowerShell:**

```powershell
venv\Scripts\Activate.ps1
```

**Git Bash:**

```bash
source venv/Scripts/activate
```

Po aktywacji zobaczysz `(venv)` przed promptem:

```
(venv) C:\Projects\ModulationPSKProject>
```

#### Linux/Mac

```bash
source venv/bin/activate
```

Po aktywacji zobaczysz `(venv)` przed promptem:

```
(venv) user@computer:~/ModulationPSKProject$
```

### Dezaktywacja srodowiska wirtualnego

Na wszystkich systemach:

```bash
deactivate
```

### Sprawdzanie aktywnego srodowiska

**Windows:**

```cmd
where python
```

**Linux/Mac:**

```bash
which python
```

Jesli srodowisko jest aktywne, sciezka powinna wskazywac na `venv/`:

```
/path/to/project/venv/bin/python
```

---

## Konfiguracja srodowiska

### Zmienne srodowiskowe (opcjonalne)

Dla zaawansowanych uzytkownikow mozna skonfigurowac zmienne srodowiskowe:

#### Windows

```cmd
set PYTHONPATH=%PYTHONPATH%;C:\path\to\ModulationPSKProject\src
```

Lub na stale przez System Properties → Environment Variables.

#### Linux/Mac

```bash
export PYTHONPATH=$PYTHONPATH:/path/to/ModulationPSKProject/src
```

Mozna dodac do `~/.bashrc` lub `~/.zshrc` dla stalej konfiguracji.

### Konfiguracja IDE

#### PyCharm

1. Otworz projekt
2. File → Settings → Project → Python Interpreter
3. Wybierz srodowisko wirtualne: `venv/bin/python` (Linux/Mac) lub `venv\Scripts\python.exe` (Windows)

#### Visual Studio Code

1. Otworz projekt
2. Ctrl+Shift+P → "Python: Select Interpreter"
3. Wybierz srodowisko wirtualne: `./venv/bin/python`

#### Jupyter Notebook (opcjonalnie)

```bash
pip install jupyter
python -m ipykernel install --user --name=venv --display-name="ModulationPSK"
```

---

## Weryfikacja instalacji

### Test kompletnej instalacji

Uzyj dostarczonego skryptu testowego (jesli dostepny):

```bash
python test_environment.py
```

### Test reczny

#### Test 1: Import modulow

```python
# test_imports.py
import sys
print(f"Python version: {sys.version}")

import numpy as np
print(f"NumPy version: {np.__version__}")

import scipy
print(f"SciPy version: {scipy.__version__}")

import matplotlib
print(f"Matplotlib version: {matplotlib.__version__}")

print("\nAll imports successful!")
```

Uruchom:

```bash
python test_imports.py
```

#### Test 2: Podstawowa funkcjonalnosc

```python
# test_basic.py
import numpy as np
from scipy.special import erfc
import matplotlib.pyplot as plt

# Test NumPy
arr = np.array([1, 2, 3])
print(f"NumPy test: {np.sum(arr)} (should be 6)")

# Test SciPy
result = erfc(0)
print(f"SciPy test: erfc(0) = {result} (should be 1.0)")

# Test Matplotlib
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 2, 3])
plt.close(fig)
print("Matplotlib test: OK")

print("\nAll tests passed!")
```

#### Test 3: Import modulow projektu

```python
# test_project.py
import sys
sys.path.insert(0, 'src')

from GetBytes import gen_bites
from Modulator import bpsk_modulation
from AddAWGNNoise import add_awgn_noise

# Test podstawowy
bits = gen_bites(10)
print(f"Generated {len(bits)} bits")

symbols = bpsk_modulation(bits)
print(f"Modulated to {len(symbols)} symbols")

noisy = add_awgn_noise(symbols, 10.0)
print(f"Added AWGN noise")

print("\nProject modules work correctly!")
```

---

## Wymagania opcjonalne

### Dla rozwoju projektu

Jesli planujesz rozwijac projekt, przyda sie:

```bash
# Narzedzia developerskie
pip install pytest         # Testowanie
pip install black          # Formatowanie kodu
pip install pylint         # Analiza kodu
pip install ipython        # Interaktywna konsola

# Dodatkowe biblioteki
pip install seaborn        # Zaawansowane wykresy
pip install pandas         # Analiza danych
pip install jupyter        # Notebooki
```

### Dla lepszej wydajnosci

```bash
# Akceleracja obliczen numerycznych (opcjonalnie)
pip install numba          # JIT compilation dla NumPy
```

**Uwaga:** Numba wymaga dodatkowej konfiguracji i nie jest wymagana do podstawowego dzialania projektu.

---

## Typowe problemy

### Problem: "python" nie jest rozpoznawany

**Rozwiazanie (Windows):**

1. Zainstaluj Python ponownie z opcja "Add to PATH"
2. Lub uzyj `py` zamiast `python`:
   ```cmd
   py --version
   py -m venv venv
   ```

**Rozwiazanie (Linux/Mac):**
Uzyj `python3` zamiast `python`:

```bash
python3 --version
```

### Problem: Blad przy tworzeniu venv

**Rozwiazanie (Linux):**

```bash
sudo apt-get install python3-venv
```

### Problem: Blad przy instalacji NumPy/SciPy

**Rozwiazanie (Windows):**
Zainstaluj Microsoft Visual C++ Build Tools.

**Rozwiazanie (Linux):**

```bash
# Ubuntu/Debian
sudo apt-get install python3-dev build-essential

# Fedora/RHEL
sudo dnf install python3-devel gcc
```

### Problem: Matplotlib nie wyswietla wykresow

**Rozwiazanie:**

```python
import matplotlib
matplotlib.use('TkAgg')  # Lub 'Qt5Agg'
import matplotlib.pyplot as plt
```

---

## Podsumowanie

### Checklist instalacji

- [ ] Python 3.8+ zainstalowany
- [ ] pip dziala poprawnie
- [ ] Utworzono srodowisko wirtualne
- [ ] Zainstalowano NumPy, SciPy, Matplotlib
- [ ] Testy importu przeszly pomyslnie
- [ ] Moduly projektu importuja sie poprawnie

### Kolejny krok

Po spelnieniu wszystkich wymagan, przejdz do:

- [Instrukcja instalacji](installation.md) - szczegolowe kroki instalacji
- [Glowny README](../README.md) - szybki start i przyklady

---

**Ostatnia aktualizacja:** 2025-10-22  
**Wersja dokumentu:** 1.4.0
