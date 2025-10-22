"""
Module for digital demodulation.
Converts received symbols back to bits.
"""

import numpy as np


def bpsk_demodulation(received_symbols):
    """
    BPSK (Binary Phase-Shift Keying) demodulation.
    
    Converts received complex symbols back to binary bits
    using threshold detection on the real part.
    
    Decision rule:
    - If Real(symbol) > 0  =>  bit = 0
    - If Real(symbol) <= 0 =>  bit = 1
    
    Parameters
    ----------
    received_symbols : numpy.ndarray (complex)
        Received symbols from the channel (with noise)
    
    Returns
    -------
    numpy.ndarray (int)
        Decoded binary bits (0s and 1s)
    
    Examples
    --------
    >>> received = np.array([0.8+0.1j, -1.2-0.3j, 0.5+0.2j])
    >>> bits = bpsk_demodulation(received)
    >>> print(bits)
    [0 1 0]
    
    Notes
    -----
    This is a hard-decision detector. The threshold is at 0.
    For BPSK, we only need to look at the real part:
    - Transmitted 0 -> +1 -> after noise -> still positive (likely) -> detect 0
    - Transmitted 1 -> -1 -> after noise -> still negative (likely) -> detect 1
    
    Errors occur when noise flips the sign.
    """
    # Extract real part and apply threshold detection
    # Real part < 0  =>  bit = 1
    # Real part >= 0 =>  bit = 0
    decoded_bits = (received_symbols.real < 0).astype(int)
    
    return decoded_bits


if __name__ == "__main__":
    # This code runs ONLY when you execute this file directly
    import numpy as np
    from Modulator import bpsk_modulation
    from GetBytes import gen_bites
    from TransmissionChannel import transmission_channel
    
    print("=" * 60)
    print("Testing BPSK Demodulation")
    print("=" * 60)
    
    # Test 1: Perfect demodulation (no noise)
    print("\nTest 1: Perfect demodulation (no noise)")
    original_bits = np.array([0, 1, 0, 1, 1, 0])
    symbols = bpsk_modulation(original_bits)
    decoded_bits = bpsk_demodulation(symbols)
    
    print(f"Original bits: {original_bits}")
    print(f"Decoded bits:  {decoded_bits}")
    print(f"Match: {np.array_equal(original_bits, decoded_bits)}")
    
    # Test 2: With noise
    print("\n" + "=" * 60)
    print("Test 2: Demodulation with noise")
    print("=" * 60)
    
    # Generate random bits
    n_bits = 1000
    original_bits = gen_bites(n_bits)
    
    # Modulate
    symbols = bpsk_modulation(original_bits)
    
    # Test with different noise levels
    for eb_n0_db in [0, 5, 10, 15]:
        # Transmit through noisy channel
        received = transmission_channel(symbols, eb_n0_db)
        
        # Demodulate
        decoded_bits = bpsk_demodulation(received)
        
        # Calculate errors
        errors = np.sum(original_bits != decoded_bits)
        ber = errors / n_bits
        
        print(f"\nEb/N0 = {eb_n0_db:2d} dB:")
        print(f"  Errors: {errors}/{n_bits}")
        print(f"  BER: {ber:.6f}")
    
    print("\nNote: Higher Eb/N0 => Lower BER (fewer errors)")