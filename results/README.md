# Results Directory

## Przeznaczenie

Ten katalog jest przeznaczony do przechowywania wynikow symulacji projektu ModulationPSKProject.

## Zawartosc

Po uruchomieniu symulacji (python src/main.py), w tym katalogu pojawia sie:

### Wykresy BER (Bit Error Rate)

- `bpsk_ber_curve.png` - Wykres BER vs Eb/N0 dla modulacji BPSK
- `qpsk_ber_curve.png` - Wykres BER vs Eb/N0 dla modulacji QPSK
- `8psk_ber_curve.png` - Wykres BER vs Eb/N0 dla modulacji 8-PSK
- `qam16_ber_curve.png` - Wykres BER vs Eb/N0 dla modulacji 16-QAM
- `qam64_ber_curve.png` - Wykres BER vs Eb/N0 dla modulacji 64-QAM
- `comparison_all_modulations.png` - Porownanie wszystkich modulacji na jednym wykresie

### Diagramy konstelacji

- `bpsk_constellation.png` - Diagram konstelacji BPSK
- `qpsk_constellation.png` - Diagram konstelacji QPSK
- `8psk_constellation.png` - Diagram konstelacji 8-PSK
- `qam16_constellation.png` - Diagram konstelacji 16-QAM
- `qam64_constellation.png` - Diagram konstelacji 64-QAM

### Diagramy konstelacji z szumem

- `bpsk_constellation_noisy.png` - Diagram konstelacji BPSK po przejsciu przez kanal
- `qpsk_constellation_noisy.png` - Diagram konstelacji QPSK po przejsciu przez kanal
- `8psk_constellation_noisy.png` - Diagram konstelacji 8-PSK po przejsciu przez kanal
- `qam16_constellation_noisy.png` - Diagram konstelacji 16-QAM po przejsciu przez kanal

### Dane surowe (opcjonalnie)

- `simulation_data.csv` - Dane surowe z symulacji w formacie CSV
- `ber_results.txt` - Wyniki BER w formacie tekstowym

## Format plikow

### Wykresy PNG

- Rozdzielczosc: 1920x1080 px (lub inna ustawiona w kodzie)
- DPI: 300 (dla wysokiej jakosci)
- Format: PNG z przezroczystoscia

### Wykresy PDF (opcjonalnie)

- Format wektorowy dla publikacji naukowych
- Wysokiej jakosci skalowanie

### Dane CSV

```csv
Eb_N0_dB,BER_BPSK,BER_QPSK,BER_8PSK,BER_QAM16
0,0.078,0.095,0.156,0.234
1,0.062,0.078,0.132,0.198
...
```

## Uwagi

- Ten katalog jest ignorowany przez Git (.gitignore), aby nie wersjonowac duzych plikow wynikow
- Wykresy sa generowane automatycznie podczas kazdego uruchomienia symulacji
- Poprzednie wyniki moga byc nadpisane - zrob kopie waznych wynikow przed ponownym uruchomieniem
- Jesli katalog nie istnieje, zostanie utworzony automatycznie przez skrypt instalacyjny

## Czyszczenie wynikow

Aby usunac wszystkie wyniki:

**Windows:**

```cmd
del /Q results\*.png
del /Q results\*.pdf
del /Q results\*.csv
```

**Linux/Mac:**

```bash
rm -f results/*.png
rm -f results/*.pdf
rm -f results/*.csv
```

## Eksport wynikow

Wyniki moga byc eksportowane do:

- Prezentacji (PowerPoint, Google Slides)
- Raportow (Word, LaTeX)
- Publikacji naukowych
- Stron internetowych

## Rozmiar plikow

Przyblizone rozmiary plikow:

- Wykres PNG (pojedynczy): ~200-500 KB
- Wykres PDF (pojedynczy): ~50-150 KB
- Dane CSV: ~10-100 KB (zalezne od liczby punktow)

Calkowity rozmiar po pelnej symulacji: ~5-10 MB

## Lokalizacja

```
ModulationPSKProject/
└── results/              ← Ten katalog
    ├── .gitkeep
    ├── README.md         ← Ten plik
    └── (wygenerowane pliki wynikow)
```

## Dodatkowe informacje

Wiecej informacji o wynikach symulacji znajdziesz w:

- [Glowny README](../README.md)
- [Dokumentacja kodu](../docs/code-documentation.md)
- [Instrukcja uzycia](../docs/installation.md)

---

**Ostatnia aktualizacja:** 2025-10-22  
**Wersja:** 1.4.0
