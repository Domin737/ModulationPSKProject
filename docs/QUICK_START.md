# QUICK START GUIDE

## 🚀 Get Running in 5 Minutes

### 1. Install (1 minute)

**Windows:**
```bash
setup.bat
```

**Linux/Mac:**
```bash
chmod +x setup.sh
./setup.sh
```

### 2. Activate (10 seconds)

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 3. Run (3 minutes)

```bash
cd src
python main.py
```

### 4. Check Results

```bash
ls ../results/
# You should see 5 PNG files
```

---

## ✅ That's It!

Your simulation is complete. Check `results/` folder for plots.

---

## 📖 For More Information:

- **README.md** - Full documentation
- **DEPLOYMENT_GUIDE.md** - Detailed setup
- **COMPLETE_PROJECT_SUMMARY.md** - What you have

---

## 🧪 Test Individual Modules:

```bash
cd src
python GetBytes.py      # Test bit generator
python Modulator.py     # Test all modulators
python Demodulator.py   # Test all demodulators
```

---

## 💡 Quick Example:

```python
from GetBytes import gen_bites
from Modulator import bpsk_modulation
from TransmissionChannel import transmission_channel
from Demodulator import bpsk_demodulation
import numpy as np

# Simple BPSK test
bits = gen_bites(1000)
symbols = bpsk_modulation(bits)
received = transmission_channel(symbols, 10)
decoded = bpsk_demodulation(received)
ber = np.sum(bits != decoded) / len(bits)
print(f"BER = {ber}")
```

---

**Need Help?** → Read README.md

**Version:** 1.0.0  
**Status:** ✅ Complete
