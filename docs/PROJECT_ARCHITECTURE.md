# Architektura projektu ModulationPSKProject

## Przeglad projektu

Projekt symuluje system komunikacji cyfrowej z modulacja fazowa (PSK) i amplitudowo-fazowa (QAM), uwzgledniajac zaklócenia w kanale transmisyjnym.

## Analiza istniejacego kodu

### Co juz zostalo zaimplementowane:

#### 1. GetBytes.py ✓
- **Status:** GOTOWE
- **Funkcja:** Generowanie losowych bitow (0 lub 1)
- **Implementacja:** `gen_bites(N_bits)` - zwraca tablice N losowych bitow

#### 2. Modulator.py ✓ (czesc)
- **Status:** CZESCIOWO GOTOWE (tylko BPSK)
- **Funkcja:** Modulacja BPSK - mapowanie bitow na symbole
- **Implementacja:** `bpsk_modulation(bits)` - mapuje bit 1→-1, bit 0→+1
- **Do zrobienia:** QPSK, 8-PSK, QAM

#### 3. AddAWGNNoise.py ✓
- **Status:** GOTOWE
- **Funkcja:** Dodawanie szumu AWGN (Additive White Gaussian Noise)
- **Implementacja:** `add_awgn_noise(bpskSymbols, Eb_No_db)`
- **Dzialanie:**
  - Konwersja Eb/N0 z dB na liczbe
  - Obliczanie mocy szumu N0
  - Generowanie szumu gaussowskiego (I i Q)
  - Dodawanie szumu do symboli

#### 4. Demodulator.py
- **Status:** PUSTY
- **Do zrobienia:** Demodulacja symboli z powrotem na bity

#### 5. TransmissionChannel.py
- **Status:** PUSTY  
- **Do zrobienia:** Model kanalu transmisyjnego

#### 6. main.py
- **Status:** SZKIELET
- **Do zrobienia:** Glowny program z symulacjami

## Architektura systemu

```
┌─────────────────────────────────────────────────────────────────┐
│                    SYSTEM KOMUNIKACJI CYFROWEJ                   │
└─────────────────────────────────────────────────────────────────┘

[Bity] → [Modulator] → [Kanal] → [Demodulator] → [Bity odebrane]
  ↑                        ↓
GetBytes.py          TransmissionChannel.py
                      (+ AddAWGNNoise.py)

```

### Przeplyw danych:

1. **Generacja danych:**
   - `GetBytes.py` generuje losowe bity do transmisji

2. **Modulacja:**
   - `Modulator.py` przeksztalca bity w symbole zespolone
   - Typy modulacji: BPSK, QPSK, 8-PSK, QAM

3. **Kanal transmisyjny:**
   - `TransmissionChannel.py` symuluje przesylanie przez kanal
   - `AddAWGNNoise.py` dodaje szum AWGN

4. **Demodulacja:**
   - `Demodulator.py` odtwarza bity z odebranych symboli

5. **Analiza:**
   - `main.py` porownuje wysłane i odebrane bity
   - Obliczanie BER (Bit Error Rate)
   - Generowanie wykresow

## Szczegolowa specyfikacja modulow

### Modul 1: GetBytes.py [GOTOWE]
```python
def gen_bites(N_bits):
    # Generuje N losowych bitow (0 lub 1)
    return numpy.array [N_bits]
```

### Modul 2: Modulator.py [DO ROZSZERZENIA]

#### BPSK [GOTOWE]
- 2 symbole: {-1, +1}
- 1 bit na symbol
- Mapowanie: 0→+1, 1→-1

#### QPSK [DO ZROBIENIA]
- 4 symbole: {±1±j}/√2
- 2 bity na symbol
- Punkty na okregu jednostkowym: 45°, 135°, 225°, 315°

#### 8-PSK [DO ZROBIENIA]
- 8 symboli równo rozmieszczonych na okregu
- 3 bity na symbol
- Katy: 0°, 45°, 90°, 135°, 180°, 225°, 270°, 315°

#### QAM [DO ZROBIENIA]
- Przykladowo 16-QAM: 16 symboli
- 4 bity na symbol
- Siatka 4×4 punktow

### Modul 3: TransmissionChannel.py [DO ZAIMPLEMENTOWANIA]
```python
def transmission_channel(symbols, Eb_N0_db):
    # Symuluje kanal z szumem AWGN
    # 1. Transmisja symboli
    # 2. Dodanie szumu (wywolanie add_awgn_noise)
    # 3. Zwrot odebranych symboli
```

### Modul 4: AddAWGNNoise.py [GOTOWE]
- Profesjonalna implementacja
- Parametr: Eb/N0 w dB
- Generuje szum zespolony (I + jQ)

### Modul 5: Demodulator.py [DO ZAIMPLEMENTOWANIA]

#### Demodulacja BPSK
- Decyzja progowa: Re(symbol) > 0 → bit 0, Re(symbol) < 0 → bit 1

#### Demodulacja QPSK
- Obliczenie fazy: atan2(Im, Re)
- Przedzial [0, 2π) podzielony na 4 regiony

#### Demodulacja 8-PSK
- Obliczenie fazy
- Przedzial [0, 2π) podzielony na 8 regionow

#### Demodulacja QAM
- Decyzje progowe oddzielnie dla I i Q

### Modul 6: main.py [DO ZAIMPLEMENTOWANIA]

Funkcje glowne:
1. `simulate_modulation(mod_type, Eb_N0_range, N_bits)`
   - Symulacja dla danej modulacji
   - Przejscie przez zakres Eb/N0
   - Obliczanie BER

2. `plot_ber_curves(results)`
   - Generowanie wykresow BER vs Eb/N0
   - Porownanie roznych modulacji

3. `plot_constellation(symbols, title)`
   - Wykres konstelacji symboli

## Plan implementacji

### Faza 1: Zakonczenie podstawowej funkcjonalnosci BPSK
- [ ] TransmissionChannel.py - implementacja
- [ ] Demodulator.py - demodulacja BPSK
- [ ] main.py - podstawowa symulacja BPSK
- [ ] Test end-to-end dla BPSK

### Faza 2: Rozszerzenie o QPSK
- [ ] Modulator.py - dodanie qpsk_modulation()
- [ ] Demodulator.py - dodanie qpsk_demodulation()
- [ ] main.py - symulacja QPSK
- [ ] Porownanie BPSK vs QPSK

### Faza 3: Rozszerzenie o 8-PSK
- [ ] Modulator.py - dodanie psk8_modulation()
- [ ] Demodulator.py - dodanie psk8_demodulation()
- [ ] main.py - symulacja 8-PSK

### Faza 4: Rozszerzenie o QAM
- [ ] Modulator.py - dodanie qam_modulation()
- [ ] Demodulator.py - dodanie qam_demodulation()
- [ ] main.py - symulacja QAM

### Faza 5: Analiza i dokumentacja
- [ ] Generowanie kompletnych wykresow
- [ ] Analiza wynikow
- [ ] Dokumentacja README.md
- [ ] Testy i walidacja

## Metryki i testy

### BER (Bit Error Rate)
```
BER = (liczba blednych bitow) / (calkowita liczba bitow)
```

### Zakres Eb/N0
- Typowo: -5 dB do 15 dB
- Krok: 1 dB
- Dla kazdego punktu: symulacja z duzą liczba bitow (np. 10000)

### Oczekiwane wyniki
- BPSK: najlepsza odpornosc na szum (BER maleje najszybciej)
- QPSK: podobna do BPSK dla tego samego Eb/N0
- 8-PSK: gorsza odpornosc (symbole blizej siebie)
- QAM: zalezy od konfiguracji

## Struktura plikow koncowych

```
ModulationPSKProject/
├── GetBytes.py              # [GOTOWE]
├── Modulator.py             # [BPSK gotowe, reszta do zrobienia]
├── AddAWGNNoise.py          # [GOTOWE]
├── Demodulator.py           # [DO ZROBIENIA]
├── TransmissionChannel.py   # [DO ZROBIENIA]
├── main.py                  # [DO ZROBIENIA]
├── requirements.txt         # [GOTOWE]
├── setup.sh                 # [GOTOWE]
├── setup.bat                # [GOTOWE]
├── README.md                # [DO AKTUALIZACJI]
├── INSTALLATION.md          # [GOTOWE]
├── PROJECT_ARCHITECTURE.md  # [TEN PLIK]
└── results/                 # [Katalog na wykresy]
    ├── ber_comparison.png
    ├── bpsk_constellation.png
    ├── qpsk_constellation.png
    ├── 8psk_constellation.png
    └── qam_constellation.png
```

## Zalecenia techniczne

1. **Konwencje nazewnicze:**
   - Funkcje: `lowercase_with_underscores`
   - Stale: `UPPERCASE_WITH_UNDERSCORES`
   - Klasy: `PascalCase`

2. **Dokumentacja:**
   - Kazda funkcja z docstringiem
   - Komentarze przy skomplikowanych obliczeniach
   - README z przykladami uzycia

3. **Testy:**
   - Weryfikacja poprawnosci modulacji/demodulacji
   - Test bez szumu (BER = 0)
   - Test z bardzo duzym szumem (BER → 0.5 dla BPSK)

4. **Optymalizacja:**
   - Wykorzystanie operacji wektorowych NumPy
   - Unikanie petli Python tam gdzie mozliwe
   - Efektywne generowanie szumu

## Referencje

- Wikipedia: Phase-shift keying
- Wikipedia: Quadrature amplitude modulation
- "Digital Communications" - John Proakis
- "Communication Systems" - Simon Haykin
