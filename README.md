# Digital Modulation Simulation (BPSK, QPSK, 8-PSK, 16-QAM)

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-Educational-green.svg)]()
[![Status](https://img.shields.io/badge/status-complete-success.svg)]()

Complete simulation of digital communication systems with various modulation schemes and AWGN channel.

## Features

✅ **Complete implementation** of 4 modulation schemes:

- **BPSK** (Binary Phase-Shift Keying)
- **QPSK** (Quadrature Phase-Shift Keying)
- **8-PSK** (8-ary Phase-Shift Keying)
- **16-QAM** (16-Quadrature Amplitude Modulation)

✅ **AWGN Channel** simulation with configurable Eb/N0

✅ **BER Analysis** - Bit Error Rate calculations and comparison

✅ **Visualization** - BER curves and constellation diagrams

## Quick Start

### 1. Setup

**Windows:**

```bash
setup.bat
```

**Linux/Mac:**

```bash
chmod +x setup.sh
./setup.sh
```

### 2. Activate Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/Mac:**

```bash
source venv/bin/activate
```

### 3. Run Simulation

```bash
cd src
python main.py
```

## Project Structure

```
ModulationPSKProject/
│
├── src/                      # Source code
│   ├── GetBytes.py          # Random bit generator
│   ├── Modulator.py         # All modulators (BPSK, QPSK, 8-PSK, 16-QAM)
│   ├── AddAWGNNoise.py      # AWGN noise generator
│   ├── TransmissionChannel.py # Transmission channel
│   ├── Demodulator.py       # All demodulators
│   └── main.py              # Main simulation program
│
├── results/                  # Generated plots and results
│   ├── ber_comparison.png   # BER comparison plot
│   └── *_constellation.png  # Constellation diagrams
│
├── requirements.txt          # Python dependencies
├── setup.bat                 # Windows setup script
├── setup.sh                  # Unix setup script
├── .gitignore                # Git ignore rules
└── README.md                 # This file
```

## Requirements

- Python 3.8 or higher
- NumPy >= 1.24.0
- SciPy >= 1.10.0
- Matplotlib >= 3.7.0

## Usage Examples

### Example 1: Basic Simulation

```python
from GetBytes import gen_bites
from Modulator import bpsk_modulation
from TransmissionChannel import transmission_channel
from Demodulator import bpsk_demodulation
import numpy as np

# Generate random bits
bits = gen_bites(1000)

# BPSK modulation
symbols = bpsk_modulation(bits)

# Transmit through channel (Eb/N0 = 10 dB)
received = transmission_channel(symbols, eb_n0_db=10)

# Demodulate
decoded_bits = bpsk_demodulation(received)

# Calculate BER
ber = np.sum(bits != decoded_bits) / len(bits)
print(f"BER = {ber:.6f}")
```

### Example 2: Test Individual Modules

```bash
cd src

# Test bit generator
python GetBytes.py

# Test all modulators
python Modulator.py

# Test AWGN noise
python AddAWGNNoise.py

# Test all demodulators
python Demodulator.py
```

### Example 3: Custom Simulation

```python
from Modulator import qpsk_modulation
from Demodulator import qpsk_demodulation

# Your custom simulation code here
```

## Modulation Schemes

| Scheme | Bits/Symbol | Symbols | Spectral Efficiency |
| ------ | ----------- | ------- | ------------------- |
| BPSK   | 1           | 2       | 1 bit/Hz            |
| QPSK   | 2           | 4       | 2 bits/Hz           |
| 8-PSK  | 3           | 8       | 3 bits/Hz           |
| 16-QAM | 4           | 16      | 4 bits/Hz           |

## Output Files

After running `main.py`, the following files are generated in `results/`:

- `ber_comparison.png` - BER vs Eb/N0 for all modulations
- `bpsk_constellation.png` - BPSK constellation diagram
- `qpsk_constellation.png` - QPSK constellation diagram
- `8psk_constellation.png` - 8-PSK constellation diagram
- `16qam_constellation.png` - 16-QAM constellation diagram

## Simulation Parameters

Default parameters in `main.py`:

- **Eb/N0 range:** -2 dB to 12 dB
- **Number of bits:** 10,000 per simulation point
- **Step size:** 1 dB

You can modify these in the `main()` function.

## Understanding the Results

### BER (Bit Error Rate)

- Lower BER = better performance
- BER < 10⁻⁵ is considered excellent
- BER ≈ 0.5 means random guessing (very bad)

### Eb/N0 (Energy per Bit to Noise Ratio)

- Measured in dB
- Higher Eb/N0 = less noise = better performance
- Typical range: -2 dB to 15 dB

### Expected Performance

- **BPSK:** Best noise immunity
- **QPSK:** Similar to BPSK, but 2× throughput
- **8-PSK:** 3× throughput, worse BER
- **16-QAM:** 4× throughput, worst BER

## Troubleshooting

### Error: ModuleNotFoundError

```bash
# Make sure you're in the src directory
cd src
python main.py
```

### Error: No module named 'numpy'

```bash
# Install dependencies
pip install -r requirements.txt
```

### Plots not showing

- Plots are automatically saved to `results/` folder
- Check the `results/` directory for PNG files

## Theory

### BPSK Modulation

Maps bits directly to antipodal signals:

- Bit 0 → +1
- Bit 1 → -1

### QPSK Modulation

Maps 2 bits to 4 phase points on unit circle:

- 00 → 45°
- 01 → 135°
- 10 → 315° (or -45°)
- 11 → 225° (or -135°)

### AWGN Channel

Adds Gaussian noise with:

- Mean = 0
- Variance based on Eb/N0

## References

1. [Phase-shift keying - Wikipedia](https://en.wikipedia.org/wiki/Phase-shift_keying)
2. [QAM - Wikipedia](https://en.wikipedia.org/wiki/Quadrature_amplitude_modulation)
3. Proakis, J. G., "Digital Communications", 5th Edition
4. Haykin, S., "Communication Systems", 4th Edition

## License

Educational project - free to use for learning purposes.

## Author

ModulationPSKProject

## Version

1.1.0 - Complete implementation

---

**Last Updated:** 2025-10-22  
**Status:** ✅ Complete and fully functional
