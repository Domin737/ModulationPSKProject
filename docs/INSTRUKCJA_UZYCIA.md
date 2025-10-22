# INSTRUKCJA UZYCIA - ModulationPSKProject

## Spis tresci
1. Wymagania
2. Instalacja
3. Uruchomienie
4. Przyklady uzycia
5. Interpretacja wynikow
6. Rozwiazywanie problemow

---

## 1. WYMAGANIA

### Wymagania systemowe:
- System operacyjny: Windows, Linux lub macOS
- Python 3.8 lub nowszy
- pip (menadzer pakietow Python)
- Minimum 2 GB RAM
- Minimum 100 MB miejsca na dysku

### Sprawdzenie wersji Python:

**Windows:**
```bash
python --version
```

**Linux/macOS:**
```bash
python3 --version
```

Powinnas zobaczyc: `Python 3.8.x` lub nowszy

---

## 2. INSTALACJA

### Metoda 1: Automatyczna (Zalecana)

**Krok 1:** Pobierz wszystkie pliki projektu do jednego katalogu

**Krok 2:** Otworz terminal/wiersz polecen w katalogu projektu

**Krok 3:** Utworz wirtualne srodowisko

**Windows:**
```bash
python -m venv venv
```

**Linux/macOS:**
```bash
python3 -m venv venv
```

**Krok 4:** Aktywuj wirtualne srodowisko

**Windows (CMD):**
```bash
venv\Scripts\activate
```

**Windows (PowerShell):**
```bash
venv\Scripts\Activate.ps1
```

**Linux/macOS:**
```bash
source venv/bin/activate
```

Po aktywacji zobaczysz `(venv)` przed promptem.

**Krok 5:** Zainstaluj zaleznosci
```bash
pip install -r requirements.txt
```

### Metoda 2: Manualna instalacja bibliotek

Jesli nie masz pliku `requirements.txt`, zainstaluj recznie:

```bash
pip install numpy>=1.24.0
pip install scipy>=1.10.0
pip install matplotlib>=3.7.0
```

### Weryfikacja instalacji

Sprawdz czy wszystko zostalo zainstalowane:

```bash
pip list
```

Powinny byc widoczne:
- numpy (wersja >= 1.24.0)
- scipy (wersja >= 1.10.0)
- matplotlib (wersja >= 3.7.0)

---

## 3. URUCHOMIENIE

### 3.1 Glowna symulacja (Zalecane)

Aby uruchomic pelna symulacje wszystkich modulacji:

```bash
python main.py
```

**Co sie stanie:**
1. Program wykona symulacje dla BPSK, QPSK, 8-PSK i 16-QAM
2. Dla kazdej modulacji przejdzie przez zakres Eb/N0 od -2 do 12 dB
3. Obliczy BER dla kazdego punktu
4. Wygeneruje wykresy i zapisze je jako pliki PNG

**Czas wykonania:** 1-3 minuty (w zaleznosci od komputera)

**Wyjscie na ekran:**
```
======================================================================
                PSK & QAM MODULATION SIMULATION
======================================================================

Simulation parameters:
  Number of bits per simulation: 10000
  Eb/N0 range: [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] dB

======================================================================
Simulating BPSK
----------------------------------------------------------------------
BPSK     | Eb/N0 = -2 dB | BER = 0.156800
BPSK     | Eb/N0 = -1 dB | BER = 0.135600
...
BPSK     | Eb/N0 = 12 dB | BER = 0.000000

[podobnie dla QPSK, 8-PSK, 16-QAM]
...

======================================================================
Generating BER comparison plot...
======================================================================

Plot saved as: ber_comparison.png

======================================================================
Generating constellation diagrams...
======================================================================

Constellation plot saved as: bpsk_constellation.png
...

======================================================================
Simulation completed successfully!
======================================================================

Generated files:
  - ber_comparison.png
  - bpsk_constellation.png
  - qpsk_constellation.png
  - 8psk_constellation.png
  - 16qam_constellation.png
```

### 3.2 Test poszczegolnych modulow

Kazdy modul zawiera wbudowane testy. Mozesz je uruchomic osobno:

**Test generatora bitow:**
```bash
python GetBytes.py
```

**Test modulatorow:**
```bash
python Modulator.py
```

**Test szumu AWGN:**
```bash
python AddAWGNNoise.py
```

**Test kanalu transmisyjnego:**
```bash
python TransmissionChannel.py
```

**Test demodulatorow:**
```bash
python Demodulator.py
```

### 3.3 Wlasna symulacja (Zaawansowane)

Mozesz utworzyc wlasny skrypt:

```python
from GetBytes import gen_bites
from Modulator import bpsk_modulation
from TransmissionChannel import transmission_channel
from Demodulator import bpsk_demodulation
import numpy as np

# Parametry
n_bits = 1000
eb_n0_db = 10

# Symulacja
bits = gen_bites(n_bits)
symbols = bpsk_modulation(bits)
received = transmission_channel(symbols, eb_n0_db)
decoded = bpsk_demodulation(received)

# Wyniki
errors = np.sum(bits != decoded)
ber = errors / n_bits
print(f"BER = {ber:.6f}")
```

---

## 4. PRZYKLADY UZYCIA

### Przyklad 1: Podstawowa symulacja BPSK

```python
import numpy as np
from GetBytes import gen_bites
from Modulator import bpsk_modulation
from TransmissionChannel import transmission_channel
from Demodulator import bpsk_demodulation

# Wygeneruj 1000 bitow
bits = gen_bites(1000)
print(f"Wygenerowano {len(bits)} bitow")

# Modulacja BPSK
symbols = bpsk_modulation(bits)
print(f"Utworzono {len(symbols)} symboli")

# Transmisja przez kanal z Eb/N0 = 10 dB
received_symbols = transmission_channel(symbols, eb_n0_db=10)

# Demodulacja
decoded_bits = bpsk_demodulation(received_symbols)

# Oblicz BER
errors = np.sum(bits != decoded_bits)
ber = errors / len(bits)
print(f"BER = {ber:.6f}")
print(f"Liczba bledow: {errors}/{len(bits)}")
```

### Przyklad 2: Porownanie modulacji dla stalego Eb/N0

```python
from GetBytes import gen_bites
from Modulator import bpsk_modulation, qpsk_modulation, psk8_modulation
from TransmissionChannel import transmission_channel
from Demodulator import bpsk_demodulation, qpsk_demodulation, psk8_demodulation
import numpy as np

eb_n0_db = 8  # 8 dB

# BPSK
bits_bpsk = gen_bites(1000)
symbols = bpsk_modulation(bits_bpsk)
received = transmission_channel(symbols, eb_n0_db)
decoded = bpsk_demodulation(received)
ber_bpsk = np.sum(bits_bpsk != decoded) / len(bits_bpsk)

# QPSK (potrzebuje parzystej liczby bitow)
bits_qpsk = gen_bites(1000)
symbols = qpsk_modulation(bits_qpsk)
received = transmission_channel(symbols, eb_n0_db)
decoded = qpsk_demodulation(received)
ber_qpsk = np.sum(bits_qpsk != decoded) / len(bits_qpsk)

# 8-PSK (potrzebuje liczby bitow podzielnej przez 3)
bits_8psk = gen_bites(999)  # 999 = 3 * 333
symbols = psk8_modulation(bits_8psk)
received = transmission_channel(symbols, eb_n0_db)
decoded = psk8_demodulation(received)
ber_8psk = np.sum(bits_8psk != decoded) / len(bits_8psk)

print(f"Eb/N0 = {eb_n0_db} dB:")
print(f"  BPSK BER:  {ber_bpsk:.6f}")
print(f"  QPSK BER:  {ber_qpsk:.6f}")
print(f"  8-PSK BER: {ber_8psk:.6f}")
```

### Przyklad 3: Wykres BER dla jednej modulacji

```python
import numpy as np
import matplotlib.pyplot as plt
from GetBytes import gen_bites
from Modulator import bpsk_modulation
from TransmissionChannel import transmission_channel
from Demodulator import bpsk_demodulation

eb_n0_range = range(-2, 13)  # -2 dB do 12 dB
ber_values = []

for eb_n0_db in eb_n0_range:
    bits = gen_bites(10000)
    symbols = bpsk_modulation(bits)
    received = transmission_channel(symbols, eb_n0_db)
    decoded = bpsk_demodulation(received)
    
    ber = np.sum(bits != decoded) / len(bits)
    ber_values.append(ber)
    print(f"Eb/N0 = {eb_n0_db:2d} dB, BER = {ber:.6f}")

# Wykres
plt.figure(figsize=(10, 6))
plt.semilogy(eb_n0_range, ber_values, 'bo-', linewidth=2)
plt.grid(True, which='both')
plt.xlabel('Eb/N0 (dB)')
plt.ylabel('BER')
plt.title('BPSK Performance')
plt.savefig('my_bpsk_plot.png', dpi=300)
plt.show()
```

### Przyklad 4: Wizualizacja konstelacji

```python
import numpy as np
import matplotlib.pyplot as plt
from GetBytes import gen_bites
from Modulator import qpsk_modulation
from TransmissionChannel import transmission_channel

# Wygeneruj symbole
bits = gen_bites(2000)  # 1000 symboli QPSK
symbols = qpsk_modulation(bits)

# Dodaj szum
noisy_symbols = transmission_channel(symbols, eb_n0_db=10)

# Wykres
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Czysty sygnal
ax1.scatter(symbols.real, symbols.imag, alpha=0.6)
ax1.set_title('QPSK - Czysty sygnal')
ax1.set_xlabel('In-Phase')
ax1.set_ylabel('Quadrature')
ax1.grid(True)
ax1.axis('equal')

# Z szumem
ax2.scatter(noisy_symbols.real, noisy_symbols.imag, alpha=0.3, s=10)
ax2.set_title('QPSK - Eb/N0 = 10 dB')
ax2.set_xlabel('In-Phase')
ax2.set_ylabel('Quadrature')
ax2.grid(True)
ax2.axis('equal')

plt.tight_layout()
plt.savefig('my_qpsk_constellation.png', dpi=300)
plt.show()
```

---

## 5. INTERPRETACJA WYNIKOW

### 5.1 Wykres BER vs Eb/N0

**Co pokazuje:**
- Os X: Eb/N0 w decybelach (jakosc sygnalu)
- Os Y: BER w skali logarytmicznej

**Jak czytac:**
- Linia opadajaca w prawo = lepsze wyniki przy wyzszym Eb/N0
- Nizej polozony wykres = lepsza modulacja
- Stromszy spadek = szybsza poprawa przy zwiekszenium Eb/N0

**Przykladowa interpretacja:**
```
BER = 10^-3 (0.001) przy Eb/N0 = 8 dB dla BPSK
Oznacza to: 1 blad na 1000 bitow
```

### 5.2 Diagramy konstelacji

**Czysty sygnal:**
- Punkty skupione w konkretnych miejscach
- Reprezentuja idealne symbole modulacji

**Z szumem:**
- Punkty rozrzucone wokol idealnych pozycji
- Wiekszy rozrzut = wiekszy szum
- Jesli punkty nachodza na siebie = wiecej bledow

### 5.3 Typowe wartosci BER

**Bardzo dobre polaczenie:**
- BER < 10^-5 (mniej niz 1 blad na 100,000 bitow)

**Dobre polaczenie:**
- BER = 10^-3 do 10^-4 (1-10 bledow na 10,000 bitow)

**Slabe polaczenie:**
- BER > 10^-2 (wiecej niz 1 blad na 100 bitow)

**Krytyczne:**
- BER ≈ 0.5 (polowa bitow bledna - jak losowe zgadywanie)

### 5.4 Porownanie modulacji

**Oczekiwane wyniki:**

| Modulacja | Bity/symbol | Odpornosc na szum | Wydajnosc |
|-----------|-------------|-------------------|-----------|
| BPSK      | 1           | Najlepsza         | Najnizsza |
| QPSK      | 2           | Bardzo dobra      | Srednia   |
| 8-PSK     | 3           | Srednia           | Dobra     |
| 16-QAM    | 4           | Najgorsza         | Najwyzsza |

**Ogolna zasada:**
- Wieksza wydajnosc (wiecej bitow/symbol) = gorsza odpornosc na szum
- Trzeba wybrac kompromis pomiedzy wydajnoscia a niezawodnoscia

---

## 6. ROZWIAZYWANIE PROBLEMOW

### Problem 1: "python: command not found"

**Przyczyna:** Python nie jest zainstalowany lub nie jest w PATH

**Rozwiazanie:**
- Windows: Pobierz Python z python.org i zainstaluj
- Linux: `sudo apt install python3` (Ubuntu/Debian)
- macOS: `brew install python3`

### Problem 2: "ModuleNotFoundError: No module named 'numpy'"

**Przyczyna:** Biblioteka numpy nie jest zainstalowana

**Rozwiazanie:**
```bash
pip install numpy scipy matplotlib
```

### Problem 3: "ImportError: cannot import name 'gen_bites'"

**Przyczyna:** Pliki nie sa w tym samym katalogu

**Rozwiazanie:**
- Upewnij sie, ze wszystkie pliki .py sa w jednym katalogu
- Uruchamiaj skrypty z tego samego katalogu

### Problem 4: Wykresy nie wyswietlaja sie

**Przyczyna:** Brak GUI backend dla matplotlib

**Rozwiazanie:**
- Wykresy sa automatycznie zapisywane jako pliki PNG
- Sprawdz katalog projektu
- Alternatywnie: zainstaluj `python3-tk` (Linux)

### Problem 5: "ValueError: Number of bits must be even for QPSK"

**Przyczyna:** QPSK wymaga parzystej liczby bitow

**Rozwiazanie:**
```python
# ZLE:
bits = gen_bites(1001)  # Nieparzysta!

# DOBRZE:
bits = gen_bites(1000)  # Parzysta
```

### Problem 6: BER = 0.5 dla wszystkich Eb/N0

**Przyczyna:** Prawdopodobnie blad w demodulatorze lub niezgodnosc liczby bitow

**Rozwiazanie:**
- Sprawdz czy liczba bitow jest wielokrotnoscia bits_per_symbol
- Dla QPSK: n_bits % 2 == 0
- Dla 8-PSK: n_bits % 3 == 0
- Dla 16-QAM: n_bits % 4 == 0

### Problem 7: Bardzo wolne wykonanie

**Przyczyna:** Zbyt duza liczba bitow

**Rozwiazanie:**
- Zmniejsz `n_bits` w `main.py` z 10000 do 5000 lub 1000
- Zmniejsz zakres Eb/N0

### Problem 8: "Permission denied" przy aktywacji venv (Windows PowerShell)

**Przyczyna:** Polityka wykonywania skryptow

**Rozwiazanie:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Problem 9: Wyniki roznia sie przy kazdym uruchomieniu

**Przyczyna:** To normalne - szum jest losowy!

**Rozwiazanie (opcjonalne - dla powtarzalnosci):**
```python
import numpy as np
np.random.seed(42)  # Ustaw ziarno przed symulacja
```

---

## 7. DODATKOWE WSKAZOWKI

### 7.1 Optymalizacja czasu symulacji

Aby przyspieszyc symulacje:

1. Zmniejsz liczbe bitow:
   ```python
   n_bits = 5000  # zamiast 10000
   ```

2. Zmniejsz zakres Eb/N0:
   ```python
   eb_n0_range = range(0, 11)  # zamiast -2 do 12
   ```

3. Symuluj mniej modulacji:
   ```python
   modulations = ['BPSK', 'QPSK']  # zamiast wszystkich
   ```

### 7.2 Zapisywanie wynikow

Aby zapisac wyniki BER do pliku:

```python
import csv

# Po zakonczeniu symulacji
with open('results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Eb/N0 (dB)', 'BPSK BER', 'QPSK BER'])
    for i, eb_n0 in enumerate(eb_n0_range):
        writer.writerow([eb_n0, ber_bpsk[i], ber_qpsk[i]])
```

### 7.3 Wlasne parametry

Mozesz dostosowac parametry w `main.py`:

```python
# Zmien zakres Eb/N0
eb_n0_range = range(-5, 16)  # Szerszy zakres

# Zmien liczbe bitow
n_bits = 50000  # Wieksza dokladnosc (wolniej)

# Dodaj wiecej punktow danych
n_bits = 1000  # Szybsze, mniej dokladne
```

### 7.4 Debugowanie

Aby zobaczyc szczegolowe informacje:

```python
# Dodaj na poczatku skryptu
import numpy as np
np.set_printoptions(precision=4, suppress=True)

# Wyswietl przyklady symboli
print(f"Pierwsze 10 symboli: {symbols[:10]}")
print(f"Pierwsze 10 odebranych: {received_symbols[:10]}")
```

---

## 8. CZESTO ZADAWANE PYTANIA (FAQ)

**Q: Ile czasu trwa pelna symulacja?**
A: 1-3 minuty dla domyslnych parametrow (10000 bitow, 4 modulacje, 15 punktow Eb/N0).

**Q: Czy moge uruchomic na starszym Pythonie (3.6)?**
A: Technicznie tak, ale zalecamy Python 3.8+.

**Q: Czy wykresy sa automatycznie zapisywane?**
A: Tak, jako pliki PNG w katalogu projektu.

**Q: Czy moge zmienic kolory na wykresach?**
A: Tak, edytuj funkcje `plot_ber_curves()` w `main.py`.

**Q: Dlaczego QPSK ma podobne BER jak BPSK?**
A: To prawidlowe! QPSK ma taka sama odpornosc na szum jak BPSK przy tej samej energii na bit.

**Q: Co jesli chce symulowac tylko jedna modulacje?**
A: Uruchom:
```bash
python -c "from main import simulate_modulation; simulate_modulation('BPSK', range(-2,13), 10000)"
```

**Q: Jak sprawdzic czy instalacja jest poprawna?**
A: Uruchom testy:
```bash
python GetBytes.py
python Modulator.py
python Demodulator.py
```

---

## 9. KONTAKT I WSPARCIE

### Jesli masz problemy:

1. Sprawdz sekcje "Rozwiazywanie problemow" w tym dokumencie
2. Upewnij sie, ze wszystkie pliki sa w jednym katalogu
3. Sprawdz czy wirtualne srodowisko jest aktywne
4. Przeczytaj komunikaty bledow - czesto wskazuja przyczyne

### Przydatne zasoby:

- Dokumentacja NumPy: https://numpy.org/doc/
- Dokumentacja SciPy: https://scipy.org/
- Dokumentacja Matplotlib: https://matplotlib.org/
- Wikipedia - Phase-shift keying: https://en.wikipedia.org/wiki/Phase-shift_keying
- Wikipedia - QAM: https://en.wikipedia.org/wiki/Quadrature_amplitude_modulation

---

## 10. PODSUMOWANIE

### Podstawowe komendy:

```bash
# Instalacja
python -m venv venv
source venv/bin/activate  # (Linux/Mac) lub venv\Scripts\activate (Windows)
pip install -r requirements.txt

# Uruchomienie
python main.py

# Testy
python GetBytes.py
python Modulator.py
python Demodulator.py

# Dezaktywacja
deactivate
```

### Struktura plikow:

```
ModulationPSKProject/
├── GetBytes.py               # Generator bitow
├── Modulator.py              # Modulatory
├── AddAWGNNoise.py           # Generator szumu
├── TransmissionChannel.py    # Kanal
├── Demodulator.py            # Demodulatory
├── main.py                   # Program glowny
├── requirements.txt          # Zaleznosci
├── README.md                 # Dokumentacja
└── [wykresy].png            # Wygenerowane wykresy
```

### Oczekiwane wyniki:

Po uruchomieniu `python main.py` powinienes uzyskac:
- 5 plikow PNG z wykresami
- Wydruki BER dla roznych modulacji i Eb/N0
- Czas wykonania: 1-3 minuty

---

**Powodzenia w eksperymentach z modulacjami cyfrowymi!**

**Data:** 2025-10-22  
**Wersja:** 1.0  
**Status:** Gotowe do uzycia
