# Code Documentation - ModulationPSKProject

## Wprowadzenie

Ten dokument wyjas nia jak dziala kod aplikacji ModulationPSKProject. Dla kazdego modulu przedstawiona jest teoria, fragmenty kodu z wyjas nieniami oraz przyklady numeryczne pokazujace dzialanie krok po kroku.

---

## 1. GetBytes.py - Generator losowych bitow

### Teoria

W systemach komunikacji cyfrowej informacja jest reprezentowana jako ciag bitow (0 i 1). Generator bitow to punkt startowy symulacji - tworzy losowe dane, ktore bedziemy transmitowac.

### Implementacja

```python
def gen_bites(n_bits):
    return np.random.randint(0, 2, size=n_bits)
```

**Dlaczego tak jest napisane:**

1. **`np.random.randint(0, 2, ...)`** - generuje losowe liczby calkowite z zakresu [0, 2), czyli 0 lub 1

   - Argument `0` - dolna granica (wlacznie)
   - Argument `2` - gorna granica (wylacznie)
   - Wynik: tylko wartosci 0 i 1

2. **`size=n_bits`** - okresl a rozmiar tablicy
   - Zwraca tablice NumPy zamiast pojedynczej wartosci
   - Tablica jest wydajniejsza niz lista Python przy duzych danych

**Przyklad numeryczny:**

```python
# Wywolanie:
bits = gen_bites(10)

# Mozliwy wynik:
# array([1, 0, 1, 1, 0, 0, 1, 0, 1, 1])

# Kazde wywolanie da inny wynik (losowe):
# array([0, 0, 1, 0, 1, 1, 0, 1, 0, 0])
```

---

## 2. Modulator.py - Modulacja cyfrowa

### 2.1 BPSK Modulation

#### Teoria

BPSK (Binary Phase-Shift Keying) to najprostsza modulacja fazowa:

- Mapuje kazdy bit na symbol zespolony
- Bit 0 → +1 (faza 0°)
- Bit 1 → -1 (faza 180°)

Dlaczego takie mapowanie? Bo:

1. Symbole sa maksymalnie oddalone (lepsza odpornosc na szum)
2. Srednia wartosc = 0 (brak skladowej DC)
3. Energia symbolu = 1 (normalizacja)

#### Implementacja

```python
def bpsk_modulation(bits):
    symbols = 1 - 2 * bits
    return symbols.astype(complex)
```

**Dlaczego wzor `1 - 2 * bits`:**

Przeanalizujmy transformacje:

- Gdy `bits = 0`: `symbols = 1 - 2*0 = 1 - 0 = +1` ✓
- Gdy `bits = 1`: `symbols = 1 - 2*1 = 1 - 2 = -1` ✓

Alternatywne podej scia i dlaczego NIE sa uzyte:

```python
# Metoda 1: Instrukcja warunkowa (WOLNIEJSZA)
symbols = np.where(bits == 0, 1, -1)  # Dziala, ale wolniej

# Metoda 2: Mapowanie slownikowe (NAJMNIEJ WYDAJNE)
mapping = {0: 1, 1: -1}
symbols = np.array([mapping[b] for b in bits])  # Bardzo wolne dla duzych danych

# Metoda 3: Nasza (NAJSZYBSZA)
symbols = 1 - 2 * bits  # Operacja wektorowa - szybka!
```

**Konwersja na `complex`:**

```python
return symbols.astype(complex)
```

Dlaczego? Choc BPSK ma tylko skladowa rzeczywista (I), konwersja na typ zespolony jest potrzebna bo:

1. Szum AWGN bedzie zespolony (I + jQ)
2. Inne modulacje (QPSK, QAM) maja skladowa urojona
3. Jednolity format dla wszystkich modulacji

#### Przyklad numeryczny krok po kroku

```python
# Wejscie:
bits = np.array([0, 1, 0, 1])

# Krok 1: Operacja 2 * bits
temp = 2 * bits
# temp = [0, 2, 0, 2]

# Krok 2: Operacja 1 - temp
symbols = 1 - temp
# symbols = [1, -1, 1, -1]

# Krok 3: Konwersja na complex
symbols = symbols.astype(complex)
# symbols = [1+0j, -1+0j, 1+0j, -1+0j]
```

**Wykres konstelacji BPSK:**

```
Imaginary (Q)
      ^
      |
      |
  -1  |  +1      <- Symbole na osi rzeczywistej
------+------> Real (I)
      |
      |
```

### 2.2 QPSK Modulation

#### Teoria

QPSK (Quadrature PSK) mapuje 2 bity na 1 symbol:

- Wydajnosc: 2 bity/symbol (2x wieksza niz BPSK)
- 4 punkty konstelacji rozmieszczone co 90°

**Kodowanie Graya** - sasiednie symbole roznia sie tylko 1 bitem:

```
  (-1+j)     (+1+j)
    01         00
      \       /
       \  |  /
        \ | /
    -----+-----
        / | \
       /  |  \
    11         10
  (-1-j)     (+1-j)
```

Dlaczego Gray coding? Gdy szum przesunie symbol do sasiedniego punktu, pomylka to tylko 1 bit (nie 2).

#### Implementacja - Mapowanie

```python
qpsk_map = {
    (0, 0): norm * (1 + 1j),   # 00 -> 45 degrees
    (0, 1): norm * (-1 + 1j),  # 01 -> 135 degrees
    (1, 1): norm * (-1 - 1j),  # 11 -> 225 degrees
    (1, 0): norm * (1 - 1j)    # 10 -> 315 degrees
}
```

**Dlaczego slownik zamiast formuly matematycznej:**

Dla QPSK z Gray coding nie ma prostej formuly jak dla BPSK. Mozliwe podej scia:

```python
# Metoda 1: Slownik (UZYTE) - czytelne, szybkie dla malych konstelacji
qpsk_map = {...}
symbols = [qpsk_map[tuple(pair)] for pair in bit_pairs]

# Metoda 2: Funkcja trygonometryczna (MOZLIWE) - uniwersalna, ale skomplikowana
angle = (bit0 * 2 + bit1) * np.pi/2 + np.pi/4  # Wymaga logiki Gray coding
symbol = np.exp(1j * angle)

# Metoda 3: Lookup table jako tablica (WYDAJNIEJSZE dla bardzo duzych danych)
constellation = np.array([1+1j, -1+1j, 1-1j, -1-1j]) / np.sqrt(2)
indices = bits[::2] * 2 + bits[1::2]
symbols = constellation[indices]
```

#### Normalizacja energii

```python
norm = 1 / np.sqrt(2)
```

**Dlaczego `1/sqrt(2)`:**

Chcemy aby energia symbolu = 1 (tak jak w BPSK).

```
Dla punktu (1+j):
|1+j|^2 = 1^2 + 1^2 = 2  <- Za duzo!

Po normalizacji ((1+j)/sqrt(2)):
|(1+j)/sqrt(2)|^2 = (1^2 + 1^2) / 2 = 2/2 = 1 ✓
```

Matematycznie:

```
E[|s|^2] = 1  <- Chcemy jednostkowa energie
|s|^2 = |a + jb|^2 = a^2 + b^2 = 1^2 + 1^2 = 2
norm = 1/sqrt(2) aby: norm^2 * 2 = 1
```

#### Przyklad numeryczny

```python
# Wejscie:
bits = np.array([0, 0, 0, 1, 1, 1, 1, 0])

# Krok 1: Reshape na pary
bit_pairs = bits.reshape(-1, 2)
# bit_pairs = [[0,0], [0,1], [1,1], [1,0]]

# Krok 2: Normalizacja
norm = 1 / np.sqrt(2)  # norm ≈ 0.7071

# Krok 3: Mapowanie
# Para [0,0] -> norm * (1+1j) = 0.7071 + 0.7071j
# Para [0,1] -> norm * (-1+1j) = -0.7071 + 0.7071j
# Para [1,1] -> norm * (-1-1j) = -0.7071 - 0.7071j
# Para [1,0] -> norm * (1-1j) = 0.7071 - 0.7071j

symbols = [0.7071+0.7071j, -0.7071+0.7071j, -0.7071-0.7071j, 0.7071-0.7071j]

# Weryfikacja energii:
|0.7071+0.7071j|^2 = 0.7071^2 + 0.7071^2 = 0.5 + 0.5 = 1.0 ✓
```

### 2.3 8-PSK Modulation

#### Teoria

8-PSK mapuje 3 bity na 1 symbol:

- Wydajnosc: 3 bity/symbol
- 8 punktow rowno rozmieszczonych na okregu
- Katy: 0°, 45°, 90°, 135°, 180°, 225°, 270°, 315°

**Trade-off:** Wieksza wydajnosc, ale gorsza odpornosc na szum (punkty blizej siebie).

#### Implementacja

```python
angles = np.array([0, 1, 3, 2, 6, 7, 5, 4]) * np.pi / 4
constellation = np.exp(1j * angles)
```

**Dlaczego tablica katow `[0, 1, 3, 2, 6, 7, 5, 4]`:**

To kodowanie Graya dla 8-PSK! Sekwencja nie jest [0,1,2,3,4,5,6,7] bo chcemy aby sasiednie symbole na okregu roznily sie tylko 1 bitem:

```
Indeks bitowy | Kat (*pi/4) | Bity (Gray)
--------------|-------------|------------
     000      |      0      |    000
     001      |      1      |    001
     011      |      3      |    011  <- Uwaga: zmiana pozycji
     010      |      2      |    010
     110      |      6      |    110
     111      |      7      |    111
     101      |      5      |    101
     100      |      4      |    100
```

**Formula Eulera:**

```python
constellation = np.exp(1j * angles)
```

Wykorzystuje wzor Eulera: `e^(j*θ) = cos(θ) + j*sin(θ)`

Przyklad:

```
angle = pi/4 (45 degrees)
symbol = e^(j*pi/4) = cos(45°) + j*sin(45°)
       = 0.7071 + j*0.7071
```

**Dlaczego nie uzywamy cos() i sin() oddzielnie:**

```python
# Metoda 1: Formula Eulera (UZYTE) - krotsza, czytelniejsza
constellation = np.exp(1j * angles)

# Metoda 2: Cos i Sin oddzielnie (DLUZSZE)
constellation = np.cos(angles) + 1j * np.sin(angles)

# Oba daja ten sam wynik, ale exp() jest:
# 1. Krotsza w zapisie
# 2. Szybsza obliczeniowo (jedna funkcja zamiast dwoch)
# 3. Bardziej czytelna matematycznie
```

#### Przyklad numeryczny

```python
# Wejscie:
bits = np.array([0, 0, 0, 0, 0, 1, 0, 1, 1])

# Krok 1: Reshape na trojki
bit_triplets = bits.reshape(-1, 3)
# bit_triplets = [[0,0,0], [0,0,1], [0,1,1]]

# Krok 2: Konwersja binarnie-dziesietnie
# [0,0,0] -> 0*4 + 0*2 + 0*1 = 0
# [0,0,1] -> 0*4 + 0*2 + 1*1 = 1
# [0,1,1] -> 0*4 + 1*2 + 1*1 = 3

indices = [0, 1, 3]

# Krok 3: Mapowanie na katy (Gray coding)
angles_rad = [0, 1, 3] * np.pi/4
# angles_rad = [0, pi/4, 3*pi/4]

# Krok 4: Utworzenie symboli
# Symbol 0: e^(j*0) = cos(0) + j*sin(0) = 1 + 0j
# Symbol 1: e^(j*pi/4) = cos(45°) + j*sin(45°) = 0.7071 + 0.7071j
# Symbol 3: e^(j*3*pi/4) = cos(135°) + j*sin(135°) = -0.7071 + 0.7071j

symbols = [1+0j, 0.7071+0.7071j, -0.7071+0.7071j]
```

### 2.4 QAM-16 Modulation

#### Teoria

16-QAM (Quadrature Amplitude Modulation):

- 4 bity na symbol (najwyzsza wydajnosc)
- 16 punktow w siatce 4×4
- Rozne amplitudy I FAZY (nie tylko fazy jak PSK)

**Struktura:**

- Pierwsze 2 bity → skladowa I (in-phase)
- Ostatnie 2 bity → skladowa Q (quadrature)

**Poziomy PAM-4:** {-3, -1, +1, +3}

#### Implementacja - PAM-4 Mapping

```python
pam4_map = {
    (0, 0): -3,
    (0, 1): -1,
    (1, 1): +1,
    (1, 0): +3
}
```

**Dlaczego takie mapowanie:**

1. **Kodowanie Graya** - sasiednie poziomy roznia sie 1 bitem:

   ```
   -3      -1      +1      +3
   00      01      11      10
   ```

2. **Symetryczne poziomy** - dla prostoty detekcji:

   ```
   Progi detekcji: -2, 0, +2

   -3  |  -1  |  +1  |  +3
       -2     0      +2
   ```

3. **Nieparzystosc {-3,-1,+1,+3}** - dlaczego nie {-2,-1,+1,+2}?
   - Nieparzystosc daje wieksza odleglosc miedzy punktami
   - Lepsza odpornosc na szum

#### Normalizacja QAM

```python
norm = 1 / np.sqrt(10)
symbols = symbols * norm
```

**Dlaczego `1/sqrt(10)`:**

Obliczmy srednia energie symbolu QAM bez normalizacji:

```
Wszystkie mozliwe symbole (I+jQ):
(-3-3j), (-3-1j), (-3+1j), (-3+3j),
(-1-3j), (-1-1j), (-1+1j), (-1+3j),
(+1-3j), (+1-1j), (+1+1j), (+1+3j),
(+3-3j), (+3-1j), (+3+1j), (+3+3j)

Energia jednego symbolu:
E = |I + jQ|^2 = I^2 + Q^2

Dla (±3, ±3): E = 9 + 9 = 18  (4 symbole)
Dla (±3, ±1): E = 9 + 1 = 10  (8 symboli)
Dla (±1, ±1): E = 1 + 1 = 2   (4 symbole)

Srednia energia:
E_avg = (4*18 + 8*10 + 4*2) / 16
      = (72 + 80 + 8) / 16
      = 160 / 16
      = 10

Normalizacja: norm = 1/sqrt(10) aby E_avg = 1
```

#### Przyklad numeryczny

```python
# Wejscie:
bits = np.array([0, 0, 0, 0, 1, 1, 1, 1])

# Krok 1: Reshape na czworki
bit_groups = bits.reshape(-1, 4)
# bit_groups = [[0,0,0,0], [1,1,1,1]]

# Krok 2: Podzial na I i Q
# Symbol 1: I_bits=[0,0], Q_bits=[0,0]
# Symbol 2: I_bits=[1,1], Q_bits=[1,1]

# Krok 3: Mapowanie PAM-4
# [0,0] -> -3
# [1,1] -> +1

# Symbol 1: I=-3, Q=-3 -> -3-3j
# Symbol 2: I=+1, Q=+1 -> +1+1j

symbols_unnorm = [-3-3j, +1+1j]

# Krok 4: Normalizacja
norm = 1/np.sqrt(10)  # norm ≈ 0.316

symbols = symbols_unnorm * norm
# Symbol 1: (-3-3j) * 0.316 = -0.949 - 0.949j
# Symbol 2: (+1+1j) * 0.316 = +0.316 + 0.316j

# Weryfikacja energii:
|-0.949 - 0.949j|^2 = 0.949^2 + 0.949^2 = 0.9 + 0.9 = 1.8
|+0.316 + 0.316j|^2 = 0.316^2 + 0.316^2 = 0.1 + 0.1 = 0.2

# Srednia: (1.8 + 0.2) / 2 = 1.0 ✓
```

**Wykres konstelacji 16-QAM:**

```
        Q
        ^
        |
    o o o o   <- poziomy: +3
    o o o o   <- poziomy: +1
--------|---------> I
    o o o o   <- poziomy: -1
    o o o o   <- poziomy: -3
        |
   -3  -1 +1 +3
```

---

## 3. AddAWGNNoise.py - Szum AWGN

### Teoria

**AWGN** (Additive White Gaussian Noise):

- **Additive**: dodawany do sygnalu (nie multiplikatywny)
- **White**: rowna moc w calym pasmie czestotliwosci
- **Gaussian**: rozklad normalny (Gaussa)

**Eb/N0** - Energy per bit to Noise power spectral density ratio:

- Miara jakosci kanalu
- W dB: wyzsze = lepszy kanal = mniej szumu
- Typowy zakres: -5 dB do 15 dB

### Implementacja - Konwersja Eb/N0

```python
eb_n0 = 10 ** (eb_n0_db / 10.0)
```

**Dlaczego ta formula:**

Konwersja z decybeli (dB) na skale liniowa:

```
dB = 10 * log10(linear)
Odwrotnie:
linear = 10^(dB/10)

Przyklad:
Eb/N0 = 10 dB
eb_n0 = 10^(10/10) = 10^1 = 10  (skala liniowa)
```

**Dlaczego Eb/N0 w dB:**

- Wygodniejsze: zakres 0-15 zamiast 1-1000000
- Standardowe w telekomunikacji
- Latwe porownywanie logarytmiczne

### Moc szumu

```python
eb = 1.0
n0 = eb / eb_n0
sigma = np.sqrt(n0 / 2)
```

**Matematyka krok po kroku:**

1. **Normalizacja energii bitu:**

   ```
   Eb = 1.0  <- Zakl adamy znormalizowana energie
   ```

2. **Obliczenie N0:**

   ```
   N0 = Eb / (Eb/N0)

   Przyklad: Eb/N0 = 10 (linear)
   N0 = 1.0 / 10 = 0.1
   ```

3. **Obliczenie odchylenia standardowego:**
   ```
   sigma = sqrt(N0 / 2)
   ```

**Dlaczego N0/2:**

Szum zespolony ma dwie niezalezne skladowe (I i Q):

```
Calkowita moc szumu = N0
Moc w I = N0/2
Moc w Q = N0/2

Odchylenie std dla kazdej skladowej:
sigma_I = sigma_Q = sqrt(N0/2)
```

Matematycznie dla zmiennej Gaussowskiej:

```
Variance = sigma^2
Moc = E[X^2] = sigma^2

Dla szumu zespolonego:
Moc_total = Moc_I + Moc_Q = sigma^2 + sigma^2 = 2*sigma^2

Wiec:
N0 = 2*sigma^2
sigma = sqrt(N0/2)
```

### Generowanie szumu

```python
noise_i = sigma * np.random.normal(0, 1, size=n_symbols)
noise_q = sigma * np.random.normal(0, 1, size=n_symbols)
awgn_noise = noise_i + 1j * noise_q
```

**Dlaczego dwie niezalezne skladowe:**

1. **Szum fizyczny** w systemie radiowym ma dwa wymiary:

   - I (in-phase) - skladowa zgodna w fazie
   - Q (quadrature) - skladowa przesunieta o 90°

2. **Niezaleznosc** I i Q:

   ```python
   np.random.normal(0, 1, size=n)  <- Niezalezne wywolania
   ```

   Generujemy dwa osobne ciagi losowe

3. **Kombinacja zespolona:**
   ```python
   noise = noise_i + 1j * noise_q
   ```
   Tworzy szum zespolony o odpowiedniej mocy

### Przyklad numeryczny

```python
# Parametry:
symbols = np.array([1.0, -1.0], dtype=complex)
eb_n0_db = 10.0

# Krok 1: Konwersja Eb/N0 z dB
eb_n0 = 10^(10/10) = 10

# Krok 2: Obliczenie N0
eb = 1.0
n0 = 1.0 / 10 = 0.1

# Krok 3: Obliczenie sigma
sigma = sqrt(0.1 / 2) = sqrt(0.05) = 0.2236

# Krok 4: Generowanie szumu
# (przykladowe wartosci z rozkladu normalnego)
noise_i = 0.2236 * [-0.5, 0.3] = [-0.112, 0.067]
noise_q = 0.2236 * [0.8, -0.2] = [0.179, -0.045]

# Krok 5: Szum zespolony
noise = [-0.112+0.179j, 0.067-0.045j]

# Krok 6: Dodanie szumu
received = symbols + noise
received = [1.0-0.112+0.179j, -1.0+0.067-0.045j]
received = [0.888+0.179j, -0.933-0.045j]

# Weryfikacja mocy szumu:
Srednia moc = E[|noise|^2]
            = (0.112^2 + 0.179^2 + 0.067^2 + 0.045^2) / 2
            = (0.0125 + 0.032 + 0.0045 + 0.002) / 2
            = 0.051 / 2 ≈ 0.025

# To odpowiada: sigma^2 * 2 = 0.2236^2 * 2 = 0.05 * 2 = 0.1 = N0 ✓
```

**Wplyw Eb/N0 na szum:**

```
Eb/N0 = 0 dB  (eb_n0=1):
  N0 = 1.0 / 1 = 1.0
  sigma = sqrt(0.5) = 0.707  <- Duzy szum!

Eb/N0 = 10 dB (eb_n0=10):
  N0 = 1.0 / 10 = 0.1
  sigma = sqrt(0.05) = 0.224  <- Sredni szum

Eb/N0 = 20 dB (eb_n0=100):
  N0 = 1.0 / 100 = 0.01
  sigma = sqrt(0.005) = 0.071  <- Maly szum!
```

---

## 4. TransmissionChannel.py - Kanal transmisyjny

### Teoria

Model kanalu transmisyjnego symuluje co dzieje sie z sygnalem pomiedzy nadajnikiem a odbiornikiem. W najprostszym modelu (AWGN):

```
y(t) = x(t) + n(t)

gdzie:
x(t) - sygnal nadany
n(t) - szum AWGN
y(t) - sygnal odebrany
```

### Implementacja

```python
def transmission_channel(symbols, eb_n0_db):
    received_symbols = add_awgn_noise(symbols, eb_n0_db)
    return received_symbols
```

**Dlaczego tak prosta funkcja:**

1. **Separacja odpowiedzialnosci (Separation of Concerns):**

   ```python
   # Zle podejscie - wszystko w jednym miejscu:
   def transmission_channel(symbols, eb_n0_db):
       eb_n0 = 10 ** (eb_n0_db / 10.0)
       eb = 1.0
       n0 = eb / eb_n0
       sigma = np.sqrt(n0 / 2)
       # ... caly kod generacji szumu ...

   # Dobre podejscie - modularna struktura:
   def transmission_channel(symbols, eb_n0_db):
       return add_awgn_noise(symbols, eb_n0_db)
   ```

2. **Latwos c rozszerzenia:**

   ```python
   # W przyszlosci mozna dodac inne typy kanalow:
   def transmission_channel(symbols, eb_n0_db, channel_type='awgn'):
       if channel_type == 'awgn':
           return add_awgn_noise(symbols, eb_n0_db)
       elif channel_type == 'rayleigh':
           return rayleigh_fading(symbols, eb_n0_db)
       elif channel_type == 'rician':
           return rician_fading(symbols, eb_n0_db)
   ```

3. **Czytelnosc kodu:**
   - Nazwa `transmission_channel` jasno mowi CO robi funkcja
   - Uzytkownik nie musi znac szczegolow implementacji szumu
   - API (interfejs) jest prosty

### Przyklad uzycia

```python
# Nadajnik:
bits = gen_bites(100)
symbols = bpsk_modulation(bits)

# Kanal (tutaj dzieje sie degradacja sygnalu):
received = transmission_channel(symbols, eb_n0_db=10)

# Odbiornik:
decoded = bpsk_demodulation(received)
```

**Co sie dzieje wewnatrz:**

```
symbols = [1+0j, -1+0j, 1+0j, -1+0j]
                    |
                    v
         transmission_channel()
                    |
                    v
            add_awgn_noise()
                    |
                    v
received = [0.95+0.12j, -0.88-0.15j, 1.03+0.08j, -1.12+0.05j]
            ^            ^             ^            ^
            |            |             |            |
      blisko +1    blisko -1     blisko +1    blisko -1
```

---

## 5. Demodulator.py - Demodulacja

### 5.1 BPSK Demodulation

#### Teoria

Demodulacja BPSK polega na prostej decyzji progowej:

- Jezeli Re(symbol) > 0 → bit = 0
- Jezeli Re(symbol) < 0 → bit = 1

**Dlaczego tylko skladowa Re:**
W BPSK wszystkie symbole leza na osi rzeczywistej:

```
    Q
    ^
    |
-1  |  +1     <- Symbole
----+----> I
    |
```

Szum moze dodac skladowa urojona, ale ignorujemy ja i patrzymy tylko na I.

#### Implementacja

```python
def bpsk_demodulation(received_symbols):
    decoded_bits = (received_symbols.real < 0).astype(int)
    return decoded_bits
```

**Analiza krok po kroku:**

```python
# Krok 1: Wyciagniecie skladowej rzeczywistej
received_symbols.real  # np. [0.95, -0.88, 1.03]

# Krok 2: Porownanie z progiem (0)
received_symbols.real < 0  # np. [False, True, False]

# Krok 3: Konwersja boolean -> int
(...).astype(int)  # np. [0, 1, 0]
```

**Dlaczego `< 0` a nie `> 0`:**

Przypomnijmy mapowanie w modulatorze:

```
bit 0 → symbol +1
bit 1 → symbol -1
```

Wiec demodulacja:

```
symbol > 0 → bit 0
symbol < 0 → bit 1
```

W kodzie:

```python
# Metoda 1: (received < 0).astype(int)
# False (>0) -> 0 -> bit 0 ✓
# True (<0)  -> 1 -> bit 1 ✓

# Metoda 2: (received > 0).astype(int)
# True (>0)  -> 1 -> bit 1 ✗ ZLEEE!
# False (<0) -> 0 -> bit 0 ✗ ZLEEE!

# Metoda 3: Poprawiona wersja metody 2
1 - (received > 0).astype(int)  # Dziala, ale bardziej skomplikowane
```

#### Przyklad numeryczny

```python
# Odbieramy symbole z szumem:
received = np.array([0.88+0.12j, -0.95-0.08j, 1.12+0.05j, -1.03-0.11j])

# Krok 1: Skladowa Re
re = [0.88, -0.95, 1.12, -1.03]

# Krok 2: Porownanie < 0
comparison = [False, True, False, True]

# Krok 3: Konwersja
decoded = [0, 1, 0, 1]

# Oryginalne bity (przed modulacja):
original = [0, 1, 0, 1]

# Porownanie:
decoded == original  # [True, True, True, True]
# 0 bledow! (przy dobrym Eb/N0)
```

### 5.2 QPSK Demodulation

#### Teoria

QPSK ma 4 symbole w 4 kwadrantach:

```
        Q
        ^
 01 (-1+j) | (1+j) 00
        \ | /
    -----+------> I
        / | \
 11 (-1-j) | (1-j) 10

Decyzje:
- Znak Re(symbol) -> pierwszy bit
- Znak Im(symbol) -> drugi bit
```

#### Implementacja

```python
for idx, (i, q) in enumerate(zip(i_component, q_component)):
    if i >= 0 and q >= 0:      # Kwadrant I
        bits[2*idx:2*idx+2] = [0, 0]
    elif i < 0 and q >= 0:     # Kwadrant II
        bits[2*idx:2*idx+2] = [0, 1]
    elif i < 0 and q < 0:      # Kwadrant III
        bits[2*idx:2*idx+2] = [1, 1]
    else:                       # Kwadrant IV (i >= 0, q < 0)
        bits[2*idx:2*idx+2] = [1, 0]
```

**Dlaczego petla zamiast operacji wektorowej:**

```python
# Metoda 1: Petla (UZYTE) - czytelna dla 4 przypadkow
for idx, (i, q) in enumerate(...):
    if i >= 0 and q >= 0: bits[...] = [0,0]
    elif ...

# Metoda 2: Wektorowa (MOZLIWE) - szybsza, ale mniej czytelna
bit0 = (i_component < 0).astype(int)
bit1_temp = (q_component < 0).astype(int)
# + dodatkowa logika dla Gray coding...

# Metoda 3: Lookup table (DOBRA dla duzych danych)
quadrant = (i_component < 0) * 2 + (q_component < 0)
bits_lut = [[0,0], [1,0], [0,1], [1,1]]
bits = [bits_lut[q] for q in quadrant]
```

Wybor metody 1 (petla) bo:

- Kod jest czytelny i latwy do zrozumienia
- Jasno widac mapowanie Gray code
- Wydajnosc jest wystarczajaca dla typowych symulacji

#### Przyklad numeryczny

```python
# Odbieramy symbole:
received = [0.68+0.72j, -0.65+0.73j, -0.71-0.69j, 0.74-0.68j]

# Symbol 1: I=0.68>0, Q=0.72>0 -> Kwadrant I -> bity [0,0]
# Symbol 2: I=-0.65<0, Q=0.73>0 -> Kwadrant II -> bity [0,1]
# Symbol 3: I=-0.71<0, Q=-0.69<0 -> Kwadrant III -> bity [1,1]
# Symbol 4: I=0.74>0, Q=-0.68<0 -> Kwadrant IV -> bity [1,0]

decoded = [0, 0, 0, 1, 1, 1, 1, 0]
```

### 5.3 8-PSK Demodulation

#### Teoria

8-PSK wymaga bardziej zaawansowanej demodulacji - musimy znalezc najblizszy punkt konstelacji:

```
    111
     |
110--+--001
     |
101--+--010
     |
    100
```

Uzywamy **minimum distance detection** - wybieramy symbol o najmniejszej odleglosci Euklidesowej.

#### Implementacja

```python
# Konstelacja referencyjna
angles = np.array([0, 1, 3, 2, 6, 7, 5, 4]) * np.pi / 4
constellation = np.exp(1j * angles)

# Dla kazdego odbieranego symbolu:
for idx, symbol in enumerate(received_symbols):
    # Oblicz odleglosci do wszystkich punktow konstelacji
    distances = np.abs(symbol - constellation)

    # Znajdz indeks najblizszego punktu
    closest_idx = np.argmin(distances)

    # Konwertuj indeks na 3 bity
    bit0 = (closest_idx >> 2) & 1
    bit1 = (closest_idx >> 1) & 1
    bit2 = closest_idx & 1
```

**Dlaczego obliczamy wszystkie odleglosci:**

```python
distances = np.abs(symbol - constellation)
```

Odleglosc Euklidesowa miedzy punktami zespolonymi:

```
d = |z1 - z2| = sqrt((Re(z1)-Re(z2))^2 + (Im(z1)-Im(z2))^2)
```

NumPy robi to automatycznie przez `np.abs()` dla liczb zespolonych.

**Konwersja indeksu na bity:**

```python
bit0 = (closest_idx >> 2) & 1  # Najstarszy bit
bit1 = (closest_idx >> 1) & 1  # Sredni bit
bit2 = closest_idx & 1         # Najmłodszy bit
```

Operacje bitowe krok po kroku:

```
closest_idx = 5 (decimal) = 101 (binary)

bit0 = (101 >> 2) & 1
     = 001 & 1
     = 1

bit1 = (101 >> 1) & 1
     = 010 & 1
     = 0

bit2 = 101 & 1
     = 1

Wynik: [1, 0, 1]
```

**Dlaczego >> (shift) a nie dzielenie:**

```python
# Metoda 1: Bit shifting (UZYTE) - szybsze
bit0 = (idx >> 2) & 1

# Metoda 2: Dzielenie (WOLNIEJSZE)
bit0 = (idx // 4) % 2

# Metoda 3: String conversion (NAJWOLNIEJSZE)
binary_str = bin(idx)[2:].zfill(3)
bit0 = int(binary_str[0])
```

Operacje bitowe sa najszybsze na poziomie procesora.

#### Przyklad numeryczny

```python
# Konstelacja (8 punktow):
constellation = [1+0j, 0.707+0.707j, 0+1j, -0.707+0.707j,
                 -1+0j, -0.707-0.707j, 0-1j, 0.707-0.707j]

# Odbieramy symbol z szumem:
received_symbol = 0.65 + 0.75j

# Krok 1: Oblicz odleglosci
d0 = |0.65+0.75j - 1+0j| = |−0.35+0.75j| = 0.828
d1 = |0.65+0.75j - 0.707+0.707j| = |−0.057+0.043j| = 0.072  <- MIN!
d2 = |0.65+0.75j - 0+1j| = |0.65−0.25j| = 0.697
...

# Krok 2: Znajdz minimum
closest_idx = 1

# Krok 3: Konwertuj na bity
1 (dec) = 001 (bin)
bits = [0, 0, 1]
```

### 5.4 QAM-16 Demodulation

#### Teoria

16-QAM to siatka 4×4 - demodulujemy osobno skladowa I i Q uzywajac progov:

```
Progi dla I (i Q):
-3      -1      +1      +3
   -2      0       +2     <- Progi decyzyjne

Decyzja:
I < -2  -> bity [0,0]
-2≤I<0  -> bity [0,1]
0≤I<2   -> bity [1,1]
I ≥ 2   -> bity [1,0]
```

#### Implementacja - PAM-4 Demodulation

```python
def pam4_demod(value):
    if value < -2:
        return [0, 0]  # -3
    elif value < 0:
        return [0, 1]  # -1
    elif value < 2:
        return [1, 1]  # +1
    else:
        return [1, 0]  # +3
```

**Dlaczego te progi:**

```
Oryginalne poziomy: -3, -1, +1, +3

Progi sa w polowie miedzy poziomami:
Prog1 = (-3 + -1) / 2 = -2
Prog2 = (-1 + +1) / 2 = 0
Prog3 = (+1 + +3) / 2 = +2

Regions:
value < -2:   najbliżej -3 -> [0,0]
-2 ≤ value < 0: najbliżej -1 -> [0,1]
0 ≤ value < 2:  najbliżej +1 -> [1,1]
value ≥ 2:    najbliżej +3 -> [1,0]
```

**Denormalizacja:**

```python
norm = np.sqrt(10)
denorm_symbols = received_symbols * norm
```

Dlaczego? W modulatorze normalizowalismy przez `1/sqrt(10)`. Teraz musimy cofnac normalizacje aby progi [-2, 0, +2] dzialaly:

```
Normalny symbol: 0.316 + 0.316j  (po normalizacji)
Denormalizowany: 1 + 1j  (oryginalne poziomy)
```

#### Przyklad numeryczny

```python
# Odbieramy symbol:
received = 0.29 + 0.32j  (znormalizowany)

# Krok 1: Denormalizacja
norm = sqrt(10) = 3.162
denorm = (0.29 + 0.32j) * 3.162
       = 0.917 + 1.012j

# Krok 2: Demodulacja I (0.917)
0.917 > 0 i 0.917 < 2
-> [1, 1]

# Krok 3: Demodulacja Q (1.012)
1.012 > 0 i 1.012 < 2
-> [1, 1]

# Wynik:
bits = [1, 1, 1, 1]

# To odpowiada punktowi (+1, +1) w konstelacji ✓
```

---

## 6. main.py - Program glowny

### 6.1 Obliczanie BER

```python
def calculate_ber(original_bits, decoded_bits):
    errors = np.sum(original_bits != decoded_bits)
    ber = errors / len(original_bits)
    return ber
```

**Matematyka:**

```
BER = (liczba blednych bitow) / (calkowita liczba bitow)

Przyklad:
original = [0, 1, 0, 1, 1, 0]
decoded  = [0, 1, 1, 1, 0, 0]
           ✓  ✓  ✗  ✓  ✗  ✓

errors = 2
ber = 2/6 = 0.333
```

**Implementacja wektorowa:**

```python
original_bits != decoded_bits
# [False, False, True, False, True, False]

np.sum([False, False, True, False, True, False])
# False=0, True=1
# 0 + 0 + 1 + 0 + 1 + 0 = 2
```

### 6.2 Symulacja dla jednej modulacji

```python
def simulate_bpsk(eb_n0_range, n_bits=10000):
    ber_values = []

    for eb_n0_db in eb_n0_range:
        # Generuj nowe bity dla kazdego Eb/N0
        bits = gen_bites(n_bits)

        # Modulacja
        symbols = bpsk_modulation(bits)

        # Kanal
        received_symbols = transmission_channel(symbols, eb_n0_db)

        # Demodulacja
        decoded_bits = bpsk_demodulation(received_symbols)

        # BER
        ber = calculate_ber(bits, decoded_bits)
        ber_values.append(ber)

    return ber_values
```

**Dlaczego petla po Eb/N0:**

Chcemy zobaczyc jak BER zmienia sie w zaleznosci od jakosci kanalu:

```
Eb/N0 = 0 dB  -> duzo szumu -> wysoki BER (np. 0.1)
Eb/N0 = 5 dB  -> sredni szum -> sredni BER (np. 0.01)
Eb/N0 = 10 dB -> malo szumu -> niski BER (np. 0.0001)
```

**Dlaczego generujemy nowe bity w kazdej iteracji:**

```python
# Zle podejscie - te same bity dla wszystkich Eb/N0:
bits = gen_bites(n_bits)  # RAZ, przed petla
for eb_n0_db in eb_n0_range:
    symbols = bpsk_modulation(bits)  # Te same bity!
    ...

# Dobre podejscie - nowe bity w kazdej iteracji:
for eb_n0_db in eb_n0_range:
    bits = gen_bites(n_bits)  # Nowe losowe bity
    ...
```

Dlaczego? Bo chcemy symulowac **rozne sekwencje** danych dla kazdego poziomu szumu. To daje bardziej reprezentatywne wyniki (srednia po roznych danych).

### 6.3 Wykres BER

```python
plt.semilogy(eb_n0_range, ber_values, 'bo-', linewidth=2, markersize=8)
```

**Dlaczego `semilogy` (logarytmic scale):**

BER zmienia sie o wiele rzedow wielkosci:

```
BER przy 0 dB:  0.1 (10^-1)
BER przy 5 dB:  0.01 (10^-2)
BER przy 10 dB: 0.0001 (10^-4)
BER przy 15 dB: 0.000001 (10^-6)
```

Na skali liniowej wszystkie wartosci blisko 0 dB bylby niewidoczne. Skala logarytmiczna pokazuje wszystkie wartosci wyraznie:

```
Linear scale:          Logarithmic scale:
|                      10^0  |
|*                     10^-1 |*
|                      10^-2 | *
|                      10^-3 |  *
|                      10^-4 |   *
|____                  10^-5 |____*
```

### 6.4 Wykres konstelacji

```python
def plot_constellations():
    # Generuj symbole
    symbols = bpsk_modulation(bits)

    # Dodaj szum
    noisy = transmission_channel(symbols, eb_n0_db=10)

    # Wykres
    ax.scatter(noisy.real, noisy.imag, alpha=0.5, c='blue', label='Received')
    ax.scatter(symbols.real, symbols.imag, s=200, c='red', marker='x', label='Ideal')
```

**Co pokazuje wykres:**

```
Ideal constellation:     Noisy constellation:

    Q                        Q
    |                        | . .
 X  |  X                  X .| . X
----+---->I               ----.+----->I
    |                      . .| .
                              |

Czerwone X: idealne symbole (bez szumu)
Niebieskie punkty: odbierane symbole (z szumem)
```

**Interpretacja:**

- Punkty skupione wokol X -> dobry kanal (wysoki Eb/N0)
- Punkty rozproszone -> zly kanal (niski Eb/N0)
- Punkty wychodzace poza regiony -> mozliwe bledy demodulacji

### 6.5 get_results_path() - Uniwersalne sciezki

```python
def get_results_path():
    script_dir = Path(__file__).parent.resolve()

    if script_dir.name == 'src':
        results_dir = script_dir.parent / 'results'
    else:
        results_dir = script_dir / 'results'

    results_dir.mkdir(parents=True, exist_ok=True)

    return results_dir
```

**Dlaczego taka logika:**

Problem: Skrypt moze byc uruchamiany z roznych miejsc:

```
# Opcja 1: z katalogu src/
$ cd src
$ python main.py
# __file__ = /path/to/project/src/main.py
# script_dir = /path/to/project/src
# results powinny byc w: /path/to/project/results

# Opcja 2: z katalogu glownego
$ cd project
$ python src/main.py
# __file__ = /path/to/project/src/main.py
# script_dir = /path/to/project/src
# results powinny byc w: /path/to/project/results
```

**Rozwiazanie:**

```python
# Krok 1: Znajdz katalog gdzie jest main.py
script_dir = Path(__file__).parent.resolve()
# /path/to/project/src

# Krok 2: Sprawdz czy jestesmy w src/
if script_dir.name == 'src':
    # Tak - przejdz poziom wyzej, potem do results/
    results_dir = script_dir.parent / 'results'
    # /path/to/project/results
else:
    # Nie - jestesmy w glownym katalogu
    results_dir = script_dir / 'results'
    # /path/to/project/results

# Krok 3: Utworz katalog jesli nie istnieje
results_dir.mkdir(parents=True, exist_ok=True)
```

**Dlaczego `parents=True`:**

```python
# Jesli cala sciezka nie istnieje:
# /path/to/project/results

# parents=False (domyslnie):
mkdir('results')  # ERROR! Katalog /path/to/project nie istnieje!

# parents=True:
mkdir('results')  # OK! Utworzy /path/to/project i /path/to/project/results
```

**Dlaczego `exist_ok=True`:**

```python
# exist_ok=False (domyslnie):
mkdir('results')  # ERROR! Katalog juz istnieje!

# exist_ok=True:
mkdir('results')  # OK! Jesli istnieje, nie rob nic
```

---

## 7. Przyklady kompletnej symulacji

### Przyklad 1: BPSK end-to-end z liczbami

```python
# Parametry
n_bits = 8
eb_n0_db = 10

# KROK 1: Generacja bitow
bits = gen_bites(8)
# bits = [1, 0, 1, 1, 0, 0, 1, 0]

# KROK 2: Modulacja BPSK
symbols = bpsk_modulation(bits)
# symbols = [-1, +1, -1, -1, +1, +1, -1, +1]  (as complex)

# KROK 3: Kanal (szum)
# Eb/N0 = 10 dB -> eb_n0 = 10 -> N0 = 0.1 -> sigma = 0.224

# Przykladowy szum:
noise = [0.15+0.12j, -0.08+0.05j, 0.11-0.09j, -0.13+0.14j,
         0.09-0.08j, -0.12+0.11j, 0.14-0.06j, -0.11+0.08j]

received = symbols + noise
# received = [-0.85+0.12j, +0.92+0.05j, -0.89-0.09j, -1.13+0.14j,
#             +1.09-0.08j, +0.88+0.11j, -0.86-0.06j, +0.89+0.08j]

# KROK 4: Demodulacja BPSK
# Patrzymy na Re(received):
# -0.85 < 0 -> bit 1 ✓
# +0.92 > 0 -> bit 0 ✓
# -0.89 < 0 -> bit 1 ✓
# -1.13 < 0 -> bit 1 ✓
# +1.09 > 0 -> bit 0 ✓
# +0.88 > 0 -> bit 0 ✓
# -0.86 < 0 -> bit 1 ✓
# +0.89 > 0 -> bit 0 ✓

decoded = [1, 0, 1, 1, 0, 0, 1, 0]

# KROK 5: Oblicz BER
errors = sum(bits != decoded)  # 0 bledow!
ber = 0 / 8 = 0.0  # Idealne odbieranie przy Eb/N0=10dB
```

### Przyklad 2: QPSK z bledem

```python
# Parametry
bits = [0, 0, 0, 1, 1, 1, 1, 0]
eb_n0_db = 0  # Niski SNR!

# KROK 1: Modulacja QPSK
# Para [0,0] -> 0.707+0.707j
# Para [0,1] -> -0.707+0.707j
# Para [1,1] -> -0.707-0.707j
# Para [1,0] -> 0.707-0.707j

symbols = [0.707+0.707j, -0.707+0.707j, -0.707-0.707j, 0.707-0.707j]

# KROK 2: Kanal z duzym szumem
# Eb/N0 = 0 dB -> N0 = 1.0 -> sigma = 0.707  (DUZY SZUM!)

noise = [0.5+0.8j, -0.6+0.4j, 0.7-0.9j, -0.5+0.6j]

received = symbols + noise
# received = [1.207+1.507j, -1.307+1.107j, -0.007-1.607j, 0.207-0.107j]

# KROK 3: Demodulacja QPSK
# Symbol 1: I=1.207>0, Q=1.507>0 -> [0,0] ✓ OK
# Symbol 2: I=-1.307<0, Q=1.107>0 -> [0,1] ✓ OK
# Symbol 3: I=-0.007<0, Q=-1.607<0 -> [1,1] ✓ OK
# Symbol 4: I=0.207>0, Q=-0.107<0 -> [1,0] ✓ OK

# Mimo duzego szumu, wszystkie OK! (szczescie)

# Ale gdyby szum byl wiekszy:
noise_worse = [1.0+1.2j, -0.3+0.9j, 1.2-0.5j, -1.0+0.4j]
received_worse = [1.707+1.907j, -1.007+1.607j, 0.493-1.207j, -0.293-0.307j]

# Symbol 3: I=0.493>0, Q=-1.207<0 -> [1,0] ✗ BLAD! (powinno byc [1,1])
# 2 bity bledne z 8 -> BER = 0.25
```

---

## 8. Najczestsze pytania (FAQ)

### Q1: Dlaczego normalizujemy energie symboli?

**A:** Zeby sprawiedliwie porownywac rozne modulacje. Bez normalizacji:

```
BPSK: |symbol|^2 = 1  (symbole: ±1)
QPSK: |symbol|^2 = 2  (symbole: ±1±j, przed normalizacja)

To nie jest uczciwe porownanie! QPSK ma 2x wieksza moc.

Po normalizacji:
BPSK: E[|s|^2] = 1
QPSK: E[|s|^2] = 1
8-PSK: E[|s|^2] = 1
QAM: E[|s|^2] = 1

Teraz porownanie jest fair - ta sama moc, rozne modulacje.
```

### Q2: Dlaczego uzywamy liczb zespolonych dla BPSK jesli symbole sa tylko rzeczywiste?

**A:** Dla **konsystencji** i **uniwersalnosci**:

1. **Szum AWGN jest zespolony** (ma skladowa I i Q)
2. **Inne modulacje sa zespolone** (QPSK, QAM)
3. **Jednolity interfejs** - wszystkie funkcje przyjmuja i zwracaja typ `complex`

```python
# Gdyby BPSK bylo float, a QPSK complex:
def demodulate(symbols, mod_type):
    if mod_type == 'bpsk':
        # Specjalny kod dla float
        ...
    else:
        # Inny kod dla complex
        ...

# Z ujednoliconym complex:
def demodulate(symbols, mod_type):
    # Jeden kod dla wszystkich!
    ...
```

### Q3: Dlaczego Eb/N0 a nie SNR?

**A:** **Eb/N0 jest uniwersalne** dla roznych modulacji:

```
SNR (Signal-to-Noise Ratio) zalezy od:
- Mocy sygnalu
- Szerokosci pasma
- Szybkosci transmisji

Eb/N0 (Energy per bit to Noise) nie zalezy od:
- Szybkosci transmisji
- Szerokosci pasma

Przyklad:
BPSK: 1 bit/symbol -> SNR = Eb/N0
QPSK: 2 bity/symbol -> SNR = 2 * Eb/N0
8-PSK: 3 bity/symbol -> SNR = 3 * Eb/N0

Eb/N0 jest takie samo dla porownania!
```

### Q4: Dlaczego Gray coding?

**A:** **Minimalizuje bledy** gdy szum przesuwa symbol do sasiedniego punktu:

```
Binary coding:      Gray coding:
00  01              00  01
  \/                  \/
  /\                  /\
10  11              11  10

Binary: 01->11 = 2 bity bledne
Gray: 01->11 = 1 bit bledny

Statystycznie: Gray code ma nizsza BER!
```

### Q5: Dlaczego BER nie jest zawsze 0 nawet przy wysokim Eb/N0?

**A:** Bo **szum jest losowy**:

```
Nawet przy Eb/N0 = 20 dB (bardzo dobry kanal):
- Teoretyczny BER ≈ 10^-10 (prawie 0)
- Ale w symulacji 10000 bitow:
  * Oczekiwana liczba bledow = 10000 * 10^-10 = 0.000001
  * Mozliwe 0, 1, lub 2 bledy (losowo)

W praktyce:
- Dla nieskonczonej liczby bitow: BER -> 0
- Dla skonc zonej symulacji: BER oscyluje wokol 0
```

---

## 9. Podsumowanie - Przepływ danych

Cala aplikacja w jednym schemacie:

```
┌─────────────────┐
│   gen_bites()   │ Losowe bity: [0,1,1,0,...]
└────────┬────────┘
         │
         v
┌─────────────────┐
│   *_modulation()│ Symbole zespolone
└────────┬────────┘
         │
         v
┌─────────────────┐
│ transmission_   │ Symbole + szum AWGN
│   _channel()    │
└────────┬────────┘
         │
         v
┌─────────────────┐
│ *_demodulation()│ Bity odtworzone
└────────┬────────┘
         │
         v
┌─────────────────┐
│ calculate_ber() │ BER = bledy/total
└─────────────────┘
         │
         v
┌─────────────────┐
│   Wykresy       │ Wyniki: BER vs Eb/N0
└─────────────────┘
```

---

## Koniec dokumentacji

Ten dokument wyjasnil jak dziala kod aplikacji ModulationPSKProject od podstaw. Kazda decyzja implementacyjna zostala uzasadniona, a przyklady numeryczne pokazuja dokladnie co dzieje sie z danymi w kazdym kroku.

**Kluczowe zasady projektu:**

1. **Normalizacja energii** - uczciwe porownanie
2. **Operacje wektorowe** - wydajnosc
3. **Gray coding** - minimalizacja bledow
4. **Modularnosc** - latwosc rozszerzania
5. **Typ complex** - uniwersalnosc

Jesli masz pytania o konkretny fragment kodu, wróc do odpowiedniej sekcji tego dokumentu!
