"""
Module for digital modulation.
Currently implements BPSK (Binary Phase-Shift Keying).
Future: QPSK, 8-PSK, QAM.
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
    
    Notes
    -----
    Mapping formula: symbol = 1 - 2 * bit
    - When bit = 0: symbol = 1 - 2*0 = 1
    - When bit = 1: symbol = 1 - 2*1 = -1
    
    This is the standard BPSK constellation on the real axis.
    """
    # Map bits to symbols: 0 -> +1, 1 -> -1
    symbols = 1 - 2 * bits
    
    # Convert to complex type (required for channel simulation)
    return symbols.astype(complex)


if __name__ == "__main__":
    # This code runs ONLY when you execute this file directly
    print("=" * 60)
    print("Testing BPSK Modulation")
    print("=" * 60)
    
    # Test 1: Generate random bits
    print("\nTest 1: Random bits")
    test_bits = gen_bites(10)
    print(f"Generated bits:\n{test_bits}")
    
    # Test 2: Modulate
    test_symbols = bpsk_modulation(test_bits)
    print(f"\nBPSK symbols:\n{test_symbols}")
    
    # Test 3: Verify properties
    print(f"\nProperties:")
    print(f"  - Symbol type: {test_symbols.dtype}")
    print(f"  - Number of symbols: {len(test_symbols)}")
    print(f"  - Unique values: {np.unique(test_symbols)}")
    
    # Test 4: Known input
    print("\n" + "=" * 60)
    print("Test 2: Known input [0, 1, 0, 1]")
    known_bits = np.array([0, 1, 0, 1])
    known_symbols = bpsk_modulation(known_bits)
    print(f"Input bits:  {known_bits}")
    print(f"Output symbols: {known_symbols}")
    print(f"Expected: [ 1.+0.j -1.+0.j  1.+0.j -1.+0.j]")