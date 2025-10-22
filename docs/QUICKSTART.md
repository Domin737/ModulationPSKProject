# Quick Start Guide

Szybki start dla projektu ModulationPSKProject

## Krok 1: Konfiguracja (2 minuty)

### Windows
```bash
setup.bat
```

### Linux/Mac
```bash
chmod +x setup.sh
./setup.sh
```

## Krok 2: Test srodowiska (30 sekund)

Aktywuj srodowisko:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

Uruchom test:
```bash
python test_environment.py
```

Powinnas zobaczyc: `✓ Wszystkie testy przeszly pomyslnie!`

## Krok 3: Zrozumienie struktury projektu

### Co juz dziala:
- ✓ `GetBytes.py` - generowanie bitow
- ✓ `Modulator.py` - modulacja BPSK
- ✓ `AddAWGNNoise.py` - dodawanie szumu

### Co wymaga implementacji:
- ⚠ `TransmissionChannel.py` - kanal transmisyjny
- ⚠ `Demodulator.py` - demodulatory
- ⚠ `main.py` - symulacje i wykresy

## Krok 4: Plan dzialania

Rekomendowana kolejnosc implementacji:

1. **TransmissionChannel.py** (15 min)
   - Funkcja symulujaca kanal z szumem

2. **Demodulator.py - BPSK** (20 min)
   - Demodulacja BPSK (decyzja progowa)

3. **main.py - podstawowa symulacja** (30 min)
   - Symulacja BPSK
   - Obliczanie BER
   - Prosty wykres

4. **Rozszerzenie o QPSK** (45 min)
   - Modulator QPSK
   - Demodulator QPSK
   - Testy

5. **Rozszerzenie o 8-PSK i QAM** (60 min)
   - Analogicznie jak QPSK

6. **Finalizacja** (30 min)
   - Dokumentacja
   - Wykresy porownawcze
   - README

## Krok 5: Szczegolowa dokumentacja

Przeczytaj:
- `INSTALLATION.md` - szczegoly instalacji
- `PROJECT_ARCHITECTURE.md` - architektura i plan
- `README.md` - ogolny przeglad

## Przydatne komendy

### Uruchomienie programu
```bash
python main.py
```

### Uruchomienie konkretnego modulu (test)
```bash
python Modulator.py
python AddAWGNNoise.py
```

### Instalacja dodatkowych pakietow
```bash
pip install nazwa_pakietu
```

### Zamrożenie zaleznosci
```bash
pip freeze > requirements.txt
```

## Wskazowki

1. **Zacznij od testow** - upewnij sie ze rozumiesz jak dziala istniejacy kod
2. **Malymi krokami** - implementuj po jednej funkcji i testuj
3. **Uzywaj konstelacji** - wizualizacja pomaga zrozumiec modulacje
4. **Testuj bez szumu** - najpierw sprawdz czy modulacja/demodulacja dziala idealnie

## Kontakt i pomoc

Jesli masz pytania dotyczace:
- **Teorii**: sprawdz Wikipedia (Phase-shift keying, QAM)
- **Kodu**: sprawdz komentarze w plikach projektu
- **Instalacji**: sprawdz INSTALLATION.md
- **Architektury**: sprawdz PROJECT_ARCHITECTURE.md

## Checkpoints

Po kazdym etapie powinienes byc w stanie:

- [ ] Srodowisko skonfigurowane i przetestowane
- [ ] Rozumiem strukture projektu
- [ ] TransmissionChannel.py zaimplementowane
- [ ] Demodulator BPSK dziala
- [ ] main.py generuje wykres BER dla BPSK
- [ ] QPSK zaimplementowane i przetestowane
- [ ] 8-PSK zaimplementowane
- [ ] QAM zaimplementowane
- [ ] Pelna dokumentacja gotowa
- [ ] Wszystkie wykresy wygenerowane

Powodzenia!
