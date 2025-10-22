"""
Modulator.py - Digital modulation schemes

This module implements various digital modulation schemes:
- BPSK (Binary Phase-Shift Keying)
- QPSK (Quadrature Phase-Shift Keying)
- 8-PSK (8-ary Phase-Shift Keying)
- 16-QAM (16-Quadrature Amplitude Modulation)
"""

import numpy as np
from GetBytes import gen_bites


def bpsk_modulation(bits):
    """
    BPSK (Binary Phase-Shift Keying) modulation
    
    Maps bits to complex symbols:
    - bit 0 -> +1+0j
    - bit 1 -> -1+0j
    
    Parameters:
    -----------
    bits : numpy.ndarray
        Array of binary bits (0s and 1s)
    
    Returns:
    --------
    numpy.ndarray (complex)
        BPSK modulated symbols
    """
    symbols = 1 - 2 * bits
    return symbols.astype(complex)


def qpsk_modulation(bits):
    """
    QPSK (Quadrature Phase-Shift Keying) modulation
    
    Maps 2 bits to complex symbols on unit circle:
    - 00 -> ( 1+1j)/sqrt(2)  = 45 degrees
    - 01 -> (-1+1j)/sqrt(2)  = 135 degrees
    - 10 -> ( 1-1j)/sqrt(2)  = -45 degrees
    - 11 -> (-1-1j)/sqrt(2)  = -135 degrees
    
    Parameters:
    -----------
    bits : numpy.ndarray
        Array of binary bits. Length must be even.
    
    Returns:
    --------
    numpy.ndarray (complex)
        QPSK modulated symbols
    """
    if len(bits) % 2 != 0:
        raise ValueError("Number of bits must be even for QPSK")
    
    bits_reshaped = bits.reshape(-1, 2)
    symbols = np.zeros(len(bits_reshaped), dtype=complex)
    
    for i, bit_pair in enumerate(bits_reshaped):
        if bit_pair[0] == 0 and bit_pair[1] == 0:
            symbols[i] = (1 + 1j) / np.sqrt(2)
        elif bit_pair[0] == 0 and bit_pair[1] == 1:
            symbols[i] = (-1 + 1j) / np.sqrt(2)
        elif bit_pair[0] == 1 and bit_pair[1] == 0:
            symbols[i] = (1 - 1j) / np.sqrt(2)
        else:
            symbols[i] = (-1 - 1j) / np.sqrt(2)
    
    return symbols


def psk8_modulation(bits):
    """
    8-PSK (8-ary Phase-Shift Keying) modulation
    
    Maps 3 bits to complex symbols on unit circle.
    8 points equally spaced at: 0, 45, 90, 135, 180, 225, 270, 315 degrees
    
    Parameters:
    -----------
    bits : numpy.ndarray
        Array of binary bits. Length must be multiple of 3.
    
    Returns:
    --------
    numpy.ndarray (complex)
        8-PSK modulated symbols
    """
    if len(bits) % 3 != 0:
        raise ValueError("Number of bits must be multiple of 3 for 8-PSK")
    
    bits_reshaped = bits.reshape(-1, 3)
    decimal_values = bits_reshaped[:, 0] * 4 + bits_reshaped[:, 1] * 2 + bits_reshaped[:, 2]
    angles = decimal_values * np.pi / 4
    symbols = np.exp(1j * angles)
    
    return symbols


def qam16_modulation(bits):
    """
    16-QAM (16-Quadrature Amplitude Modulation) modulation
    
    Maps 4 bits to complex symbols in a 4x4 grid.
    Levels: {-3, -1, +1, +3} normalized by sqrt(10)
    
    Parameters:
    -----------
    bits : numpy.ndarray
        Array of binary bits. Length must be multiple of 4.
    
    Returns:
    --------
    numpy.ndarray (complex)
        16-QAM modulated symbols (normalized)
    """
    if len(bits) % 4 != 0:
        raise ValueError("Number of bits must be multiple of 4 for 16-QAM")
    
    bits_reshaped = bits.reshape(-1, 4)
    i_bits = bits_reshaped[:, :2]
    q_bits = bits_reshaped[:, 2:]
    
    def map_to_level(bit_pair):
        val = bit_pair[:, 0] * 2 + bit_pair[:, 1]
        levels = np.array([3, 1, -1, -3])
        return levels[val]
    
    i_component = map_to_level(i_bits)
    q_component = map_to_level(q_bits)
    symbols = i_component + 1j * q_component
    symbols = symbols / np.sqrt(10)
    
    return symbols


if __name__ == "__main__":
    print("=" * 60)
    print("Testing All Modulation Schemes")
    print("=" * 60)
    print()
    
    # Test BPSK
    print("1. BPSK Modulation")
    print("-" * 60)
    test_bits = gen_bites(8)
    print(f"Bits:    {test_bits}")
    symbols = bpsk_modulation(test_bits)
    print(f"Symbols: {symbols}")
    print()
    
    # Test QPSK
    print("2. QPSK Modulation")
    print("-" * 60)
    test_bits = gen_bites(8)
    print(f"Bits:    {test_bits}")
    symbols = qpsk_modulation(test_bits)
    print(f"Symbols: {symbols}")
    print()
    
    # Test 8-PSK
    print("3. 8-PSK Modulation")
    print("-" * 60)
    test_bits = gen_bites(12)
    print(f"Bits:    {test_bits}")
    symbols = psk8_modulation(test_bits)
    print(f"Symbols: {symbols}")
    print()
    
    # Test 16-QAM
    print("4. 16-QAM Modulation")
    print("-" * 60)
    test_bits = gen_bites(12)
    print(f"Bits:    {test_bits}")
    symbols = qam16_modulation(test_bits)
    print(f"Symbols: {symbols}")
    print()
    
    print("=" * 60)
    print("All tests completed successfully!")
    print("=" * 60)