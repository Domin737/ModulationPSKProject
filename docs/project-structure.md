# Struktura projektu

## Wersja: 1.4.0

Szczegolowy opis struktury katalogowej i architektury projektu ModulationPSKProject.

---

## Spis tresci

1. [Struktura katalogowa](#struktura-katalogowa)
2. [Opis katalogow](#opis-katalogow)
3. [Opis plikow](#opis-plikow)
4. [Architektura systemu](#architektura-systemu)
5. [Przeplyw danych](#przeplyw-danych)
6. [Moduly projektu](#moduly-projektu)
7. [Zaleznosci](#zaleznosci)

---

## Struktura katalogowa

```
ModulationPSKProject/
│
├── docs/                           # Dokumentacja projektu
│   ├── index.md                   # Indeks dokumentacji
│   ├── requirements-and-environment.md  # Wymagania i srodowisko
│   ├── installation.md            # Instrukcja instalacji
│   ├── project-structure.md       # Struktura projektu (TEN PLIK)
│   ├── error-handling.md          # Obsluga bledow
│   └── code-documentation.md      # Dokumentacja kodu
│
├── results/                        # Wyniki symulacji
│   ├── .gitkeep                   # Placeholder dla Git
│   ├── README.md                  # Opis katalogu wynikow
│   ├── *.png                      # Wykresy BER
│   ├── *.pdf                      # Eksportowane wykresy
│   └── *.csv                      # Dane symulacji (opcjonalnie)
│
├── src/                            # Kod zrodlowy projektu
│   ├── GetBytes.py                # Generator losowych bitow
│   ├── Modulator.py               # Modulatory (BPSK, QPSK, 8-PSK, QAM)
│   ├── AddAWGNNoise.py            # Generator szumu AWGN
│   ├── TransmissionChannel.py     # Model kanalu transmisyjnego
│   ├── Demodulator.py             # Demodulatory
│   └── main.py                    # Program glowny - symulacje
│
├── venv/                           # Srodowisko wirtualne Python
│   ├── bin/  (Linux/Mac)          # Skrypty Python
│   ├── Scripts/  (Windows)        # Skrypty Python
│   ├── lib/                       # Biblioteki Python
│   └── ...                        # Inne pliki venv
│
├── .gitignore                      # Pliki ignorowane przez Git
├── .gitattributes                 # Atrybuty Git
├── requirements.txt               # Zaleznosci Python
├── setup.bat                      # Instalator Windows
├── setup.sh                       # Instalator Linux/Mac
└── README.md                      # Glowna dokumentacja projektu
```

---

## Opis katalogow

### 📁 `docs/`

**Przeznaczenie:** Dokumentacja projektu

**Zawartosc:**

- Instrukcje instalacji i konfiguracji
- Dokumentacja techniczna
- Przewodniki uzytkownika
- Opis architektury

**Wazne pliki:**

- `index.md` - punkt wyjscia dokumentacji
- `code-documentation.md` - szczegolowy opis kodu

**Kto korzysta:**

- Uzytkownicy poczatkujacy
- Programisci rozwijajacy projekt
- Dokumentacja referencyjna

---

### 📁 `results/`

**Przeznaczenie:** Przechowywanie wynikow symulacji

**Zawartosc:**

- Wykresy BER vs Eb/N0 (PNG, PDF)
- Diagramy konstelacji
- Dane surowe (CSV)
- Raporty symulacji

**Generowane przez:**

- `main.py` - podczas uruchamiania symulacji
- Funkcje plot\_\* z Matplotlib

**Struktura plikow:**

```
results/
├── bpsk_ber_curve.png          # Wykres BER dla BPSK
├── qpsk_ber_curve.png          # Wykres BER dla QPSK
├── comparison_all.png          # Porownanie wszystkich modulacji
├── bpsk_constellation.png      # Konstelacja BPSK
├── qpsk_constellation.png      # Konstelacja QPSK
├── 8psk_constellation.png      # Konstelacja 8-PSK
├── qam16_constellation.png     # Konstelacja 16-QAM
└── simulation_data.csv         # Dane surowe (opcjonalnie)
```

**Uwaga:** Katalog `results/` nie jest wersjonowany w Git (.gitignore).

---

### 📁 `src/`

**Przeznaczenie:** Kod zrodlowy projektu

**Zawartosc:**

- Moduly implementujace logike systemu
- Program glowny do uruchamiania symulacji
- Funkcje pomocnicze

**Organizacja:**

- Kazdy modul to osobny plik .py
- Funkcje powiazane w jednym pliku
- Clear separation of concerns

**Struktura logiczna:**

```
Generacja → Modulacja → Kanal → Demodulacja → Analiza
   ↓            ↓          ↓          ↓            ↓
GetBytes   Modulator   Trans-    Demodulator    main.py
                       Channel
```

---

### 📁 `venv/`

**Przeznaczenie:** Izolowane srodowisko Python

**Zawartosc:**

- Interpreter Python
- Zainstalowane biblioteki (NumPy, SciPy, Matplotlib)
- Skrypty aktywacji

**Lokalizacja binariow:**

- **Linux/Mac:** `venv/bin/python`
- **Windows:** `venv\Scripts\python.exe`

**Uwaga:** Katalog `venv/` nie jest wersjonowany w Git (.gitignore).

---

## Opis plikow

### Pliki konfiguracyjne

#### `requirements.txt`

**Przeznaczenie:** Lista zaleznosci Python

**Zawartosc:**

```txt
numpy>=1.24.0,<2.0.0
scipy>=1.10.0,<2.0.0
matplotlib>=3.7.0,<4.0.0
```

**Uzycie:**

```bash
pip install -r requirements.txt
```

---

#### `setup.bat` (Windows)

**Przeznaczenie:** Automatyczna instalacja na Windows

**Funkcje:**

1. Sprawdzenie Python
2. Utworzenie venv
3. Instalacja zaleznosci
4. Weryfikacja

**Uzycie:**

```cmd
setup.bat
```

---

#### `setup.sh` (Linux/Mac)

**Przeznaczenie:** Automatyczna instalacja na Linux/Mac

**Funkcje:**

1. Sprawdzenie Python3
2. Utworzenie venv
3. Instalacja zaleznosci
4. Weryfikacja

**Uzycie:**

```bash
chmod +x setup.sh
./setup.sh
```

---

#### `.gitignore`

**Przeznaczenie:** Okreslenie plikow ignorowanych przez Git

**Ignorowane:**

- `venv/` - srodowisko wirtualne
- `__pycache__/` - cache Python
- `*.pyc` - skompilowane pliki Python
- `results/*.png` - wykresy
- `.idea/` - pliki IDE

---

#### `README.md`

**Przeznaczenie:** Glowna dokumentacja projektu

**Zawartosc:**

- Krotki opis projektu
- Szybki start
- Przyklady uzycia
- Linki do pelnej dokumentacji

---

### Pliki kodu zrodlowego

#### `src/GetBytes.py`

**Funkcja:** Generator losowych bitow

**Glowna funkcja:**

```python
def gen_bites(N_bits):
    """Generate N random bits (0 or 1)"""
    return np.random.randint(0, 2, size=(N_bits))
```

**Zastosowanie:**

- Generowanie danych do transmisji
- Testy modulatorow
- Symulacje

**Zaleznosci:**

- NumPy

---

#### `src/Modulator.py`

**Funkcja:** Modulacja bitow na symbole

**Implementowane modulacje:**

1. **BPSK** - 1 bit/symbol
   ```python
   def bpsk_modulation(bits)
   ```
2. **QPSK** - 2 bity/symbol
   ```python
   def qpsk_modulation(bits)
   ```
3. **8-PSK** - 3 bity/symbol
   ```python
   def psk8_modulation(bits)
   ```
4. **QAM** - 4+ bity/symbol
   ```python
   def qam16_modulation(bits)
   def qam64_modulation(bits)
   ```

**Zaleznosci:**

- NumPy

**Wyjscie:**

- Tablica symboli zespolonych (complex128)

---

#### `src/AddAWGNNoise.py`

**Funkcja:** Dodawanie szumu AWGN

**Glowna funkcja:**

```python
def add_awgn_noise(symbols, eb_n0_db):
    """Add AWGN noise to symbols"""
    # Konwersja Eb/N0 z dB
    # Obliczenie mocy szumu
    # Generowanie szumu gaussowskiego (I+jQ)
    # Dodanie do symboli
    return received_symbols
```

**Parametry:**

- `symbols` - symbole modulowane (complex)
- `eb_n0_db` - stosunek Eb/N0 w dB

**Zaleznosci:**

- NumPy

**Teoria:**

- Model szumu AWGN (Additive White Gaussian Noise)
- Rozklad normalny dla I i Q

---

#### `src/TransmissionChannel.py`

**Funkcja:** Model kanalu transmisyjnego

**Glowna funkcja:**

```python
def transmission_channel(symbols, eb_n0_db):
    """Simulate transmission through AWGN channel"""
    return add_awgn_noise(symbols, eb_n0_db)
```

**Model:**

- Kanal AWGN (bez fedingu, bez przesuniec)
- Moze byc rozszerzony o:
  - Fading
  - Interferencje
  - Przesuniecia fazowe

**Zaleznosci:**

- `AddAWGNNoise.py`

---

#### `src/Demodulator.py`

**Funkcja:** Demodulacja symboli na bity

**Implementowane demodulatory:**

1. **BPSK**
   ```python
   def bpsk_demodulation(symbols)
   # Decyzja progowa: Re(symbol) > 0 → bit=0
   ```
2. **QPSK**
   ```python
   def qpsk_demodulation(symbols)
   # Detekcja kwadrantow
   ```
3. **8-PSK**
   ```python
   def psk8_demodulation(symbols)
   # Detekcja fazy (8 sektorow)
   ```
4. **QAM**
   ```python
   def qam16_demodulation(symbols)
   # Detekcja odleglosci minimalne
   ```

**Metody demodulacji:**

- Detekcja progowa (BPSK)
- Detekcja odleglosci (PSK, QAM)
- Maximum Likelihood

**Zaleznosci:**

- NumPy

---

#### `src/main.py`

**Funkcja:** Program glowny - symulacje i analiza

**Glowne funkcje:**

1. **Symulacja pojedynczej modulacji**

   ```python
   def simulate_modulation(mod_type, eb_n0_range, n_bits)
   ```

2. **Obliczanie BER**

   ```python
   def calculate_ber(original_bits, decoded_bits)
   ```

3. **Wykresy BER**

   ```python
   def plot_ber_curve(eb_n0_range, ber_values, title)
   ```

4. **Wykresy konstelacji**

   ```python
   def plot_constellation(symbols, title)
   ```

5. **Porownanie modulacji**
   ```python
   def compare_modulations(eb_n0_range, n_bits)
   ```

**Zaleznosci:**

- Wszystkie moduly projektu
- Matplotlib (wykresy)

---

## Architektura systemu

### Diagram architektury

```
┌─────────────────────────────────────────────────────────────┐
│                    SYSTEM KOMUNIKACJI                         │
└─────────────────────────────────────────────────────────────┘

         ┌──────────────┐
         │  GetBytes.py │
         │ (Generator   │
         │   bitow)     │
         └──────┬───────┘
                │
                ↓ [bity: 0,1,0,1,...]
         ┌──────────────┐
         │ Modulator.py │
         │  BPSK/QPSK/  │
         │   8-PSK/QAM  │
         └──────┬───────┘
                │
                ↓ [symbole zespolone]
         ┌──────────────────────┐
         │ TransmissionChannel  │
         │    + AWGN Noise      │
         └──────┬───────────────┘
                │
                ↓ [symbole + szum]
         ┌──────────────┐
         │Demodulator.py│
         │   Detekcja   │
         │   symboli    │
         └──────┬───────┘
                │
                ↓ [odkodowane bity]
         ┌──────────────┐
         │   main.py    │
         │  Obliczanie  │
         │  BER, wykresy│
         └──────────────┘
                │
                ↓
         ┌──────────────┐
         │  results/    │
         │  Wykresy i   │
         │  dane        │
         └──────────────┘
```

### Warstwy systemu

#### Warstwa 1: Generacja danych

- **Modul:** `GetBytes.py`
- **Funkcja:** Generowanie losowych bitow
- **Output:** Tablica bitow [0, 1, 0, 1, ...]

#### Warstwa 2: Modulacja

- **Modul:** `Modulator.py`
- **Funkcja:** Przeksztalcenie bitow na symbole
- **Output:** Tablica symboli zespolonych

#### Warstwa 3: Kanal transmisyjny

- **Moduly:** `TransmissionChannel.py`, `AddAWGNNoise.py`
- **Funkcja:** Symulacja transmisji z szumem
- **Output:** Symbole z dodanym szumem

#### Warstwa 4: Demodulacja

- **Modul:** `Demodulator.py`
- **Funkcja:** Odzyskanie bitow z symboli
- **Output:** Odkodowane bity

#### Warstwa 5: Analiza

- **Modul:** `main.py`
- **Funkcja:** Obliczanie BER, generowanie wykresow
- **Output:** Wykresy, dane statystyczne

---

## Przeplyw danych

### Szczegolowy przeplyw

```
1. Generacja bitow
   gen_bites(1000) → [0,1,1,0,1,...] (1000 bitow)

2. Modulacja (przykład QPSK)
   qpsk_modulation([0,1,1,0,...])
   → Para bitow → Symbol zespolony
   [0,1] → (0.707 + 0.707j)
   [1,0] → (-0.707 + 0.707j)
   ...
   → [symbols] (500 symboli dla 1000 bitow)

3. Kanal
   transmission_channel(symbols, eb_n0_db=10)
   → symbols + AWGN noise
   → [noisy_symbols]

4. Demodulacja
   qpsk_demodulation(noisy_symbols)
   → Symbol → Para bitow
   (0.75 + 0.68j) → [0,1]
   ...
   → [decoded_bits] (1000 bitow)

5. Analiza
   BER = sum(bits != decoded_bits) / len(bits)
   plot_ber_curve(...)
   → results/qpsk_ber.png
```

---

## Moduly projektu

### Diagram zaleznosci modulow

```
main.py
   ├── GetBytes.py
   ├── Modulator.py
   ├── TransmissionChannel.py
   │      └── AddAWGNNoise.py
   ├── Demodulator.py
   └── matplotlib

TransmissionChannel.py
   └── AddAWGNNoise.py

Wszystkie moduly
   └── numpy

Moduly wykorzystujace scipy
   └── Demodulator.py (erfc)
   └── main.py (analiza teoretyczna)
```

### Interfejsy modulow

#### GetBytes

```
Input:  N_bits (int)
Output: ndarray[N_bits] (typ: int)
```

#### Modulator

```
Input:  bits (ndarray)
Output: symbols (ndarray, dtype=complex)
```

#### TransmissionChannel

```
Input:  symbols (ndarray, complex), eb_n0_db (float)
Output: received_symbols (ndarray, complex)
```

#### Demodulator

```
Input:  received_symbols (ndarray, complex)
Output: decoded_bits (ndarray, int)
```

---

## Zaleznosci

### Biblioteki zewnetrzne

```
numpy (>=1.24.0)
   ├── Operacje na tablicach
   ├── Funkcje matematyczne
   └── Generowanie liczb losowych

scipy (>=1.10.0)
   ├── Funkcje specjalne (erfc)
   └── Przetwarzanie sygnalow

matplotlib (>=3.7.0)
   ├── Wykresy 2D
   ├── Konstelacje
   └── Wykresy BER
```

### Zaleznosci wewnetrzne

```
main.py
   → wymaga wszystkich innych modulow

TransmissionChannel.py
   → wymaga AddAWGNNoise.py

Pozostale moduly
   → niezalezne (tylko numpy)
```

---

## Wzorce projektowe

### 1. Modularnosc

- Kazda funkcjonalnosc w osobnym pliku
- Clear interfaces
- Low coupling, high cohesion

### 2. Kompozycja funkcji

```python
# Zamiast jednej wielkiej funkcji:
result = generate_and_transmit_and_decode(params)

# Mamy:
bits = gen_bites(N)
symbols = modulate(bits)
received = channel(symbols)
decoded = demodulate(received)
```

### 3. Reusable components

- Funkcje generyczne (np. add_awgn_noise dla wszystkich modulacji)
- Parametryzowane funkcje (eb_n0_db jako argument)

---

## Rozszerzenia

### Planowane funkcjonalnosci

1. **Nowe modulacje**

   - Lokalizacja: `src/Modulator.py`, `src/Demodulator.py`
   - Dodaj funkcje: `ofdm_modulation()`, `fsk_modulation()`

2. **Zaawansowane modele kanalow**

   - Lokalizacja: `src/TransmissionChannel.py`
   - Dodaj: Rayleigh fading, Rician fading

3. **Korekcja bledow**

   - Nowy modul: `src/ErrorCorrection.py`
   - Implementacja: Turbo codes, LDPC

4. **GUI**
   - Nowy katalog: `src/gui/`
   - Framework: tkinter, PyQt

---

## Najlepsze praktyki

### Organizacja kodu

✅ **Dobre:**

- Jeden modul = jedna odpowiedzialnosc
- Funkcje krotkie i czytelne
- Docstringi dla wszystkich funkcji

❌ **Zle:**

- Wszystko w jednym pliku
- Funkcje o wielu odpowiedzialnosciach
- Brak dokumentacji

### Nazewnictwo

✅ **Dobre:**

```python
def bpsk_modulation(bits):
def calculate_ber(original, decoded):
eb_n0_db = 10.0
```

❌ **Zle:**

```python
def mod(b):
def calc(a, b):
x = 10.0
```

### Dokumentacja

✅ **Dobre:**

```python
def add_awgn_noise(symbols, eb_n0_db):
    """
    Add AWGN noise to symbols.

    Parameters:
    -----------
    symbols : ndarray (complex)
        Modulated symbols
    eb_n0_db : float
        Eb/N0 ratio in dB

    Returns:
    --------
    ndarray (complex)
        Symbols with added noise
    """
```

---

## Podsumowanie

### Struktura w liczbach

- **7 modulow Python** (src/)
- **6 dokumentow** (docs/)
- **3 pliki konfiguracyjne** (requirements.txt, setup.bat, setup.sh)
- **~15 funkcji glownych** (rozne modulacje, demodulacje, analizy)

### Kluczowe katalogi

1. **src/** - kod zrodlowy (najwazniejszy)
2. **docs/** - dokumentacja
3. **results/** - wyniki symulacji

### Nastepne kroki

Aby lepiej zrozumiec implementacje:

1. Przeczytaj [Dokumentacje kodu](code-documentation.md)
2. Przeanalizuj kod w katalogu `src/`
3. Uruchom symulacje i zobacz wyniki

---

**Ostatnia aktualizacja:** 2025-10-22  
**Wersja dokumentu:** 1.4.0
