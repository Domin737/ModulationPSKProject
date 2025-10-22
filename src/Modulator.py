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
    
    Example:
    --------
    >>> bits = np.array([0, 1, 0, 1])
    >>> symbols = bpsk_modulation(bits)
    >>> print(symbols)
    [ 1.+0.j -1.+0.j  1.+0.j -1.+0.j]
    """
    # Map: 0 -> +1, 1 -> -1
    symbols = 1 - 2 * bits
    return symbols.astype(complex)


def qpsk_modulation(bits):
    """
    QPSK (Quadrature Phase-Shift Keying) modulation
    
    Maps 2 bits to complex symbols on unit circle:
    - 00 -> ( 1+1j)/sqrt(2)  = 45 degrees
    - 01 -> (-1+1j)/sqrt(2)  = 135 degrees
    - 10 -> ( 1-1j)/sqrt(2)  = -45 degrees (315 degrees)
    - 11 -> (-1-1j)/sqrt(2)  = -135 degrees (225 degrees)
    
    Parameters:
    -----------
    bits : numpy.ndarray
        Array of binary bits (0s and 1s). Length must be even.
    
    Returns:
    --------
    numpy.ndarray (complex)
        QPSK modulated symbols
    
    Example:
    --------
    >>> bits = np.array([0, 0, 0, 1, 1, 0, 1, 1])
    >>> symbols = qpsk_modulation(bits)
    """
    if len(bits) % 2 != 0:
        raise ValueError("Number of bits must be even for QPSK")
    
    # Reshape bits into pairs
    bits_reshaped = bits.reshape(-1, 2)
    
    # Map bit pairs to symbols
    symbols = np.zeros(len(bits_reshaped), dtype=complex)
    
    for i, bit_pair in enumerate(bits_reshaped):
        if bit_pair[0] == 0 and bit_pair[1] == 0:      # 00
            symbols[i] = (1 + 1j) / np.sqrt(2)
        elif bit_pair[0] == 0 and bit_pair[1] == 1:    # 01
            symbols[i] = (-1 + 1j) / np.sqrt(2)
        elif bit_pair[0] == 1 and bit_pair[1] == 0:    # 10
            symbols[i] = (1 - 1j) / np.sqrt(2)
        else:                                            # 11
            symbols[i] = (-1 - 1j) / np.sqrt(2)
    
    return symbols


def psk8_modulation(bits):
    """
    8-PSK (8-ary Phase-Shift Keying) modulation
    
    Maps 3 bits to complex symbols on unit circle:
    8 points equally spaced at: 0, 45, 90, 135, 180, 225, 270, 315 degrees
    
    Mapping:
    - 000 -> exp(j*0*pi/4)   = 1+0j          (0 degrees)
    - 001 -> exp(j*1*pi/4)   = (1+1j)/sqrt(2) (45 degrees)
    - 010 -> exp(j*2*pi/4)   = 0+1j          (90 degrees)
    - 011 -> exp(j*3*pi/4)   = (-1+1j)/sqrt(2) (135 degrees)
    - 100 -> exp(j*4*pi/4)   = -1+0j         (180 degrees)
    - 101 -> exp(j*5*pi/4)   = (-1-1j)/sqrt(2) (225 degrees)
    - 110 -> exp(j*6*pi/4)   = 0-1j          (270 degrees)
    - 111 -> exp(j*7*pi/4)   = (1-1j)/sqrt(2) (315 degrees)
    
    Parameters:
    -----------
    bits : numpy.ndarray
        Array of binary bits (0s and 1s). Length must be multiple of 3.
    
    Returns:
    --------
    numpy.ndarray (complex)
        8-PSK modulated symbols
    """
    if len(bits) % 3 != 0:
        raise ValueError("Number of bits must be multiple of 3 for 8-PSK")
    
    # Reshape bits into triplets
    bits_reshaped = bits.reshape(-1, 3)
    
    # Convert triplets to decimal (0-7)
    decimal_values = bits_reshaped[:, 0] * 4 + bits_reshaped[:, 1] * 2 + bits_reshaped[:, 2]
    
    # Map to 8-PSK constellation (8 points on unit circle)
    # Symbol k is at angle k * pi/4
    angles = decimal_values * np.pi / 4
    symbols = np.exp(1j * angles)
    
    return symbols


def qam16_modulation(bits):
    """
    16-QAM (Quadrature Amplitude Modulation) modulation
    
    Maps 4 bits to complex symbols in a 4x4 grid:
    Levels: {-3, -1, +1, +3}
    
    Parameters:
    -----------
    bits : numpy.ndarray
        Array of binary bits (0s and 1s). Length must be multiple of 4.
    
    Returns:
    --------
    numpy.ndarray (complex)
        16-QAM modulated symbols (normalized)
    """
    if len(bits) % 4 != 0:
        raise ValueError("Number of bits must be multiple of 4 for 16-QAM")
    
    # Reshape bits into groups of 4
    bits_reshaped = bits.reshape(-1, 4)
    
    # Split into I and Q components (2 bits each)
    i_bits = bits_reshaped[:, :2]  # First 2 bits for I
    q_bits = bits_reshaped[:, 2:]  # Last 2 bits for Q
    
    # Map 2 bits to amplitude levels: 00->+3, 01->+1, 10->-1, 11->-3
    def map_to_level(bit_pair):
        val = bit_pair[:, 0] * 2 + bit_pair[:, 1]
        # 00=0->+3, 01=1->+1, 10=2->-1, 11=3->-3
        levels = np.array([3, 1, -1, -3])
        return levels[val]
    
    i_component = map_to_level(i_bits)
    q_component = map_to_level(q_bits)
    
    # Combine into complex symbols
    symbols = i_component + 1j * q_component
    
    # Normalize to average power = 1
    # Average power of 16-QAM with levels {-3,-1,+1,+3} is 10
    symbols = symbols / np.sqrt(10)
    
    return symbols


# Test code - only runs when script is executed directly
if __name__ == "__main__":
    print("=" * 60)
    print("Testing all modulation schemes")
    print("=" * 60)
    print()
    
    # Test BPSK
    print("1. BPSK Modulation")
    print("-" * 60)
    test_bits_bpsk = gen_bites(8)
    print(f"Bits:    {test_bits_bpsk}")
    symbols_bpsk = bpsk_modulation(test_bits_bpsk)
    print(f"Symbols: {symbols_bpsk}")
    print()
    
    # Test QPSK
    print("2. QPSK Modulation")
    print("-" * 60)
    test_bits_qpsk = gen_bites(8)
    print(f"Bits:    {test_bits_qpsk}")
    symbols_qpsk = qpsk_modulation(test_bits_qpsk)
    print(f"Symbols: {symbols_qpsk}")
    print()
    
    # Test 8-PSK
    print("3. 8-PSK Modulation")
    print("-" * 60)
    test_bits_8psk = gen_bites(12)
    print(f"Bits:    {test_bits_8psk}")
    symbols_8psk = psk8_modulation(test_bits_8psk)
    print(f"Symbols: {symbols_8psk}")
    print()
    
    # Test 16-QAM
    print("4. 16-QAM Modulation")
    print("-" * 60)
    test_bits_qam = gen_bites(12)
    print(f"Bits:    {test_bits_qam}")
    symbols_qam = qam16_modulation(test_bits_qam)
    print(f"Symbols: {symbols_qam}")
    print()
    
    print("=" * 60)
    print("All tests completed successfully!")
    print("=" * 60)