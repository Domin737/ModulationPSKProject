# PSK and QAM Digital Modulation Simulation

Projekt symulacji systemow modulacji cyfrowej PSK (Phase-Shift Keying) i QAM (Quadrature Amplitude Modulation) z analiza skutecznosci transmisji.

## Opis projektu

Ten projekt realizuje symulacje systemow komunikacji cyfrowej wykorzystujacych rozne typy modulacji:
- **BPSK** (Binary Phase-Shift Keying) - modulacja 2-fazowa
- **QPSK** (Quadrature Phase-Shift Keying) - modulacja 4-fazowa
- **8-PSK** - modulacja 8-fazowa
- **16-QAM** (Quadrature Amplitude Modulation) - modulacja amplitudowo-fazowa

Projekt symuluje kanal transmisyjny z szumem AWGN (Additive White Gaussian Noise) i analizuje BER (Bit Error Rate) dla roznych warunkow.

## Status projektu

### ✓ Zaimplementowane moduly:

| Modul | Status | Opis |
|-------|--------|------|
| `GetBytes.py` | ✓ Gotowe | Generator losowych bitow |
| `Modulator.py` | ✓ Gotowe | Modulatory: BPSK, QPSK, 8-PSK, 16-QAM |
| `AddAWGNNoise.py` | ✓ Gotowe | Generator szumu AWGN |
| `TransmissionChannel.py` | ✓ Gotowe | Kanal transmisyjny z szumem |
| `Demodulator.py` | ✓ Gotowe | Demodulatory dla wszystkich modulacji |
| `main.py` | ✓ Gotowe | Program glowny z symulacjami |

**Postep: 100%** - Projekt kompletny i gotowy do uruchomienia!

## Wymagania

### Wymagania systemowe:
- Python 3.8 lub nowszy
- pip (menadzer pakietow)

### Wymagane biblioteki:
```
numpy>=1.24.0
scipy>=1.10.0
matplotlib>=3.7.0
```

## Instalacja

### Krok 1: Klonowanie repozytorium (jezeli projekt jest w Git)
```bash
git clone <repository-url>
cd ModulationPSKProject
```

### Krok 2: Utworzenie wirtualnego srodowiska

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Krok 3: Instalacja zaleznosci
```bash
pip install -r requirements.txt
```

## Uzycie

### Podstawowe uruchomienie

Aby uruchomic pelna symulacje wszystkich modulacji:

```bash
python main.py
```

Program wygeneruje:
- Wykres porownawczy BER vs Eb/N0 dla wszystkich modulacji
- Diagramy konstelacji dla kazdej modulacji

### Przyklady uzycia poszczegolnych modulow

#### 1. Generowanie bitow
```python
from GetBytes import gen_bites

# Generuj 100 losowych bitow
bits = gen_bites(100)
print(bits)  # [1 0 1 1 0 ...]
```

#### 2. Modulacja BPSK
```python
from Modulator import bpsk_modulation
import numpy as np

bits = np.array([0, 1, 0, 1])
symbols = bpsk_modulation(bits)
print(symbols)  # [1.+0.j -1.+0.j  1.+0.j -1.+0.j]
```

#### 3. Modulacja QPSK
```python
from Modulator import qpsk_modulation
import numpy as np

bits = np.array([0, 0, 0, 1, 1, 0, 1, 1])  # 8 bits = 4 symbols
symbols = qpsk_modulation(bits)
print(symbols)
```

#### 4. Dodawanie szumu AWGN
```python
from AddAWGNNoise import add_awgn_noise
import numpy as np

symbols = np.array([1.0, -1.0, 1.0, -1.0], dtype=complex)
eb_n0_db = 10.0  # 10 dB

noisy_symbols = add_awgn_noise(symbols, eb_n0_db)
print(noisy_symbols)
```

#### 5. Transmisja przez kanal
```python
from TransmissionChannel import transmission_channel
import numpy as np

symbols = np.array([1.0, -1.0, 1.0], dtype=complex)
received = transmission_channel(symbols, eb_n0_db=10)
print(received)
```

#### 6. Demodulacja BPSK
```python
from Demodulator import bpsk_demodulation
import numpy as np

received_symbols = np.array([0.9, -1.1, 0.8, -0.9], dtype=complex)
decoded_bits = bpsk_demodulation(received_symbols)
print(decoded_bits)  # [0 1 0 1]
```

#### 7. Pelna symulacja (End-to-End)
```python
from GetBytes import gen_bites
from Modulator import bpsk_modulation
from TransmissionChannel import transmission_channel
from Demodulator import bpsk_demodulation
import numpy as np

# Generuj bity
bits = gen_bites(1000)

# Modulacja
symbols = bpsk_modulation(bits)

# Transmisja przez kanal z szumem
received_symbols = transmission_channel(symbols, eb_n0_db=10)

# Demodulacja
decoded_bits = bpsk_demodulation(received_symbols)

# Oblicz BER
errors = np.sum(bits != decoded_bits)
ber = errors / len(bits)
print(f"BER = {ber}")
```

## Typy modulacji

### BPSK (Binary PSK)
- **Symbole:** 2 (-1, +1)
- **Bity na symbol:** 1
- **Konstelacja:** Punkty na osi rzeczywistej
- **Zastosowanie:** Najlepsza odpornosc na szum
- **Mapowanie:** 
  - Bit 0 → +1+0j
  - Bit 1 → -1+0j

### QPSK (Quadrature PSK)
- **Symbole:** 4 punkty na okregu jednostkowym
- **Bity na symbol:** 2
- **Konstelacja:** 4 punkty (45°, 135°, 225°, 315°)
- **Zastosowanie:** Dwukrotnie wyzsza wydajnosc niz BPSK przy podobnej BER
- **Mapowanie:**
  - 00 → (+1+1j)/√2 (45°)
  - 01 → (-1+1j)/√2 (135°)
  - 10 → (+1-1j)/√2 (315°)
  - 11 → (-1-1j)/√2 (225°)

### 8-PSK
- **Symbole:** 8 punktow rowno rozmieszczonych na okregu
- **Bity na symbol:** 3
- **Konstelacja:** 8 punktow co 45° (0°, 45°, 90°, ..., 315°)
- **Zastosowanie:** Wyzsza wydajnosc, gorsza odpornosc na szum
- **Mapowanie:** 000-111 → exp(j*k*π/4), gdzie k=0..7

### 16-QAM
- **Symbole:** 16 punktow w siatce 4×4
- **Bity na symbol:** 4
- **Konstelacja:** Siatka z poziomami {-3, -1, +1, +3}
- **Zastosowanie:** Wysoka wydajnosc, wymaga dobrego SNR
- **Normalizacja:** Symbole podzielone przez √10 dla sredniej mocy = 1

## Parametry symulacji

### Eb/N0 (Energy per bit to Noise power spectral density ratio)
- Miara jakosci sygnalu w systemie cyfrowym
- Wyrazana w decybelach (dB)
- Wyzsze wartosci oznaczaja mniej szumu
- Typowy zakres symulacji: -2 dB do 12 dB

### BER (Bit Error Rate)
- Stosunek blednych bitow do calkowitej liczby bitow
- Wzor: BER = (liczba bledow) / (liczba bitow)
- Cel: BER < 10⁻³ dla wiekszosci systemow
- Typowy zakres: 10⁻⁵ do 10⁻¹

### Szum AWGN
Additive White Gaussian Noise - model szumu charakteryzujacy sie:
- Gaussowskim rozkladem (normalnym)
- Biala gestosc widmowa mocy (rowna moc w calym widmie)
- Addytywny charakter (dodawany do sygnalu)

## Wykresy i wyniki

Program generuje nastepujace wykresy:

1. **ber_comparison.png** - Porownanie BER vs Eb/N0 dla wszystkich modulacji
2. **bpsk_constellation.png** - Diagram konstelacji BPSK (czysty i z szumem)
3. **qpsk_constellation.png** - Diagram konstelacji QPSK
4. **8psk_constellation.png** - Diagram konstelacji 8-PSK
5. **16qam_constellation.png** - Diagram konstelacji 16-QAM

## Struktura projektu

```
ModulationPSKProject/
├── GetBytes.py              # Generator bitow
├── Modulator.py             # Modulatory (BPSK, QPSK, 8-PSK, 16-QAM)
├── AddAWGNNoise.py          # Generator szumu AWGN
├── TransmissionChannel.py   # Kanal transmisyjny
├── Demodulator.py           # Demodulatory
├── main.py                  # Program glowny
├── requirements.txt         # Zaleznosci
└── README.md                # Ten plik
```

## Teoria

### Relacja teoretyczna BER dla BPSK
```
BER_BPSK = 0.5 * erfc(sqrt(Eb/N0))
```

gdzie:
- `erfc` - funkcja bledu komplementarna
- `Eb/N0` - energia bitu do mocy szumu (wartosc liniowa, nie dB)

### Zaleznosc BER od Eb/N0
- **Niskie Eb/N0** (< 0 dB): Duzo szumu, BER → 0.5 (losowe zgadywanie)
- **Srednie Eb/N0** (0-10 dB): BER maleje eksponencjalnie
- **Wysokie Eb/N0** (> 10 dB): Bardzo niskie BER (< 10⁻⁴)

### Porownanie modulacji
- **BPSK**: Najlepsza odpornosc na szum, najnizsza wydajnosc (1 bit/symbol)
- **QPSK**: Dobry kompromis - 2× wyzsza wydajnosc niz BPSK przy podobnej BER
- **8-PSK**: 3 bity/symbol, gorsza BER niz QPSK
- **16-QAM**: 4 bity/symbol, najgorsza odpornosc na szum

## Testowanie

Kazdy modul zawiera wbudowane testy. Aby je uruchomic:

```bash
# Test generatora bitow
python GetBytes.py

# Test modulatorow
python Modulator.py

# Test szumu AWGN
python AddAWGNNoise.py

# Test kanalu transmisyjnego
python TransmissionChannel.py

# Test demodulatorow
python Demodulator.py
```

## Rozwiazywanie problemow

### Problem: ImportError
**Rozwiazanie:** Upewnij sie, ze wszystkie pliki sa w tym samym katalogu i ze srodowisko wirtualne jest aktywne.

### Problem: ModuleNotFoundError: numpy
**Rozwiazanie:** Zainstaluj wymagane biblioteki:
```bash
pip install -r requirements.txt
```

### Problem: Wykresy nie wyswietlaja sie
**Rozwiazanie:** Wykresy sa automatycznie zapisywane jako pliki PNG. Sprawdz katalog projektu.

### Problem: BER = 0.5 dla wszystkich Eb/N0
**Rozwiazanie:** Sprawdz czy liczba bitow jest wielokrotnoscia bits_per_symbol dla danej modulacji.

## Najlepsze praktyki

1. **Liczba bitow**: Uzywaj duzej liczby bitow (> 1000) dla dokladnej symulacji BER
2. **Zakres Eb/N0**: Symuluj szeroki zakres (-2 do 15 dB) aby zobaczyc pelne zachowanie
3. **Normalizacja**: Symbole sa znormalizowane do sredniej mocy = 1
4. **Losowość**: Uzyj `np.random.seed()` dla powtarzalnych wynikow

## Przykladowe wyniki

Typowe wartosci BER dla Eb/N0 = 10 dB:
- **BPSK**: ~10⁻⁵
- **QPSK**: ~10⁻⁵
- **8-PSK**: ~10⁻³
- **16-QAM**: ~10⁻²

## Licencja

Projekt edukacyjny - Study Work Project

## Referencje

1. **Phase-shift keying** - https://en.wikipedia.org/wiki/Phase-shift_keying
2. **Quadrature amplitude modulation** - https://en.wikipedia.org/wiki/Quadrature_amplitude_modulation
3. Proakis J. G., "Digital Communications", 5th Edition
4. Haykin S., "Communication Systems", 4th Edition

## Autor

ModulationPSKProject Team

## Wersja

1.0.0 - Projekt kompletny

---

**Ostatnia aktualizacja:** 2025-10-22  
**Status:** ✓ Gotowy do uzycia
