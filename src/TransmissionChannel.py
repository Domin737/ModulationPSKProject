import numpy as np
from AddAWGNNoise import add_awgn_noise


def transmission_channel(symbols, eb_n0_db):
    """
    Simulate transmission through AWGN channel
    
    This function models a transmission channel with Additive White 
    Gaussian Noise (AWGN). It takes modulated symbols as input and 
    returns the same symbols corrupted by noise.
    
    Parameters:
    -----------
    symbols : numpy.ndarray (complex)
        Transmitted symbols (from modulator)
    eb_n0_db : float
        Eb/N0 ratio in dB (Energy per bit to Noise power spectral density)
        Higher values mean better signal quality (less noise)
    
    Returns:
    --------
    numpy.ndarray (complex)
        Received symbols with added AWGN noise
    
    Example:
    --------
    >>> symbols = np.array([1.0, -1.0, 1.0], dtype=complex)
    >>> received = transmission_channel(symbols, eb_n0_db=10.0)
    >>> print(received)  # Will be close to original but with noise
    """
    # Add AWGN noise to symbols
    received_symbols = add_awgn_noise(symbols, eb_n0_db)
    
    return received_symbols


# Test code
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