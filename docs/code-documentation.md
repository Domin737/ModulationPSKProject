# Dokumentacja kodu

## Wersja: 1.4.0

**STATUS: W PRZYGOTOWANIU**

Ten dokument bedzie zawierac szczegolowa dokumentacje techniczna kodu zrodlowego projektu ModulationPSKProject, w tym:

- Szczegolowy opis kazdego modulu
- Dokumentacje wszystkich funkcji i klas
- Wyjaśnienia teoretyczne algorytmow
- Przyklady uzycia
- Testy i walidacje
- Rozszerzenia i modyfikacje

---

## Spis tresci (planowany)

### 1. Wprowadzenie teoretyczne

- Teoria modulacji cyfrowych
- Matematyka kanalu AWGN
- Analiza BER

### 2. Modul GetBytes.py

- Funkcja gen_bites()
- Generator losowych bitow
- Przyklady i testy

### 3. Modul Modulator.py

- Modulacja BPSK
  - Teoria
  - Implementacja
  - Mapowanie bitow
- Modulacja QPSK
  - Teoria
  - Konstelacja
  - Mapowanie bitow
- Modulacja 8-PSK
- Modulacja QAM

### 4. Modul AddAWGNNoise.py

- Teoria szumu AWGN
- Model matematyczny
- Implementacja
- Parametry Eb/N0

### 5. Modul TransmissionChannel.py

- Model kanalu transmisyjnego
- AWGN channel
- Rozszerzenia (fading, interference)

### 6. Modul Demodulator.py

- Demodulacja BPSK
- Demodulacja QPSK
- Demodulacja 8-PSK
- Demodulacja QAM
- Metody detekcji

### 7. Modul main.py

- Glowna petla symulacji
- Obliczanie BER
- Generowanie wykresow
- Analiza wynikow

### 8. Przyklady uzycia

- Podstawowe przyklady
- Zaawansowane scenariusze
- Modyfikacje i rozszerzenia

### 9. Testy i walidacja

- Testy jednostkowe
- Testy integracyjne
- Walidacja wynikow

### 10. Rozszerzenia

- Jak dodac nowa modulacje
- Jak dodac nowy model kanalu
- Jak dodac korekcje bledow

---

## Uwaga

Ten dokument jest w trakcie przygotowania i bedzie dostepny w nastepnej wersji projektu.

W miedzyczasie, zapoznaj sie z:

- Komentarzami w kodzie zrodlowym (katalog `src/`)
- [Struktura projektu](project-structure.md) - przeglad architektury
- [Glowny README](../README.md) - przyklady uzycia

---

## Tymczasowe zrodla informacji

### Dla zrozumienia kodu:

1. **Przeczytaj kod zrodlowy:**

   - Wszystkie moduly w katalogu `src/`
   - Komentarze w kodzie

2. **Uruchom przyklady:**

   ```bash
   cd src
   python main.py
   ```

3. **Eksperymentuj:**

   ```python
   from GetBytes import gen_bites
   from Modulator import bpsk_modulation

   bits = gen_bites(10)
   print("Bits:", bits)

   symbols = bpsk_modulation(bits)
   print("Symbols:", symbols)
   ```

### Dla zrozumienia teorii:

1. **Wikipedia:**

   - [Phase-shift keying](https://en.wikipedia.org/wiki/Phase-shift_keying)
   - [QAM](https://en.wikipedia.org/wiki/Quadrature_amplitude_modulation)
   - [AWGN](https://en.wikipedia.org/wiki/Additive_white_Gaussian_noise)

2. **Ksiazki:**

   - "Digital Communications" - John Proakis
   - "Communication Systems" - Simon Haykin

3. **Kursy online:**
   - Coursera: Digital Signal Processing
   - MIT OpenCourseWare: Communication Systems

---

## Planowana data ukończenia

**Wersja 1.5.0** - Q1 2026

---

## Kontakt

Pytania dotyczace kodu mozna kierowac przez:

- Issues w repozytorium projektu
- E-mail do autora projektu

---

**Ostatnia aktualizacja:** 2025-10-22  
**Wersja dokumentu:** 1.4.0 (Placeholder)  
**Status:** W przygotowaniu
