"""
Module for digital modulation.
Implements: BPSK, QPSK, 8-PSK, 16-QAM
"""

import numpy as np
from GetBytes import gen_bites


def bpsk_modulation(bits):
    """
    BPSK (Binary Phase-Shift Keying) modulation.
    
    Maps binary bits to complex symbols:
    - bit 0 -> +1+0j (phase 0 degrees)
    - bit 1 -> -1+0j (phase 180 degrees)
    
    Parameters
    ----------
    bits : numpy.ndarray
        Array of binary bits (0s and 1s)
    
    Returns
    -------
    numpy.ndarray (complex128)
        BPSK modulated complex symbols
    
    Examples
    --------
    >>> bits = np.array([0, 1, 0, 1])
    >>> symbols = bpsk_modulation(bits)
    >>> print(symbols)
    [ 1.+0.j -1.+0.j  1.+0.j -1.+0.j]
    """
    symbols = 1 - 2 * bits
    return symbols.astype(complex)


def qpsk_modulation(bits):
    """
    QPSK (Quadrature Phase-Shift Keying) modulation.
    
    Maps 2 bits to one complex symbol (4 possible symbols).
    Constellation points are at 45, 135, 225, 315 degrees.
    
    Mapping (Gray coding):
    - 00 -> (+1+j)/sqrt(2)  (45 degrees)
    - 01 -> (-1+j)/sqrt(2)  (135 degrees)
    - 11 -> (-1-j)/sqrt(2)  (225 degrees)
    - 10 -> (+1-j)/sqrt(2)  (315 degrees)
    
    Parameters
    ----------
    bits : numpy.ndarray
        Array of binary bits (length must be even)
    
    Returns
    -------
    numpy.ndarray (complex128)
        QPSK modulated complex symbols
    
    Examples
    --------
    >>> bits = np.array([0, 0, 0, 1, 1, 1, 1, 0])
    >>> symbols = qpsk_modulation(bits)
    >>> # Returns 4 symbols (2 bits per symbol)
    
    Notes
    -----
    - 2 bits per symbol (twice as efficient as BPSK)
    - Similar BER performance to BPSK at same Eb/N0
    - Normalized to unit energy: symbols have magnitude 1
    """
    # Check if number of bits is even
    if len(bits) % 2 != 0:
        raise ValueError("Number of bits must be even for QPSK")
    
    # Reshape bits into pairs
    bit_pairs = bits.reshape(-1, 2)
    
    # Normalization factor for unit energy
    norm = 1 / np.sqrt(2)
    
    # Mapping dictionary
    qpsk_map = {
        (0, 0): norm * (1 + 1j),   # 00 -> 45 degrees
        (0, 1): norm * (-1 + 1j),  # 01 -> 135 degrees
        (1, 1): norm * (-1 - 1j),  # 11 -> 225 degrees
        (1, 0): norm * (1 - 1j)    # 10 -> 315 degrees
    }
    
    # Map each bit pair to symbol
    symbols = np.array([qpsk_map[tuple(pair)] for pair in bit_pairs], dtype=complex)
    
    return symbols


def psk8_modulation(bits):
    """
    8-PSK (8-Phase Shift Keying) modulation.
    
    Maps 3 bits to one complex symbol (8 possible symbols).
    Constellation points are equally spaced on unit circle.
    
    Mapping (Gray coding):
    Points at: 0, 45, 90, 135, 180, 225, 270, 315 degrees
    
    Parameters
    ----------
    bits : numpy.ndarray
        Array of binary bits (length must be multiple of 3)
    
    Returns
    -------
    numpy.ndarray (complex128)
        8-PSK modulated complex symbols
    
    Examples
    --------
    >>> bits = np.array([0, 0, 0, 0, 0, 1, 0, 1, 0])
    >>> symbols = psk8_modulation(bits)
    >>> # Returns 3 symbols (3 bits per symbol)
    
    Notes
    -----
    - 3 bits per symbol (50% more efficient than QPSK)
    - Worse BER performance than QPSK (symbols closer together)
    - Normalized to unit energy
    """
    # Check if number of bits is multiple of 3
    if len(bits) % 3 != 0:
        raise ValueError("Number of bits must be multiple of 3 for 8-PSK")
    
    # Reshape bits into triplets
    bit_triplets = bits.reshape(-1, 3)
    
    # 8-PSK constellation (Gray coding)
    # Angles: 0, 45, 90, 135, 180, 225, 270, 315 degrees
    angles = np.array([0, 1, 3, 2, 6, 7, 5, 4]) * np.pi / 4
    
    # Create constellation points
    constellation = np.exp(1j * angles)
    
    # Map each triplet to symbol index (binary to decimal)
    symbol_indices = bit_triplets[:, 0] * 4 + bit_triplets[:, 1] * 2 + bit_triplets[:, 2]
    
    # Get corresponding symbols
    symbols = constellation[symbol_indices]
    
    return symbols


def qam16_modulation(bits):
    """
    16-QAM (16-Quadrature Amplitude Modulation) modulation.
    
    Maps 4 bits to one complex symbol (16 possible symbols).
    Constellation is a 4x4 grid of points.
    
    Mapping:
    4 bits -> (I, Q) coordinates
    First 2 bits -> I (in-phase) component
    Last 2 bits -> Q (quadrature) component
    
    Constellation points at: {-3, -1, +1, +3} x {-3j, -1j, +1j, +3j}
    Normalized to unit average energy.
    
    Parameters
    ----------
    bits : numpy.ndarray
        Array of binary bits (length must be multiple of 4)
    
    Returns
    -------
    numpy.ndarray (complex128)
        16-QAM modulated complex symbols
    
    Examples
    --------
    >>> bits = np.array([0, 0, 0, 0, 1, 1, 1, 1])
    >>> symbols = qam16_modulation(bits)
    >>> # Returns 2 symbols (4 bits per symbol)
    
    Notes
    -----
    - 4 bits per symbol (twice as efficient as QPSK)
    - Requires higher SNR than PSK (non-constant envelope)
    - Normalized to unit average energy: E[|s|^2] = 1
    """
    # Check if number of bits is multiple of 4
    if len(bits) % 4 != 0:
        raise ValueError("Number of bits must be multiple of 4 for 16-QAM")
    
    # Reshape bits into groups of 4
    bit_groups = bits.reshape(-1, 4)
    
    # Split into I and Q bits
    i_bits = bit_groups[:, 0:2]  # First 2 bits for I
    q_bits = bit_groups[:, 2:4]  # Last 2 bits for Q
    
    # Mapping for 2 bits to PAM-4 levels: {-3, -1, +1, +3}
    pam4_map = {
        (0, 0): -3,
        (0, 1): -1,
        (1, 1): +1,
        (1, 0): +3
    }
    
    # Map I and Q components
    i_components = np.array([pam4_map[tuple(pair)] for pair in i_bits])
    q_components = np.array([pam4_map[tuple(pair)] for pair in q_bits])
    
    # Create complex symbols
    symbols = i_components + 1j * q_components
    
    # Normalize to unit average energy
    # Average energy of unnormalized 16-QAM: E[|s|^2] = 10
    # Normalization factor: 1/sqrt(10)
    norm = 1 / np.sqrt(10)
    symbols = symbols * norm
    
    return symbols


if __name__ == "__main__":
    print("=" * 60)
    print("Testing All Modulation Schemes")
    print("=" * 60)
    
    # Test 1: BPSK
    print("\n1. BPSK Modulation")
    print("-" * 60)
    bpsk_bits = np.array([0, 1, 0, 1])
    bpsk_symbols = bpsk_modulation(bpsk_bits)
    print(f"Bits (4):    {bpsk_bits}")
    print(f"Symbols (4): {bpsk_symbols}")
    print(f"Energy: {np.mean(np.abs(bpsk_symbols)**2):.6f} (should be ~1.0)")
    
    # Test 2: QPSK
    print("\n2. QPSK Modulation")
    print("-" * 60)
    qpsk_bits = np.array([0, 0, 0, 1, 1, 1, 1, 0])
    qpsk_symbols = qpsk_modulation(qpsk_bits)
    print(f"Bits (8):    {qpsk_bits}")
    print(f"Symbols (4): {qpsk_symbols}")
    print(f"Energy: {np.mean(np.abs(qpsk_symbols)**2):.6f} (should be ~1.0)")
    
    # Test 3: 8-PSK
    print("\n3. 8-PSK Modulation")
    print("-" * 60)
    psk8_bits = np.array([0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1])
    psk8_symbols = psk8_modulation(psk8_bits)
    print(f"Bits (12):   {psk8_bits}")
    print(f"Symbols (4): {psk8_symbols}")
    print(f"Energy: {np.mean(np.abs(psk8_symbols)**2):.6f} (should be ~1.0)")
    
    # Test 4: 16-QAM
    print("\n4. 16-QAM Modulation")
    print("-" * 60)
    qam_bits = np.array([0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0])
    qam_symbols = qam16_modulation(qam_bits)
    print(f"Bits (16):   {qam_bits}")
    print(f"Symbols (4): {qam_symbols}")
    print(f"Energy: {np.mean(np.abs(qam_symbols)**2):.6f} (should be ~1.0)")
    
    # Summary
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"BPSK:   1 bit/symbol  - 4 bits -> 4 symbols")
    print(f"QPSK:   2 bits/symbol - 8 bits -> 4 symbols")
    print(f"8-PSK:  3 bits/symbol - 12 bits -> 4 symbols")
    print(f"16-QAM: 4 bits/symbol - 16 bits -> 4 symbols")