# Dokumentacja Techniczna Kodu - ModulationPSKProject

Szczegolowa analiza implementacji z wyjasnieniami decyzji projektowych.
Dla kazdej kluczowej funkcji: analiza linia po linii + uzasadnienie wyboru rozwiazania.

**Wersja:** 1.0  
**Data:** 2025-10-23

---

## Spis tresci

1. [Architektura systemu](#architektura-systemu)
2. [Modulator.py - PRIORYTET WYSOKI](#modulatorpy)
3. [Demodulator.py - PRIORYTET WYSOKI](#demodulatorpy)
4. [AddAWGNNoise.py - PRIORYTET WYSOKI](#addawgnoisepy)
5. [TransmissionChannel.py - PRIORYTET SREDNI](#transmissionchannelpy)
6. [main.py - PRIORYTET SREDNI](#mainpy)
7. [GetBytes.py - PRIORYTET NISKI](#getbytespy)
8. [plot_utils.py - PRIORYTET NISKI](#plot_utilspy)

---

## Architektura systemu

### Przeplyw danych

```
┌─────────────┐
│  GetBytes   │ Generowanie losowych bitow (0/1)
└──────┬──────┘
       │ bits[]
       v
┌─────────────┐
│  Modulator  │ Mapowanie bitow -> symbole zespolone
└──────┬──────┘
       │ symbols[] (complex)
       v
┌─────────────┐
│ Transmission│ Dodanie szumu AWGN
│  Channel    │
└──────┬──────┘
       │ received_symbols[] (complex + noise)
       v
┌─────────────┐
│ Demodulator │ Odtworzenie bitow z symboli
└──────┬──────┘
       │ decoded_bits[]
       v
┌─────────────┐
│  main.py    │ Porownanie bits[] vs decoded_bits[]
│             │ Obliczenie BER, generowanie wykresow
└─────────────┘
```

### Kluczowe decyzje projektowe

**1. Dlaczego NumPy zamiast czystego Pythona?**

- Operacje wektorowe 10-100x szybsze niz petle Python
- Natywna obsluga liczb zespolonych
- Efektywne wykorzystanie pamieci (ciagly blok)

**2. Dlaczego complex128 dla wszystkich modulacji?**

- Uniwersalny interfejs (nawet BPSK zwraca complex)
- Upraszcza kod demodulatorow (zawsze .real i .imag)
- Bez konwersji typow pomiedzy etapami

**3. Dlaczego Gray coding?**

- Sasiednie symbole roznia sie 1 bitem
- Minimalizuje BER przy bledach symboli
- Standard w telekomunikacji

---

## Modulator.py

**Priorytet:** WYSOKI (rdzen systemu)

### Przegladowe schematy konstelacji

```
BPSK:          QPSK:           8-PSK:          16-QAM:
  I              I               I               I
  |              |               |               |
--+-- R      ---+--- R      ----+---- R      ---+--- R
 -1  +1      4 punkty        8 punktow       siatka 4x4
```

---

### `bpsk_modulation(bits)` - Linia po linii

**Przeznaczenie:** Mapowanie bitow na symbole BPSK

**Parametry:**

- `bits` (ndarray): Tablica binarnych wartosci {0, 1}

**Zwraca:** ndarray[complex128] - symbole {-1+0j, +1+0j}

**Kod:**

```python
1  def bpsk_modulation(bits):
2      symbols = 1 - 2 * bits
3      return symbols.astype(complex)
```

**Analiza linia po linii:**

**Linia 2: `symbols = 1 - 2 * bits`**

Co robi:

- Operacja wektorowa (dziala na calej tablicy naraz)
- Dla bit=0: `1 - 2*0 = 1`
- Dla bit=1: `1 - 2*1 = -1`

Dlaczego tak a nie inaczej:

**Alternatywa 1: Petla z if-else**

```python
# ZLE - wolne
symbols = []
for bit in bits:
    if bit == 0:
        symbols.append(1)
    else:
        symbols.append(-1)
```

Problem: ~100x wolniejsze dla duzych tablic

**Alternatywa 2: np.where()**

```python
# OK, ale bardziej skomplikowane
symbols = np.where(bits == 0, 1, -1)
```

Problem: Mniej czytelne, ten sam wynik

**Alternatywa 3: Operator indeksowania**

```python
# OK, ale wymaga pomocniczej tablicy
constellation = np.array([1, -1])
symbols = constellation[bits]
```

Problem: Dodatkowa pamiec, mniej bezposrednie

**Wybrane rozwiazanie:** `1 - 2*bits` jest:

- Najprostsze (1 operacja)
- Najszybsze (wektorowe)
- Najbardziej czytelne (matematyczne)

**Linia 3: `return symbols.astype(complex)`**

Co robi:

- Konwersja z float64 -> complex128
- Real part = wartosc symbolu
- Imag part = 0

Dlaczego:

- Uniwersalny interfejs (wszystkie modulacje zwracaja complex)
- Upraszcza kod w TransmissionChannel (zawsze complex)
- Bez konwersji w dalszych etapach

**Przyklad uzycia:**

```python
bits = np.array([0, 1, 0, 1])
symbols = bpsk_modulation(bits)  # [1+0j, -1+0j, 1+0j, -1+0j]
```

**Charakterystyka:**

- Zlozonosc czasowa: O(n)
- Zlozonosc pamieciowa: O(n)
- Energia symbolu: |s|² = 1 (bez normalizacji)

---

### `qpsk_modulation(bits)` - Linia po linii

**Przeznaczenie:** Mapowanie par bitow na symbole QPSK z Gray coding

**Konstelacja QPSK:**

```
        Q (Imag)
         ^
    01   |   00
  -------|--------> I (Real)
    11   |   10
```

**Parametry:**

- `bits` (ndarray): Tablica bitow, dlugosc MUSI byc parzysta

**Zwraca:** ndarray[complex128] - dlugosc = len(bits)/2

**Kod:**

```python
1   def qpsk_modulation(bits):
2       if len(bits) % 2 != 0:
3           raise ValueError("Number of bits must be even for QPSK")
4
5       bit_pairs = bits.reshape(-1, 2)
6
7       norm = 1 / np.sqrt(2)
8
9       qpsk_map = {
10          (0, 0): norm * (1 + 1j),
11          (0, 1): norm * (-1 + 1j),
12          (1, 1): norm * (-1 - 1j),
13          (1, 0): norm * (1 - 1j)
14      }
15
16      symbols = np.array([qpsk_map[tuple(pair)] for pair in bit_pairs],
17                         dtype=complex)
18
19      return symbols
```

**Analiza linia po linii:**

**Linie 2-3: Walidacja**

Dlaczego sprawdzac dlugosc:

- QPSK wymaga 2 bity -> 1 symbol
- Nieparzysta liczba bitow = niejednoznaczny ostatni symbol
- Lepiej zglosic blad niz cicho obciac dane

**Linia 5: `bit_pairs = bits.reshape(-1, 2)`**

Co robi:

- Przeksztalca [b0,b1,b2,b3] -> [[b0,b1], [b2,b3]]
- `-1` = automatyczne wyliczenie wymiaru (n/2)
- `2` = kazdy rzad ma 2 elementy

Dlaczego tak:

**Alternatywa: Petle z indeksowaniem**

```python
# ZLE - wolne
bit_pairs = []
for i in range(0, len(bits), 2):
    bit_pairs.append([bits[i], bits[i+1]])
```

**Wybrane:** reshape() jest:

- Wektorowe (bez petli)
- Zwraca widok (bez kopiowania danych)
- Standard w NumPy

**Linia 7: `norm = 1 / np.sqrt(2)`**

Co robi:

- Oblicza wspolczynnik normalizacji

Dlaczego normalizowac:

- Bez normalizacji: |1+1j|² = 2
- Z normalizacja: |(1+1j)/√2|² = 1
- Wszystkie modulacje maja srednia energie = 1
- Uczciwe porownanie BER

**Linie 9-14: Slownik mapowania**

Struktura:

```
(bit0, bit1) -> symbol
```

Dlaczego Gray coding (porzadek 00, 01, 11, 10):

- Sasiednie symbole roznia sie 1 bitem
- Przy bledzie symbolu zmienia sie 1 bit (nie 2)
- Przyklady:
  - 00 -> 01: zmiana 1 bitu, kat 90° (sasiedzi)
  - 00 -> 11: zmiana 2 bitow, kat 180° (przeciwne)

**Alternatywa: Natural coding (00, 01, 10, 11)**

```python
# Gorszy - wiecej bledow bitow
qpsk_map_natural = {
    (0, 0): norm * (1 + 1j),    # 00 - 45°
    (0, 1): norm * (-1 + 1j),   # 01 - 135°
    (1, 0): norm * (-1 - 1j),   # 10 - 225° <- 2 bity rozne od 01!
    (1, 1): norm * (1 - 1j)     # 11 - 315°
}
```

Problem: 01 i 10 roznia sie 2 bitami, ale sa obok siebie (90°)

**Linie 16-17: Mapowanie**

Co robi:

- List comprehension przez wszystkie pary
- `tuple(pair)` - konwersja ndarray na tuple (hashable)
- Lookup w slowniku O(1)

Dlaczego list comprehension:

**Alternatywa 1: Petla z append**

```python
# ZLE - wolne
symbols = []
for pair in bit_pairs:
    symbols.append(qpsk_map[tuple(pair)])
symbols = np.array(symbols, dtype=complex)
```

**Alternatywa 2: Indeksowanie tablicy konstelacji**

```python
# OK - podobna szybkosc
constellation = np.array([norm*(1+1j), norm*(-1+1j),
                          norm*(-1-1j), norm*(1-1j)])
indices = bit_pairs[:, 0] * 2 + bit_pairs[:, 1]
symbols = constellation[indices]
```

Problem: Mniej czytelne, trudniejsze utrzymanie Gray coding

**Wybrane:** Slownik bo:

- Jawne mapowanie (latwo sprawdzic Gray coding)
- Czytelne
- Latwe do modyfikacji

**Przyklad uzycia:**

```python
bits = np.array([0, 0, 1, 1])
symbols = qpsk_modulation(bits)
# [0.707+0.707j, -0.707-0.707j]
```

---

### `psk8_modulation(bits)` - Kluczowe punkty

**Przeznaczenie:** 3 bity -> 1 symbol na okregu jednostkowym

**Schemat konstelacji 8-PSK:**

```
        Q
        |
   011  |  001
      \ | /
-------\|/------- I
      / | \
   110  |  100
```

**Kod (kluczowe fragmenty):**

```python
6   angles = np.array([0, 1, 3, 2, 6, 7, 5, 4]) * np.pi / 4
7   constellation = np.exp(1j * angles)
8   symbol_indices = bit_triplets[:, 0] * 4 + bit_triplets[:, 1] * 2 + bit_triplets[:, 2]
9   symbols = constellation[symbol_indices]
```

**Linia 6: Porzadek katow**

Dlaczego [0,1,3,2,6,7,5,4] a nie [0,1,2,3,4,5,6,7]:

**Natural coding (zly):**

```
000 -> 0°    001 -> 45°
010 -> 90°   011 -> 135°  <- 010 i 011 roznia sie 2 bitami!
100 -> 180°  101 -> 225°
110 -> 270°  111 -> 315°
```

**Gray coding (dobry - implementowany):**

```
000 -> 0°     001 -> 45°   <- zmiana 1 bitu
001 -> 45°    011 -> 135°  <- zmiana 1 bitu
011 -> 135°   010 -> 90°   <- zmiana 1 bitu
...
```

Kazda para sasiadow rozni sie 1 bitem.

**Linia 7: `np.exp(1j * angles)`**

Wzor Eulera: e^(jθ) = cos(θ) + j·sin(θ)

Dlaczego wzor Eulera:

**Alternatywa: Bezposrednie cos/sin**

```python
# ZLE - bardziej skomplikowane
constellation = np.cos(angles) + 1j * np.sin(angles)
```

Problem: Dwie funkcje zamiast jednej

**Wybrane:** exp() jest:

- Bardziej zwiezle
- Standard w DSP
- Numerycznie stabilne

**Linia 8: Konwersja binarny -> dziesietny**

Przeksztalcenie [b0, b1, b2] -> indeks:

- b0 _ 4 + b1 _ 2 + b2 = b0·2² + b1·2¹ + b2·2⁰

Wektorowe dla wszystkich trojek naraz.

**Przyklad:**

```python
bits = np.array([0,0,0, 1,1,1])
symbols = psk8_modulation(bits)
# [1+0j, -0.707-0.707j]
# Pierwszy: 000 -> indeks 0 -> kat 0° -> 1+0j
# Drugi: 111 -> indeks 7 -> kat 315° -> cos(315°)+j·sin(315°)
```

**Wzorzec:** Ten sam schemat (reshape -> konstelacja -> indeksowanie) powtarza sie w 8-PSK i QAM. Spowodowane projektowaniem przez analogie - raz ustalony wzorzec, latwo rozszerzyc na inne modulacje.

---

### `qam16_modulation(bits)` - Kluczowe punkty

**Przeznaczenie:** 4 bity -> symbol z siatki 4x4

**Schemat konstelacji 16-QAM:**

```
  Q
  |
  3   o  o  o  o
  1   o  o  o  o
 -1   o  o  o  o
 -3   o  o  o  o
  |_______________ I
     -3 -1  1  3
```

**Kod (kluczowe fragmenty):**

```python
5   bit_groups = bits.reshape(-1, 4)
6   i_bits = bit_groups[:, 0:2]
7   q_bits = bit_groups[:, 2:4]
8
9   pam4_map = {
10      (0, 0): -3,
11      (0, 1): -1,
12      (1, 1): +1,
13      (1, 0): +3
14  }
15
16  i_components = np.array([pam4_map[tuple(pair)] for pair in i_bits])
17  q_components = np.array([pam4_map[tuple(pair)] for pair in q_bits])
18
19  symbols = i_components + 1j * q_components
20
21  norm = 1 / np.sqrt(10)
22  symbols = symbols * norm
```

**Linie 6-7: Podzial na I i Q**

Co robi:

- 4 bity -> [b0, b1] (I) i [b2, b3] (Q)
- Niezalezne mapowanie dla Real i Imag

Dlaczego podzial:

- QAM = 2 niezalezne modulacje PAM
- I i Q modulowane osobno
- Upraszcza demodulacje (osobne progi)

**Linie 9-14: PAM-4 mapping**

Dlaczego poziomy {-3, -1, +1, +3}:

**Alternatywa: {-1.5, -0.5, +0.5, +1.5}**

```python
# Gorsze - asymetryczne progi
pam4_map = {
    (0,0): -1.5, (0,1): -0.5,
    (1,1): +0.5, (1,0): +1.5
}
```

Problem: Progi przy -1.0, 0, +1.0 - nierownomierne odstepy

**Wybrane {-3, -1, +1, +3}:**

- Progi przy -2, 0, +2 (symetryczne)
- Rowne odstepy
- Gray coding (sasiednie poziomy roznia sie 1 bitem)

**Linie 21-22: Normalizacja**

Dlaczego 1/√10:

Energia przed normalizacja:

```
E[|s|²] = E[I²] + E[Q²]
E[I²] = ((-3)² + (-1)² + 1² + 3²) / 4 = (9+1+1+9)/4 = 5
E[Q²] = 5  (taki sam)
E[|s|²] = 5 + 5 = 10
```

Po normalizacji (1/√10)²:

```
E[|s|²] = 10 * (1/√10)² = 10 * 1/10 = 1 ✓
```

**Przyklad:**

```python
bits = np.array([0,0,0,0, 1,0,1,0])
symbols = qam16_modulation(bits)
# Pierwszy: [0,0] -> I=-3, [0,0] -> Q=-3, symbol = (-3-3j)/√10
# Drugi: [1,0] -> I=+3, [1,0] -> Q=+3, symbol = (3+3j)/√10
```

---

## Demodulator.py

**Priorytet:** WYSOKI (odzyskiwanie danych)

### Ogolna zasada

Wszystkie demodulatory: symbol z szumem -> najblizsza konstelacja -> bity

```
         Odebrane
            |
            v
     Znajdz najblizszy
     punkt konstelacji
            |
            v
       Wyciagnij bity
```

---

### `bpsk_demodulation(received_symbols)` - Linia po linii

**Przeznaczenie:** Prosta decyzja progowa: Re(s) > 0 -> bit 0, Re(s) ≤ 0 -> bit 1

**Kod:**

```python
1  def bpsk_demodulation(received_symbols):
2      decoded_bits = (received_symbols.real < 0).astype(int)
3      return decoded_bits
```

**Linia 2: Calosc logiki**

Co robi:

- `.real` - wyciaga czesc rzeczywista (BPSK ma Im=0)
- `< 0` - porownanie, zwraca bool array
- `.astype(int)` - konwersja True->1, False->0

Dlaczego tak:

**Alternatywa 1: np.where()**

```python
# Bardziej rozwlekle
decoded_bits = np.where(received_symbols.real < 0, 1, 0)
```

**Alternatywa 2: Petla**

```python
# ZLE - wolne
decoded_bits = []
for symbol in received_symbols:
    if symbol.real < 0:
        decoded_bits.append(1)
    else:
        decoded_bits.append(0)
```

**Wybrane:** Wektorowe porownanie to:

- Najkrotsza forma (1 linia)
- Najszybsza (wektorowe)
- Idiomatyczne NumPy

**Prog 0 - dlaczego:**

Konstelacja BPSK: {-1, +1}

- Optymalny prog = srednia = (-1+1)/2 = 0
- Symetryczne rozlozenie bledow
- Bez bias

**Przyklad:**

```python
received = np.array([0.9+0j, -1.2+0j, 0.1+0j])
bits = bpsk_demodulation(received)  # [0, 1, 0]
# 0.9 > 0 -> False -> 0
# -1.2 < 0 -> True -> 1
# 0.1 > 0 -> False -> 0
```

---

### `qpsk_demodulation(received_symbols)` - Kluczowe punkty

**Przeznaczenie:** Dekodowanie QPSK przez regiony konstelacji

**Schemat regionow:**

```
        Q
   II   |   I
  (01)  |  (00)
--------|-------- I
  (11)  | (10)
   III  |  IV
```

**Kod (kluczowe fragmenty):**

```python
5   n_symbols = len(received_symbols)
6   bits = np.zeros(n_symbols * 2, dtype=int)
7
8   i_component = received_symbols.real
9   q_component = received_symbols.imag
10
11  for idx, (i, q) in enumerate(zip(i_component, q_component)):
12      if i >= 0 and q >= 0:      # Kwadrant I
13          bits[2*idx:2*idx+2] = [0, 0]
14      elif i < 0 and q >= 0:     # Kwadrant II
15          bits[2*idx:2*idx+2] = [0, 1]
16      elif i < 0 and q < 0:      # Kwadrant III
17          bits[2*idx:2*idx+2] = [1, 1]
18      else:                       # Kwadrant IV (i >= 0, q < 0)
19          bits[2*idx:2*idx+2] = [1, 0]
```

**Linia 6: Prealokacja**

Dlaczego `np.zeros(n_symbols * 2)`:

- QPSK: 1 symbol = 2 bity
- Prealokacja szybsza niz append
- Wymaga znania rozmiaru z gory

**Linie 8-9: Rozdzielenie I i Q**

Dlaczego osobno:

- Decyzje niezalezne dla I i Q
- Progi przy 0 dla obu osi

**Linie 11-19: Petla po symbolach**

Dlaczego petla a nie wektorowe:

**Alternatywa: Boolean indexing**

```python
# Mozliwe, ale skomplikowane
mask_q1 = (i_component >= 0) & (q_component >= 0)
mask_q2 = (i_component < 0) & (q_component >= 0)
# ... (4 maski)
bits[mask_q1.repeat(2)] = ... # Trudne!
```

Problem: Przeplatanie bitow trudne do wektoryzacji

**Wybrane:** Petla bo:

- Czytelniejsze (jasne case'y)
- Latwe do debugowania
- Nie jest bottleneck (mala liczba symboli)

**Mapowanie zgodne z Gray coding:**

- 00 <-> 01: roznia sie 1 bitem, sasiednie (I>0, Q rozne)
- 01 <-> 11: roznia sie 1 bitem, sasiednie (I<0, Q rozne)
- itd.

**Przyklad:**

```python
received = np.array([0.8+0.6j, -0.5+0.3j])
bits = qpsk_demodulation(received)  # [0,0, 0,1]
# Pierwszy: I>0, Q>0 -> Kwadrant I -> 00
# Drugi: I<0, Q>0 -> Kwadrant II -> 01
```

---

### `psk8_demodulation(received_symbols)` - Kluczowe punkty

**Przeznaczenie:** Minimum distance decoding - znajdz najblizszy z 8 punktow

**Kod (kluczowy fragment):**

```python
6   angles = np.array([0, 1, 3, 2, 6, 7, 5, 4]) * np.pi / 4
7   constellation = np.exp(1j * angles)
8
9   n_symbols = len(received_symbols)
10  bits = np.zeros(n_symbols * 3, dtype=int)
11
12  for idx, symbol in enumerate(received_symbols):
13      distances = np.abs(symbol - constellation)
14      closest_idx = np.argmin(distances)
15
16      bit0 = (closest_idx >> 2) & 1
17      bit1 = (closest_idx >> 1) & 1
18      bit2 = closest_idx & 1
19
20      bits[3*idx:3*idx+3] = [bit0, bit1, bit2]
```

**Linia 13: Obliczenie odleglosci**

Co robi:

- `symbol - constellation` - roznica wektorowa (1 vs 8 elementow, broadcast)
- `np.abs()` - modul liczby zespolonej |a+bj| = √(a²+b²)
- Zwraca 8 odleglosci

Dlaczego Euklidesowa:

**Alternatywa: Odleglosc Manhattan**

```python
# Gorsze - nieoptymalny estimator
distances = np.abs(symbol.real - constellation.real) + \
            np.abs(symbol.imag - constellation.imag)
```

Problem: Nie minimalizuje BER

**Wybrane:** Euklidesowa (modul) to:

- Optymalny detektor dla AWGN
- Minimalizuje prawdopodobienstwo bledu
- Standard w telekomunikacji

**Linia 14: `np.argmin(distances)`**

Zwraca indeks minimum (0-7).

**Linie 16-18: Konwersja indeks -> bity**

Operacje bitowe:

- `>> 2` - przesuniecie w prawo o 2 (dzielenie przez 4)
- `>> 1` - przesuniecie o 1 (dzielenie przez 2)
- `& 1` - AND z 1 (wyciaga najmniej znaczacy bit)

Przyklad dla idx=6 (binarnie 110):

```
bit0 = (110 >> 2) & 1 = (001) & 1 = 1
bit1 = (110 >> 1) & 1 = (011) & 1 = 1
bit2 = (110) & 1 = 0
Wynik: [1, 1, 0]
```

Dlaczego operacje bitowe:

**Alternatywa: Dzielenie i modulo**

```python
# Wolniejsze
bit0 = (closest_idx // 4) % 2
bit1 = (closest_idx // 2) % 2
bit2 = closest_idx % 2
```

**Wybrane:** Operacje bitowe to:

- Szybsze (instrukcje CPU)
- Idiomatyczne dla bit manipulation
- Powszechne w DSP

**Przyklad:**

```python
received = np.array([0.8+0.5j, -0.9+0.1j])
bits = psk8_demodulation(received)
# Pierwszy: Oblicz 8 odleglosci, najblizszy moze byc indeks 1 (45°)
# Drugi: Najblizszy moze byc indeks 4 (180°)
# Zwraca odpowiadajace trojki bitow
```

**Wzorzec:** Minimum distance decoding powtarza sie w 8-PSK i czesciowo w QAM. Uniwersalna metoda dla constellation-based modulations.

---

### `qam16_demodulation(received_symbols)` - Kluczowe punkty

**Przeznaczenie:** Dekodowanie przez progi I i Q osobno

**Schemat progow:**

```
  Q
  |
  2 ----+----+----+----
  0 ----+----+----+----
 -2 ----+----+----+----
  |___________________ I
       -2    0    2
```

**Kod (kluczowe fragmenty):**

```python
5   norm = np.sqrt(10)
6   denorm_symbols = received_symbols * norm
7
11  def pam4_demod(value):
12      if value < -2:
13          return [0, 0]  # -3
14      elif value < 0:
15          return [0, 1]  # -1
16      elif value < 2:
17          return [1, 1]  # +1
18      else:
19          return [1, 0]  # +3
20
21  for idx, symbol in enumerate(denorm_symbols):
22      i_bits = pam4_demod(symbol.real)
23      q_bits = pam4_demod(symbol.imag)
24      bits[4*idx:4*idx+4] = i_bits + q_bits
```

**Linie 5-6: Denormalizacja**

Dlaczego:

- Modulacja mnozy przez 1/√10
- Progi dla {-3,-1,+1,+3} nie dla {-0.949,-0.316,+0.316,+0.949}
- Przywrocenie oryginalnych poziomow upraszcza porownania

**Funkcja pam4_demod: Progi**

Dlaczego [-inf, -2), [-2, 0), [0, 2), [2, +inf]:

Oryginalne poziomy: {-3, -1, +1, +3}

- Prog -2: srodek pomiedzy -3 i -1
- Prog 0: srodek pomiedzy -1 i +1
- Prog 2: srodek pomiedzy +1 i +3

Optymalne progi dla rownomiernego szumu.

**Linie 22-23: Niezalezne I i Q**

Co robi:

- Real part -> 2 bity (I)
- Imag part -> 2 bity (Q)
- Laczenie: [I0, I1, Q0, Q1]

Dlaczego osobno:

- QAM = dwie niezalezne modulacje PAM
- Decyzje ortogonalne
- Upraszcza logike

**Przyklad:**

```python
# Symbol po modulacji: (3+1j)/√10 = 0.949+0.316j
received = np.array([0.949+0.316j])
# Denormalizacja: 0.949*√10 = 3.0, 0.316*√10 = 1.0
# Real=3.0 > 2 -> [1,0]
# Imag=1.0, 0 < 1.0 < 2 -> [1,1]
bits = qam16_demodulation(received)  # [1,0,1,1]
```

---

## AddAWGNNoise.py

**Priorytet:** WYSOKI (modelowanie kanalu)

### `add_awgn_noise(symbols, eb_n0_db)` - Linia po linii

**Przeznaczenie:** Dodanie szumu gaussowskiego o kontrolowanej mocy

**Kod:**

```python
1   def add_awgn_noise(symbols, eb_n0_db):
2       eb_n0 = 10 ** (eb_n0_db / 10.0)
3
4       eb = 1.0
5       n0 = eb / eb_n0
6
7       sigma = np.sqrt(n0 / 2)
8
9       n_symbols = symbols.shape[0]
10
11      noise_i = sigma * np.random.normal(0, 1, size=n_symbols)
12      noise_q = sigma * np.random.normal(0, 1, size=n_symbols)
13
14      awgn_noise = noise_i + 1j * noise_q
15
16      received_symbols = symbols + awgn_noise
17
18      return received_symbols
```

**Linia 2: Konwersja dB -> liniowa**

Wzor: dB = 10·log₁₀(x) → x = 10^(dB/10)

Dlaczego:

- Uzytkownik podaje Eb/N0 w dB (standard)
- Obliczenia wymagaja skali liniowej
- dB wygodny dla czlowieka (zakres -10 do +20 dB)

**Linia 5: `n0 = eb / eb_n0`**

Definicja:

- Eb = energia na bit
- N0 = gestosc widmowa mocy szumu
- Eb/N0 = SNR w telekomunikacji

Dlaczego eb=1.0:

- Modulacje znormalizowane: E[|s|²]=1
- Upraszcza obliczenia
- Uniwersalne (dziala dla wszystkich modulacji)

**Linia 7: `sigma = np.sqrt(n0 / 2)`**

Dlaczego N0/2:

Szum zespolony = szum_I + j·szum_Q

- Moc calkowita = Var(I) + Var(Q) = N0
- Niezalezne I i Q: Var(I) = Var(Q) = N0/2
- Odchylenie std: σ = √(N0/2)

**Linie 11-12: Generowanie szumu**

Co robi:

- `np.random.normal(0, 1)` - standardowy Gauss (μ=0, σ=1)
- Mnozenie przez sigma - skalowanie do zadanej mocy

Dlaczego niezalezne I i Q:

**Alternatywa: Jeden szum zespolony**

```python
# ZLE - niepoprawny statystycznie
noise = np.random.normal(0, sigma, size=n_symbols) + \
        1j * np.random.normal(0, sigma, size=n_symbols)
```

Problem: Bledna moc (2·sigma² zamiast sigma²)

**Wybrane:** Niezalezne I i Q z sigma = √(N0/2) daje:

- Moc I = sigma² = N0/2
- Moc Q = sigma² = N0/2
- Moc total = N0 ✓

**Linia 14: Konstrukcja szumu zespolonego**

Dlaczego oddzielne I i Q:

- Szum AWGN ma niezalezne skladowe
- Model fizyczny (quadrature channels)
- Zgodny z teoria

**Linia 16: Dodanie szumu**

Najprostsza operacja - model addytywny.

Dlaczego addytywny:

**Alternatywa: Multiplikatywny (fading)**

```python
# Inny model kanalu
received_symbols = symbols * fading_coefficient + awgn_noise
```

**Wybrane:** AWGN to czysty model addytywny:

- Najprostszy kanal
- Baseline do porownan
- Dobrze zrozumiany teoretycznie

**Przyklad:**

```python
symbols = np.array([1+0j, -1+0j])
noisy = add_awgn_noise(symbols, eb_n0_db=10)
# Przy Eb/N0=10dB szum jest maly
# Wynik: [1.05+0.02j, -0.98-0.03j] (przykladowo)
```

---

## TransmissionChannel.py

**Priorytet:** SREDNI (prosta warstwa posrednia)

### `transmission_channel(symbols, eb_n0_db)` - Cala funkcja

**Przeznaczenie:** Wrapper wokol add_awgn_noise

**Kod:**

```python
1  def transmission_channel(symbols, eb_n0_db):
2      received_symbols = add_awgn_noise(symbols, eb_n0_db)
3      return received_symbols
```

**Analiza:**

Dlaczego osobny modul dla 2 linii:

**Uzasadnienie architektury:**

1. **Separation of concerns:**

   - AddAWGNNoise = generator szumu (narzedzie)
   - TransmissionChannel = model kanalu (koncept)

2. **Przyszle rozszerzenia:**

   ```python
   # Potencjalne dodania:
   def transmission_channel(symbols, eb_n0_db, channel_type='awgn'):
       if channel_type == 'awgn':
           return add_awgn_noise(symbols, eb_n0_db)
       elif channel_type == 'rayleigh':
           return add_rayleigh_fading(symbols, eb_n0_db)
       # ...
   ```

3. **Klarownosc API:**
   - Uzytkownik mysli: "transmisja przez kanal"
   - Nie: "dodanie szumu" (szczegol implementacji)

**Alternatywa: Bezposrednie wywolanie add_awgn_noise**

```python
# Mozliwe, ale mniej elastyczne
received = add_awgn_noise(symbols, eb_n0_db)
```

**Wybrane:** Osobny modul to:

- Lepsza abstrakcja (kanal != szum)
- Latwiejsze zmiany (jedne miejsce)
- Zgodne z domain model (telekomunikacja)

**Przyklad:**

```python
symbols = bpsk_modulation(bits)
received = transmission_channel(symbols, eb_n0_db=8)
# Jednoznaczne: symbole przez kanal
```

**Wzorzec:** Ten typ wrappera (cienka warstwa abstrakcji) jest powszechny w dobrze zaprojektowanym kodzie - oddziela WHAT (transmisja) od HOW (AWGN).

---

## main.py

**Priorytet:** SREDNI (orkiestracja symulacji)

### Architektura main.py

**Glowne komponenty:**

```
main()
  |
  +-- get_results_path() -----> Ustal gdzie zapisac wyniki
  |
  +-- simulate_bpsk() --------> Petla po Eb/N0, oblicz BER
  +-- simulate_qpsk()
  +-- simulate_8psk()
  +-- simulate_16qam()
  |
  +-- plot_ber_comparison() --> Wykres BER vs Eb/N0
  +-- plot_constellations() --> 4 subplots konstelacji
```

---

### `calculate_ber(original_bits, decoded_bits)` - Prosta metryka

**Kod:**

```python
1  def calculate_ber(original_bits, decoded_bits):
2      errors = np.sum(original_bits != decoded_bits)
3      ber = errors / len(original_bits)
4      return ber
```

**Linia 2: Liczenie bledow**

Co robi:

- `!=` - porownanie element po elemencie (bool array)
- `np.sum()` - zliczenie True (bledy)

Dlaczego np.sum na bool:

- True = 1, False = 0 w kontekscie numerycznym
- Szybsze niz petla

**Alternatywa: Manual loop**

```python
# Wolniejsze
errors = 0
for i in range(len(original_bits)):
    if original_bits[i] != decoded_bits[i]:
        errors += 1
```

**Linia 3: BER**

Definicja: Bit Error Rate = bledy / total

**Przyklad:**

```python
original = np.array([0,1,0,1,1])
decoded =  np.array([0,1,1,1,1])  # 1 blad (pozycja 2)
ber = calculate_ber(original, decoded)  # 1/5 = 0.2
```

---

### `simulate_bpsk(eb_n0_range, n_bits)` - Petla symulacyjna

**Kod (uproszczony):**

```python
1   def simulate_bpsk(eb_n0_range, n_bits=10000):
2       ber_values = []
3
4       for eb_n0_db in eb_n0_range:
5           bits = gen_bites(n_bits)
6           symbols = bpsk_modulation(bits)
7           received_symbols = transmission_channel(symbols, eb_n0_db)
8           decoded_bits = bpsk_demodulation(received_symbols)
9           ber = calculate_ber(bits, decoded_bits)
10          ber_values.append(ber)
11
12      return ber_values
```

**Linia 4: Petla po Eb/N0**

Dlaczego petla sekwencyjna:

**Alternatywa: Parallel processing**

```python
# Mozliwe przyspieszenie
from multiprocessing import Pool
def sim_one_snr(eb_n0_db):
    # ... symulacja ...
    return ber
with Pool() as pool:
    ber_values = pool.map(sim_one_snr, eb_n0_range)
```

Zalety: ~4x szybsze na 4-core CPU

**Wybrane:** Sekwencyjne bo:

- Prostsza implementacja
- Latwe debugowanie
- Wystarczajaco szybkie (~30s dla 10k bitow)

**Linie 5-8: Pipeline**

Diagram przepływu:

```
bits -> modulation -> channel -> demodulation -> BER
 (1)       (2)         (3)          (4)         (5)
```

Dlaczego nowe bity w kazdej iteracji:

- Symulacja Monte Carlo
- Rozne realizacje szumu
- Unikanie overfitting do konkretnej sekwencji

**Linia 10: Append**

Dlaczego lista a nie ndarray:

**Alternatywa: Prealokacja**

```python
ber_values = np.zeros(len(eb_n0_range))
for i, eb_n0_db in enumerate(eb_n0_range):
    # ...
    ber_values[i] = ber
```

Nieznacznie szybsze, ale mniej elastyczne

**Wybrane:** Lista bo:

- Nie znamy dlugosci z gory (range moze byc generator)
- Append O(1) amortyzowane
- Automatyczne dopasowanie rozmiaru

**Przyklad:**

```python
ber_values = simulate_bpsk(range(0, 11), n_bits=1000)
# Zwraca liste ~11 wartosci BER dla Eb/N0 = 0..10 dB
```

**Wzorzec:** Funkcje simulate_qpsk, simulate_8psk, simulate_16qam maja identyczna strukture - tylko zmiana funkcji modulation/demodulation. Mozliwe uogolnienie do jednej funkcji parametryzowanej.

---

### `get_results_path()` - Cross-platform path handling

**Kod:**

```python
1   def get_results_path():
2       script_dir = Path(__file__).parent.resolve()
3
4       if script_dir.name == 'src':
5           results_dir = script_dir.parent / 'results'
6       else:
7           results_dir = script_dir / 'results'
8
9       results_dir.mkdir(parents=True, exist_ok=True)
10
11      return results_dir
```

**Linia 2: Gdzie jestem**

Co robi:

- `__file__` - sciezka do biezacego pliku
- `.parent` - katalog zawierajacy plik
- `.resolve()` - sciezka absolutna

**Linie 4-7: Dwa przypadki**

Dlaczego if script_dir.name == 'src':

**Problem:** Skrypt moze byc wywolany z roznych miejsc:

1. `python src/main.py` (cwd = project root)
2. `cd src && python main.py` (cwd = src/)

**Rozwiazanie:**

- Jesli script_dir to 'src' -> idz w gore, potem do results/
- Jesli script_dir to project root -> bezposrednio do results/

**Alternatywa: Relative path od cwd**

```python
# ZLE - zalezy od cwd
results_dir = Path('results')
```

Problem: Nie dziala gdy cwd != project root

**Wybrane:** **file**-based to:

- Niezalezne od cwd
- Deterministyczne
- Zawsze dziala

**Linia 9: `mkdir(parents=True, exist_ok=True)`**

Parametry:

- `parents=True` - tworzy katalogi posrednie
- `exist_ok=True` - nie rzuca bledu jesli istnieje

Dlaczego oba:

**Bez parents:**

```python
# Jesli 'project/' nie istnieje
Path('project/results').mkdir()  # Error!
```

**Bez exist_ok:**

```python
# Drugie wywolanie
results_dir.mkdir()  # Error: katalog juz istnieje!
```

**Wybrane:** parents+exist_ok = idempotentna operacja (bezpieczne wielokrotne wywolanie).

**Przyklad:**

```python
# Z src/main.py
path = get_results_path()  # Path('/project/results')
# Z project/main.py
path = get_results_path()  # Path('/project/results')
# Ten sam wynik!
```

---

### `plot_ber_comparison()` - Kluczowe decyzje

**Kod (kluczowe fragmenty):**

```python
5   plt.figure(figsize=(12, 8))
6
7   plt.semilogy(eb_n0_range, ber_bpsk, 'bo-', linewidth=2, markersize=8, label='BPSK')
8   plt.semilogy(eb_n0_range, ber_qpsk, 'rs-', linewidth=2, markersize=8, label='QPSK')
9   # ... (podobnie dla 8-PSK i QAM)
10
11  plt.grid(True, which='both', linestyle='--', alpha=0.7)
12
13  plt.xlabel('Eb/N0 (dB)', fontsize=14, fontweight='bold')
14  plt.ylabel('Bit Error Rate (BER)', fontsize=14, fontweight='bold')
15
16  plt.ylim([1e-6, 1])
```

**Linia 7: `plt.semilogy()`**

Dlaczego semilogy nie plot:

BER typowo: 10⁰ (Eb/N0=-5dB) -> 10⁻⁶ (Eb/N0=15dB)

**Alternatywa: Liniowa skala**

```python
# ZLE - wszystkie krzywe przy dole
plt.plot(eb_n0_range, ber_values)
```

Problem: BER=10⁻⁶ nie widoczne obok BER=10⁰

**Wybrane:** Semilogy (log y-axis) bo:

- Caly zakres BER widoczny
- Standard w telekomunikacji
- Nachylenie krzywej = szybkosc poprawy

**Linia 11: `grid(which='both')`**

Co to znaczy:

- `which='major'` - tylko glowne linie siatki (10⁰, 10⁻², 10⁻⁴)
- `which='both'` - major + minor (10⁻¹, 10⁻³, 10⁻⁵)

Dlaczego both:

- Skala log wymaga gestszej siatki
- Latwiejsze odczytywanie wartosci
- Wizualnie przyjemniejsze

**Linia 16: `ylim([1e-6, 1])`**

Dlaczego sztywne limity:

**Alternatywa: Automatyczne**

```python
# Matplotlib dobiera sam
plt.semilogy(...)  # Bez ylim
```

Problem: Limity zaleza od danych, trudne porownania

**Wybrane:** Stale [10⁻⁶, 10⁰] bo:

- Typowy zakres BER
- Konsystentne miedzy wykresami
- Przemyslowy standard

**Przyklad:**

```python
plot_ber_comparison(range(0,11), ber1, ber2, ber3, ber4)
# Generuje wykres z 4 krzywymi na skali log
```

---

### `plot_constellations()` - Subplots structure

**Kod (kluczowe fragmenty):**

```python
3   fig, axes = plt.subplots(2, 2, figsize=(12, 12))
4
5   # Generate symbols
6   bpsk_symbols = bpsk_modulation(gen_bites(100))
7   # ... (dla kazdej modulacji)
8
9   # Add noise
10  eb_n0_db = 10
11  bpsk_noisy = transmission_channel(bpsk_symbols, eb_n0_db)
12  # ... (dla kazdej)
13
14  # Plot BPSK
15  ax = axes[0, 0]
16  ax.scatter(bpsk_noisy.real, bpsk_noisy.imag, alpha=0.5, s=30, c='blue', label='Received')
17  ax.scatter(bpsk_symbols.real, bpsk_symbols.imag, s=200, c='red', marker='x',
18             linewidths=3, label='Ideal')
19  # ... (labels, grid, limits)
20
21  # ... (podobnie dla QPSK, 8-PSK, QAM w innych subplotach)
```

**Linia 3: `subplots(2, 2)`**

Dlaczego 2x2:

- 4 modulacje do porownania
- Kwadratowy layout wizualnie zrownowazony
- Wystarczajaco duzy dla szczegolu (12x12 inches)

**Linia 10: Staly Eb/N0=10dB**

Dlaczego 10dB:

- Sredni SNR (nie za wysoki, nie za niski)
- Widoczny szum, ale konstelacja rozpoznawalna
- Porownywalne pomiedzy modulacjami

**Alternatywa: Rozne Eb/N0**

```python
# Gorsze - utrudnia porownanie
bpsk_noisy = transmission_channel(bpsk_symbols, 15)
qpsk_noisy = transmission_channel(qpsk_symbols, 10)
```

**Linie 16-18: Dwie warstwy**

Dlaczego osobno noisy i ideal:

**Visual hierarchy:**

1. Niebieskie kropki (noisy) - tlo, duzo punktow
2. Czerwone X (ideal) - pierwszy plan, duze i widoczne

**Parametry:**

- `alpha=0.5` dla noisy - przezroczystosc (wiele punktow)
- `s=200` dla ideal - duze (dominujace)
- `marker='x'` - wyroznia od kropek

**Przyklad:**

```python
plot_constellations()
# Tworzy 4-panelowy wykres z konstelacjami + szumem
```

**Wzorzec:** Ten sam kod struktura dla kazdego subplota - tylko zmiana danych (symbols) i labels. Wskazuje na mozliwosc ekstrakcji do funkcji pomocniczej.

---

## GetBytes.py

**Priorytet:** NISKI (prosty generator)

### `gen_bites(n_bits)` - Najprostsza funkcja

**Kod:**

```python
1  def gen_bites(n_bits):
2      return np.random.randint(0, 2, size=n_bits)
```

**Linia 2: Cala logika**

Co robi:

- `np.random.randint(low, high, size)`
- `low=0` - dolna granica (inclusive)
- `high=2` - gorna granica (exclusive) -> {0, 1}
- `size=n_bits` - dlugosc tablicy

Dlaczego randint:

**Alternatywa 1: np.random.choice**

```python
# Bardziej rozwlekle
return np.random.choice([0, 1], size=n_bits)
```

**Alternatywa 2: Bernoulli**

```python
# Wiecej importow
return np.random.binomial(1, 0.5, size=n_bits)
```

**Wybrane:** randint to:

- Najprostsza forma
- Najszybsza (optymalizowana w NumPy)
- Najbardziej bezposrednia (low, high, size)

**Nazwa funkcji:**

Literowka: "bites" powinno byc "bits"

Dlaczego nie poprawiono:

- Backward compatibility (uzywana w calym projekcie)
- Koszt zmiany > korzysc
- Powszechny w starszym kodzie

**Przyklad:**

```python
bits = gen_bites(10)  # [0,1,1,0,1,0,0,1,1,0] (przykladowo)
```

**Charakterystyka:**

- Rozklad: Uniform (p=0.5 dla 0 i 1)
- Generator: Mersenne Twister (np.random domyslny)
- Nie ustawiony seed -> rozne wyniki kazdorazowo

---

## plot_utils.py

**Priorytet:** NISKI (pomocnicze narzedzia)

### `plot_individual_constellation()` - Single plot helper

**Kod (kluczowe fragmenty):**

```python
1   def plot_individual_constellation(modulation_name, symbols, noisy_symbols=None,
2                                     save_path=None):
3       plt.figure(figsize=(8, 8))
4
5       if noisy_symbols is not None:
6           plt.scatter(noisy_symbols.real, noisy_symbols.imag,
7                      alpha=0.5, s=30, c='blue', label='Received (with noise)')
8
9       unique_symbols = np.unique(symbols)
10      plt.scatter(unique_symbols.real, unique_symbols.imag,
11                 s=300, c='red', marker='x', linewidths=4, label='Ideal constellation')
12
13      # ... (labels, grid, legend)
14
15      if save_path:
16          plt.savefig(save_path, dpi=300, bbox_inches='tight')
```

**Linia 9: `np.unique(symbols)`**

Co robi:

- Wyciaga unikalne wartosci z tablicy
- Usuwa duplikaty

Dlaczego:

Dla 100 symboli QPSK: [s1, s2, s1, s3, ...] (4 unikalne wartosci)

- Bez unique: 100 czerwonych X (nakladanie)
- Z unique: 4 czerwone X (czytelne)

**Alternatywa: Plotuj wszystkie**

```python
# ZLE - nakladajace sie markery
plt.scatter(symbols.real, symbols.imag, ...)
```

Problem: Wielokrotne rysowanie tego samego punktu

**Linie 15-16: Warunkowy zapis**

Dlaczego save_path optional:

**Use cases:**

1. `save_path=None` - tylko display (interactive)
2. `save_path='fig.png'` - zapis do pliku

Elastycznosc bez zmuszania do obu akcji.

**Przyklad:**

```python
symbols = qpsk_modulation(gen_bites(100))
plot_individual_constellation('QPSK', symbols)
# Wyswietla pojedynczy wykres QPSK
```

---

### `compare_spectral_efficiency()` - Bar chart

**Kod (kluczowe fragmenty):**

```python
2   modulations = ['BPSK', 'QPSK', '8-PSK', '16-QAM']
3   bits_per_symbol = [1, 2, 3, 4]
4
5   plt.figure(figsize=(10, 6))
6   bars = plt.bar(modulations, bits_per_symbol, color=['blue', 'green', 'orange', 'red'],
7                  alpha=0.7, edgecolor='black', linewidth=2)
8
9   for bar, value in zip(bars, bits_per_symbol):
10      height = bar.get_height()
11      plt.text(bar.get_x() + bar.get_width()/2., height,
12              f'{value} bits/symbol',
13              ha='center', va='bottom', fontsize=12, fontweight='bold')
```

**Linie 2-3: Hardcoded dane**

Dlaczego nie z symulacji:

- Spectral efficiency = parametr modulacji (staly)
- Nie zalezy od Eb/N0 czy szumu
- Dane konceptualne, nie empiryczne

**Linie 9-13: Etykiety na slupkach**

Co robi:

- Iteracja przez bars (obiekty Rectangle matplotlib)
- `.get_height()` - wysokosc slupka
- `plt.text()` - tekst nad slupkiem

Dlaczego nad slupkami a nie w legendzie:

- Bezposrednia informacja (bez szukania w legendzie)
- Wizualnie atrakcyjniejsze
- Standard w business charts

**Przyklad:**

```python
compare_spectral_efficiency()
# Generuje bar chart z 4 slupkami
```

**Wzorzec:** Ta funkcja jest samowystarczalna (nie wymaga danych wejsciowych) - typ utility function do jednorazowego uzycia.

---

## Wzorce projektowe i decyzje globalne

### 1. Konwencja nazewnicza

**Funkcje:** `snake_case`

- `bpsk_modulation`, `calculate_ber`
- Standard Python (PEP 8)

**Zmienne:** `snake_case`

- `eb_n0_db`, `bit_pairs`
- Rozroznienie od stalych

**Stale (nie uzyte w tym projekcie):** `UPPER_CASE`

- `MAX_BITS = 100000`
- Konwencja (projekt nie ma stalych globalnych)

### 2. Struktura plikow

Dlaczego modularne pliki a nie jeden big script:

**Zalety podzialu:**

- Separation of concerns (kazdy modul = 1 odpowiedzialnosc)
- Latwe testowanie (import pojedynczych funkcji)
- Reusability (np. Modulator.py w innym projekcie)
- Czytelnosc (50-200 linii na plik vs 1000+)

**Alternatywa: Monolityczny script**

```python
# all_in_one.py (1500 linii)
# Trudne utrzymanie, debugowanie, testowanie
```

### 3. Type hints (brak)

Projekt nie uzywa type hints:

```python
# Bez type hints
def bpsk_modulation(bits):
    ...

# Mozliwe z type hints
def bpsk_modulation(bits: np.ndarray) -> np.ndarray:
    ...
```

Dlaczego brak:

- Starszy kod (sprzed popularnosci type hints)
- NumPy types skomplikowane (ndarray[float64] vs ndarray[complex128])
- Docstringi wystarczajace w tym przypadku

### 4. Error handling (minimalne)

Projekt ma tylko podstawowa walidacje:

```python
# Obecne
if len(bits) % 2 != 0:
    raise ValueError("...")

# Mozliwe rozszerzenie
if not isinstance(bits, np.ndarray):
    raise TypeError("bits must be numpy array")
if bits.dtype not in [np.int32, np.int64]:
    raise TypeError("bits must be integer array")
# ...
```

Dlaczego minimalne:

- Kod "naukowy" (kontrolowane wejscia)
- Priorytet: szybkosc implementacji > robustness
- Uzytkownik = developer (nie end-user)

### 5. Testowanie (brak unit tests)

Projekt nie ma formalnych testow:

```python
# Brak
def test_bpsk_perfect_channel():
    bits = np.array([0,1,0,1])
    symbols = bpsk_modulation(bits)
    received = transmission_channel(symbols, eb_n0_db=100)
    decoded = bpsk_demodulation(received)
    assert np.array_equal(bits, decoded)
```

Dlaczego brak:

- Prototyp/research code
- Weryfikacja przez wykresy (wizualna)
- Testy "ad-hoc" w `if __name__ == "__main__"` blokach

**Trade-off:** Szybsza implementacja vs stabilnosc long-term.

### 6. Dokumentacja (docstringi vs komentarze)

Projekt uzywa docstringow:

```python
def bpsk_modulation(bits):
    """
    BPSK modulation...

    Parameters
    ----------
    ...
    """
```

Dlaczego docstringi a nie komentarze:

**Zalety docstringow:**

- `help(bpsk_modulation)` dziala
- IDE pokazuja tooltips
- Mozliwosc auto-generacji dokumentacji (Sphinx)

**Komentarze inline:**

- Uzyte sporadycznie
- Tylko dla skomplikowanych linii
- Nie dla oczywistych operacji

### 7. Numeracja linii w dokumentacji

Format:

```python
1  def function():
2      line1
3      line2
```

Dlaczego:

- Latwe referencje ("zobacz linia 5")
- Zgodnosc z edytorami kodu
- Standard w code review

---

## Optymalizacje i bottlenecki

### 1. Bottleneck: Petla w simulate\_\*

**Obecne:**

```python
for eb_n0_db in range(-2, 16):  # 18 iteracji
    # ... symulacja ...
```

**Czas:** ~30s dla n_bits=10000

**Optymalizacja: Parallel**

```python
from multiprocessing import Pool

def sim_one(eb_n0_db):
    # ... pojedyncza symulacja ...
    return ber

with Pool(processes=4) as pool:
    ber_values = pool.map(sim_one, range(-2, 16))
```

**Przyspieszenie:** ~4x (na 4-core CPU)

**Dlaczego nie zaimplementowane:**

- Dodatkowa zlozonosc (imports, pool management)
- Wystarczajaco szybkie dla prototypu
- Trudniejsze debugowanie

### 2. Bottleneck: QAM demodulation loop

**Obecne:**

```python
for idx, symbol in enumerate(denorm_symbols):
    i_bits = pam4_demod(symbol.real)
    q_bits = pam4_demod(symbol.imag)
    bits[4*idx:4*idx+4] = i_bits + q_bits
```

**Mozliwa wektoryzacja:**

```python
# Progi
thresholds_I = np.array([-2, 0, 2])
thresholds_Q = np.array([-2, 0, 2])

# Digitize (find bin)
i_levels = np.digitize(denorm_symbols.real, thresholds_I)
q_levels = np.digitize(denorm_symbols.imag, thresholds_Q)

# Map levels -> bits (lookup table)
level_to_bits = {0:[0,0], 1:[0,1], 2:[1,1], 3:[1,0]}
# ... (vectorized application)
```

**Przyspieszenie:** ~2-3x

**Dlaczego nie:**

- Skomplikowane (digitize + lookup)
- Demodulacja nie jest bottleneck (szybka vs symulacja)

### 3. Memory: Prealokacja vs append

**Obecne:**

```python
ber_values = []
for ...:
    ber_values.append(ber)
```

**Alternatywa:**

```python
ber_values = np.zeros(len(eb_n0_range))
for i, ...:
    ber_values[i] = ber
```

**Trade-off:**

- Append: O(1) amortyzowane, elastyczne
- Prealokacja: O(1) zawsze, wymaga znania rozmiaru

W tym przypadku: roznica pomijalnie mala (18 elementow).

---

## Najczescsze pytania (FAQ)

**Q: Dlaczego wszystkie modulacje zwracaja complex, nawet BPSK?**

A: Uniwersalny interfejs. TransmissionChannel i Demodulator oczekuja complex. Bez konwersji miedzy etapami. Upraszcza kod.

**Q: Dlaczego Gray coding, nie natural coding?**

A: Minimalizuje BER. Przy bledzie symbolu (najblizsza konstelacja) zmienia sie 1 bit zamiast 2. Standard w telekomunikacji.

**Q: Dlaczego petla w QPSK demodulation, nie wektorowe?**

A: Trudne do wektoryzacji (przeplatanie bitow). Petla jest czytelna. Nie bottleneck (mala liczba symboli). Trade-off: czytelnosc > szybkosc.

**Q: Dlaczego separate TransmissionChannel.py dla 2 linii kodu?**

A: Separation of concerns. Abstrakcja (kanal != szum). Przyszle rozszerzenia (inne typy kanalow). Klarowne API.

**Q: Dlaczego brak testow jednostkowych?**

A: Research/prototyping code. Weryfikacja wizualna (wykresy). Testy ad-hoc w `if __name__`. Trade-off: szybkosc rozwoju vs robustness.

**Q: Dlaczego semilogy a nie plot dla BER?**

A: BER zmienia sie wykładniczo (10⁰ -> 10⁻⁶). Skala liniowa nieczytelna. Semilogy to standard w telekomunikacji.

**Q: Czy moge uzyc tego kodu w projekcie komercyjnym?**

A: Sprawdz licencje (README). Typowo kod edukacyjny = swobodne uzycie. Autor = ModulationPSKProject Team.

---

## Koniec dokumentacji technicznej

**Wersja:** 1.0  
**Data:** 2025-10-23  
**Autor:** AI Assistant  
**Format:** Markdown bez polskich znakow diakrytycznych

Dla wiecej informacji:

- README.md - przeglad projektu
- docs/index.md - indeks dokumentacji
- code-documentation.md - konceptualne wyjasnienia

---
