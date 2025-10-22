# ModulationPSKProject

Projekt symulacji systemow modulacji cyfrowej PSK (Phase-Shift Keying) i QAM (Quadrature Amplitude Modulation) z analiza skutecznosci transmisji.

## Opis projektu

Projekt realizuje symulacje systemow komunikacji cyfrowej wykorzystujacych rozne typy modulacji:
- **BPSK** (Binary Phase-Shift Keying) - modulacja 2-fazowa
- **QPSK** (Quadrature Phase-Shift Keying) - modulacja 4-fazowa
- **8-PSK** - modulacja 8-fazowa
- **QAM** (Quadrature Amplitude Modulation) - modulacja amplitudowo-fazowa

Projekt symuluje kanal transmisyjny z szumem AWGN (Additive White Gaussian Noise) i analizuje BER (Bit Error Rate) dla roznych warunkow.

## Status projektu

### ✓ Zaimplementowane:
- Generator losowych bitow (`GetBytes.py`)
- Modulator BPSK (`Modulator.py`)
- Generator szumu AWGN (`AddAWGNNoise.py`)

### ⚠ Do zaimplementowania:
- Kanal transmisyjny (`TransmissionChannel.py`)
- Demodulatory (`Demodulator.py`)
- Modulatory: QPSK, 8-PSK, QAM
- Glowny program symulacyjny (`main.py`)
- Wykresy i analiza wynikow

## Instalacja

### Wymagania
- Python 3.8 lub nowszy
- pip (menadzer pakietow)

### Szybka instalacja

#### Windows
```bash
setup.bat
```

#### Linux/Mac
```bash
chmod +x setup.sh
./setup.sh
```

### Manualna instalacja

1. Utworz wirtualne srodowisko:
```bash
python -m venv venv
```

2. Aktywuj srodowisko:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

3. Zainstaluj zaleznosci:
```bash
pip install -r requirements.txt
```

### Test instalacji

```bash
python test_environment.py
```

## Struktura projektu

```
ModulationPSKProject/
├── GetBytes.py              # Generator bitow [GOTOWE]
├── Modulator.py             # Modulatory [BPSK gotowe]
├── AddAWGNNoise.py          # Generator szumu AWGN [GOTOWE]
├── Demodulator.py           # Demodulatory [DO ZROBIENIA]
├── TransmissionChannel.py   # Kanal transmisyjny [DO ZROBIENIA]
├── main.py                  # Program glowny [DO ZROBIENIA]
├── requirements.txt         # Zaleznosci
├── setup.sh / setup.bat     # Skrypty instalacyjne
├── test_environment.py      # Test srodowiska
├── README.md                # Ten plik
├── INSTALLATION.md          # Szczegolowa instrukcja instalacji
├── PROJECT_ARCHITECTURE.md  # Architektura projektu
└── QUICKSTART.md            # Szybki start
```

## Uzycie

### Przyklady

#### 1. Generowanie bitow
```python
from GetBytes import gen_bites

bits = gen_bites(100)  # Generuj 100 losowych bitow
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

#### 3. Dodawanie szumu AWGN
```python
from AddAWGNNoise import add_awgn_noise
import numpy as np

symbols = np.array([1.0, -1.0, 1.0, -1.0], dtype=complex)
Eb_N0_db = 10.0  # 10 dB

noisy_symbols = add_awgn_noise(symbols, Eb_N0_db)
print(noisy_symbols)
```

#### 4. Pelna symulacja (po implementacji)
```python
from GetBytes import gen_bites
from Modulator import bpsk_modulation
from TransmissionChannel import transmission_channel
from Demodulator import bpsk_demodulation

# Generuj bity
bits = gen_bites(1000)

# Modulacja
symbols = bpsk_modulation(bits)

# Transmisja przez kanal z szumem
received_symbols = transmission_channel(symbols, Eb_N0_db=10)

# Demodulacja
decoded_bits = bpsk_demodulation(received_symbols)

# Oblicz BER
errors = np.sum(bits != decoded_bits)
ber = errors / len(bits)
print(f"BER = {ber}")
```

## Typy modulacji

### BPSK (Binary PSK)
- 2 symbole: -1, +1
- 1 bit na symbol
- Konstelacja: punkty na osi rzeczywistej
- Najlepsza odpornosc na szum

### QPSK (Quadrature PSK)
- 4 symbole: (±1±j)/√2
- 2 bity na symbol
- Konstelacja: 4 punkty na okregu (45°, 135°, 225°, 315°)
- Dwukrotnie wyzsza wydajnosc niz BPSK przy podobnej BER

### 8-PSK
- 8 symboli rowno rozmieszczonych na okregu
- 3 bity na symbol
- Konstelacja: 8 punktow co 45°
- Wyzsza wydajnosc, gorsza odpornosc na szum

### 16-QAM
- 16 symboli w siatce 4×4
- 4 bity na symbol
- Rozna amplituda i faza
- Wysoka wydajnosc, wymaga dobrego SNR

## Parametry symulacji

### Eb/N0 (Energy per bit to Noise power spectral density ratio)
- Miara jakosci sygnalu w systemie cyfrowym
- Wyrazana w decybelach (dB)
- Typowy zakres: -5 dB do 15 dB

### BER (Bit Error Rate)
- Stosunek blednych bitow do calkowitej liczby bitow
- Wzor: BER = (liczba bledow) / (liczba bitow)
- Cel: BER < 10^-3 dla wiekszosci systemow

## Teoria

### Szum AWGN
Additive White Gaussian Noise - model szumu charakteryzujacy sie:
- Gaussowskim rozkladem (normalnym)
- Biala gestosc widmowa mocy (rowna moc w calym widmie)
- Addytywny charakter (dodawany do sygnalu)

### Relacja teoretyczna BER dla BPSK
```
BER_BPSK = 0.5 * erfc(sqrt(Eb/N0))
```

gdzie:
- `erfc` - funkcja bledu komplementarna
- `Eb/N0` - energia bitu do mocy szumu (wartość liniowa, nie dB)

## Wykresy i analiza

Projekt generuje nastepujace wykresy:
1. **BER vs Eb/N0** - porownanie wszystkich modulacji
2. **Konstelacje** - wizualizacja symboli dla kazdej modulacji
3. **Konstelacje z szumem** - symbole po przejsciu przez kanal

## Plan rozwoju projektu

### Faza 1: Podstawowa funkcjonalnosc BPSK
1. Implementacja `TransmissionChannel.py`
2. Implementacja `Demodulator.py` (BPSK)
3. Podstawowa symulacja w `main.py`
4. Test end-to-end

### Faza 2: QPSK
1. Implementacja modulatora QPSK
2. Implementacja demodulatora QPSK
3. Symulacja i porownanie z BPSK

### Faza 3: 8-PSK
1. Implementacja modulatora 8-PSK
2. Implementacja demodulatora 8-PSK
3. Analiza porownawcza

### Faza 4: QAM
1. Implementacja modulatora QAM
2. Implementacja demodulatora QAM
3. Pelna analiza porownawcza

### Faza 5: Finalizacja
1. Optymalizacja kodu
2. Pelna dokumentacja
3. Generowanie raportow

## Dokumentacja

- **INSTALLATION.md** - szczegolowe instrukcje instalacji
- **PROJECT_ARCHITECTURE.md** - architektura i analiza kodu
- **QUICKSTART.md** - szybki start dla poczatkujacych
- **README.md** - ten plik (przeglad projektu)

## Wymagane biblioteki

- **NumPy** - obliczenia numeryczne, tablice
- **SciPy** - funkcje matematyczne, przetwarzanie sygnalow
- **Matplotlib** - generowanie wykresow

## Licencja

Projekt edukacyjny - Study Work Project

## Autor

ModulationPSKProject Team

## Wersja

0.5.0 (w trakcie rozwoju)

## Changelog

### v0.5.0 (Aktualny)
- ✓ Implementacja GetBytes.py
- ✓ Implementacja Modulator.py (BPSK)
- ✓ Implementacja AddAWGNNoise.py
- ✓ Przygotowanie dokumentacji
- ✓ Skrypty instalacyjne
- ⚠ TransmissionChannel.py - w trakcie
- ⚠ Demodulator.py - w trakcie
- ⚠ main.py - w trakcie

## Referencje

1. **Phase-shift keying** - https://en.wikipedia.org/wiki/Phase-shift_keying
2. **Quadrature amplitude modulation** - https://en.wikipedia.org/wiki/Quadrature_amplitude_modulation
3. Proakis J. G., "Digital Communications", 5th Edition
4. Haykin S., "Communication Systems", 4th Edition

## FAQ

**Q: Dlaczego BPSK mapuje bit 1 na -1 a bit 0 na +1?**
A: To standardowa konwencja w komunikacji cyfrowej. Mapowanie 1→-1, 0→+1 upraszcza obliczenia i jest zgodne z teoria.

**Q: Co to jest Eb/N0?**
A: To stosunek energii przypadajacej na jeden bit do gestosci widmowej mocy szumu. Im wyzsze Eb/N0, tym lepsza jakosc transmisji.

**Q: Czym rozni sie QPSK od BPSK?**
A: QPSK przesyla 2 bity na symbol (vs 1 bit w BPSK), wiec ma dwukrotnie wyzsza wydajnosc przy podobnej odpornosci na bledy.

**Q: Jak uruchomic projekt?**
A: 
1. Uruchom setup.sh (Linux/Mac) lub setup.bat (Windows)
2. Aktywuj venv: `source venv/bin/activate` (Linux/Mac) lub `venv\Scripts\activate` (Windows)
3. Uruchom: `python main.py`

**Q: Gdzie znajde szczegolowa dokumentacje?**
A: Sprawdz pliki INSTALLATION.md, PROJECT_ARCHITECTURE.md i QUICKSTART.md

## Kontakt

W przypadku pytan lub problemow:
1. Sprawdz dokumentacje w plikach .md
2. Przeczytaj komentarze w kodzie zrodlowym
3. Uruchom test_environment.py aby zweryfikowac instalacje

---

**Ostatnia aktualizacja:** 2025-10-22
**Status:** W trakcie rozwoju
**Postep:** 30% (3/10 modulow gotowych)
