"""
Module for digital demodulation.
Implements: BPSK, QPSK, 8-PSK, 16-QAM demodulation
"""

import numpy as np


def bpsk_demodulation(received_symbols):
    """
    BPSK demodulation using threshold detection.
    
    Decision rule:
    - If Real(symbol) > 0  =>  bit = 0
    - If Real(symbol) <= 0 =>  bit = 1
    
    Parameters
    ----------
    received_symbols : numpy.ndarray (complex)
        Received symbols from channel
    
    Returns
    -------
    numpy.ndarray (int)
        Decoded binary bits
    """
    decoded_bits = (received_symbols.real < 0).astype(int)
    return decoded_bits


def qpsk_demodulation(received_symbols):
    """
    QPSK demodulation using minimum distance detection.
    
    Detects which constellation point is closest to received symbol.
    
    Constellation (Gray coding):
    - 00 -> (+1+j)/sqrt(2)  (45 degrees)
    - 01 -> (-1+j)/sqrt(2)  (135 degrees)
    - 11 -> (-1-j)/sqrt(2)  (225 degrees)
    - 10 -> (+1-j)/sqrt(2)  (315 degrees)
    
    Parameters
    ----------
    received_symbols : numpy.ndarray (complex)
        Received QPSK symbols
    
    Returns
    -------
    numpy.ndarray (int)
        Decoded binary bits (2x length of input)
    
    Notes
    -----
    Uses simplified detection:
    - First bit:  sign of Real part (Re < 0 => bit 1)
    - Second bit: sign of Imag part (Im < 0 => bit 1)
    Then applies Gray code correction.
    """
    n_symbols = len(received_symbols)
    bits = np.zeros(n_symbols * 2, dtype=int)
    
    # Extract I and Q components
    i_component = received_symbols.real
    q_component = received_symbols.imag
    
    # Decision regions (Gray coding)
    for idx, (i, q) in enumerate(zip(i_component, q_component)):
        if i >= 0 and q >= 0:      # Quadrant I
            bits[2*idx:2*idx+2] = [0, 0]
        elif i < 0 and q >= 0:     # Quadrant II
            bits[2*idx:2*idx+2] = [0, 1]
        elif i < 0 and q < 0:      # Quadrant III
            bits[2*idx:2*idx+2] = [1, 1]
        else:                       # Quadrant IV (i >= 0, q < 0)
            bits[2*idx:2*idx+2] = [1, 0]
    
    return bits


def psk8_demodulation(received_symbols):
    """
    8-PSK demodulation using minimum distance detection.
    
    Detects which of 8 constellation points is closest
    to received symbol based on phase angle.
    
    Parameters
    ----------
    received_symbols : numpy.ndarray (complex)
        Received 8-PSK symbols
    
    Returns
    -------
    numpy.ndarray (int)
        Decoded binary bits (3x length of input)
    
    Notes
    -----
    8 constellation points at angles: 0, 45, 90, 135, 180, 225, 270, 315 degrees
    Gray coding used for bit assignment.
    """
    # 8-PSK constellation with Gray coding
    angles = np.array([0, 1, 3, 2, 6, 7, 5, 4]) * np.pi / 4
    constellation = np.exp(1j * angles)
    
    n_symbols = len(received_symbols)
    bits = np.zeros(n_symbols * 3, dtype=int)
    
    # For each received symbol, find closest constellation point
    for idx, symbol in enumerate(received_symbols):
        # Calculate distances to all constellation points
        distances = np.abs(symbol - constellation)
        
        # Find index of closest point
        closest_idx = np.argmin(distances)
        
        # Convert index to 3 bits
        bit0 = (closest_idx >> 2) & 1
        bit1 = (closest_idx >> 1) & 1
        bit2 = closest_idx & 1
        
        bits[3*idx:3*idx+3] = [bit0, bit1, bit2]
    
    return bits


def qam16_demodulation(received_symbols):
    """
    16-QAM demodulation using threshold detection.
    
    Detects I and Q components separately using multi-level thresholds.
    
    Decision regions:
    I/Q levels: {-3, -1, +1, +3} (before normalization)
    Thresholds at: -2, 0, +2
    
    Parameters
    ----------
    received_symbols : numpy.ndarray (complex)
        Received 16-QAM symbols (normalized)
    
    Returns
    -------
    numpy.ndarray (int)
        Decoded binary bits (4x length of input)
    
    Notes
    -----
    First 2 bits from I component, last 2 bits from Q component.
    Uses Gray coding for bit assignment.
    """
    # Denormalize symbols (reverse the 1/sqrt(10) normalization)
    norm = np.sqrt(10)
    denorm_symbols = received_symbols * norm
    
    n_symbols = len(received_symbols)
    bits = np.zeros(n_symbols * 4, dtype=int)
    
    # PAM-4 demodulation mapping (Gray coded)
    def pam4_demod(value):
        if value < -2:
            return [0, 0]  # -3
        elif value < 0:
            return [0, 1]  # -1
        elif value < 2:
            return [1, 1]  # +1
        else:
            return [1, 0]  # +3
    
    # Demodulate each symbol
    for idx, symbol in enumerate(denorm_symbols):
        i_bits = pam4_demod(symbol.real)
        q_bits = pam4_demod(symbol.imag)
        bits[4*idx:4*idx+4] = i_bits + q_bits
    
    return bits


if __name__ == "__main__":
    # Test all demodulators
    from Modulator import bpsk_modulation, qpsk_modulation, psk8_modulation, qam16_modulation
    from GetBytes import gen_bites
    from TransmissionChannel import transmission_channel
    
    print("=" * 60)
    print("Testing All Demodulation Schemes")
    print("=" * 60)
    
    # Test parameters
    eb_n0_db = 10  # Good channel
    
    # Test 1: BPSK
    print("\n1. BPSK Demodulation")
    print("-" * 60)
    bpsk_bits = gen_bites(20)
    bpsk_symbols = bpsk_modulation(bpsk_bits)
    bpsk_received = transmission_channel(bpsk_symbols, eb_n0_db)
    bpsk_decoded = bpsk_demodulation(bpsk_received)
    bpsk_errors = np.sum(bpsk_bits != bpsk_decoded)
    print(f"Transmitted bits: {bpsk_bits}")
    print(f"Decoded bits:     {bpsk_decoded}")
    print(f"Errors: {bpsk_errors}/{len(bpsk_bits)} - BER: {bpsk_errors/len(bpsk_bits):.4f}")
    
    # Test 2: QPSK
    print("\n2. QPSK Demodulation")
    print("-" * 60)
    qpsk_bits = gen_bites(20)
    qpsk_symbols = qpsk_modulation(qpsk_bits)
    qpsk_received = transmission_channel(qpsk_symbols, eb_n0_db)
    qpsk_decoded = qpsk_demodulation(qpsk_received)
    qpsk_errors = np.sum(qpsk_bits != qpsk_decoded)
    print(f"Transmitted bits: {qpsk_bits}")
    print(f"Decoded bits:     {qpsk_decoded}")
    print(f"Errors: {qpsk_errors}/{len(qpsk_bits)} - BER: {qpsk_errors/len(qpsk_bits):.4f}")
    
    # Test 3: 8-PSK
    print("\n3. 8-PSK Demodulation")
    print("-" * 60)
    psk8_bits = gen_bites(21)  # Multiple of 3
    psk8_symbols = psk8_modulation(psk8_bits)
    psk8_received = transmission_channel(psk8_symbols, eb_n0_db)
    psk8_decoded = psk8_demodulation(psk8_received)
    psk8_errors = np.sum(psk8_bits != psk8_decoded)
    print(f"Transmitted bits: {psk8_bits}")
    print(f"Decoded bits:     {psk8_decoded}")
    print(f"Errors: {psk8_errors}/{len(psk8_bits)} - BER: {psk8_errors/len(psk8_bits):.4f}")
    
    # Test 4: 16-QAM
    print("\n4. 16-QAM Demodulation")
    print("-" * 60)
    qam_bits = gen_bites(20)  # Multiple of 4
    qam_symbols = qam16_modulation(qam_bits)
    qam_received = transmission_channel(qam_symbols, eb_n0_db)
    qam_decoded = qam16_demodulation(qam_received)
    qam_errors = np.sum(qam_bits != qam_decoded)
    print(f"Transmitted bits: {qam_bits}")
    print(f"Decoded bits:     {qam_decoded}")
    print(f"Errors: {qam_errors}/{len(qam_bits)} - BER: {qam_errors/len(qam_bits):.4f}")
    
    print("\n" + "=" * 60)
    print(f"All tests completed at Eb/N0 = {eb_n0_db} dB")
    print("=" * 60)