"""
Module for generating random binary bits.
Used as input data for modulation simulations.
"""

import numpy as np


def gen_bites(n_bits):
    """
    Generate random binary bits (0 or 1).
    
    Note: Function name contains typo 'bites' instead of 'bits',
    kept for consistency with existing codebase.
    
    Parameters
    ----------
    n_bits : int
        Number of random bits to generate
    
    Returns
    -------
    numpy.ndarray
        Array of random binary values (0s and 1s)
    
    Examples
    --------
    >>> bits = gen_bites(10)
    >>> print(bits)
    [1 0 1 1 0 1 0 0 1 1]
    >>> len(bits)
    10
    """
    return np.random.randint(0, 2, size=n_bits)


if __name__ == "__main__":
    # This code runs ONLY when you execute this file directly
    # Not when you import it in another file
    print("=" * 60)
    print("Testing GetBytes.py")
    print("=" * 60)
    
    # Generate 20 random bits
    test_bits = gen_bites(20)
    print(f"\nGenerated bits:\n{test_bits}")
    print(f"\nNumber of bits: {len(test_bits)}")
    print(f"Number of 1s: {np.sum(test_bits)}")
    print(f"Number of 0s: {len(test_bits) - np.sum(test_bits)}")