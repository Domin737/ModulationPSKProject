# ModulationPSKProject - Indeks Dokumentacji

## Wersja: 1.4.0

Witaj w dokumentacji projektu ModulationPSKProject - systemu symulacji modulacji cyfrowych PSK i QAM.

---

## O projekcie

ModulationPSKProject to zaawansowane narzedzie edukacyjne i badawcze do symulacji systemow komunikacji cyfrowej. Projekt umozliwia:

- Symulacje roznych typow modulacji (BPSK, QPSK, 8-PSK, QAM)
- Modelowanie kanalu transmisyjnego z szumem AWGN
- Analize wydajnosci transmisji (BER vs Eb/N0)
- Wizualizacje konstelacji i charakterystyk

---

## Nawigacja po dokumentacji

### 📋 Podstawowe informacje

#### 1. [Wymagania i srodowisko](requirements-and-environment.md)

Szczegolowe informacje o wymaganiach systemowych, potrzebnych bibliotekach i konfiguracji srodowiska.

**Zawiera:**

- Wymagania systemowe (Python, system operacyjny, RAM)
- Wymagane biblioteki Python (NumPy, SciPy, Matplotlib)
- Wymagania dodatkowe dla roznych systemow operacyjnych
- Konfiguracja srodowiska wirtualnego
- Weryfikacja instalacji

**Czas czytania:** ~5 minut

---

#### 2. [Instrukcja instalacji](installation.md)

Krok po kroku instrukcje instalacji dla roznych systemow operacyjnych.

**Zawiera:**

- Instalacja na Windows (z graficznymi instrukcjami)
- Instalacja na Linux (Ubuntu, Fedora, inne dystrybucje)
- Instalacja na macOS
- Rozwiazywanie problemow instalacyjnych
- Weryfikacja poprawnej instalacji
- Manualna instalacja (dla zaawansowanych uzytkownikow)

**Czas czytania:** ~10 minut  
**Czas instalacji:** 5-15 minut

---

#### 3. [Struktura projektu](project-structure.md)

Szczegolowy opis struktury katalogowej i organizacji kodu.

**Zawiera:**

- Diagram struktury katalogowej
- Opis kazdego katalogu i pliku
- Diagram przeplywu danych
- Architektura modulow
- Zaleznosci miedzy modulami
- Wzorce projektowe uzyte w projekcie

**Czas czytania:** ~15 minut

---

### 🔧 Szczegoly techniczne

#### 4. [Obsluga bledow](error-handling.md)

Kompletny przewodnik po bledach i ich rozwiazaniach.

**Zawiera:**

- Bledy instalacji (Python, pip, venv)
- Bledy importu modulow
- Bledy wykonania (NumPy, SciPy, Matplotlib)
- Bledy w obliczeniach i symulacjach
- Problemy z wydajnoscia
- Diagnostyka i debugowanie
- FAQ - czeste pytania i odpowiedzi

**Czas czytania:** ~10 minut  
**Referencyjny:** Przegladaj gdy napotkasz problem

---

#### 5. [Dokumentacja kodu](code-documentation.md)

Szczegolowa dokumentacja techniczna kodu zrodlowego.

**Zawiera:**

- Opis kazdego modulu Python
- Dokumentacja funkcji i klas
- Przyklady uzycia
- Wyjaśnienia teoretyczne
- Algorytmy i implementacje
- Testy i walidacja
- Rozszerzenia i modyfikacje

**Czas czytania:** ~30-45 minut  
**Status:** Dokument szczegolowy dla programistow

---

## Porzadek czytania dokumentacji

### Dla poczatkujacych

Jesli dopiero zaczynasz z projektem, przeczytaj dokumenty w nastepujacej kolejnosci:

1. **Ten plik (index.md)** - uzyskaj ogolny przeglad
2. **[Wymagania i srodowisko](requirements-and-environment.md)** - sprawdz czy Twoj system spelnia wymagania
3. **[Instrukcja instalacji](installation.md)** - zainstaluj projekt
4. **[Struktura projektu](project-structure.md)** - poznaj organizacje projektu
5. **Glowny README.md** (w katalogu glownym) - przyklady uzycia
6. W razie problemow: **[Obsluga bledow](error-handling.md)**

**Calkowity czas:** ~30-40 minut

---

### Dla zaawansowanych uzytkownikow

Jesli znasz podstawy i chcesz zaglebic sie w szczegoly:

1. **[Struktura projektu](project-structure.md)** - architektura
2. **[Dokumentacja kodu](code-documentation.md)** - szczegoly implementacji
3. Kod zrodlowy w katalogu `src/`
4. W razie potrzeby: **[Obsluga bledow](error-handling.md)**

**Calkowity czas:** ~1-2 godziny

---

### Dla programistow chcacych modyfikowac kod

Jesli planujesz rozwijac lub modyfikowac projekt:

1. **[Struktura projektu](project-structure.md)** - poznaj architekture
2. **[Dokumentacja kodu](code-documentation.md)** - szczegoly implementacji
3. **Kod zrodlowy** - przeczytaj i przeanalizuj
4. **[Wymagania i srodowisko](requirements-and-environment.md)** - srodowisko developerskie
5. **[Obsluga bledow](error-handling.md)** - debugowanie

**Calkowity czas:** ~2-3 godziny

---

## Szybkie linki

### Instalacja

- [Wymagania systemowe](requirements-and-environment.md#wymagania-systemowe)
- [Instalacja Windows](installation.md#windows)
- [Instalacja Linux](installation.md#linux)
- [Instalacja macOS](installation.md#macos)

### Korzystanie z projektu

- [Szybki start](../README.md#szybki-start)
- [Przyklady uzycia](../README.md#uzycie)
- [Podstawy teoretyczne](../README.md#podstawy-teoretyczne)

### Pomoc

- [Czeste problemy](error-handling.md#czeste-problemy)
- [FAQ](error-handling.md#faq)
- [Rozwiazywanie problemow](error-handling.md#diagnostyka)

### Kod

- [Struktura katalogow](project-structure.md#struktura-katalogowa)
- [Moduly projektu](code-documentation.md#moduly)
- [API funkcji](code-documentation.md#api-reference)

---

## Konwencje uzyte w dokumentacji

### Oznaczenia

- ✅ **Gotowe** - w pelni zaimplementowane i przetestowane
- ⚠️ **W trakcie** - czesc funkcjonalnosci dostepna
- ❌ **Brak** - nie zaimplementowane
- 📋 **Dokumentacja** - dodatkowe informacje
- 🔧 **Techniczne** - szczegoly implementacji
- 💡 **Wskazowka** - pomocna informacja
- ⚡ **Uwaga** - wazna informacja

### Bloki kodu

```python
# Przyklad kodu Python
import numpy as np
```

```bash
# Komendy terminala/CMD
python main.py
```

### Struktura katalogowa

```
katalog/
├── plik1.py
└── plik2.py
```

---

## Slowa kluczowe

Aby szybko znalezc informacje na okreslony temat, uzyj:

- **Instalacja**: [Instrukcja instalacji](installation.md)
- **Python**: [Wymagania](requirements-and-environment.md#python)
- **NumPy, SciPy, Matplotlib**: [Biblioteki](requirements-and-environment.md#biblioteki)
- **BPSK, QPSK, 8-PSK, QAM**: [Dokumentacja kodu](code-documentation.md#modulacje)
- **BER**: [Dokumentacja kodu](code-documentation.md#analiza-ber)
- **Eb/N0**: [Dokumentacja kodu](code-documentation.md#parametry-kanalu)
- **AWGN**: [Dokumentacja kodu](code-documentation.md#szum-awgn)
- **Bledy**: [Obsluga bledow](error-handling.md)
- **Struktura**: [Struktura projektu](project-structure.md)

---

## Wersja dokumentacji

- **Wersja projektu:** 1.4.0
- **Wersja dokumentacji:** 1.4.0
- **Data ostatniej aktualizacji:** 2025-10-22
- **Status:** Kompletna i aktualna

---

## Informacje dodatkowe

### Wymagana wiedza

Aby efektywnie korzystac z projektu, przydatna bedzie podstawowa wiedza z zakresu:

- **Programowanie w Python** (poziom podstawowy)
- **Przetwarzanie sygnalow** (poziom podstawowy)
- **Systemy telekomunikacyjne** (poziom podstawowy - opcjonalnie)

### Czas potrzebny na naukę

- **Instalacja i pierwsze uruchomienie:** 15-30 minut
- **Podstawowe uzycie:** 1-2 godziny
- **Zaawansowane uzycie:** 4-6 godzin
- **Pelne zrozumienie i modyfikacja kodu:** 8-12 godzin

### Wsparcie

W przypadku pytan lub problemow:

1. Sprawdz [Obsluge bledow](error-handling.md)
2. Przeczytaj [FAQ](error-handling.md#faq)
3. Sprawdz glowny [README.md](../README.md)

---

## Mapa dokumentacji

```
docs/
├── index.md (TEN PLIK)
│   └── Punkt wyjscia - nawigacja po dokumentacji
│
├── requirements-and-environment.md
│   └── Wymagania systemowe i konfiguracja srodowiska
│
├── installation.md
│   └── Szczegolowe instrukcje instalacji dla kazdego OS
│
├── project-structure.md
│   └── Architektura i organizacja projektu
│
├── error-handling.md
│   └── Rozwiazywanie problemow i czeste bledy
│
└── code-documentation.md
    └── Dokumentacja techniczna kodu zrodlowego
```

---

## Kolejne kroki

Po przeczytaniu tej strony:

1. Jesli jeszcze nie zainstalowałes projektu:
   → Przejdz do [Instrukcji instalacji](installation.md)

2. Jesli projekt juz działa:
   → Przejdz do glownego [README.md](../README.md) i zobacz przyklady uzycia

3. Jesli chcesz poznac szczegoly:
   → Przejdz do [Dokumentacji kodu](code-documentation.md)

4. Jesli masz problemy:
   → Przejdz do [Obslugi bledow](error-handling.md)

---

**Powodzenia w pracy z ModulationPSKProject!** 🚀

---

_Dokumentacja stworzona dla projektu ModulationPSKProject v1.4.0_  
_Ostatnia aktualizacja: 2025-10-22_
