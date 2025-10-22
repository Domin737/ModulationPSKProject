"""
Module for simulating transmission channel.
Models signal transmission through a noisy channel.
"""

from AddAWGNNoise import add_awgn_noise


def transmission_channel(symbols, eb_n0_db):
    """
    Simulate transmission through an AWGN channel.
    
    This function models a real communication channel where
    the transmitted signal is corrupted by additive white
    Gaussian noise (AWGN).
    
    Parameters
    ----------
    symbols : numpy.ndarray (complex)
        Transmitted symbols (output from modulator)
    eb_n0_db : float
        Channel quality: Eb/N0 ratio in dB
        Higher value = better channel = less noise
        Typical range: -5 dB to 15 dB
    
    Returns
    -------
    numpy.ndarray (complex)
        Received symbols (with added noise)
    
    Examples
    --------
    >>> import numpy as np
    >>> symbols = np.array([1.0, -1.0, 1.0], dtype=complex)
    >>> received = transmission_channel(symbols, eb_n0_db=10)
    >>> # received will be close to symbols, with some noise
    
    Notes
    -----
    Current implementation models only AWGN channel.
    Future extensions could include:
    - Fading (Rayleigh, Rician)
    - Frequency offset
    - Phase noise
    - Multipath propagation
    """
    # Transmit symbols through AWGN channel
    # (add noise to simulate channel impairments)
    received_symbols = add_awgn_noise(symbols, eb_n0_db)
    
    return received_symbols


if __name__ == "__main__":
    # This code runs ONLY when you execute this file directly
    import numpy as np
    from Modulator import bpsk_modulation
    from GetBytes import gen_bites
    
    print("=" * 60)
    print("Testing Transmission Channel")
    print("=" * 60)
    
    # Test 1: Transmit BPSK symbols through channel
    print("\nTest 1: BPSK through channel")
    
    # Generate bits and modulate
    bits = gen_bites(10)
    symbols = bpsk_modulation(bits)
    
    print(f"Original bits: {bits}")
    print(f"Transmitted symbols: {symbols}")
    
    # Transmit through channel with different noise levels
    for eb_n0_db in [0, 5, 10]:
        received = transmission_channel(symbols, eb_n0_db)
        print(f"\nEb/N0 = {eb_n0_db} dB:")
        print(f"Received: {received}")
    
    # Test 2: Perfect channel (very high Eb/N0)
    print("\n" + "=" * 60)
    print("Test 2: Nearly perfect channel (20 dB)")
    print("=" * 60)
    
    perfect_received = transmission_channel(symbols, eb_n0_db=20)
    difference = np.abs(symbols - perfect_received)
    print(f"Max difference from original: {np.max(difference):.6f}")
    print("(Should be very small)")