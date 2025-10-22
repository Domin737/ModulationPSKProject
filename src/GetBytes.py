"""
GetBytes.py - Random bit generator for digital communication simulation

This module provides functionality to generate random binary bits
for testing modulation schemes.
"""

import numpy as np


def gen_bites(n_bits):
    """
    Generate random binary bits (0 or 1)
    
    Parameters:
    -----------
    n_bits : int
        Number of bits to generate
    
    Returns:
    --------
    numpy.ndarray
        Array of random bits (0s and 1s)
    
    Example:
    --------
    >>> bits = gen_bites(10)
    >>> print(bits)
    [1 0 1 1 0 1 0 0 1 1]
    """
    return np.random.randint(0, 2, size=(n_bits))


if __name__ == "__main__":
    print("=" * 60)
    print("Testing Random Bit Generation")
    print("=" * 60)
    print()
    
    # Test 1: Generate bits
    print("Test 1: Generate 20 random bits")
    print("-" * 60)
    bits = gen_bites(20)
    print(f"Generated bits: {bits}")
    print(f"Number of bits: {len(bits)}")
    print()
    
    # Test 2: Verify all values are 0 or 1
    print("Test 2: Verify all values are binary")
    print("-" * 60)
    all_binary = np.all((bits == 0) | (bits == 1))
    print(f"All values are 0 or 1: {all_binary}")
    print()
    
    # Test 3: Check distribution
    print("Test 3: Generate many bits and check distribution")
    print("-" * 60)
    many_bits = gen_bites(10000)
    ones_count = np.sum(many_bits)
    zeros_count = len(many_bits) - ones_count
    print(f"Total bits: {len(many_bits)}")
    print(f"Ones:  {ones_count} ({100*ones_count/len(many_bits):.1f}%)")
    print(f"Zeros: {zeros_count} ({100*zeros_count/len(many_bits):.1f}%)")
    print()
    
    print("=" * 60)
    print("All tests completed!")
    print("=" * 60)