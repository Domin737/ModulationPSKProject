# Theoretical Background - Digital Modulation Systems

## Wprowadzenie

Wyobraz sobie, ze chcesz wyslac wiadomosc do kolegi, ktory jest po drugiej stronie ogrodu. Mozesz krzyknac, ale jesli jest glosno, moze Cie nie uslyszec. Mozesz tez uzyc latarki i migac nia - jasne = 1, ciemne = 0. To jest w zasadzie to, co robi modulacja cyfrowa!

**Modulacja cyfrowa** to sposob na "pakowanie" informacji cyfrowej (bitow: 0 i 1) do fali elektromagnetycznej, ktora moze byc przeslana przez powietrze, kabel, lub swiatlo.

### Po co nam modulacja?

Nie mozemy po prostu "wyslac bitow" przez powietrze. Dlaczego?

1. **Bity to tylko logiczna koncepcja** - musimy je przeksztalcic w cos fizycznego (fale radiowe)
2. **Anteny maja preferowane czestotliwosci** - fale bardzo niskiej czestotliwosci wymagalyby ogromnych anten
3. **Chcemy wykorzystac dostepne pasmo** - transmisja na wyzszych czestotliwosciach pozwala przeslac wiecej danych

**Analogia:** Wyobraz sobie, ze bity to listy, a modulacja to koperty. Nie mozesz wyslac listow bez kopert - musisz je zapakowac w cos, co moze byc przetransportowane przez system pocztowy (fale radiowe).

---

## 1. Podstawy: Sygnal, Amplituda, Faza, Czestotliwosc

Zanim zrozumiemy modulacje, musimy zrozumiec fale.

### 1.1 Co to jest sygnal?

Sygnal elektromagnetyczny to fala - cos, co oscyluje (faluje) w czasie. Najprostszy przyklad to **sinusoida**:

```
Amplituda (A)
    ^
  A |     ╱╲        ╱╲
    |    ╱  ╲      ╱  ╲
  0 |---╱----╲----╱----╲----> Czas (t)
    |        ╲  ╱        ╲  ╱
 -A |         ╲╱          ╲╱
```

**Wzor matematyczny:**

```
s(t) = A * cos(2π * f * t + φ)

gdzie:
A = Amplituda (wysokosc fali)
f = Czestotliwosc (ile razy na sekunde fala sie powtarza)
φ = Faza poczatkowa (gdzie fala zaczyna)
t = Czas
```

### 1.2 Trzy parametry fali

Fala sinusoidalna ma trzy kluczowe parametry, ktorymi mozemy manipulowac:

#### **1.2.1 Amplituda (A)**

To "wysokosc" fali - jak mocny jest sygnal.

```
Duza amplituda:         Mala amplituda:
      ╱╲                    ╱╲
     ╱  ╲                  ╱  ╲
────╱────╲────          ──────────
         ╲  ╱              ╲╱
          ╲╱
```

**Analogia:** Glosnosc dzwieku - moze byc glosno lub cicho, ale to wciaz ten sam dzwiek.

#### **1.2.2 Czestotliwosc (f)**

Ile razy na sekunde fala sie powtarza (mierzone w Hz - Hertz).

```
Wysoka czestotliwosc:      Niska czestotliwosc:
╱╲╱╲╱╲╱╲╱╲                ╱────╲       ╱────╲
            czas                    czas
```

**Analogia:** Wysokosc dzwieku - wysoki pisk vs. niski bas.

**Przyklad:**

- FM Radio: ~100 MHz (100 milionow razy na sekunde!)
- WiFi: 2.4 GHz lub 5 GHz (miliardy razy na sekunde!)

#### **1.2.3 Faza (φ)**

To "przesuniecie" fali w czasie - gdzie fala zaczyna.

```
Faza 0°:          Faza 90°:         Faza 180°:
  ╱╲                ╲               ╲  ╱
 ╱  ╲              ╱ ╲               ╲╱
╱────╲            ───╲╱              ──────
      ╲  ╱            ╱╲                ╱╲
       ╲╱                               ╱  ╲
```

**Analogia:** Wyobraz sobie dwie osoby biegnace w kolko. Moga biegac z ta sama predkoscia (czestotliwoscia), ale jeden moze byc "do przodu" wzgledem drugiego. To jest róznica faz.

**Wazne:** W modulacji cyfrowej bedziemy **zmieniac te parametry**, zeby zakodowac informacje (bity)!

---

## 2. Czym jest modulacja?

**Modulacja** = zmiana parametrow fali nosnej, aby przenosila informacje

**Fala nosna (carrier)** = podstawowa fala o stalej czestotliwosci, ktora "niesie" nasze dane

Mamy trzy podstawowe typy modulacji:

1. **AM (Amplitude Modulation)** - zmieniamy amplitudę
2. **FM (Frequency Modulation)** - zmieniamy czestotliwosc
3. **PM (Phase Modulation)** - zmieniamy faze

**W naszej aplikacji skupiamy sie na modulacji fazowej (PM) i amplitudowo-fazowej!**

### 2.1 Po co nam liczby zespolone?

Zauwaz, ze w kodzie uzywamy typu `complex` (liczby zespolone). Dlaczego?

Liczba zespolona: **z = I + jQ**

- **I** = skladowa "in-phase" (w fazie) = Re(z)
- **Q** = skladowa "quadrature" (przesunieta o 90°) = Im(z)

```
Plaszczyzna zespolona (IQ plane):
        Q (urojona)
        ^
        |
    I+jQ|
        |
────────┼────────> I (rzeczywista)
        |
        |
```

**Dlaczego to jest uzyteczne?**

Kazda fala sinusoidalna moze byc reprezentowana jako punkt na plaszczzyzne zespolone:

- Odleglosc od (0,0) = amplituda fali
- Kat od osi I = faza fali

**Przyklad:**

```
z = 1 + 0j  -> amplituda = 1, faza = 0°
z = 0 + 1j  -> amplituda = 1, faza = 90°
z = -1 + 0j -> amplituda = 1, faza = 180°
z = 0.707 + 0.707j -> amplituda = 1, faza = 45°
```

**Formula Eulera** laczy to wszystko:

```
e^(jφ) = cos(φ) + j*sin(φ)

To pozwala zapisac fale jako:
s(t) = A * e^(j*2π*f*t)
```

---

## 3. BPSK - Binary Phase-Shift Keying

### 3.1 Idea

BPSK to **najprostsza modulacja cyfrowa**:

- Przesylamy **1 bit na symbol**
- Mamy **2 mozliwe symbole** (stany fazy)

**Mapowanie:**

```
bit 0 → faza 0°   → symbol +1
bit 1 → faza 180° → symbol -1
```

### 3.2 Diagram konstelacji

```
        Q (Imaginary)
        ^
        |
        |
   -1   |   +1
   (1)  |   (0)
────────┼────────> I (Real)
        |
        |
```

Symbole leza na osi rzeczywistej - dlatego BPSK to tez **2-PAM** (2-level Pulse Amplitude Modulation).

### 3.3 Dlaczego to dziala?

Gdy przesylamy symbol +1 lub -1, odbiornik musi tylko sprawdzic:

- Czy odebranej symbol jest blizej +1 czy -1?

**Prog decyzyjny** = 0

```
Odebrany symbol:
  > 0  →  dekoduj jako bit 0
  < 0  →  dekoduj jako bit 1
```

### 3.4 Przyklad transmisji

```
Bity do wyslania:    0  1  0  1
                     ↓  ↓  ↓  ↓
Symbole BPSK:       +1 -1 +1 -1
                     ↓  ↓  ↓  ↓
Przeslano fale:     ╱╲ ╲╱ ╱╲ ╲╱

Odbiornik dekoduje:  0  1  0  1  ✓
```

### 3.5 Zalety i wady

**Zalety:**

- ✓ Najprostsza implementacja
- ✓ Najlepsza odpornosc na szum (symbole maksymalnie oddalone)
- ✓ Niskie wymagania mocy

**Wady:**

- ✗ Niska wydajnosc (tylko 1 bit/symbol)
- ✗ Wolna transmisja danych

**Gdzie sie to stosuje:**

- Satelity (mala moc, duza odleglosc)
- RFID tagi
- Starsze modemy

---

## 4. QPSK - Quadrature Phase-Shift Keying

### 4.1 Idea

QPSK to **ulepszona wersja BPSK**:

- Przesylamy **2 bity na symbol**
- Mamy **4 mozliwe symbole** (stany fazy)

**Mapowanie (Gray coding):**

```
00 → 45°  → (+1+j)/√2
01 → 135° → (-1+j)/√2
11 → 225° → (-1-j)/√2
10 → 315° → (+1-j)/√2
```

### 4.2 Diagram konstelacji

```
        Q
        ^
        |
   01   |   00     <- 2 bity przypisane
    •   |   •         do kazdego symbolu
        |
────────┼────────> I
        |
    •   |   •
   11   |   10
        |
```

Symbole tworza "krzyż" pod katami 45°, 135°, 225°, 315°.

### 4.3 Dlaczego Gray coding?

**Gray coding** oznacza, ze sasiednie symbole roznia sie tylko **1 bitem**.

```
Bez Gray coding:        Z Gray coding:
   00  01                  00  01
    •   •                   •   •

    •   •                   •   •
   10  11                  11  10
   ↑                          ↑
   2 bity sie roznia!     Tylko 1 bit!
```

**Dlaczego to wazne?** Gdy szum przesuwa symbol do sasiedniego punktu, pomylka dotyczy tylko 1 bitu zamiast 2. To **zmniejsza BER** (Bit Error Rate).

### 4.4 Wydajnosc vs BPSK

QPSK ma **2x wieksza wydajnosc** niz BPSK!

```
BPSK: 1000 symboli = 1000 bitow
QPSK: 1000 symboli = 2000 bitow  <- Dwa razy wiecej!
```

**Przy tej samej predkosci symboli, QPSK przesyla dwa razy wiecej danych.**

### 4.5 Zalety i wady

**Zalety:**

- ✓ 2x wyzsza wydajnosc niz BPSK
- ✓ Podobna odpornosc na szum jak BPSK (przy tym samym Eb/N0)
- ✓ Efektywne wykorzystanie pasma

**Wady:**

- ✗ Bardziej skomplikowana implementacja niz BPSK
- ✗ Wymaga demodulacji dwoch skladowych (I i Q)

**Gdzie sie to stosuje:**

- WiFi (802.11)
- LTE (4G)
- Satelitarna TV (DVB-S)
- GPS

---

## 5. 8-PSK - 8-Phase Shift Keying

### 5.1 Idea

8-PSK to **dalsza ekstensja** koncepcji PSK:

- Przesylamy **3 bity na symbol**
- Mamy **8 mozliwych symboli**

**Mapowanie:**

```
000 → 0°   → 1+0j
001 → 45°  → 0.707+0.707j
011 → 90°  → 0+1j
...
(8 punktow rowno rozmieszczonych na okregu)
```

### 5.2 Diagram konstelacji

```
        Q
        ^
    010 | 011
     •  |  •
   001• | •100
        |
────────┼────────> I
        |
   111• | •101
     •  |  •
    110 | 100
```

### 5.3 Trade-off: Wydajnosc vs Odpornosc

8-PSK daje **50% wieksza wydajnosc** niz QPSK:

```
QPSK:  2 bity/symbol
8-PSK: 3 bity/symbol  <- 1.5x wiecej
```

ALE punkty konstelacji sa **blizej siebie**:

```
Kat miedzy sasiednimi punktami:
BPSK:  180° (duzo miejsca!)
QPSK:  90°
8-PSK: 45°  (punkty blizej - latwo sie pomylic!)
```

**Co to oznacza?**

- 8-PSK wymaga **lepszego kanalu** (wyzsze Eb/N0) niz QPSK
- Przy tym samym szumie, 8-PSK ma **wyzsze BER** (wiecej bledow)

### 5.4 Zalety i wady

**Zalety:**

- ✓ 50% wyzsza wydajnosc niz QPSK
- ✓ Wciaz stosunkowo prosta implementacja

**Wady:**

- ✗ Gorsza odpornosc na szum niz QPSK
- ✗ Wymaga ok. 4 dB wyzszego SNR dla tego samego BER

**Gdzie sie to stosuje:**

- Satelitarna komunikacja (gdy pasmo jest ograniczone)
- Niektore tryby WiFi
- Systemy radiowe wojskowe

---

## 6. QAM - Quadrature Amplitude Modulation

### 6.1 Idea

QAM to **najbardziej zaawansowana modulacja** w naszej aplikacji:

- Zmienia **zarowno amplitude JAK I faze**
- Symbole tworza **siatke** na plaszczyznie IQ

Najpopularniejsze warianty:

- **16-QAM**: 4 bity/symbol, 16 symboli
- **64-QAM**: 6 bitow/symbol, 64 symbole
- **256-QAM**: 8 bitow/symbol, 256 symboli

### 6.2 Diagram konstelacji 16-QAM

```
        Q
        ^
    • • | • •    <- 16 punktow
    • • | • •       w siatce 4x4
────────┼────────> I
    • • | • •
    • • | • •
```

Punkty sa rozmieszczone w regularnej siatce o roznych amplitudach:

```
Poziomy I: {-3, -1, +1, +3}  (po normalizacji)
Poziomy Q: {-3, -1, +1, +3}

Przyklad symboli:
(-3-3j), (-3-1j), (-3+1j), (-3+3j),
(-1-3j), (-1-1j), (-1+1j), (-1+3j),
...
```

### 6.3 Dlaczego QAM jest tak wydajny?

QAM wykorzystuje **dwa wymiary** (I i Q) efektywnie:

```
BPSK:  Tylko os I                    -> 1 bit/symbol
QPSK:  I i Q, ale stala amplituda    -> 2 bity/symbol
8-PSK: I i Q, stala amplituda        -> 3 bity/symbol
16-QAM: I i Q, ROZNE amplitudy       -> 4 bity/symbol!
```

### 6.4 Demodulacja QAM

QAM demoduluje skladowe I i Q **niezaleznie**:

```
1. Odbierz symbol: 0.95 + 0.32j

2. Demoduluj I (0.95):
   0.95 > 0 i 0.95 < 2  ->  bity [1,1]

3. Demoduluj Q (0.32):
   0.32 > 0 i 0.32 < 2  ->  bity [1,1]

4. Wynik: [1,1,1,1]
```

### 6.5 Trade-off: Wysoka wydajnosc, wysokie wymagania

16-QAM przesyla **2x wiecej** danych niz QPSK, ale:

```
Wymagane SNR dla BER = 10^-5:
BPSK:   ~9.6 dB
QPSK:   ~9.6 dB
16-QAM: ~14.5 dB  <- Potrzeba 5 dB wiecej!
64-QAM: ~18.5 dB  <- Jeszcze wiecej!
```

**Wniosek:** QAM jest swietny dla **dobrych kanalow** (krotki dystans, brak przeszkod), ale zly dla **trudnych warunkow** (daleki dystans, przeszkody).

### 6.6 Zalety i wady

**Zalety:**

- ✓ Bardzo wysoka wydajnosc spektralna
- ✓ Skalowalne (mozna uzyc 64-QAM, 256-QAM, 1024-QAM)
- ✓ Optymalne wykorzystanie pasma

**Wady:**

- ✗ Wymaga wysokiego SNR
- ✗ Bardzo wrazliwe na szum i znieksztalcenia
- ✗ Skomplikowana implementacja
- ✗ Wymaga liniowych wzmacniaczy (kosztowne!)

**Gdzie sie to stosuje:**

- **WiFi** (802.11ac/ax: do 1024-QAM!)
- **LTE/5G** (adaptacyjnie: od QPSK do 256-QAM)
- **Telewizja kablowa** (DOCSIS)
- **DSL/modemy** (xDSL)

---

## 7. Porownanie modulacji - Wielki Trade-off

### 7.1 Tabela porownawcza

```
┌──────────┬──────────────┬─────────────────┬──────────────┬─────────────┐
│ Modulacja│ Bity/symbol  │ Punkty          │ Odpornosc    │ Zastosowanie│
│          │              │ konstelacji     │ na szum      │             │
├──────────┼──────────────┼─────────────────┼──────────────┼─────────────┤
│ BPSK     │      1       │       2         │  Najlepsza   │  Satelity   │
│          │              │                 │              │  RFID       │
├──────────┼──────────────┼─────────────────┼──────────────┼─────────────┤
│ QPSK     │      2       │       4         │  Bardzo dobra│  WiFi       │
│          │              │                 │              │  LTE        │
├──────────┼──────────────┼─────────────────┼──────────────┼─────────────┤
│ 8-PSK    │      3       │       8         │  Srednia     │  Satelity   │
│          │              │                 │              │              │
├──────────┼──────────────┼─────────────────┼──────────────┼─────────────┤
│ 16-QAM   │      4       │      16         │  Niska       │  WiFi       │
│          │              │                 │              │  LTE (dobry │
│          │              │                 │              │   sygnal)   │
├──────────┼──────────────┼─────────────────┼──────────────┼─────────────┤
│ 64-QAM   │      6       │      64         │  Bardzo niska│  WiFi-AC    │
│          │              │                 │              │  5G         │
├──────────┼──────────────┼─────────────────┼──────────────┼─────────────┤
│ 256-QAM  │      8       │     256         │  Minimalna   │  WiFi-6     │
│          │              │                 │              │  Kablowka   │
└──────────┴──────────────┴─────────────────┴──────────────┴─────────────┘
```

### 7.2 Fundamentalny trade-off

To jest **najwazniejsza zasada** w telekomunikacji:

```
            Wysoka wydajnosc
                   ^
                   |
      256-QAM •   |
       64-QAM •   |
       16-QAM •   |
        8-PSK •   |
         QPSK •   |
         BPSK •   |
              |
              +─────────────────> Wysoka odpornosc na szum

NIE MOZNA MIEC OBUUU!
```

**Analogia:** To jak samochod:

- Chcesz duzy (duzo miejsca) → zuzywa duzo paliwa
- Chcesz ekonomiczny → mniejszy, mniej miejsca

Nie mozesz miec duzego SUV-a, ktory zuzywa 3L/100km!

### 7.3 Adaptacyjna modulacja (AMC)

Nowoczesne systemy (LTE, WiFi) **zmieniaja modulacje dynamicznie**:

```
Scenariusz 1: Telefon blisko stacji bazowej
├─> Mocny sygnal (wysoki SNR)
├─> System wybiera: 256-QAM
└─> Wynik: Bardzo szybki internet!

Scenariusz 2: Telefon daleko od stacji
├─> Slaby sygnal (niski SNR)
├─> System wybiera: QPSK lub nawet BPSK
└─> Wynik: Wolniejszy internet, ale stabilny!
```

To nazywa sie **Adaptive Modulation and Coding (AMC)**.

### 7.4 Kiedy uzywac ktorej modulacji?

**BPSK:**

- Gdy moc jest ograniczona (satelity, baterie)
- Gdy dystans jest bardzo duzy
- Gdy priorytet = niezawodnosc, nie predkosc

**QPSK:**

- "Zloty srodek" dla wiekszosci zastosowan
- Dobry balans wydajnosci i odpornosci
- Standardowy wybor dla WiFi i LTE

**8-PSK:**

- Gdy potrzebujesz wiecej niz QPSK, ale nie masz dość SNR dla QAM
- Satelitarne linki z ograniczonym pasmem

**16/64/256-QAM:**

- Tylko dla **bardzo dobrych kanalow**
- Krotkie dystanse (WiFi w tym samym pokoju)
- Polaczenia kablowe
- Gdy potrzebujesz maksymalnej predkosci

---

## 8. Kanal transmisyjny i szum

### 8.1 Model kanalu AWGN

W rzeczywistosci sygnal nigdy nie dociera idealnie. Po drodze zbiera **szum**.

**AWGN** = Additive White Gaussian Noise (Addytywny Bialy Szum Gaussowski)

```
Nadajnik          Kanal           Odbiornik
   |               |                  |
   |--[Symbol]--->|---[Szum]---->|   |
   |    (s)        |   (+n)       |   |
   |               |              |   |
   |               v              v   |
   |          y = s + n               |
```

### 8.2 Co to jest AWGN?

**Additive** - szum sie DODAJE do sygnalu:

```
y(t) = s(t) + n(t)

Odebrany = Wyslany + Szum
```

**White** - szum ma rowna moc we wszystkich czestotliwosciach:

```
    Moc
     ^
     |||||||||||||||||||||  <- Bialy szum (wszystkie czest. rowne)
     +--------------------> Czestotliwosc
```

**Gaussian** - wartosci szumu maja rozklad normalny (Gaussa):

```
Prawdopodobienstwo
       ^
       |     ╱‾╲        <- Krzywa dzwonowa
       |    ╱   ╲
       |   ╱     ╲
       |  ╱       ╲
       +──────────────> Wartosc szumu
            0
```

### 8.3 Skad sie bierze szum?

1. **Szum termiczny** - ruchy atomow w przewodnikach (zawsze obecny!)
2. **Interferencje** - inne urzadzenia nadajace na podobnych czestotliwosciach
3. **Tlo elektromagnetyczne** - burze, gwiazdy, cosmic radiation
4. **Szum elektroniki** - wzmacniacze, oscylatory

**Nie mozemy wyeliminowac szumu - mozemy tylko go zmniejszyc lub byc na niego odporni!**

### 8.4 Wplyw szumu na konstelacje

Bez szumu:

```
    Q
    |
  o | o    <- Idealne punkty
────┼────> I
  o | o
```

Z szumem (niski SNR):

```
    Q
    |
 .°o°| °o°.   <- Punkty "rozmazane"
 °  .| . °    szumem
────┼────> I
 °. o|o °.
  . °|° .
```

Jezeli szum jest zbyt duzy, punkty sie **nakladaja** i odbiornik nie moze ich rozroznic!

---

## 9. BER i Eb/N0 - Miary jakosci

### 9.1 BER (Bit Error Rate)

**BER** = Stosunek blednych bitow do wszystkich bitow

```
BER = Liczba_bledow / Calkowita_liczba_bitow

Przyklad:
Wyslano:  1 0 1 1 0 0 1 0 (8 bitow)
Odebrano: 1 0 0 1 0 0 1 0
          ✓ ✓ ✗ ✓ ✓ ✓ ✓ ✓

BER = 1 / 8 = 0.125 = 12.5%
```

**Typowe wymagania BER:**

```
10^-3  (0.001)  = Minimalne dla glosu (1 blad na 1000 bitow)
10^-6  (0.000001) = Dobre dla danych
10^-9            = Bardzo dobre (Ethernet)
10^-12           = Swietne (swiatlo wodowe)
```

### 9.2 Eb/N0 - Energia na bit do szumu

**Eb/N0** to **najwazniejsza miara jakosci kanalu** w komunikacji cyfrowej.

```
Eb = Energia przypadajaca na jeden bit
N0 = Gestosc widmowa mocy szumu

Eb/N0 = Energia_bitu / Moc_szumu_na_Hz
```

**Dlaczego nie SNR?**

SNR (Signal-to-Noise Ratio) zalezy od szybkosci transmisji. Eb/N0 **nie zalezy**!

```
Przyklad:
System A: BPSK, 1 Mbit/s, SNR = 10 dB -> Eb/N0 = 10 dB
System B: QPSK, 2 Mbit/s, SNR = 13 dB -> Eb/N0 = 10 dB

Te same Eb/N0 = mozna porownac!
```

**Eb/N0 w dB:**

Eb/N0 jest zwykle wyrazane w decybelach (dB):

```
Eb/N0 (dB) = 10 * log10(Eb/N0)

Przyklad:
Eb/N0 = 100 (linear)
Eb/N0 (dB) = 10 * log10(100) = 10 * 2 = 20 dB
```

### 9.3 Krzywe BER vs Eb/N0

To jest **kluczowy wykres** w telekomunikacji:

```
BER
 ^
 |
10^0 |•
     |  •
10^-2|    •  BPSK
     |      ••
10^-4|        ••  QPSK
     |          •••
10^-6|             ••• 16-QAM
     |                •••
10^-8|___________________•••___> Eb/N0 (dB)
     0   5   10   15   20
```

**Co ten wykres mowi:**

1. Im wyzsze Eb/N0 (lepszy kanal) → nizsze BER (mniej bledow)
2. BPSK jest najlepszy (najnizsze BER dla danego Eb/N0)
3. 16-QAM potrzebuje ~5 dB wiecej niz QPSK dla tego samego BER

### 9.4 Teoretyczny BER dla BPSK

Dla BPSK istnieje wzor teoretyczny:

```
BER_BPSK = (1/2) * erfc(sqrt(Eb/N0))

gdzie erfc() = komplementarna funkcja bledu
```

**Przyklady:**

```
Eb/N0 = 0 dB:   BER ≈ 0.0786 (8% bledow!)
Eb/N0 = 5 dB:   BER ≈ 0.0035 (0.35%)
Eb/N0 = 10 dB:  BER ≈ 4×10^-6 (0.0004%)
Eb/N0 = 15 dB:  BER ≈ 3×10^-11 (prawie zero!)
```

### 9.5 Co nasza aplikacja symuluje?

Nasza aplikacja:

1. **Generuje losowe bity** (dane do wyslania)
2. **Moduluje** je (BPSK/QPSK/8-PSK/QAM)
3. **Dodaje szum AWGN** (symuluje kanal)
4. **Demoduluje** (odtwarza bity)
5. **Oblicza BER** (porownuje wyslane vs odebrane)
6. **Powtarza dla roznych Eb/N0** (tworzy krzywa BER)

**Wynik:** Wykresy pokazujace jak dobra jest kazda modulacja!

---

## 10. Praktyczne zastosowania

### 10.1 WiFi (802.11)

WiFi uzywa **wielu modulacji** w zaleznosci od warunkow:

```
802.11b (1999):
├─> BPSK: 1 Mbit/s
├─> QPSK: 2 Mbit/s
└─> Max: 11 Mbit/s

802.11g (2003):
├─> QPSK, 16-QAM, 64-QAM
└─> Max: 54 Mbit/s

802.11n (2009):
├─> Do 64-QAM + MIMO
└─> Max: 600 Mbit/s

802.11ac (2013):
├─> Do 256-QAM + MIMO
└─> Max: 6.93 Gbit/s

802.11ax/WiFi-6 (2019):
├─> Do 1024-QAM!
└─> Max: 9.6 Gbit/s
```

**Kluczowa cecha:** WiFi **adaptacyjnie zmienia** modulacje:

- Blisko routera → uzywa 256-QAM (szybko!)
- Daleko lub przeszkody → spada do QPSK (wolniej, ale stabilnie)

### 10.2 LTE/4G

LTE to **bardzo elastyczny system**:

```
Warunki:          Modulacja:    Szybkosc:
───────────────────────────────────────────
Idealny sygnal    256-QAM       ~300 Mbit/s
Dobry sygnal      64-QAM        ~150 Mbit/s
Sredni sygnal     16-QAM        ~75 Mbit/s
Slaby sygnal      QPSK          ~30 Mbit/s
Bardzo slaby      BPSK          ~15 Mbit/s
```

**Przykład w praktyce:**

- Stoisz obok masztu 4G → telefon pokazuje pełne kreski → szybki internet (64/256-QAM)
- Jedziesz pociągiem → telefon traci sygnał → wolniejszy internet (QPSK/BPSK)

### 10.3 5G/NR

5G idzie jeszcze dalej:

- **Do 1024-QAM** w idealnych warunkach
- **Masywny MIMO** (wiele anten)
- **mmWave** (fale milimetrowe - bardzo wysokie czestotliwosci)

```
5G Scenarios:
┌────────────────┬────────────────┬──────────────┐
│  Scenariusz    │  Modulacja     │  Predkosc    │
├────────────────┼────────────────┼──────────────┤
│  Indoor        │  1024-QAM      │  ~10 Gbit/s  │
│  (short range) │                │              │
├────────────────┼────────────────┼──────────────┤
│  Urban macro   │  256-QAM       │  ~1 Gbit/s   │
├────────────────┼────────────────┼──────────────┤
│  Rural         │  64-QAM        │  ~100 Mbit/s │
└────────────────┴────────────────┴──────────────┘
```

### 10.4 Satelity

Komunikacja satelitarna to **ekstremalne warunki**:

- Dystans: ~36,000 km (geostacjonarne)
- Opoznienie: ~240 ms (w jedna strone!)
- Bardzo slaby sygnal

**Dlaczego BPSK/QPSK dominuja:**

```
Satelita
   △
   |  36000 km!
   |  Sygnal BARDZO slaby
   |
   v
  ───  Antena naziemna

Problem: Tak duzy dystans = ogromny szum
Rozwiazanie: BPSK lub QPSK (odporne na szum)
```

Przyklady:

- **GPS**: BPSK (niezawodnosc > predkosc)
- **Satelitarna TV**: QPSK, 8-PSK (balans)
- **Satelitarny internet (Starlink)**: QPSK do 16-QAM (nowoczesne, nizsza orbita)

### 10.5 Modulacja w codziennym zyciu

Kiedy uzywasz modulacji (prawdopodobnie nawet o tym nie wiedzac):

```
Rano:
07:00 - Budzisz sie → smartwatch (Bluetooth: QPSK/8-PSK)
07:30 - Scrollujesz Instagram → WiFi (64-QAM)
08:00 - Jedzie do pracy → GPS (BPSK)

W pracy:
09:00 - Video call → LTE (16-QAM)
12:00 - Zamawiasz jedzenie → 5G (256-QAM)
15:00 - Streaming muzyka → WiFi-6 (1024-QAM)

Wieczorem:
19:00 - Netflix 4K → Kabel (256-QAM)
21:00 - Grasz online → WiFi (64-QAM)
23:00 - Smart home → Zigbee (QPSK)
```

**Wszystko wokol Ciebie dziala dzieki modulacji cyfrowej!**

---

## 11. Podsumowanie

### 11.1 Kluczowe wnioski

1. **Modulacja = pakowanie bitow do fal radiowych**

   - Nie mozemy "wyslac bitow" - musimy je modulowac

2. **Trade-off: Wydajnosc ↔ Odpornosc**

   - BPSK: Wolny ale niezawodny
   - QAM: Szybki ale wymaga dobrego kanalu

3. **Szum jest nieunikniony**

   - AWGN to model matematyczny szumu
   - BER mierzy jak dobrze sobie radzimy

4. **Eb/N0 to uniwersalna miara**

   - Pozwala porownywac rozne systemy
   - Im wyzsze, tym lepsza jakosc

5. **Nowoczesne systemy sa adaptacyjne**
   - WiFi, LTE, 5G zmieniaja modulacje dynamicznie
   - Maksymalizuja predkosc przy danym SNR

### 11.2 Co robi nasza aplikacja?

Nasza symulacja to **uproszczony model** prawdziwego systemu komunikacyjnego:

```
┌─────────────────────────────────────────────────┐
│  1. NADAJNIK                                    │
│     ├─> Generuj losowe bity                     │
│     └─> Moduluj (BPSK/QPSK/8-PSK/QAM)           │
├─────────────────────────────────────────────────┤
│  2. KANAL                                       │
│     └─> Dodaj szum AWGN (symuluj srodowisko)   │
├─────────────────────────────────────────────────┤
│  3. ODBIORNIK                                   │
│     ├─> Demoduluj symbole                      │
│     └─> Odtwarz bity                            │
├─────────────────────────────────────────────────┤
│  4. ANALIZA                                     │
│     ├─> Oblicz BER                              │
│     ├─> Wygeneruj krzywe BER vs Eb/N0           │
│     └─> Porownaj modulacje                      │
└─────────────────────────────────────────────────┘
```

**Cel:** Zrozumiec jak rozne modulacje radzs sobie w roznych warunkach!

### 11.3 Dlaczego to jest wazne?

Rozumienie modulacji cyfrowej to klucz do zrozumienia:

- Jak dziala internet bezprzewodowy
- Dlaczego czasami WiFi jest wolny
- Jak dziala telefon komorkowy
- Jak satelity komunikuja sie z Ziemia
- Jak 5G osiaga tak duze predkosci

**To podstawa nowoczesnej telekomunikacji!**

---

## 12. Dodatkowe zrodla

### Wikipedia (angielski):

- [Phase-shift keying](https://en.wikipedia.org/wiki/Phase-shift_keying)
- [Quadrature amplitude modulation](https://en.wikipedia.org/wiki/Quadrature_amplitude_modulation)
- [AWGN channel](https://en.wikipedia.org/wiki/Additive_white_Gaussian_noise)
- [Bit error rate](https://en.wikipedia.org/wiki/Bit_error_rate)

### Ksiazki (dla chetnych do glebszej wiedzy):

- "Digital Communications" - John Proakis
- "Communication Systems" - Simon Haykin
- "Wireless Communications" - Andrea Goldsmith

### Online resources:

- [MIT OpenCourseWare - Digital Communications](https://ocw.mit.edu/)
- [Khan Academy - Signals and Systems](https://www.khanacademy.org/)
- [3Blue1Brown - Fourier Transform](https://www.youtube.com/3blue1brown) (wizualizacje!)

---

## Glosariusz

**Amplituda** - Wysokosc fali; jak "mocny" jest sygnal

**Faza** - Przesuniecie fali w czasie; gdzie fala zaczyna

**Czestotliwosc** - Ile razy na sekunde fala sie powtarza (Hz)

**Konstelacja** - Diagram pokazujacy mozliwe symbole modulacji na plaszczyznie IQ

**Eb/N0** - Energia na bit do gestosci mocy szumu; miara jakosci kanalu

**BER** - Bit Error Rate; stosunek blednych bitow do wszystkich

**SNR** - Signal-to-Noise Ratio; stosunek mocy sygnalu do szumu

**AWGN** - Additive White Gaussian Noise; model matematyczny szumu

**Gray coding** - Kodowanie gdzie sasiednie symbole roznia sie 1 bitem

**Modulacja** - Proces zmiany parametrow fali nosnej aby przeniesc informacje

**Demodulacja** - Proces odtwarzania informacji z zmodulowanej fali

**Symbol** - Jednostka informacji w modulacji (moze reprezentowac 1 lub wiecej bitow)

**Adaptive Modulation** - Dynamiczna zmiana modulacji w zaleznosci od warunkow

---

**Koniec dokumentu teoretycznego**

Ten dokument wyjas nil podstawy teoretyczne systemow modulacji cyfrowej. Dla szczegolow implementacji w kodzie, zobacz `code-documentation.md`.

**Sukcesu w nauce!** 📡📶🚀
