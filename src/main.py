"""
Main simulation program for PSK modulation analysis.
Simulates BPSK transmission and analyzes performance.
"""

import numpy as np
import matplotlib.pyplot as plt
from GetBytes import gen_bites
from Modulator import bpsk_modulation
from TransmissionChannel import transmission_channel
from Demodulator import bpsk_demodulation


def calculate_ber(original_bits, decoded_bits):
    """
    Calculate Bit Error Rate (BER).
    
    BER is the ratio of incorrectly decoded bits to total bits.
    It's the main metric for evaluating communication system performance.
    
    Parameters
    ----------
    original_bits : numpy.ndarray
        Original transmitted bits
    decoded_bits : numpy.ndarray
        Decoded received bits
    
    Returns
    -------
    float
        Bit Error Rate (0.0 to 1.0)
        0.0 = perfect (no errors)
        0.5 = random guessing (worst case for binary)
    
    Examples
    --------
    >>> original = np.array([0, 1, 0, 1])
    >>> decoded = np.array([0, 1, 1, 1])  # one error
    >>> ber = calculate_ber(original, decoded)
    >>> print(ber)
    0.25
    """
    errors = np.sum(original_bits != decoded_bits)
    ber = errors / len(original_bits)
    return ber


def simulate_bpsk(eb_n0_range, n_bits=10000):
    """
    Simulate BPSK transmission over a range of Eb/N0 values.
    
    This function runs a complete simulation:
    1. Generate random bits
    2. Modulate to BPSK symbols
    3. Transmit through noisy channel
    4. Demodulate back to bits
    5. Calculate BER
    
    Repeat for each Eb/N0 value to see how performance
    changes with channel quality.
    
    Parameters
    ----------
    eb_n0_range : array-like
        Range of Eb/N0 values in dB to simulate
        Example: range(-2, 11) for -2 to 10 dB
    n_bits : int, optional
        Number of bits to transmit for each Eb/N0 point
        More bits = more accurate BER estimate
        Default: 10000
    
    Returns
    -------
    list
        BER values corresponding to each Eb/N0 point
    
    Examples
    --------
    >>> eb_n0_range = range(0, 11)
    >>> ber_values = simulate_bpsk(eb_n0_range, n_bits=10000)
    >>> # ber_values contains BER for 0, 1, 2, ..., 10 dB
    """
    ber_values = []
    
    print(f"Simulating with {n_bits} bits per point...")
    print("-" * 60)
    
    for eb_n0_db in eb_n0_range:
        # Step 1: Generate random bits
        bits = gen_bites(n_bits)
        
        # Step 2: BPSK Modulation
        symbols = bpsk_modulation(bits)
        
        # Step 3: Transmission through noisy channel
        received_symbols = transmission_channel(symbols, eb_n0_db)
        
        # Step 4: BPSK Demodulation
        decoded_bits = bpsk_demodulation(received_symbols)
        
        # Step 5: Calculate BER
        ber = calculate_ber(bits, decoded_bits)
        ber_values.append(ber)
        
        # Display progress
        print(f"Eb/N0 = {eb_n0_db:2d} dB  =>  BER = {ber:.6f}")
    
    return ber_values


def plot_ber_curve(eb_n0_range, ber_values, save_path='results/bpsk_ber_curve.png'):
    """
    Plot BER vs Eb/N0 curve.
    
    Creates a logarithmic plot showing how Bit Error Rate
    decreases as channel quality (Eb/N0) increases.
    
    Parameters
    ----------
    eb_n0_range : array-like
        Eb/N0 values in dB (x-axis)
    ber_values : array-like
        BER values (y-axis)
    save_path : str, optional
        Path to save the plot
        Default: 'results/bpsk_ber_curve.png'
    
    Notes
    -----
    The plot uses logarithmic scale for BER (y-axis) because
    BER can vary over many orders of magnitude (e.g., 1e-1 to 1e-6).
    """
    plt.figure(figsize=(10, 6))
    
    # Plot with logarithmic y-axis
    plt.semilogy(eb_n0_range, ber_values, 'bo-', linewidth=2, 
                 markersize=8, label='BPSK (Simulated)')
    
    # Grid for readability
    plt.grid(True, which='both', linestyle='--', alpha=0.7)
    
    # Labels
    plt.xlabel('Eb/N0 (dB)', fontsize=12)
    plt.ylabel('Bit Error Rate (BER)', fontsize=12)
    plt.title('BPSK Performance in AWGN Channel', fontsize=14, fontweight='bold')
    
    # Legend
    plt.legend(fontsize=11)
    
    # Tight layout
    plt.tight_layout()
    
    # Save
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"\nPlot saved as: {save_path}")
    
    # Display
    plt.show()


def main():
    """
    Main function - runs the complete BPSK simulation.
    """
    print("=" * 60)
    print("BPSK MODULATION SIMULATION")
    print("=" * 60)
    print()
    
    # Simulation parameters
    eb_n0_range = range(-2, 11)  # -2 dB to 10 dB
    n_bits = 10000  # bits per simulation point
    
    print("Simulation Parameters:")
    print(f"  - Modulation: BPSK")
    print(f"  - Number of bits: {n_bits}")
    print(f"  - Eb/N0 range: {list(eb_n0_range)} dB")
    print()
    
    # Run simulation
    print("Running simulation...")
    print()
    ber_values = simulate_bpsk(eb_n0_range, n_bits)
    
    print()
    print("-" * 60)
    print("Simulation complete!")
    print()
    
    # Plot results
    print("Generating plot...")
    plot_ber_curve(eb_n0_range, ber_values)
    
    print()
    print("=" * 60)
    print("DONE!")
    print("=" * 60)


if __name__ == "__main__":
    main()