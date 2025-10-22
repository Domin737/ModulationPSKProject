# Digital Modulation Simulation (BPSK, QPSK, 8-PSK, 16-QAM)

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-Educational-green.svg)]()
[![Status](https://img.shields.io/badge/status-complete-success.svg)]()

## Wersja: 1.4.0

Projekt symulacyjny systemow modulacji cyfrowej PSK (Phase-Shift Keying) i QAM (Quadrature Amplitude Modulation) z analiza skutecznosci transmisji w obecnosci szumu AWGN.

## Opis projektu

ModulationPSKProject to zaawansowane narzedzie do symulacji i analizy roznych typow modulacji cyfrowej stosowanych w systemach telekomunikacyjnych. Projekt realizuje:

- **Modulacje cyfrowe**: BPSK, QPSK, 8-PSK, QAM (16-QAM, 64-QAM)
- **Model kanalu transmisyjnego**: Symulacja kanalu z szumem AWGN (Additive White Gaussian Noise)
- **Analiza wydajnosci**: Obliczanie BER (Bit Error Rate) w funkcji Eb/N0
- **Wizualizacja**: Wykresy BER, diagramy konstelacji, porownania modulacji

## Cechy projektu

### Zaimplementowane modulacje

- **BPSK** (Binary Phase-Shift Keying) - 1 bit/symbol
- **QPSK** (Quadrature Phase-Shift Keying) - 2 bity/symbol
- **8-PSK** - 3 bity/symbol
- **QAM** (Quadrature Amplitude Modulation) - 4+ bity/symbol

### Funkcjonalnosci

- Generator losowych bitow
- Modulatory dla wszystkich typow modulacji
- Model kanalu z szumem AWGN (kontrolowany parametr Eb/N0)
- Demodulatory z detekcja progowa/odleglosciowa
- Obliczanie BER (Bit Error Rate)
- Porownanie z teoretycznymi krzywymi BER
- Wizualizacja konstelacji i wykresow BER

## Szybki start

### 1. Instalacja srodowiska

**Windows:**

```bash
setup.bat
```

**Linux/Mac:**

```bash
chmod +x setup.sh
./setup.sh
```

### 2. Aktywacja srodowiska

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/Mac:**

```bash
source venv/bin/activate
```

### 3. Uruchomienie symulacji

```bash
cd src
python main.py
```

## Struktura projektu

```
ModulationPSKProject/
├── docs/                    # Dokumentacja
│   ├── index.md            # Indeks dokumentacji
│   ├── requirements-and-environment.md
│   ├── installation.md
│   ├── project-structure.md
│   ├── error-handling.md
│   └── code-documentation.md
├── results/                 # Wyniki symulacji i wykresy
├── src/                     # Kod zrodlowy
│   ├── GetBytes.py         # Generator bitow
│   ├── Modulator.py        # Modulatory
│   ├── AddAWGNNoise.py     # Generator szumu AWGN
│   ├── TransmissionChannel.py  # Model kanalu
│   ├── Demodulator.py      # Demodulatory
│   └── main.py             # Program glowny
├── requirements.txt         # Zaleznosci Python
├── setup.bat               # Instalator Windows
├── setup.sh                # Instalator Linux/Mac
└── README.md               # Ten plik

```

## Wymagania

### Wymagania systemowe

- Python 3.8 lub nowszy (zalecany Python 3.9+)
- System operacyjny: Windows 10/11, Linux, macOS
- RAM: minimum 2 GB (zalecane 4 GB)
- Miejsce na dysku: ~500 MB (wraz ze srodowiskiem wirtualnym)

### Wymagane biblioteki

- **NumPy** (>=1.24.0) - obliczenia numeryczne
- **SciPy** (>=1.10.0) - funkcje matematyczne i przetwarzanie sygnalow
- **Matplotlib** (>=3.7.0) - wizualizacja wykresow

## Uzycie

### Przyklad 1: Podstawowa symulacja BPSK

```python
from GetBytes import gen_bites
from Modulator import bpsk_modulation
from TransmissionChannel import transmission_channel
from Demodulator import bpsk_demodulation

# Generuj 1000 bitow
bits = gen_bites(1000)

# Modulacja BPSK
symbols = bpsk_modulation(bits)

# Transmisja przez kanal (Eb/N0 = 10 dB)
received = transmission_channel(symbols, eb_n0_db=10.0)

# Demodulacja
decoded_bits = bpsk_demodulation(received)

# Oblicz BER
errors = sum(bits != decoded_bits)
ber = errors / len(bits)
print(f"BER = {ber:.6f}")
```

### Przyklad 2: Porownanie modulacji

```python
from main import compare_modulations

# Porownaj BPSK, QPSK, 8-PSK dla zakresu Eb/N0
eb_n0_range = range(0, 15)  # 0 do 14 dB
compare_modulations(eb_n0_range, n_bits=10000)
```

### Przyklad 3: Wizualizacja konstelacji

```python
from main import plot_constellation
from Modulator import qpsk_modulation
from GetBytes import gen_bites

# Generuj symbole QPSK
bits = gen_bites(1000)
symbols = qpsk_modulation(bits)

# Wyswietl konstelacje
plot_constellation(symbols, title='QPSK Constellation')
```

## Podstawy teoretyczne

### Modulacja PSK

Modulacja PSK (Phase-Shift Keying) koduje informacje poprzez zmiane fazy sygnalu nosnego. Rozne typy PSK roznią sie liczba punktow konstelacji:

- **BPSK**: 2 punkty (0°, 180°) - 1 bit/symbol
- **QPSK**: 4 punkty (45°, 135°, 225°, 315°) - 2 bity/symbol
- **8-PSK**: 8 punktow co 45° - 3 bity/symbol

### Szum AWGN

AWGN (Additive White Gaussian Noise) to model matematyczny szumu w kanale transmisyjnym:

- **Additive** - dodawany do sygnalu
- **White** - rowna moc w caym pasmie czestotliwosci
- **Gaussian** - rozklad normalny (Gaussa)

### Eb/N0

Eb/N0 to stosunek energii przypadajacej na jeden bit (Eb) do gestosci widmowej mocy szumu (N0). Jest kluczowym parametrem charakteryzujacym jakosc kanalu transmisyjnego:

- Wysoki Eb/N0 → niski BER (dobra jakosc)
- Niski Eb/N0 → wysoki BER (zła jakosc)

### BER (Bit Error Rate)

BER to stosunek liczby blednie odebranych bitow do calkowitej liczby bitow:

```
BER = liczba_bledow / calkowita_liczba_bitow
```

Dla BPSK, teoretyczny BER wynosi:

```
BER_BPSK = 0.5 * erfc(sqrt(Eb/N0))
```

gdzie erfc() to komplementarna funkcja bledu.

## Dokumentacja

Pelna dokumentacja dostepna w katalogu `docs/`:

- [Indeks dokumentacji](docs/index.md)
- [Wymagania i srodowisko](docs/requirements-and-environment.md)
- [Instrukcja instalacji](docs/installation.md)
- [Struktura projektu](docs/project-structure.md)
- [Obsluga bledow](docs/error-handling.md)
- [Dokumentacja kodu](docs/code-documentation.md)

## Rozwoj projektu

### Planowane funkcjonalnosci

- [ ] Modulacje QAM wyzszych rzedu (256-QAM, 1024-QAM)
- [ ] Model kanalu z fedingiem
- [ ] Korekcja bledow (kody konwolucyjne, turbo-kody)
- [ ] Interfejs graficzny (GUI)
- [ ] Export wynikow do CSV/Excel

### Historia wersji

**v1.4.0** (Aktualna)

- Pelna implementacja BPSK, QPSK, 8-PSK
- Implementacja QAM (16-QAM, 64-QAM)
- Ulepszona dokumentacja
- Poprawione skrypty instalacyjne

**v1.3.0**

- Dodano demodulatory dla wszystkich modulacji
- Porownania wydajnosci

**v1.2.0**

- Implementacja QPSK i 8-PSK

**v1.1.0**

- Implementacja kanalu AWGN

**v1.0.0**

- Podstawowa implementacja BPSK

## Licencja

Projekt edukacyjny - Study Work Project

## Autor

ModulationPSKProject Team

## Wsparcie

W przypadku problemow:

1. Sprawdz [dokumentacje instalacji](docs/installation.md)
2. Przejrzyj [obsluge bledow](docs/error-handling.md)
3. Upewnij sie ze wszystkie zaleznosci sa zainstalowane: `pip list`

## Przydatne linki

- [Wikipedia: Phase-shift keying](https://en.wikipedia.org/wiki/Phase-shift_keying)
- [Wikipedia: QAM](https://en.wikipedia.org/wiki/Quadrature_amplitude_modulation)
- [NumPy Documentation](https://numpy.org/doc/)
- [SciPy Documentation](https://docs.scipy.org/)
- [Matplotlib Documentation](https://matplotlib.org/)

## Cytowania

Jesli uzywasz tego projektu w pracy naukowej, prosimy o cytowanie:

```
ModulationPSKProject (2025). System symulacji modulacji cyfrowych PSK i QAM.
Dostepne na: [URL projektu]
```

---

**Ostatnia aktualizacja:** 2025-10-22  
**Status projektu:** Stabilny - Wersja produkcyjna  
**Wsparcie:** Aktywne
