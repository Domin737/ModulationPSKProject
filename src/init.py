"""
ModulationPSKProject - Digital Modulation Simulation Package

This package provides tools for simulating digital communication systems
with various modulation schemes (BPSK, QPSK, 8-PSK, QAM) and analyzing
their performance in noisy channels.

Modules
-------
GetBytes : Random bit generation
Modulator : Digital modulation (BPSK, QPSK, 8-PSK, QAM)
TransmissionChannel : Channel simulation with AWGN
AddAWGNNoise : Noise generation
Demodulator : Digital demodulation
main : Main simulation program

Examples
--------
>>> from src.GetBytes import gen_bites
>>> from src.Modulator import bpsk_modulation
>>> bits = gen_bites(10)
>>> symbols = bpsk_modulation(bits)
"""

__version__ = '0.6.0'
__author__ = 'ModulationPSKProject Team'

# You can import key functions here for easier access
# from .GetBytes import gen_bites
# from .Modulator import bpsk_modulation
# from .AddAWGNNoise import add_awgn_noise
# from .Demodulator import bpsk_demodulation
# from .TransmissionChannel import transmission_channel