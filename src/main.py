import numpy as np
import matplotlib.pyplot as plt
from GetBytes import gen_bites
from Modulator import bpsk_modulation, qpsk_modulation, psk8_modulation, qam16_modulation
from TransmissionChannel import transmission_channel
from Demodulator import bpsk_demodulation, qpsk_demodulation, psk8_demodulation, qam16_demodulation


def calculate_ber(original_bits, decoded_bits):
    """
    Calculate Bit Error Rate (BER)
    
    BER is the ratio of incorrectly decoded bits to total bits.
    
    Parameters:
    -----------
    original_bits : numpy.ndarray
        Original transmitted bits
    decoded_bits : numpy.ndarray
        Decoded received bits
    
    Returns:
    --------
    float
        Bit Error Rate (0 to 1)
    """
    errors = np.sum(original_bits != decoded_bits)
    ber = errors / len(original_bits)
    return ber


def simulate_modulation(modulation_type, eb_n0_range, n_bits=10000):
    """
    Simulate a modulation scheme over a range of Eb/N0 values
    
    Parameters:
    -----------
    modulation_type : str
        Type of modulation: 'BPSK', 'QPSK', '8-PSK', or '16-QAM'
    eb_n0_range : array-like
        Range of Eb/N0 values in dB
    n_bits : int
        Number of bits to transmit per simulation
    
    Returns:
    --------
    list
        BER values for each Eb/N0 point
    """
    ber_values = []
    
    # Select modulation and demodulation functions
    if modulation_type == 'BPSK':
        modulate = bpsk_modulation
        demodulate = bpsk_demodulation
        bits_per_symbol = 1
    elif modulation_type == 'QPSK':
        modulate = qpsk_modulation
        demodulate = qpsk_demodulation
        bits_per_symbol = 2
    elif modulation_type == '8-PSK':
        modulate = psk8_modulation
        demodulate = psk8_demodulation
        bits_per_symbol = 3
    elif modulation_type == '16-QAM':
        modulate = qam16_modulation
        demodulate = qam16_demodulation
        bits_per_symbol = 4
    else:
        raise ValueError(f"Unknown modulation type: {modulation_type}")
    
    for eb_n0_db in eb_n0_range:
        # Adjust number of bits to be multiple of bits_per_symbol
        n_bits_adjusted = (n_bits // bits_per_symbol) * bits_per_symbol
        
        # Generate random bits
        bits = gen_bites(n_bits_adjusted)
        
        # Modulation
        symbols = modulate(bits)
        
        # Transmission through channel with noise
        received_symbols = transmission_channel(symbols, eb_n0_db)
        
        # Demodulation
        decoded_bits = demodulate(received_symbols)
        
        # Calculate BER
        ber = calculate_ber(bits, decoded_bits)
        ber_values.append(ber)
        
        print(f"{modulation_type:8s} | Eb/N0 = {eb_n0_db:2d} dB | BER = {ber:.6f}")
    
    return ber_values


def plot_ber_curves(eb_n0_range, results_dict, save_path='ber_comparison.png'):
    """
    Plot BER vs Eb/N0 curves for multiple modulation schemes
    
    Parameters:
    -----------
    eb_n0_range : array-like
        Range of Eb/N0 values in dB
    results_dict : dict
        Dictionary with modulation names as keys and BER lists as values
    save_path : str
        Path to save the plot
    """
    plt.figure(figsize=(12, 8))
    
    # Define markers and colors for each modulation
    styles = {
        'BPSK': {'marker': 'o', 'color': 'blue', 'linestyle': '-'},
        'QPSK': {'marker': 's', 'color': 'red', 'linestyle': '--'},
        '8-PSK': {'marker': '^', 'color': 'green', 'linestyle': '-.'},
        '16-QAM': {'marker': 'd', 'color': 'purple', 'linestyle': ':'}
    }
    
    for mod_type, ber_values in results_dict.items():
        style = styles.get(mod_type, {})
        plt.semilogy(
            eb_n0_range, 
            ber_values, 
            marker=style.get('marker', 'o'),
            color=style.get('color', 'black'),
            linestyle=style.get('linestyle', '-'),
            linewidth=2,
            markersize=8,
            label=mod_type
        )
    
    plt.grid(True, which='both', linestyle='--', alpha=0.6)
    plt.xlabel('Eb/N0 (dB)', fontsize=14, fontweight='bold')
    plt.ylabel('Bit Error Rate (BER)', fontsize=14, fontweight='bold')
    plt.title('BER Performance Comparison for Different Modulations', 
              fontsize=16, fontweight='bold')
    plt.legend(fontsize=12, loc='best')
    plt.xlim([min(eb_n0_range), max(eb_n0_range)])
    plt.ylim([1e-5, 1])
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"\nPlot saved as: {save_path}")
    plt.show()


def plot_constellation(modulation_type, n_symbols=1000, eb_n0_db=10):
    """
    Plot constellation diagram for a modulation scheme
    
    Parameters:
    -----------
    modulation_type : str
        Type of modulation
    n_symbols : int
        Number of symbols to generate and plot
    eb_n0_db : float
        Eb/N0 in dB for noisy constellation
    """
    # Select modulation function
    if modulation_type == 'BPSK':
        modulate = bpsk_modulation
        bits_per_symbol = 1
    elif modulation_type == 'QPSK':
        modulate = qpsk_modulation
        bits_per_symbol = 2
    elif modulation_type == '8-PSK':
        modulate = psk8_modulation
        bits_per_symbol = 3
    elif modulation_type == '16-QAM':
        modulate = qam16_modulation
        bits_per_symbol = 4
    else:
        raise ValueError(f"Unknown modulation type: {modulation_type}")
    
    # Generate bits and symbols
    n_bits = n_symbols * bits_per_symbol
    bits = gen_bites(n_bits)
    symbols = modulate(bits)
    
    # Add noise
    noisy_symbols = transmission_channel(symbols, eb_n0_db)
    
    # Plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Plot 1: Clean constellation
    ax1.scatter(symbols.real, symbols.imag, alpha=0.6, s=50, c='blue')
    ax1.set_xlabel('In-Phase (I)', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Quadrature (Q)', fontsize=12, fontweight='bold')
    ax1.set_title(f'{modulation_type} Constellation (Clean)', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.axhline(y=0, color='k', linewidth=0.5)
    ax1.axvline(x=0, color='k', linewidth=0.5)
    ax1.axis('equal')
    
    # Plot 2: Noisy constellation
    ax2.scatter(noisy_symbols.real, noisy_symbols.imag, alpha=0.5, s=20, c='red')
    ax2.set_xlabel('In-Phase (I)', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Quadrature (Q)', fontsize=12, fontweight='bold')
    ax2.set_title(f'{modulation_type} Constellation (Eb/N0 = {eb_n0_db} dB)', 
                  fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.axhline(y=0, color='k', linewidth=0.5)
    ax2.axvline(x=0, color='k', linewidth=0.5)
    ax2.axis('equal')
    
    plt.tight_layout()
    save_path = f'{modulation_type.lower().replace("-", "")}_constellation.png'
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Constellation plot saved as: {save_path}")
    plt.show()


def main():
    """
    Main simulation program
    """
    print("=" * 70)
    print(" " * 15 + "PSK & QAM MODULATION SIMULATION")
    print("=" * 70)
    print()
    
    # Simulation parameters
    eb_n0_range = range(-2, 13)  # -2 dB to 12 dB
    n_bits = 10000
    
    print(f"Simulation parameters:")
    print(f"  Number of bits per simulation: {n_bits}")
    print(f"  Eb/N0 range: {list(eb_n0_range)} dB")
    print()
    
    # Store results
    results = {}
    
    # Simulate each modulation
    modulations = ['BPSK', 'QPSK', '8-PSK', '16-QAM']
    
    for mod_type in modulations:
        print("=" * 70)
        print(f"Simulating {mod_type}")
        print("-" * 70)
        ber_values = simulate_modulation(mod_type, eb_n0_range, n_bits)
        results[mod_type] = ber_values
        print()
    
    # Plot BER comparison
    print("=" * 70)
    print("Generating BER comparison plot...")
    print("=" * 70)
    plot_ber_curves(eb_n0_range, results)
    print()
    
    # Plot constellation diagrams
    print("=" * 70)
    print("Generating constellation diagrams...")
    print("=" * 70)
    for mod_type in modulations:
        plot_constellation(mod_type, n_symbols=500, eb_n0_db=10)
    print()
    
    print("=" * 70)
    print("Simulation completed successfully!")
    print("=" * 70)
    print()
    print("Generated files:")
    print("  - ber_comparison.png")
    for mod_type in modulations:
        filename = f'{mod_type.lower().replace("-", "")}_constellation.png'
        print(f"  - {filename}")


if __name__ == "__main__":
    main()