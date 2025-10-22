"""
Utility functions for plotting and visualization.
"""

import numpy as np
import matplotlib.pyplot as plt
from Modulator import bpsk_modulation, qpsk_modulation, psk8_modulation, qam16_modulation
from GetBytes import gen_bites


def plot_individual_constellation(modulation_name, symbols, noisy_symbols=None, 
                                  save_path=None):
    """
    Plot single constellation diagram.
    
    Parameters
    ----------
    modulation_name : str
        Name of modulation (e.g., 'BPSK', 'QPSK')
    symbols : numpy.ndarray
        Ideal constellation symbols
    noisy_symbols : numpy.ndarray, optional
        Received symbols with noise
    save_path : str, optional
        Path to save the figure
    """
    plt.figure(figsize=(8, 8))
    
    # Plot noisy symbols if provided
    if noisy_symbols is not None:
        plt.scatter(noisy_symbols.real, noisy_symbols.imag, 
                   alpha=0.5, s=30, c='blue', label='Received (with noise)')
    
    # Plot ideal constellation
    unique_symbols = np.unique(symbols)
    plt.scatter(unique_symbols.real, unique_symbols.imag, 
               s=300, c='red', marker='x', linewidths=4, label='Ideal constellation')
    
    # Labels and title
    plt.xlabel('In-Phase (I)', fontsize=14)
    plt.ylabel('Quadrature (Q)', fontsize=14)
    plt.title(f'{modulation_name} Constellation Diagram', fontsize=16, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=12)
    
    # Equal aspect ratio
    plt.axis('equal')
    
    # Add axes through origin
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.axvline(x=0, color='k', linewidth=0.5)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Saved: {save_path}")
    
    plt.show()


def compare_spectral_efficiency():
    """
    Create a bar chart comparing spectral efficiency of different modulations.
    """
    modulations = ['BPSK', 'QPSK', '8-PSK', '16-QAM']
    bits_per_symbol = [1, 2, 3, 4]
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(modulations, bits_per_symbol, color=['blue', 'green', 'orange', 'red'], 
                   alpha=0.7, edgecolor='black', linewidth=2)
    
    # Add value labels on bars
    for bar, value in zip(bars, bits_per_symbol):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{value} bits/symbol',
                ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    plt.xlabel('Modulation Scheme', fontsize=14, fontweight='bold')
    plt.ylabel('Bits per Symbol', fontsize=14, fontweight='bold')
    plt.title('Spectral Efficiency Comparison', fontsize=16, fontweight='bold')
    plt.ylim([0, 5])
    plt.grid(True, axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('results/spectral_efficiency.png', dpi=300, bbox_inches='tight')
    print("Saved: results/spectral_efficiency.png")
    plt.show()


if __name__ == "__main__":
    print("Plotting utilities - demonstration")
    print()
    
    # Generate sample data
    bits = gen_bites(100)
    bpsk_sym = bpsk_modulation(bits)
    
    # Plot single constellation
    print("Plotting BPSK constellation...")
    plot_individual_constellation('BPSK', bpsk_sym, 
                                  save_path='results/bpsk_constellation_demo.png')
    
    # Spectral efficiency comparison
    print("\nPlotting spectral efficiency comparison...")
    compare_spectral_efficiency()
    
    print("\nDone!")