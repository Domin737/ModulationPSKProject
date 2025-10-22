# WYJASNIENIE DZIALANIA KODU - ModulationPSKProject

## Przeglad systemu

Projekt symuluje system komunikacji cyfrowej, w ktorym:
1. Bity sa generowane losowo
2. Bity sa modulowane (przeksztalcane w symbole zespolone)
3. Symbole sa przesylane przez kanal z szumem
4. Symbole sa demodulowane z powrotem na bity
5. Obliczana jest liczba bledow (BER)

---

## MODUL 1: GetBytes.py

### Cel:
Generowanie losowych bitow do transmisji

### Jak dziala:

```python
def gen_bites(n_bits):
    return np.random.randint(0, 2, size=(n_bits))
```

**Krok po kroku:**
1. Funkcja przyjmuje liczbe bitow `n_bits`
2. `np.random.randint(0, 2, ...)` generuje losowe liczby 0 lub 1
3. `size=(n_bits)` okresla rozmiar tablicy
4. Zwraca tablice NumPy z losowymi bitami

**Przyklad:**
```python
bits = gen_bites(8)
# Wynik: [1, 0, 1, 1, 0, 0, 1, 0]
```

### Zastosowanie:
Te bity reprezentuja dane, ktore chcemy wyslac przez kanal komunikacyjny.

---

## MODUL 2: Modulator.py

### Cel:
Przeksztalcanie bitow w symbole zespolone (complex numbers)

### 2.1 BPSK (Binary Phase-Shift Keying)

**Zasada:**
- Kazdy bit jest mapowany na jeden symbol
- Bit 0 → +1
- Bit 1 → -1

```python
def bpsk_modulation(bits):
    symbols = 1 - 2 * bits
    return symbols.astype(complex)
```

**Jak dziala matematyka:**
- Jesli bit = 0: 1 - 2*0 = 1
- Jesli bit = 1: 1 - 2*1 = -1

**Przyklad:**
```python
bits = [0, 1, 0, 1]
symbols = bpsk_modulation(bits)
# Wynik: [1+0j, -1+0j, 1+0j, -1+0j]
```

**Diagram konstelacji BPSK:**
```
        -1 ●--------●--------● +1
                    0
```

### 2.2 QPSK (Quadrature Phase-Shift Keying)

**Zasada:**
- Kazde 2 bity sa mapowane na jeden symbol
- 4 mozliwe symbole na okregu jednostkowym

```python
def qpsk_modulation(bits):
    # Reshape bits into pairs
    bits_reshaped = bits.reshape(-1, 2)
    
    # Map bit pairs to symbols
    for bit_pair in bits_reshaped:
        if bit_pair == [0, 0]: symbol = (1+1j)/sqrt(2)   # 45°
        if bit_pair == [0, 1]: symbol = (-1+1j)/sqrt(2)  # 135°
        if bit_pair == [1, 0]: symbol = (1-1j)/sqrt(2)   # 315°
        if bit_pair == [1, 1]: symbol = (-1-1j)/sqrt(2)  # 225°
```

**Przyklad:**
```python
bits = [0, 0, 0, 1, 1, 0, 1, 1]
# Pary: [0,0], [0,1], [1,0], [1,1]
symbols = qpsk_modulation(bits)
# 4 symbole na okregu
```

**Diagram konstelacji QPSK:**
```
        Q
        |
   01 ● | ● 00
        |
--------+-------- I
        |
   11 ● | ● 10
        |
```

**Dlaczego dzielimy przez sqrt(2)?**
- Aby srednia moc symboli byla rowna 1
- |symbol|^2 = (1^2 + 1^2)/2 = 1

### 2.3 8-PSK

**Zasada:**
- Kazde 3 bity → 1 symbol
- 8 symboli rowno rozmieszczonych na okregu

```python
def psk8_modulation(bits):
    # Convert triplets to decimal (0-7)
    decimal_values = bits[:, 0]*4 + bits[:, 1]*2 + bits[:, 2]
    
    # Symbol k is at angle k * pi/4
    angles = decimal_values * np.pi / 4
    symbols = np.exp(1j * angles)
```

**Przyklad:**
```python
bits = [0, 0, 0]  # decimal = 0
angle = 0 * pi/4 = 0°
symbol = exp(j*0) = 1+0j

bits = [0, 0, 1]  # decimal = 1
angle = 1 * pi/4 = 45°
symbol = exp(j*pi/4) = (1+1j)/sqrt(2)
```

**Diagram konstelacji 8-PSK:**
```
        001
         |
    010  |  000
       \ | /
        \|/
   011---+---111
        /|\
       / | \
    100  |  110
         |
        101
```

### 2.4 16-QAM

**Zasada:**
- Kazde 4 bity → 1 symbol
- 16 symboli w siatce 4×4
- Rozne amplitudy i fazy

```python
def qam16_modulation(bits):
    # Split into I and Q components (2 bits each)
    i_bits = bits[:, :2]  # First 2 bits
    q_bits = bits[:, 2:]  # Last 2 bits
    
    # Map 2 bits to levels: 00→+3, 01→+1, 10→-1, 11→-3
    i_component = map_to_level(i_bits)
    q_component = map_to_level(q_bits)
    
    symbols = i_component + 1j * q_component
    symbols = symbols / sqrt(10)  # Normalization
```

**Przyklad:**
```python
bits = [0, 0, 1, 1]
# I bits: [0, 0] → +3
# Q bits: [1, 1] → -3
symbol = (3 - 3j) / sqrt(10)
```

**Diagram konstelacji 16-QAM:**
```
    Q
    |
  ● ● ● ●
  ● ● ● ●
----+---- I
  ● ● ● ●
  ● ● ● ●
    |
```

---

## MODUL 3: AddAWGNNoise.py

### Cel:
Symulacja szumu w kanale transmisyjnym

### Jak dziala:

```python
def add_awgn_noise(symbols, eb_n0_db):
    # Convert Eb/N0 from dB to linear
    eb_n0 = 10 ** (eb_n0_db / 10.0)
    
    # Calculate noise power
    eb = 1.0  # Normalized energy per bit
    n0 = eb / eb_n0
    sigma = np.sqrt(n0 / 2)
    
    # Generate Gaussian noise
    noise_i = sigma * np.random.normal(0, 1, size=n_symbols)
    noise_q = sigma * np.random.normal(0, 1, size=n_symbols)
    awgn_noise = noise_i + 1j * noise_q
    
    # Add noise to symbols
    received_symbols = symbols + awgn_noise
    return received_symbols
```

**Krok po kroku:**

1. **Konwersja Eb/N0 z dB:**
   - Eb/N0 = 10 dB
   - Eb/N0 (liniowo) = 10^(10/10) = 10

2. **Obliczenie mocy szumu:**
   - Eb = 1 (znormalizowana energia)
   - N0 = Eb / (Eb/N0) = 1/10 = 0.1
   - sigma = sqrt(N0/2) = sqrt(0.05) ≈ 0.224

3. **Generowanie szumu:**
   - Szum gaussowski z srednia = 0, odchylenie = sigma
   - Osobno dla czesci rzeczywistej (I) i urojonej (Q)

4. **Dodanie szumu:**
   - received = original + noise

**Przyklad:**
```python
symbols = [1+0j, -1+0j]
eb_n0_db = 10

# Wygenerowany szum: 0.1+0.2j, -0.15+0.1j
received = [1.1+0.2j, -1.15+0.1j]
```

**Co to jest Eb/N0?**
- Eb = Energia przypadajaca na jeden bit
- N0 = Gestosc widmowa mocy szumu
- Eb/N0 mierzy jakosc sygnalu
- Wyzsze Eb/N0 = mniej szumu = lepsza transmisja

**Typowe wartosci:**
- Eb/N0 = 0 dB: Bardzo duzo szumu, BER ≈ 0.5
- Eb/N0 = 10 dB: Umiarkowany szum, BER ≈ 10^-5 dla BPSK
- Eb/N0 = 20 dB: Bardzo maly szum, BER ≈ 0

---

## MODUL 4: TransmissionChannel.py

### Cel:
Symulacja kanalu transmisyjnego

### Jak dziala:

```python
def transmission_channel(symbols, eb_n0_db):
    received_symbols = add_awgn_noise(symbols, eb_n0_db)
    return received_symbols
```

**To prosty wrapper, ktory:**
1. Przyjmuje symbole i Eb/N0
2. Wywoluje funkcje dodawania szumu
3. Zwraca zaklocone symbole

**W rzeczywistym systemie** kanal moze rowniez modelowac:
- Fading (zanikanie)
- Interferencje
- Opoznienia
- Efekt Dopplera

---

## MODUL 5: Demodulator.py

### Cel:
Odzyskiwanie bitow z odebranych symboli

### 5.1 BPSK Demodulation

**Zasada:** Decyzja progowa
- Jesli Real(symbol) > 0 → bit = 0
- Jesli Real(symbol) < 0 → bit = 1

```python
def bpsk_demodulation(received_symbols):
    decoded_bits = (received_symbols.real < 0).astype(int)
    return decoded_bits
```

**Przyklad:**
```python
received = [0.9+0.1j, -1.1-0.05j, 0.8+0.2j]
# Real parts: [0.9, -1.1, 0.8]
# 0.9 > 0 → bit 0
# -1.1 < 0 → bit 1
# 0.8 > 0 → bit 0
decoded = [0, 1, 0]
```

**Wizualizacja:**
```
    -1    0    +1
     ●----|----|----●
          ^
    Prog decyzyjny
```

### 5.2 QPSK Demodulation

**Zasada:** Maximum Likelihood (ML) Detection
- Znajdz najblizsza konstelacje punkt
- Zamien na bity

```python
def qpsk_demodulation(received_symbols):
    # Define constellation
    constellation = [
        (1+1j)/sqrt(2),   # 00
        (-1+1j)/sqrt(2),  # 01
        (1-1j)/sqrt(2),   # 10
        (-1-1j)/sqrt(2)   # 11
    ]
    
    for symbol in received_symbols:
        # Find closest constellation point
        distances = |symbol - constellation|
        closest_index = argmin(distances)
        bits = bit_mapping[closest_index]
```

**Przyklad:**
```python
received = 0.8 + 0.9j

# Odleglosci do punktow konstelacji:
# |received - (1+1j)/sqrt(2)| = 0.15  <- Najblizszy!
# |received - (-1+1j)/sqrt(2)| = 1.5
# |received - (1-1j)/sqrt(2)| = 1.8
# |received - (-1-1j)/sqrt(2)| = 2.5

# Najblizsza: (1+1j)/sqrt(2) → bity [0, 0]
```

### 5.3 8-PSK i 16-QAM Demodulation

**Podobna zasada:**
1. Zdefiniuj wszystkie punkty konstelacji
2. Dla kazdego odebranego symbolu:
   - Oblicz odleglosc do wszystkich punktow
   - Wybierz najblizsza
   - Zamien na bity

---

## MODUL 6: main.py

### Cel:
Pelna symulacja i generowanie wykresow

### 6.1 Funkcja simulate_modulation()

```python
def simulate_modulation(modulation_type, eb_n0_range, n_bits):
    ber_values = []
    
    for eb_n0_db in eb_n0_range:
        # 1. Generate bits
        bits = gen_bites(n_bits)
        
        # 2. Modulate
        symbols = modulate(bits)
        
        # 3. Transmit through channel
        received = transmission_channel(symbols, eb_n0_db)
        
        # 4. Demodulate
        decoded = demodulate(received)
        
        # 5. Calculate BER
        ber = calculate_ber(bits, decoded)
        ber_values.append(ber)
    
    return ber_values
```

**Co sie dzieje:**

1. **Petla po Eb/N0:**
   - Dla kazdej wartosci Eb/N0 (np. 0, 1, 2, ..., 10 dB)
   - Wykonaj symulacje

2. **Dla kazdego Eb/N0:**
   - Wygeneruj losowe bity
   - Moduluj → symbole
   - Przeslij przez kanal (dodaj szum)
   - Demoduluj → zdekodowane bity
   - Policz bledy

3. **Obliczanie BER:**
   ```python
   errors = sum(bits != decoded_bits)
   ber = errors / total_bits
   ```

**Przyklad:**
```
Eb/N0 = 0 dB:
  Wysłano:  [1, 0, 1, 1, 0]
  Odebrano: [1, 1, 1, 0, 0]
  Bledy:    [0, 1, 0, 1, 0]
  BER = 2/5 = 0.4

Eb/N0 = 10 dB:
  Wysłano:  [1, 0, 1, 1, 0]
  Odebrano: [1, 0, 1, 1, 0]
  Bledy:    [0, 0, 0, 0, 0]
  BER = 0/5 = 0.0
```

### 6.2 Funkcja plot_ber_curves()

Tworzy wykres BER vs Eb/N0:

```python
plt.semilogy(eb_n0_range, ber_values)
plt.xlabel('Eb/N0 (dB)')
plt.ylabel('BER')
```

**Skala logarytmiczna (semilogy):**
- Os Y w skali logarytmicznej
- Pozwala zobaczyc BER od 1 do 10^-6

**Przykladowy wykres:**
```
BER
 1  |●
    |  ●
0.1 |    ●
    |      ●
0.01|        ●
    |          ●
0.001|           ●
    +---------------
     0  2  4  6  8  10  Eb/N0(dB)
```

### 6.3 Funkcja plot_constellation()

Tworzy diagramy konstelacji:

```python
# Clean constellation
plt.scatter(symbols.real, symbols.imag)

# Noisy constellation
noisy = transmission_channel(symbols, eb_n0_db=10)
plt.scatter(noisy.real, noisy.imag)
```

**Przyklad dla QPSK:**
```
Czysty:          Z szumem (10 dB):
   Q                  Q
   |                  |
 ● | ●              ●●|●●
   |                  |
---+---            ---+---
   |                  |
 ● | ●              ●●|●●
   |                  |
   I                  I
```

---

## JAK CALY SYSTEM DZIALA RAZEM

### Przeplyw danych - krok po kroku:

```
Krok 1: GENERACJA
[0, 1, 0, 1, 1, 0] <- gen_bites(6)

Krok 2: MODULACJA (QPSK)
[0,1] → (-1+1j)/√2
[0,1] → (-1+1j)/√2
[1,0] → (1-1j)/√2
                    <- qpsk_modulation()

Krok 3: KANAL (Eb/N0 = 10 dB)
Symbole + szum
                    <- transmission_channel()

Krok 4: DEMODULACJA
Najblizsza konstelacja → bity
[0, 1, 0, 1, 1, 0]  <- qpsk_demodulation()

Krok 5: POROWNANIE
Original: [0, 1, 0, 1, 1, 0]
Decoded:  [0, 1, 0, 1, 1, 0]
Bledy: 0
BER = 0/6 = 0
```

---

## KLUCZOWE KONCEPCJE

### 1. Modulacja
**Pytanie:** Dlaczego modulujemy?
**Odpowiedz:** Aby przeslac bity przez kanal fizyczny (fale radiowe, kable).

### 2. Szum
**Pytanie:** Skad sie bierze szum?
**Odpowiedz:** Z termicznego ruchu elektronow, interferencji, zanikania sygnalu.

### 3. Eb/N0
**Pytanie:** Co to znaczy?
**Odpowiedz:** 
- Eb = Energia jednego bitu
- N0 = Moc szumu na 1 Hz
- Eb/N0 = stosunek energii sygnalu do szumu
- Wyzsze = lepiej

### 4. BER
**Pytanie:** Co to znaczy?
**Odpowiedz:** Procent blednie odebranych bitow.
- BER = 0.01 = 1% bitow blednych
- BER = 10^-5 = 0.001% bitow blednych

### 5. Dlaczego QPSK jest lepsze niz BPSK?
**Odpowiedz:** 
- BPSK: 1 bit/symbol
- QPSK: 2 bity/symbol
- QPSK ma 2× wyzsza przepustowosc przy podobnej BER

### 6. Dlaczego 8-PSK jest gorsze niz QPSK?
**Odpowiedz:**
- 8-PSK ma wiecej punktow na tym samym okregu
- Punkty sa blizej siebie
- Latwiej pomylic punkty przy szumie
- Wyzsza BER

---

## MATEMATYKA W SKROCIE

### Konwersja dB:
```
Eb/N0 (dB) = 10 * log10(Eb/N0)
Eb/N0 = 10^(Eb/N0_dB / 10)

Przyklad:
10 dB → 10^(10/10) = 10
20 dB → 10^(20/10) = 100
```

### Moc szumu:
```
N0 = Eb / (Eb/N0)
sigma = sqrt(N0/2)

Przyklad:
Eb/N0 = 10, Eb = 1
N0 = 1/10 = 0.1
sigma = sqrt(0.05) ≈ 0.224
```

### BER:
```
BER = liczba_bledow / liczba_bitow

Przyklad:
10000 bitow, 5 bledow
BER = 5/10000 = 0.0005 = 5×10^-4
```

---

## TYPOWE WYNIKI

### BPSK:
```
Eb/N0 (dB)  BER
-2          0.15
0           0.08
2           0.02
4           0.002
6           0.0001
8           10^-5
10          10^-6
```

### QPSK:
```
Podobne do BPSK (dla tego samego Eb/N0)
```

### 8-PSK:
```
Eb/N0 (dB)  BER
-2          0.35
0           0.20
2           0.10
4           0.03
6           0.005
8           0.001
10          0.0001
```

### 16-QAM:
```
Eb/N0 (dB)  BER
-2          0.45
0           0.30
2           0.15
4           0.06
6           0.02
8           0.005
10          0.001
```

**Wniosek:** BPSK i QPSK maja najlepsza odpornosc na szum!

---

## PODSUMOWANIE

### Co robi kazdy modul:
1. **GetBytes.py** - Generuje losowe bity
2. **Modulator.py** - Bity → Symbole zespolone
3. **AddAWGNNoise.py** - Dodaje szum gaussowski
4. **TransmissionChannel.py** - Symuluje kanal
5. **Demodulator.py** - Symbole → Bity
6. **main.py** - Kontroluje symulacje i rysuje wykresy

### Jak to dziala razem:
```
Bity → Modulacja → Kanal+Szum → Demodulacja → Bity
                                                   ↓
                                            Porownanie
                                                   ↓
                                                 BER
```

### Glowne wnioski:
- Im wyzsze Eb/N0, tym nizsze BER
- BPSK jest najbardziej odporny na szum
- QPSK ma dobry kompromis: wydajnosc vs odpornosc
- 8-PSK i QAM sa bardziej podatne na szum

---

**Data:** 2025-10-22  
**Wersja:** 1.0  
**Status:** Pelne wyjasnienie gotowe
