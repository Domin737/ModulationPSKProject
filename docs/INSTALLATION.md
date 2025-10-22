# Instrukcja konfiguracji srodowiska

## Wymagania wstepne

- Python 3.8 lub nowszy (Twoj kolega uzywa Python 3.13)
- pip (menadzer pakietow Python)
- Git (opcjonalnie, do klonowania repozytorium)

## Krok 1: Weryfikacja instalacji Python

### Windows
Otworz CMD lub PowerShell i uruchom:
```bash
python --version
```

### Linux/Mac
Otworz terminal i uruchom:
```bash
python3 --version
```

Powinnas zobaczyc wersje Pythona (np. Python 3.13.0).

## Krok 2: Przejscie do katalogu projektu

```bash
cd sciezka/do/ModulationPSKProject
```

## Krok 3: Konfiguracja srodowiska

### Opcja A: Automatyczna instalacja (zalecana)

#### Windows
```bash
setup.bat
```

#### Linux/Mac
```bash
chmod +x setup.sh
./setup.sh
```

### Opcja B: Manualna instalacja

#### 1. Utworzenie wirtualnego srodowiska

**Windows:**
```bash
python -m venv venv
```

**Linux/Mac:**
```bash
python3 -m venv venv
```

#### 2. Aktywacja wirtualnego srodowiska

**Windows (CMD):**
```bash
venv\Scripts\activate.bat
```

**Windows (PowerShell):**
```bash
venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

Po aktywacji zobaczysz `(venv)` przed promptem terminala.

#### 3. Instalacja zaleznosci

```bash
pip install -r requirements.txt
```

## Krok 4: Weryfikacja instalacji

Sprawdz czy wszystkie biblioteki zostaly zainstalowane:

```bash
pip list
```

Powinny byc widoczne:
- numpy
- scipy
- matplotlib

## Krok 5: Testowe uruchomienie

```bash
python main.py
```

## Dezaktywacja srodowiska

Gdy skonczysz prace, dezaktywuj srodowisko:

```bash
deactivate
```

## Rozwiazywanie problemow

### Problem: "python" nie jest rozpoznawany
**Rozwiazanie:** Uzyj `python3` zamiast `python` (Linux/Mac) lub sprawdz czy Python jest dodany do PATH (Windows).

### Problem: Blad przy aktywacji venv na Windows PowerShell
**Rozwiazanie:** Uruchom PowerShell jako administrator i wykonaj:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Problem: Brak modulu pip
**Rozwiazanie:** Zainstaluj pip:
```bash
python -m ensurepip --upgrade
```

## Struktura projektu

```
ModulationPSKProject/
├── venv/                    # Wirtualne srodowisko (utworzone po instalacji)
├── .idea/                   # Pliki PyCharm/IntelliJ
├── GetBytes.py              # Generator losowych bitow
├── Modulator.py             # Modulatory (BPSK, QPSK, 8-PSK, QAM)
├── AddAWGNNoise.py          # Dodawanie szumu AWGN
├── Demodulator.py           # Demodulatory
├── TransmissionChannel.py   # Model kanalu transmisyjnego
├── main.py                  # Glowny program
├── requirements.txt         # Lista zaleznosci
├── setup.sh                 # Skrypt instalacyjny (Linux/Mac)
├── setup.bat                # Skrypt instalacyjny (Windows)
└── README.md                # Dokumentacja projektu
```

## Kolejne kroki

Po pomyslnej konfiguracji mozesz przejsc do rozwoju projektu:

1. Implementacja pozostalych modulatorow (QPSK, 8-PSK, QAM)
2. Implementacja demodulatorow
3. Implementacja kanalu transmisyjnego
4. Stworzenie symulacji i generowanie wykresow
5. Analiza wynikow (BER vs Eb/N0)

## Wsparcie

W razie problemow sprawdz:
- Oficjalna dokumentacje Python: https://docs.python.org/
- Dokumentacje NumPy: https://numpy.org/doc/
- Dokumentacje SciPy: https://docs.scipy.org/
- Dokumentacje Matplotlib: https://matplotlib.org/
