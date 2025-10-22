import numpy as np


def add_awgn_noise(symbols, eb_n0_db):
    """
    Add AWGN (Additive White Gaussian Noise) to symbols
    
    This function adds complex Gaussian noise to the input symbols based on
    the specified Eb/N0 ratio. The noise power is calculated to achieve the
    desired signal-to-noise ratio.
    
    Parameters:
    -----------
    symbols : numpy.ndarray (complex)
        Modulated symbols (can be from any modulation: BPSK, QPSK, 8-PSK, QAM)
    eb_n0_db : float
        Energy per bit to noise power spectral density ratio in dB
        Higher values mean less noise (better signal quality)
    
    Returns:
    --------
    numpy.ndarray (complex)
        Symbols with added AWGN noise
    
    Notes:
    ------
    - Assumes Eb = 1.0 (normalized energy per bit)
    - Generates complex Gaussian noise (I + jQ components)
    - Noise power is calculated based on Eb/N0 ratio
    - Each component (I and Q) has variance = sigma^2 = N0/2
    
    Example:
    --------
    >>> symbols = np.array([1.0, -1.0, 1.0], dtype=complex)
    >>> noisy = add_awgn_noise(symbols, eb_n0_db=10.0)
    >>> print(noisy)
    # Will be close to [1, -1, 1] but with added noise
    """
    # Convert Eb/N0 from dB to linear scale
    eb_n0 = 10 ** (eb_n0_db / 10.0)
    
    # Normalized energy per bit
    eb = 1.0
    
    # Noise power spectral density
    n0 = eb / eb_n0
    
    # Standard deviation of noise (for I and Q components)
    # Each component has variance = N0/2, so std = sqrt(N0/2)
    sigma = np.sqrt(n0 / 2)
    
    # Number of symbols
    n_symbols = symbols.shape[0]
    
    # Generate Gaussian noise for I and Q components
    # Mean = 0, Std = sigma
    noise_i = sigma * np.random.normal(0, 1, size=n_symbols)
    noise_q = sigma * np.random.normal(0, 1, size=n_symbols)
    
    # Complex AWGN noise
    awgn_noise = noise_i + 1j * noise_q
    
    # Add noise to symbols
    received_symbols = symbols + awgn_noise
    
    return received_symbols


# Test code
if __name__ == "__main__":
    print("=" * 60)
    print("Testing AWGN Noise Addition")
    print("=" * 60)
    print()
    
    # Create test symbols (BPSK: +1, -1, +1, -1, +1)
    test_symbols = np.array([1.0, -1.0, 1.0, -1.0, 1.0], dtype=complex)
    
    print(f"Original symbols: {test_symbols}")
    print()
    
    # Test with different Eb/N0 values
    eb_n0_values = [0, 5, 10, 15, 20]
    
    for eb_n0 in eb_n0_values:
        noisy_symbols = add_awgn_noise(test_symbols, eb_n0)
        
        # Calculate SNR empirically
        signal_power = np.mean(np.abs(test_symbols) ** 2)
        noise = noisy_symbols - test_symbols
        noise_power = np.mean(np.abs(noise) ** 2)
        
        if noise_power > 0:
            snr_db = 10 * np.log10(signal_power / noise_power)
        else:
            snr_db = float('inf')
        
        print(f"Eb/N0 = {eb_n0:2d} dB:")
        print(f"  Noisy symbols: {noisy_symbols}")
        print(f"  Measured SNR:  {snr_db:.2f} dB")
        print()
    
    print("=" * 60)
    print("Test completed!")
    print("=" * 60)
    print()
    print("Note: As Eb/N0 increases, noise decreases and symbols become")
    print("      closer to original values.")