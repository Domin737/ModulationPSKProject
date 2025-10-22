"""
TransmissionChannel.py - Transmission channel simulator

This module simulates a transmission channel with AWGN noise.
"""

import numpy as np
from AddAWGNNoise import add_awgn_noise


def transmission_channel(symbols, eb_n0_db):
    """
    Simulate transmission through AWGN channel
    
    Parameters:
    -----------
    symbols : numpy.ndarray (complex)
        Transmitted symbols
    eb_n0_db : float
        Eb/N0 ratio in dB
    
    Returns:
    --------
    numpy.ndarray (complex)
        Received symbols with added noise
    """
    received_symbols = add_awgn_noise(symbols, eb_n0_db)
    return received_symbols


if __name__ == "__main__":
    print("=" * 60)
    print("Testing Transmission Channel")
    print("=" * 60)
    print()
    
    # Create test symbols (BPSK)
    test_symbols = np.array([1.0, -1.0, 1.0, -1.0, 1.0], dtype=complex)
    print(f"Original symbols: {test_symbols}")
    print()
    
    # Test with different Eb/N0 values
    eb_n0_values = [0, 5, 10, 15]
    
    for eb_n0 in eb_n0_values:
        received = transmission_channel(test_symbols, eb_n0)
        print(f"Eb/N0 = {eb_n0:2d} dB:")
        print(f"  Received: {received}")
        print()
    
    print("=" * 60)
    print("Test completed!")
    print("=" * 60)