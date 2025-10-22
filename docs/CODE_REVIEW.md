# Code Review - Analiza istniejacego kodu

## Przeglad

Ten dokument zawiera szczegolowa analize kodu napisanego przez Twojego kolege oraz rekomendacje dotyczace dalszego rozwoju projektu.

## 1. GetBytes.py

### Kod:
```python
import numpy as np

def gen_bites(N_bits):
    return np.random.randint(0, 2, size=(N_bits))
```

### Analiza:
✓ **Mocne strony:**
- Prosty i czytelny
- Poprawnie uzywa NumPy do generowania losowych bitow
- Wydajny (operacje wektorowe)

⚠ **Uwagi:**
- Nazwa funkcji: "bites" powinno byc "bits" (blad ortograficzny, ale OK - zostawmy dla spojnosci z reszta projektu)
- Brak docstringa (dokumentacji funkcji)

✓ **Ocena:** BARDZO DOBRE - dziala poprawnie

### Rekomendacje:
```python
import numpy as np

def gen_bites(N_bits):
    """
    Generate random binary bits (0 or 1)
    
    Parameters:
    -----------
    N_bits : int
        Number of bits to generate
    
    Returns:
    --------
    numpy.ndarray
        Array of random bits (0s and 1s)
    
    Example:
    --------
    >>> bits = gen_bites(10)
    >>> print(bits)
    [1 0 1 1 0 1 0 0 1 1]
    """
    return np.random.randint(0, 2, size=(N_bits))
```

---

## 2. Modulator.py

### Kod:
```python
import numpy as np
from scipy.signal.windows import cosine
from GetBytes import *
import main

def bpsk_modulation(bits):
    symbols = 1-2 * bits
    return symbols.astype(complex)

x = gen_bites(10)
print(x)
print(bpsk_modulation(x))
```

### Analiza:

✓ **Mocne strony:**
- Poprawna implementacja modulacji BPSK
- Mapowanie: bit 0 → +1, bit 1 → -1 (standard)
- Zwraca typ complex (potrzebny do dalszego przetwarzania)

⚠ **Problemy i uwagi:**
1. **Import `from GetBytes import *`** - zle! Uzyj `from GetBytes import gen_bites`
2. **Import `import main`** - nie jest uzywany i moze spowodowac circular import
3. **Import `from scipy.signal.windows import cosine`** - nie jest uzywany
4. **Kod testowy na koncu** - powinien byc w bloku `if __name__ == "__main__":`
5. **Brak docstringa**
6. **Zakomentowany kod** - powinien byc usuniety lub wyjasniowany

❌ **Wazne:** Kod testowy zawsze powinien byc w bloku `if __name__ == "__main__":`, inaczej bedzie sie wykonywał przy kazdym imporcie!

✓ **Ocena:** DOBRE - poprawna logika, ale wymaga czyszczenia

### Rekomendowany kod:
```python
import numpy as np
from GetBytes import gen_bites

def bpsk_modulation(bits):
    """
    BPSK (Binary Phase-Shift Keying) modulation
    
    Maps bits to complex symbols:
    - bit 0 -> +1+0j
    - bit 1 -> -1+0j
    
    Parameters:
    -----------
    bits : numpy.ndarray
        Array of binary bits (0s and 1s)
    
    Returns:
    --------
    numpy.ndarray (complex)
        BPSK modulated symbols
    
    Example:
    --------
    >>> bits = np.array([0, 1, 0, 1])
    >>> symbols = bpsk_modulation(bits)
    >>> print(symbols)
    [ 1.+0.j -1.+0.j  1.+0.j -1.+0.j]
    """
    # Map: 0 -> +1, 1 -> -1
    symbols = 1 - 2 * bits
    return symbols.astype(complex)


# Test code - only runs when script is executed directly
if __name__ == "__main__":
    print("Testing BPSK modulation...")
    test_bits = gen_bites(10)
    print(f"Bits:    {test_bits}")
    
    test_symbols = bpsk_modulation(test_bits)
    print(f"Symbols: {test_symbols}")
```

---

## 3. AddAWGNNoise.py

### Kod:
```python
import numpy as np

def add_awgn_noise(bpskSymbols, Eb_No_db):
    Eb_no = 10**(Eb_No_db/ 10.0)
    Eb= 1.0
    N0 = Eb/Eb_no
    sigma = np.sqrt(N0/2)
    NSymbols = bpskSymbols.shape[0]
    
    noise_I =sigma * np.random.normal(0, 1, size=NSymbols)
    noise_Q =sigma * np.random.normal(0, 1, size=NSymbols)
    
    awgnNoise = noise_I + 1j * noise_Q
    recivedSymbols = bpskSymbols + awgnNoise
    return recivedSymbols
```

### Analiza:

✓✓✓ **DOSKONALY KOD!** 

✓ **Mocne strony:**
- Profesjonalna implementacja szumu AWGN
- Poprawne obliczenia Eb/N0, N0, sigma
- Generowanie szumu I i Q niezaleznie (poprawne dla sygnalu zespolonego)
- Dzialanie: szum gaussowski o odpowiedniej mocy
- Matematycznie poprawny

⚠ **Drobne uwagi:**
1. Nazwa parametru `bpskSymbols` - lepiej `symbols` (dziala dla kazdej modulacji, nie tylko BPSK)
2. Konwencja nazw: `Eb_no` → `eb_n0`, `NSymbols` → `n_symbols` (PEP 8)
3. Literowka: `recivedSymbols` → `received_symbols`
4. Brak docstringa

✓ **Ocena:** DOSKONALE - jedyny modul w pelni profesjonalny!

### Rekomendowany kod:
```python
import numpy as np

def add_awgn_noise(symbols, eb_n0_db):
    """
    Add AWGN (Additive White Gaussian Noise) to symbols
    
    Parameters:
    -----------
    symbols : numpy.ndarray (complex)
        Modulated symbols
    eb_n0_db : float
        Energy per bit to noise power spectral density ratio in dB
    
    Returns:
    --------
    numpy.ndarray (complex)
        Symbols with added AWGN noise
    
    Notes:
    ------
    - Assumes Eb = 1.0 (normalized energy per bit)
    - Generates complex Gaussian noise (I + jQ)
    - Noise power is calculated based on Eb/N0 ratio
    
    Example:
    --------
    >>> symbols = np.array([1.0, -1.0, 1.0], dtype=complex)
    >>> noisy = add_awgn_noise(symbols, eb_n0_db=10.0)
    """
    # Convert Eb/N0 from dB to linear scale
    eb_n0 = 10 ** (eb_n0_db / 10.0)
    
    # Normalized energy per bit
    eb = 1.0
    
    # Noise power spectral density
    n0 = eb / eb_n0
    
    # Standard deviation of noise (for I and Q components)
    sigma = np.sqrt(n0 / 2)
    
    # Number of symbols
    n_symbols = symbols.shape[0]
    
    # Generate Gaussian noise for I and Q components
    noise_i = sigma * np.random.normal(0, 1, size=n_symbols)
    noise_q = sigma * np.random.normal(0, 1, size=n_symbols)
    
    # Complex AWGN noise
    awgn_noise = noise_i + 1j * noise_q
    
    # Add noise to symbols
    received_symbols = symbols + awgn_noise
    
    return received_symbols
```

---

## 4. Demodulator.py

### Kod:
```python
from AddAWGNNoise import *
```

### Analiza:

❌ **PUSTY - wymaga implementacji**

⚠ **Problem:** Import `from AddAWGNNoise import *` nie jest potrzebny

---

## 5. TransmissionChannel.py

### Kod:
```python
# (pusty plik)
```

### Analiza:

❌ **PUSTY - wymaga implementacji**

---

## 6. main.py

### Kod:
```python
from GetBytes import *
import matplotlib.pyplot as plt

def make_disturbance(N_bits):
    pass # NULL

def main():
    bites = gen_bites(5)

if __name__ == "__main__":
    main()
```

### Analiza:

⚠ **SZKIELET - wymaga implementacji**

✓ **Mocne strony:**
- Poprawna struktura z `if __name__ == "__main__":`
- Import matplotlib przygotowany

⚠ **Uwagi:**
- Import `from GetBytes import *` - lepiej `from GetBytes import gen_bites`
- Funkcja `make_disturbance` - nie jest jasne co ma robic (nazwa mylaca)
- Brak wlasciwej logiki symulacji

---

## Podsumowanie

### Ocena ogolna projektu:

| Modul | Status | Ocena | Priorytet |
|-------|--------|-------|-----------|
| GetBytes.py | ✓ Gotowe | 8/10 | Niska |
| Modulator.py | ⚠ Czesc gotowa | 7/10 | Sredni |
| AddAWGNNoise.py | ✓✓ Doskonale | 10/10 | Niska |
| Demodulator.py | ❌ Pusty | 0/10 | **WYSOKI** |
| TransmissionChannel.py | ❌ Pusty | 0/10 | **WYSOKI** |
| main.py | ⚠ Szkielet | 2/10 | Wysoki |

### Postep: ~30%

### Co dziala dobrze:
1. ✓ Generator bitow
2. ✓ Modulacja BPSK
3. ✓✓✓ Generator szumu AWGN (DOSKONALY!)

### Najpilniejsze zadania:

#### Priorytet 1: TransmissionChannel.py
```python
def transmission_channel(symbols, eb_n0_db):
    """Symuluje kanal z szumem AWGN"""
    from AddAWGNNoise import add_awgn_noise
    return add_awgn_noise(symbols, eb_n0_db)
```

#### Priorytet 2: Demodulator.py (BPSK)
```python
def bpsk_demodulation(received_symbols):
    """Demodulacja BPSK: Re(symbol) > 0 -> 0, Re(symbol) < 0 -> 1"""
    bits = (received_symbols.real < 0).astype(int)
    return bits
```

#### Priorytet 3: main.py - podstawowa symulacja
- Petla po Eb/N0
- Obliczanie BER
- Wykres BER vs Eb/N0

---

## Najlepsze praktyki programowania (rekomendacje)

### 1. Imports
❌ ZLE:
```python
from GetBytes import *
```

✓ DOBRZE:
```python
from GetBytes import gen_bites
```

### 2. Naming Convention (PEP 8)
❌ ZLE:
```python
NSymbols = 10
Eb_No_db = 5.0
```

✓ DOBRZE:
```python
n_symbols = 10
eb_n0_db = 5.0
```

### 3. Docstrings
Kazda funkcja powinna miec dokumentacje:
```python
def function_name(param1, param2):
    """
    Brief description
    
    Parameters:
    -----------
    param1 : type
        Description
    
    Returns:
    --------
    type
        Description
    """
```

### 4. Test Code
Kod testowy zawsze w bloku:
```python
if __name__ == "__main__":
    # test code here
```

### 5. Comments
Komentarze po angielsku, bez polskich znakow:
```python
# Calculate noise power
n0 = eb / eb_n0

# NOT: Oblicz moc szumu (NO polish characters!)
```

---

## Plan naprawczy

### Krok 1: Czyszczenie istniejacego kodu (30 min)
1. Popraw imports w Modulator.py
2. Dodaj docstringi do wszystkich funkcji
3. Przenies kod testowy do `if __name__ == "__main__":`
4. Popraw nazwy zmiennych (PEP 8)

### Krok 2: Implementacja brakujacych modulow (2-3 godz)
1. TransmissionChannel.py
2. Demodulator.py (BPSK)
3. main.py (podstawowa symulacja)

### Krok 3: Testowanie (30 min)
1. Test bez szumu (BER = 0)
2. Test z wysokim szumem
3. Porownanie z teoria

### Krok 4: Rozszerzenia (3-4 godz)
1. QPSK
2. 8-PSK
3. QAM

---

## Wnioski

### Co zrobil dobrze Twoj kolega:
✓ Poprawna implementacja BPSK
✓ Profesjonalny kod generatora szumu
✓ Uzyl NumPy efektywnie
✓ Dobrze zrozumial problem

### Co wymaga poprawy:
⚠ Konwencje nazewnictwa (PEP 8)
⚠ Brak dokumentacji (docstrings)
⚠ Imports (unikac `import *`)
⚠ Kod testowy poza `if __name__`
⚠ Brakujace moduly

### Ogolna ocena:
**7/10** - Solidne podstawy, wymaga dopracowania i dokonczenia

Twoj kolega dobrze zrozumial teorie i zrobil solidny poczatek. Kod dziala, ale wymaga:
1. Profesjonalizacji (dokumentacja, konwencje)
2. Dokonczenia (brakujace moduly)
3. Testowania

---

**Nastepny krok:** Przejdz do implementacji brakujacych modulow uzywajac dokument PROJECT_ARCHITECTURE.md jako przewodnik.
