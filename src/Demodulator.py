import numpy as np


def bpsk_demodulation(received_symbols):
    """
    BPSK demodulation using threshold detection
    
    Decision rule:
    - Real(symbol) > 0 -> bit = 0
    - Real(symbol) < 0 -> bit = 1
    
    Parameters:
    -----------
    received_symbols : numpy.ndarray (complex)
        Received symbols from the channel
    
    Returns:
    --------
    numpy.ndarray
        Decoded bits (0s and 1s)
    
    Example:
    --------
    >>> received = np.array([0.9+0.1j, -1.2-0.05j, 0.8+0.2j])
    >>> bits = bpsk_demodulation(received)
    >>> print(bits)
    [0 1 0]
    """
    # Threshold detection on real part
    # Real > 0 means closer to +1 (bit 0)
    # Real < 0 means closer to -1 (bit 1)
    decoded_bits = (received_symbols.real < 0).astype(int)
    
    return decoded_bits


def qpsk_demodulation(received_symbols):
    """
    QPSK demodulation using ML (Maximum Likelihood) detection
    
    Determines which of 4 constellation points each received symbol
    is closest to, then maps back to 2 bits.
    
    Constellation points:
    - 00 -> ( 1+1j)/sqrt(2)  (45 deg)
    - 01 -> (-1+1j)/sqrt(2)  (135 deg)
    - 10 -> ( 1-1j)/sqrt(2)  (315 deg)
    - 11 -> (-1-1j)/sqrt(2)  (225 deg)
    
    Parameters:
    -----------
    received_symbols : numpy.ndarray (complex)
        Received symbols from the channel
    
    Returns:
    --------
    numpy.ndarray
        Decoded bits (0s and 1s)
    """
    # Define QPSK constellation
    constellation = np.array([
        (1 + 1j) / np.sqrt(2),   # 00
        (-1 + 1j) / np.sqrt(2),  # 01
        (1 - 1j) / np.sqrt(2),   # 10
        (-1 - 1j) / np.sqrt(2)   # 11
    ])
    
    bit_mapping = np.array([
        [0, 0],  # Point 0
        [0, 1],  # Point 1
        [1, 0],  # Point 2
        [1, 1]   # Point 3
    ])
    
    decoded_bits = []
    
    # For each received symbol, find closest constellation point
    for symbol in received_symbols:
        # Calculate distance to each constellation point
        distances = np.abs(symbol - constellation)
        
        # Find index of closest point
        closest_index = np.argmin(distances)
        
        # Map to bits
        decoded_bits.extend(bit_mapping[closest_index])
    
    return np.array(decoded_bits)


def psk8_demodulation(received_symbols):
    """
    8-PSK demodulation using ML detection
    
    Determines which of 8 constellation points each received symbol
    is closest to, then maps back to 3 bits.
    
    Parameters:
    -----------
    received_symbols : numpy.ndarray (complex)
        Received symbols from the channel
    
    Returns:
    --------
    numpy.ndarray
        Decoded bits (0s and 1s)
    """
    # Define 8-PSK constellation (8 points on unit circle)
    constellation = np.array([
        np.exp(1j * k * np.pi / 4) for k in range(8)
    ])
    
    # Bit mapping: 000, 001, 010, 011, 100, 101, 110, 111
    bit_mapping = np.array([
        [0, 0, 0],  # k=0
        [0, 0, 1],  # k=1
        [0, 1, 0],  # k=2
        [0, 1, 1],  # k=3
        [1, 0, 0],  # k=4
        [1, 0, 1],  # k=5
        [1, 1, 0],  # k=6
        [1, 1, 1]   # k=7
    ])
    
    decoded_bits = []
    
    # For each received symbol, find closest constellation point
    for symbol in received_symbols:
        # Calculate distance to each constellation point
        distances = np.abs(symbol - constellation)
        
        # Find index of closest point
        closest_index = np.argmin(distances)
        
        # Map to bits
        decoded_bits.extend(bit_mapping[closest_index])
    
    return np.array(decoded_bits)


def qam16_demodulation(received_symbols):
    """
    16-QAM demodulation using ML detection
    
    Determines which of 16 constellation points each received symbol
    is closest to, then maps back to 4 bits.
    
    The symbols were normalized by sqrt(10) during modulation,
    so we work with the normalized constellation.
    
    Parameters:
    -----------
    received_symbols : numpy.ndarray (complex)
        Received symbols from the channel (normalized)
    
    Returns:
    --------
    numpy.ndarray
        Decoded bits (0s and 1s)
    """
    # Define 16-QAM constellation (normalized)
    # Levels: {-3, -1, +1, +3} / sqrt(10)
    levels = np.array([-3, -1, 1, 3]) / np.sqrt(10)
    
    # Create all 16 constellation points
    constellation = []
    bit_mapping = []
    
    for i_idx, i_val in enumerate(levels):
        for q_idx, q_val in enumerate(levels):
            constellation.append(i_val + 1j * q_val)
            
            # Map indices to bits: 00->3, 01->1, 10->-1, 11->-3
            # Reverse mapping: 3->00, 1->01, -1->10, -3->11
            level_to_bits = {3: [0, 0], 1: [0, 1], -1: [1, 0], -3: [1, 1]}
            
            # Reconstruct original levels for mapping
            orig_i = int(i_val * np.sqrt(10))
            orig_q = int(q_val * np.sqrt(10))
            
            i_bits = level_to_bits[orig_i]
            q_bits = level_to_bits[orig_q]
            
            bit_mapping.append(i_bits + q_bits)
    
    constellation = np.array(constellation)
    bit_mapping = np.array(bit_mapping)
    
    decoded_bits = []
    
    # For each received symbol, find closest constellation point
    for symbol in received_symbols:
        # Calculate distance to each constellation point
        distances = np.abs(symbol - constellation)
        
        # Find index of closest point
        closest_index = np.argmin(distances)
        
        # Map to bits
        decoded_bits.extend(bit_mapping[closest_index])
    
    return np.array(decoded_bits)


# Test code
if __name__ == "__main__":
    print("=" * 60)
    print("Testing all demodulation schemes")
    print("=" * 60)
    print()
    
    # Test BPSK
    print("1. BPSK Demodulation")
    print("-" * 60)
    test_symbols_bpsk = np.array([0.9, -1.1, 0.8, -0.9], dtype=complex)
    print(f"Received: {test_symbols_bpsk}")
    bits_bpsk = bpsk_demodulation(test_symbols_bpsk)
    print(f"Decoded:  {bits_bpsk}")
    print(f"Expected: [0 1 0 1]")
    print()
    
    # Test QPSK
    print("2. QPSK Demodulation")
    print("-" * 60)
    # Approximate QPSK symbols with small noise
    test_symbols_qpsk = np.array([
        (1 + 1j) / np.sqrt(2) + 0.1,      # Should be 00
        (-1 + 1j) / np.sqrt(2) - 0.05j,   # Should be 01
    ])
    print(f"Received: {test_symbols_qpsk}")
    bits_qpsk = qpsk_demodulation(test_symbols_qpsk)
    print(f"Decoded:  {bits_qpsk}")
    print(f"Expected: [0 0 0 1]")
    print()
    
    # Test 8-PSK
    print("3. 8-PSK Demodulation")
    print("-" * 60)
    test_symbols_8psk = np.array([
        np.exp(1j * 0),           # Should be 000
        np.exp(1j * np.pi / 4),   # Should be 001
    ])
    print(f"Received: {test_symbols_8psk}")
    bits_8psk = psk8_demodulation(test_symbols_8psk)
    print(f"Decoded:  {bits_8psk}")
    print(f"Expected: [0 0 0 0 0 1]")
    print()
    
    # Test 16-QAM
    print("4. 16-QAM Demodulation")
    print("-" * 60)
    test_symbols_qam = np.array([
        (3 + 3j) / np.sqrt(10),   # Should be 0000
        (1 + 1j) / np.sqrt(10),   # Should be 0101
    ])
    print(f"Received: {test_symbols_qam}")
    bits_qam = qam16_demodulation(test_symbols_qam)
    print(f"Decoded:  {bits_qam}")
    print(f"Expected: [0 0 0 0 0 1 0 1]")
    print()
    
    print("=" * 60)
    print("All tests completed!")
    print("=" * 60)