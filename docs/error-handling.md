# Obsluga bledow

## Wersja: 1.4.0

Kompletny przewodnik po bledach, problemach i ich rozwiazaniach w projekcie ModulationPSKProject.

---

## Spis tresci

1. [Bledy instalacji](#bledy-instalacji)
2. [Bledy importu](#bledy-importu)
3. [Bledy wykonania](#bledy-wykonania)
4. [Bledy obliczen](#bledy-obliczen)
5. [Problemy z wydajnoscia](#problemy-z-wydajnoscia)
6. [Diagnostyka](#diagnostyka)
7. [FAQ](#faq)

---

## Bledy instalacji

### ERROR: Python nie jest rozpoznawany

**Komunikat:**

```
'python' is not recognized as an internal or external command
```

**Przyczyna:**
Python nie jest dodany do PATH lub nie jest zainstalowany.

**Rozwiazanie Windows:**

1. Zainstaluj Python ponownie z opcja "Add Python to PATH"
2. Lub dodaj recznie do PATH:
   ```
   C:\Users\[User]\AppData\Local\Programs\Python\Python3X\
   C:\Users\[User]\AppData\Local\Programs\Python\Python3X\Scripts\
   ```
3. Lub uzyj `py` zamiast `python`:
   ```cmd
   py --version
   py -m pip install -r requirements.txt
   ```

**Rozwiazanie Linux/Mac:**
Uzyj `python3` zamiast `python`:

```bash
python3 --version
python3 -m venv venv
```

---

### ERROR: Failed to create virtual environment

**Komunikat:**

```
Error: Command '['venv/bin/python', '-Im', 'ensurepip']' returned non-zero exit status 1
```

**Przyczyna:**
Brak pakietu python3-venv (Linux) lub uszkodzony Python.

**Rozwiazanie Ubuntu/Debian:**

```bash
sudo apt-get update
sudo apt-get install python3-venv python3-pip
```

**Rozwiazanie Fedora/RHEL:**

```bash
sudo dnf install python3-virtualenv
```

**Rozwiazanie Windows:**
Przeinstaluj Python z oficjalnej strony.

---

### ERROR: Permission denied (Linux/Mac)

**Komunikat:**

```bash
./setup.sh: Permission denied
```

**Przyczyna:**
Brak uprawnien wykonywania skryptu.

**Rozwiazanie:**

```bash
chmod +x setup.sh
./setup.sh
```

---

### ERROR: Cannot install NumPy/SciPy

**Komunikat:**

```
error: Microsoft Visual C++ 14.0 or greater is required
```

**Przyczyna (Windows):**
Brak kompilatora C++.

**Rozwiazanie Windows:**
Zainstaluj Microsoft Visual C++ Build Tools:

1. Pobierz: https://visualstudio.microsoft.com/visual-cpp-build-tools/
2. Zainstaluj "Desktop development with C++"
3. Uruchom ponownie instalacje:
   ```cmd
   pip install numpy scipy
   ```

**Komunikat (Linux):**

```
fatal error: Python.h: No such file or directory
```

**Rozwiazanie Ubuntu/Debian:**

```bash
sudo apt-get install python3-dev build-essential gfortran
sudo apt-get install libopenblas-dev liblapack-dev
pip install numpy scipy
```

**Rozwiazanie Fedora/RHEL:**

```bash
sudo dnf install python3-devel gcc gcc-gfortran
sudo dnf install openblas-devel lapack-devel
pip install numpy scipy
```

---

### ERROR: pip not found

**Komunikat:**

```
bash: pip: command not found
```

**Przyczyna:**
pip nie jest zainstalowany lub nie jest w PATH.

**Rozwiazanie:**

```bash
# Instalacja pip
python -m ensurepip --upgrade

# Lub uzyj:
python -m pip install [package]
```

---

### ERROR: setup.bat fails on Windows

**Komunikat:**

```
setup.bat is not recognized / Access denied
```

**Rozwiazanie:**

1. Uruchom CMD jako Administrator
2. Przejdz do katalogu projektu:
   ```cmd
   cd C:\path\to\ModulationPSKProject
   ```
3. Uruchom:
   ```cmd
   setup.bat
   ```

**Alternatywna metoda:**

```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## Bledy importu

### ModuleNotFoundError: No module named 'numpy'

**Komunikat:**

```python
ModuleNotFoundError: No module named 'numpy'
```

**Przyczyna:**

1. Srodowisko wirtualne nie jest aktywne
2. Biblioteka nie jest zainstalowana
3. Zla sciezka PYTHONPATH

**Rozwiazanie:**

**Krok 1: Aktywuj srodowisko**

```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

**Krok 2: Sprawdz instalacje**

```bash
pip list | grep numpy
```

**Krok 3: Zainstaluj jesli brak**

```bash
pip install numpy
# lub
pip install -r requirements.txt
```

**Krok 4: Weryfikacja**

```python
python -c "import numpy; print(numpy.__version__)"
```

---

### ModuleNotFoundError: No module named 'GetBytes'

**Komunikat:**

```python
ModuleNotFoundError: No module named 'GetBytes'
```

**Przyczyna:**
Uruchamiasz skrypt z zlego katalogu lub PYTHONPATH nie jest ustawiony.

**Rozwiazanie:**

**Metoda 1: Uruchom z wlasciwego katalogu**

```bash
cd src
python main.py
```

**Metoda 2: Uruchom jako modul**

```bash
# Z glownego katalogu projektu
python -m src.main
```

**Metoda 3: Dodaj katalog do PYTHONPATH**

```python
# Na poczatku main.py
import sys
sys.path.insert(0, '.')
# lub
sys.path.append('../src')
```

---

### ImportError: DLL load failed (Windows)

**Komunikat:**

```python
ImportError: DLL load failed while importing _multiarray_umath
```

**Przyczyna:**
Brak Visual C++ Redistributable lub konflikt wersji.

**Rozwiazanie:**

1. Zainstaluj Microsoft Visual C++ Redistributable:
   - https://aka.ms/vs/17/release/vc_redist.x64.exe
2. Przeinstaluj NumPy:
   ```cmd
   pip uninstall numpy
   pip install numpy
   ```

---

### ImportError: cannot import name 'erfc'

**Komunikat:**

```python
ImportError: cannot import name 'erfc' from 'scipy.special'
```

**Przyczyna:**
Stara wersja SciPy.

**Rozwiazanie:**

```bash
pip install --upgrade scipy
```

---

## Bledy wykonania

### RuntimeError: BLAS/LAPACK libraries not found

**Komunikat:**

```
RuntimeError: BLAS/LAPACK libraries not found
```

**Przyczyna:**
Brak bibliotek algebry liniowej.

**Rozwiazanie Ubuntu/Debian:**

```bash
sudo apt-get install libopenblas-dev liblapack-dev
pip install --force-reinstall numpy scipy
```

**Rozwiazanie Fedora/RHEL:**

```bash
sudo dnf install openblas-devel lapack-devel
pip install --force-reinstall numpy scipy
```

**Rozwiazanie macOS:**

```bash
brew install openblas lapack
pip install --force-reinstall numpy scipy
```

---

### ValueError: invalid value in multiply

**Komunikat:**

```python
ValueError: invalid value encountered in multiply
```

**Przyczyna:**
Operacja na NaN lub Inf.

**Rozwiazanie:**

**Sprawdz dane wejsciowe:**

```python
import numpy as np

# Sprawdz czy sa NaN
if np.isnan(symbols).any():
    print("WARNING: NaN detected in symbols")

# Sprawdz czy sa Inf
if np.isinf(symbols).any():
    print("WARNING: Inf detected in symbols")
```

**Debug:**

```python
# Dodaj walidacje
def validate_symbols(symbols):
    if np.isnan(symbols).any():
        raise ValueError("NaN values in symbols")
    if np.isinf(symbols).any():
        raise ValueError("Inf values in symbols")
    return True
```

---

### MemoryError: Unable to allocate array

**Komunikat:**

```python
MemoryError: Unable to allocate 7.45 GiB for an array
```

**Przyczyna:**
Zbyt duza tablica (za duzo bitow/symboli).

**Rozwiazanie:**

**Zmniejsz rozmiar symulacji:**

```python
# Zamiast:
n_bits = 10000000  # 10 milionow

# Uzyj:
n_bits = 100000    # 100 tysiecy
```

**Podziel na mniejsze bloki:**

```python
def simulate_large(n_bits_total, block_size=10000):
    total_errors = 0
    n_blocks = n_bits_total // block_size

    for i in range(n_blocks):
        bits = gen_bites(block_size)
        # ... symulacja ...
        total_errors += errors

    ber = total_errors / n_bits_total
    return ber
```

---

### RuntimeWarning: divide by zero

**Komunikat:**

```python
RuntimeWarning: divide by zero encountered in log10
```

**Przyczyna:**
BER = 0 i probujesz obliczyc log10(0).

**Rozwiazanie:**

**Dodaj minimalna wartosc:**

```python
ber = max(ber, 1e-10)  # Minimum BER
ber_db = 10 * np.log10(ber)
```

**Lub uzyj wartosc warunkowa:**

```python
if ber > 0:
    ber_db = 10 * np.log10(ber)
else:
    ber_db = -100  # Bardzo maly BER
```

---

## Bledy obliczen

### BER = 0.5 dla wszystkich Eb/N0

**Problem:**
BER zawsze wynosi 0.5 (losowe odgadywanie).

**Przyczyna:**

1. Blad w demodulatorze
2. Zle mapowanie bitow na symbole
3. Problem z decyzja progowa

**Rozwiazanie:**

**Sprawdz demodulator BPSK:**

```python
# Poprawna implementacja
def bpsk_demodulation(received_symbols):
    # Re(symbol) > 0 → bit = 0
    # Re(symbol) < 0 → bit = 1
    decoded_bits = (received_symbols.real < 0).astype(int)
    return decoded_bits
```

**Test bez szumu:**

```python
bits = np.array([0, 1, 0, 1])
symbols = bpsk_modulation(bits)
decoded = bpsk_demodulation(symbols)
assert np.array_equal(bits, decoded), "Demodulation error!"
```

---

### BER nie maleje wraz z Eb/N0

**Problem:**
BER nie poprawia sie przy wyzszym Eb/N0.

**Przyczyna:**

1. Blad w obliczaniu mocy szumu
2. Zle skalowanie symboli
3. Problem z energia bitu

**Rozwiazanie:**

**Sprawdz AddAWGNNoise.py:**

```python
def add_awgn_noise(symbols, eb_n0_db):
    # Konwersja z dB do liniowej
    eb_n0 = 10 ** (eb_n0_db / 10.0)  # WAZNE: /10.0 nie /20.0!

    # Energia bitu (znormalizowana)
    eb = 1.0

    # Gestosc mocy szumu
    n0 = eb / eb_n0

    # Odchylenie standardowe szumu
    sigma = np.sqrt(n0 / 2)  # WAZNE: /2 dla I i Q

    # ... reszta kodu ...
```

---

### Konstelacja wyglada zle

**Problem:**
Punkty konstelacji sa w zlych miejscach.

**Przyczyna:**
Blad w modulatorze.

**Rozwiazanie QPSK:**

```python
def qpsk_modulation(bits):
    # Prawidlowe mapowanie
    # 00 → (1+j)/sqrt(2)   (45°)
    # 01 → (-1+j)/sqrt(2)  (135°)
    # 11 → (-1-j)/sqrt(2)  (225°)
    # 10 → (1-j)/sqrt(2)   (315°)

    n_symbols = len(bits) // 2
    symbols = np.zeros(n_symbols, dtype=complex)

    for i in range(n_symbols):
        bit_pair = bits[2*i:2*i+2]

        if np.array_equal(bit_pair, [0, 0]):
            symbols[i] = (1 + 1j) / np.sqrt(2)
        elif np.array_equal(bit_pair, [0, 1]):
            symbols[i] = (-1 + 1j) / np.sqrt(2)
        elif np.array_equal(bit_pair, [1, 1]):
            symbols[i] = (-1 - 1j) / np.sqrt(2)
        elif np.array_equal(bit_pair, [1, 0]):
            symbols[i] = (1 - 1j) / np.sqrt(2)

    return symbols
```

---

## Problemy z wydajnoscia

### Symulacja trwa bardzo dlugo

**Problem:**
Symulacja dla duzej liczby bitow trwa godzinami.

**Rozwiazanie:**

**Optymalizacja 1: Wektoryzacja**

```python
# ZLE - petla
for i in range(len(bits)):
    symbols[i] = 1 - 2 * bits[i]

# DOBRE - wektoryzacja
symbols = 1 - 2 * bits
```

**Optymalizacja 2: Zmniejsz liczbe bitow**

```python
# Zamiast 10 milionow:
n_bits = 10000000

# Uzyj:
n_bits = 100000  # Nadal dobre statystyki
```

**Optymalizacja 3: Parallel processing**

```python
from multiprocessing import Pool

def simulate_one_eb_n0(eb_n0):
    # ... symulacja ...
    return ber

# Parallel
with Pool() as pool:
    ber_values = pool.map(simulate_one_eb_n0, eb_n0_range)
```

---

### Matplotlib powoli generuje wykresy

**Problem:**
Generowanie wykresow trwa bardzo dlugo.

**Rozwiazanie:**

**Uzyj backend bez GUI:**

```python
import matplotlib
matplotlib.use('Agg')  # Backend bez wyswietlania
import matplotlib.pyplot as plt
```

**Zmniejsz DPI:**

```python
plt.savefig('plot.png', dpi=150)  # Zamiast 300
```

---

## Diagnostyka

### Narzedzia diagnostyczne

#### 1. Sprawdzenie srodowiska

```bash
# Sprawdz Python
python --version
which python  # Linux/Mac
where python  # Windows

# Sprawdz pip
pip --version
pip list

# Sprawdz venv
echo $VIRTUAL_ENV  # Linux/Mac - powinno pokazac sciezke
echo %VIRTUAL_ENV%  # Windows
```

#### 2. Sprawdzenie bibliotek

```python
# test_libraries.py
import sys
print(f"Python: {sys.version}")

import numpy as np
print(f"NumPy: {np.__version__}")

import scipy
print(f"SciPy: {scipy.__version__}")

import matplotlib
print(f"Matplotlib: {matplotlib.__version__}")

print("\nAll libraries OK!")
```

#### 3. Sprawdzenie modulow projektu

```python
# test_modules.py
import sys
sys.path.insert(0, 'src')

try:
    from GetBytes import gen_bites
    print("✓ GetBytes.py")
except ImportError as e:
    print(f"✗ GetBytes.py: {e}")

try:
    from Modulator import bpsk_modulation
    print("✓ Modulator.py")
except ImportError as e:
    print(f"✗ Modulator.py: {e}")

# ... itd dla wszystkich modulow
```

#### 4. Test funkcjonalny

```python
# test_functional.py
import sys
sys.path.insert(0, 'src')
import numpy as np
from GetBytes import gen_bites
from Modulator import bpsk_modulation
from Demodulator import bpsk_demodulation

# Test bez szumu
print("Testing BPSK without noise...")
bits = np.array([0, 1, 0, 1, 0, 1])
symbols = bpsk_modulation(bits)
decoded = bpsk_demodulation(symbols)

if np.array_equal(bits, decoded):
    print("✓ BPSK test PASSED")
else:
    print("✗ BPSK test FAILED")
    print(f"Original: {bits}")
    print(f"Decoded:  {decoded}")
```

---

## FAQ

### Q: Jak sprawdzic czy venv jest aktywne?

**A:** Sprawdz prompt terminala:

```
(venv) user@computer:~/project$  # Aktywne
user@computer:~/project$         # Nieaktywne
```

Lub sprawdz sciezke Python:

```bash
which python  # Linux/Mac
where python  # Windows
```

Powinno pokazywac `venv/bin/python` lub `venv\Scripts\python.exe`.

---

### Q: Jak zaktualizowac biblioteki?

**A:**

```bash
pip install --upgrade numpy scipy matplotlib
# lub
pip install --upgrade -r requirements.txt
```

---

### Q: Jak usunac srodowisko i zaczac od nowa?

**A:**

```bash
# Dezaktywuj
deactivate

# Usun
rm -rf venv  # Linux/Mac
rmdir /s venv  # Windows

# Utworz nowe
python3 -m venv venv  # Linux/Mac
python -m venv venv   # Windows

# Aktywuj i zainstaluj
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

---

### Q: Dlaczego wykresy nie wyswietlaja sie?

**A:**

1. **Backend problem:**

   ```python
   import matplotlib
   matplotlib.use('TkAgg')  # Sprobuj roznych backend
   import matplotlib.pyplot as plt
   ```

2. **Brak plt.show():**

   ```python
   plt.plot([1, 2, 3], [1, 2, 3])
   plt.show()  # Dodaj to!
   ```

3. **Zapisz do pliku:**
   ```python
   plt.savefig('plot.png')
   ```

---

### Q: Jak zmienic liczbe bitow w symulacji?

**A:** W `src/main.py` zmien:

```python
n_bits = 10000  # Zmien na dowolna liczbe
```

---

### Q: Jak dodac nowa modulacje?

**A:**

1. Dodaj funkcje w `src/Modulator.py`:

   ```python
   def new_modulation(bits):
       # Implementacja
       return symbols
   ```

2. Dodaj demodulator w `src/Demodulator.py`:

   ```python
   def new_demodulation(symbols):
       # Implementacja
       return bits
   ```

3. Dodaj w `src/main.py`:
   ```python
   # W funkcji compare_modulations()
   # Dodaj wywolanie nowej modulacji
   ```

---

### Q: Co robic gdy symulacja zwraca BER = 0?

**A:**

1. Zwieksz Eb/N0 (np. do 15-20 dB)
2. Zmniejsz liczbe bitow (lepsze statystyki dla malego BER)
3. Sprawdz czy demodulator dziala poprawnie

---

### Q: Jak zmienic zakres Eb/N0?

**A:** W `src/main.py`:

```python
# Zamiast:
eb_n0_range = range(0, 15)

# Uzyj:
eb_n0_range = range(-5, 20)  # Od -5 do 19 dB
# lub
eb_n0_range = np.arange(0, 15, 0.5)  # Co 0.5 dB
```

---

## Logi i debugging

### Wlaczenie logow

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

# Uzycie
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
```

### Profilowanie wydajnosci

```python
import time

start = time.time()
# ... kod do profilowania ...
end = time.time()
print(f"Time: {end - start:.2f} seconds")
```

Lub uzyj `cProfile`:

```bash
python -m cProfile -s cumtime main.py
```

---

## Podsumowanie

### Checklist diagnostyki

Gdy napotkasz problem:

- [ ] Sprawdz czy venv jest aktywne
- [ ] Sprawdz wersje Python (>=3.8)
- [ ] Sprawdz wersje bibliotek (pip list)
- [ ] Sprawdz czy jestes we wlasciwym katalogu
- [ ] Przeczytaj komunikat bledu dokladnie
- [ ] Sprawdz logi / dodaj printy
- [ ] Przetestuj na mniejszym przykladzie
- [ ] Przeszukaj ten dokument

### Gdzie szukac pomocy

1. Ten dokument
2. [Wymagania i srodowisko](requirements-and-environment.md)
3. [Instrukcja instalacji](installation.md)
4. Dokumentacja bibliotek (NumPy, SciPy, Matplotlib)

---

**Ostatnia aktualizacja:** 2025-10-22  
**Wersja dokumentu:** 1.4.0
