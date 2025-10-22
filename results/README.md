# Results Directory

This directory contains generated plots and simulation results.

## Generated Files

After running `python src/main.py`, the following files will be created here:

### BER Analysis
- **ber_comparison.png** - BER vs Eb/N0 comparison for all modulation schemes

### Constellation Diagrams
- **bpsk_constellation.png** - BPSK constellation (clean and with noise)
- **qpsk_constellation.png** - QPSK constellation (clean and with noise)
- **8psk_constellation.png** - 8-PSK constellation (clean and with noise)
- **16qam_constellation.png** - 16-QAM constellation (clean and with noise)

## Usage

To generate results:

```bash
# Make sure you're in the project root
cd ModulationPSKProject

# Activate virtual environment
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Run simulation
cd src
python main.py
```

Results will be automatically saved to this directory.

## Notes

- All plots are saved as high-resolution PNG files (300 DPI)
- Plots are also displayed during simulation (if GUI available)
- Old plots are overwritten when you run the simulation again
- You can safely delete these files - they will be regenerated

## Git

These files are ignored by Git (see .gitignore) to keep the repository clean.
Only this README.md is tracked.
