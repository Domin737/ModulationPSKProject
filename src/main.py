"""
Main simulation program for PSK/QAM modulation analysis.
Simulates BPSK, QPSK, 8-PSK, 16-QAM and compares performance.
"""

import numpy as np
import matplotlib.pyplot as plt
from GetBytes import gen_bites
from Modulator import bpsk_modulation, qpsk_modulation, psk8_modulation, qam16_modulation
from TransmissionChannel import transmission_channel
from Demodulator import bpsk_demodulation, qpsk_demodulation, psk8_demodulation, qam16_demodulation


def calculate_ber(original_bits, decoded_bits):
    """Calculate Bit Error Rate."""
    errors = np.sum(original_bits != decoded_bits)
    ber = errors / len(original_bits)
    return ber


def simulate_bpsk(eb_n0_range, n_bits=10000):
    """Simulate BPSK transmission."""
    ber_values = []
    
    print("BPSK Simulation:")
    print("-" * 60)
    
    for eb_n0_db in eb_n0_range:
        bits = gen_bites(n_bits)
        symbols = bpsk_modulation(bits)
        received_symbols = transmission_channel(symbols, eb_n0_db)
        decoded_bits = bpsk_demodulation(received_symbols)
        ber = calculate_ber(bits, decoded_bits)
        ber_values.append(ber)
        print(f"Eb/N0 = {eb_n0_db:2d} dB  =>  BER = {ber:.6f}")
    
    return ber_values


def simulate_qpsk(eb_n0_range, n_bits=10000):
    """Simulate QPSK transmission."""
    ber_values = []
    
    # Ensure even number of bits
    if n_bits % 2 != 0:
        n_bits += 1
    
    print("QPSK Simulation:")
    print("-" * 60)
    
    for eb_n0_db in eb_n0_range:
        bits = gen_bites(n_bits)
        symbols = qpsk_modulation(bits)
        received_symbols = transmission_channel(symbols, eb_n0_db)
        decoded_bits = qpsk_demodulation(received_symbols)
        ber = calculate_ber(bits, decoded_bits)
        ber_values.append(ber)
        print(f"Eb/N0 = {eb_n0_db:2d} dB  =>  BER = {ber:.6f}")
    
    return ber_values


def simulate_8psk(eb_n0_range, n_bits=10002):
    """Simulate 8-PSK transmission."""
    ber_values = []
    
    # Ensure multiple of 3
    if n_bits % 3 != 0:
        n_bits = (n_bits // 3) * 3
    
    print("8-PSK Simulation:")
    print("-" * 60)
    
    for eb_n0_db in eb_n0_range:
        bits = gen_bites(n_bits)
        symbols = psk8_modulation(bits)
        received_symbols = transmission_channel(symbols, eb_n0_db)
        decoded_bits = psk8_demodulation(received_symbols)
        ber = calculate_ber(bits, decoded_bits)
        ber_values.append(ber)
        print(f"Eb/N0 = {eb_n0_db:2d} dB  =>  BER = {ber:.6f}")
    
    return ber_values


def simulate_16qam(eb_n0_range, n_bits=10000):
    """Simulate 16-QAM transmission."""
    ber_values = []
    
    # Ensure multiple of 4
    if n_bits % 4 != 0:
        n_bits = (n_bits // 4) * 4
    
    print("16-QAM Simulation:")
    print("-" * 60)
    
    for eb_n0_db in eb_n0_range:
        bits = gen_bites(n_bits)
        symbols = qam16_modulation(bits)
        received_symbols = transmission_channel(symbols, eb_n0_db)
        decoded_bits = qam16_demodulation(received_symbols)
        ber = calculate_ber(bits, decoded_bits)
        ber_values.append(ber)
        print(f"Eb/N0 = {eb_n0_db:2d} dB  =>  BER = {ber:.6f}")
    
    return ber_values


def plot_ber_comparison(eb_n0_range, ber_bpsk, ber_qpsk, ber_8psk, ber_16qam, 
                        save_path='results/modulation_comparison.png'):
    """Plot BER comparison for all modulation schemes."""
    plt.figure(figsize=(12, 8))
    
    # Plot all curves
    plt.semilogy(eb_n0_range, ber_bpsk, 'bo-', linewidth=2, markersize=8, label='BPSK')
    plt.semilogy(eb_n0_range, ber_qpsk, 'rs-', linewidth=2, markersize=8, label='QPSK')
    plt.semilogy(eb_n0_range, ber_8psk, 'g^-', linewidth=2, markersize=8, label='8-PSK')
    plt.semilogy(eb_n0_range, ber_16qam, 'md-', linewidth=2, markersize=8, label='16-QAM')
    
    # Grid
    plt.grid(True, which='both', linestyle='--', alpha=0.7)
    
    # Labels
    plt.xlabel('Eb/N0 (dB)', fontsize=14, fontweight='bold')
    plt.ylabel('Bit Error Rate (BER)', fontsize=14, fontweight='bold')
    plt.title('Modulation Performance Comparison in AWGN Channel', 
              fontsize=16, fontweight='bold')
    
    # Legend
    plt.legend(fontsize=12, loc='best')
    
    # Limits
    plt.xlim([eb_n0_range[0], eb_n0_range[-1]])
    plt.ylim([1e-6, 1])
    
    # Tight layout
    plt.tight_layout()
    
    # Save
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"\nComparison plot saved as: {save_path}")
    
    # Show
    plt.show()


def plot_constellations(save_path='results/constellations.png'):
    """Plot constellation diagrams for all modulation schemes."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 12))
    
    # Generate sample bits
    sample_bits_bpsk = gen_bites(100)
    sample_bits_qpsk = gen_bites(100)
    sample_bits_8psk = gen_bites(99)  # Multiple of 3
    sample_bits_16qam = gen_bites(100)
    
    # Modulate
    bpsk_symbols = bpsk_modulation(sample_bits_bpsk)
    qpsk_symbols = qpsk_modulation(sample_bits_qpsk)
    psk8_symbols = psk8_modulation(sample_bits_8psk)
    qam16_symbols = qam16_modulation(sample_bits_16qam)
    
    # Add noise
    eb_n0_db = 10
    bpsk_noisy = transmission_channel(bpsk_symbols, eb_n0_db)
    qpsk_noisy = transmission_channel(qpsk_symbols, eb_n0_db)
    psk8_noisy = transmission_channel(psk8_symbols, eb_n0_db)
    qam16_noisy = transmission_channel(qam16_symbols, eb_n0_db)
    
    # Plot BPSK
    ax = axes[0, 0]
    ax.scatter(bpsk_noisy.real, bpsk_noisy.imag, alpha=0.5, s=30, c='blue', label='Received')
    ax.scatter(bpsk_symbols.real, bpsk_symbols.imag, s=200, c='red', marker='x', 
               linewidths=3, label='Ideal')
    ax.set_xlabel('In-Phase (I)', fontsize=12)
    ax.set_ylabel('Quadrature (Q)', fontsize=12)
    ax.set_title('BPSK Constellation', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)
    
    # Plot QPSK
    ax = axes[0, 1]
    ax.scatter(qpsk_noisy.real, qpsk_noisy.imag, alpha=0.5, s=30, c='blue', label='Received')
    # Plot ideal constellation
    norm = 1/np.sqrt(2)
    ideal_qpsk = np.array([norm*(1+1j), norm*(-1+1j), norm*(-1-1j), norm*(1-1j)])
    ax.scatter(ideal_qpsk.real, ideal_qpsk.imag, s=200, c='red', marker='x', 
               linewidths=3, label='Ideal')
    ax.set_xlabel('In-Phase (I)', fontsize=12)
    ax.set_ylabel('Quadrature (Q)', fontsize=12)
    ax.set_title('QPSK Constellation', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)
    
    # Plot 8-PSK
    ax = axes[1, 0]
    ax.scatter(psk8_noisy.real, psk8_noisy.imag, alpha=0.5, s=30, c='blue', label='Received')
    # Plot ideal constellation
    angles = np.array([0, 1, 3, 2, 6, 7, 5, 4]) * np.pi / 4
    ideal_8psk = np.exp(1j * angles)
    ax.scatter(ideal_8psk.real, ideal_8psk.imag, s=200, c='red', marker='x', 
               linewidths=3, label='Ideal')
    ax.set_xlabel('In-Phase (I)', fontsize=12)
    ax.set_ylabel('Quadrature (Q)', fontsize=12)
    ax.set_title('8-PSK Constellation', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)
    
    # Plot 16-QAM
    ax = axes[1, 1]
    ax.scatter(qam16_noisy.real, qam16_noisy.imag, alpha=0.5, s=30, c='blue', label='Received')
    # Plot ideal constellation
    norm = 1/np.sqrt(10)
    ideal_16qam = []
    for i in [-3, -1, 1, 3]:
        for q in [-3, -1, 1, 3]:
            ideal_16qam.append(norm * (i + 1j*q))
    ideal_16qam = np.array(ideal_16qam)
    ax.scatter(ideal_16qam.real, ideal_16qam.imag, s=200, c='red', marker='x', 
               linewidths=3, label='Ideal')
    ax.set_xlabel('In-Phase (I)', fontsize=12)
    ax.set_ylabel('Quadrature (Q)', fontsize=12)
    ax.set_title('16-QAM Constellation', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)
    
    # Overall title
    fig.suptitle(f'Constellation Diagrams (Eb/N0 = {eb_n0_db} dB)', 
                 fontsize=16, fontweight='bold', y=0.995)
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Constellation plot saved as: {save_path}")
    plt.show()


def main():
    """Main function - runs complete simulation for all modulations."""
    print("=" * 70)
    print("DIGITAL MODULATION SIMULATION")
    print("BPSK, QPSK, 8-PSK, 16-QAM Performance Analysis")
    print("=" * 70)
    print()
    
    # Simulation parameters
    eb_n0_range = range(-2, 16)  # -2 dB to 15 dB
    n_bits = 10000
    
    print("Simulation Parameters:")
    print(f"  - Modulations: BPSK, QPSK, 8-PSK, 16-QAM")
    print(f"  - Number of bits: {n_bits}")
    print(f"  - Eb/N0 range: {list(eb_n0_range)} dB")
    print()
    
    # Run simulations
    print("=" * 70)
    print("Running Simulations...")
    print("=" * 70)
    print()
    
    print("[1/4] BPSK")
    ber_bpsk = simulate_bpsk(eb_n0_range, n_bits)
    print()
    
    print("[2/4] QPSK")
    ber_qpsk = simulate_qpsk(eb_n0_range, n_bits)
    print()
    
    print("[3/4] 8-PSK")
    ber_8psk = simulate_8psk(eb_n0_range, n_bits)
    print()
    
    print("[4/4] 16-QAM")
    ber_16qam = simulate_16qam(eb_n0_range, n_bits)
    print()
    
    print("=" * 70)
    print("Simulations Complete!")
    print("=" * 70)
    print()
    
    # Generate plots
    print("Generating plots...")
    print()
    
    print("[1/2] BER Comparison Plot...")
    plot_ber_comparison(eb_n0_range, ber_bpsk, ber_qpsk, ber_8psk, ber_16qam)
    print()
    
    print("[2/2] Constellation Diagrams...")
    plot_constellations()
    print()
    
    # Summary table
    print("=" * 70)
    print("PERFORMANCE SUMMARY")
    print("=" * 70)
    print()
    print("Eb/N0 (dB) | BPSK      | QPSK      | 8-PSK     | 16-QAM")
    print("-" * 70)
    
    for idx, eb_n0 in enumerate([0, 5, 10, 15]):
        if eb_n0 in eb_n0_range:
            i = list(eb_n0_range).index(eb_n0)
            print(f"  {eb_n0:2d}       | {ber_bpsk[i]:.6f} | {ber_qpsk[i]:.6f} | "
                  f"{ber_8psk[i]:.6f} | {ber_16qam[i]:.6f}")
    
    print()
    print("=" * 70)
    print("KEY OBSERVATIONS:")
    print("=" * 70)
    print("1. BPSK and QPSK have similar BER performance (same Eb/N0)")
    print("2. 8-PSK has worse BER than QPSK (symbols closer together)")
    print("3. 16-QAM requires highest SNR but offers 4 bits/symbol")
    print("4. Trade-off: spectral efficiency vs. power efficiency")
    print()
    print("=" * 70)
    print("DONE!")
    print("=" * 70)


if __name__ == "__main__":
    main()