"""
Test Environment Script
Sprawdza czy wszystkie wymagane biblioteki sa zainstalowane i dzialaja poprawnie
"""

import sys

def test_imports():
    """Test importu wszystkich wymaganych bibliotek"""
    print("=" * 60)
    print("TEST SRODOWISKA - ModulationPSKProject")
    print("=" * 60)
    print()
    
    tests_passed = 0
    tests_total = 0
    
    # Test 1: Python version
    tests_total += 1
    print(f"Test 1: Wersja Pythona")
    print(f"  Znaleziona wersja: {sys.version}")
    if sys.version_info >= (3, 8):
        print("  ✓ PASSED - Python 3.8+")
        tests_passed += 1
    else:
        print("  ✗ FAILED - Wymagany Python 3.8 lub nowszy")
    print()
    
    # Test 2: NumPy
    tests_total += 1
    print(f"Test 2: NumPy")
    try:
        import numpy as np
        print(f"  Znaleziona wersja: {np.__version__}")
        
        # Test podstawowej operacji
        arr = np.array([1, 2, 3])
        result = np.sum(arr)
        assert result == 6
        
        print("  ✓ PASSED - NumPy dziala poprawnie")
        tests_passed += 1
    except ImportError:
        print("  ✗ FAILED - NumPy nie jest zainstalowany")
    except Exception as e:
        print(f"  ✗ FAILED - Blad: {e}")
    print()
    
    # Test 3: SciPy
    tests_total += 1
    print(f"Test 3: SciPy")
    try:
        import scipy
        from scipy.signal.windows import cosine
        print(f"  Znaleziona wersja: {scipy.__version__}")
        
        # Test podstawowej operacji
        window = cosine(10)
        assert len(window) == 10
        
        print("  ✓ PASSED - SciPy dziala poprawnie")
        tests_passed += 1
    except ImportError:
        print("  ✗ FAILED - SciPy nie jest zainstalowany")
    except Exception as e:
        print(f"  ✗ FAILED - Blad: {e}")
    print()
    
    # Test 4: Matplotlib
    tests_total += 1
    print(f"Test 4: Matplotlib")
    try:
        import matplotlib
        import matplotlib.pyplot as plt
        print(f"  Znaleziona wersja: {matplotlib.__version__}")
        
        # Test podstawowej operacji
        fig, ax = plt.subplots()
        plt.close(fig)
        
        print("  ✓ PASSED - Matplotlib dziala poprawnie")
        tests_passed += 1
    except ImportError:
        print("  ✗ FAILED - Matplotlib nie jest zainstalowany")
    except Exception as e:
        print(f"  ✗ FAILED - Blad: {e}")
    print()
    
    # Test 5: Istniejace moduly projektu
    tests_total += 1
    print(f"Test 5: Moduly projektu")
    try:
        # Sprawdzenie czy mozna zaimportowac moduly
        import GetBytes
        import AddAWGNNoise
        import Modulator
        
        print("  Moduly znalezione:")
        print("    - GetBytes.py ✓")
        print("    - AddAWGNNoise.py ✓")
        print("    - Modulator.py ✓")
        print("  ✓ PASSED - Moduly projektu dostepne")
        tests_passed += 1
    except ImportError as e:
        print(f"  ✗ FAILED - Nie mozna zaimportowac modulow: {e}")
    except Exception as e:
        print(f"  ✗ FAILED - Blad: {e}")
    print()
    
    # Test 6: Funkcjonalny test BPSK
    tests_total += 1
    print(f"Test 6: Test funkcjonalny BPSK")
    try:
        import numpy as np
        from GetBytes import gen_bites
        from Modulator import bpsk_modulation
        from AddAWGNNoise import add_awgn_noise
        
        # Generuj bity
        bits = gen_bites(10)
        print(f"  Wygenerowano {len(bits)} bitow")
        
        # Modulacja
        symbols = bpsk_modulation(bits)
        print(f"  Zmodulowano do {len(symbols)} symboli")
        
        # Dodanie szumu
        noisy_symbols = add_awgn_noise(symbols, 10.0)
        print(f"  Dodano szum AWGN (Eb/N0 = 10 dB)")
        
        # Weryfikacja typow
        assert isinstance(symbols, np.ndarray)
        assert symbols.dtype == np.complex128
        
        print("  ✓ PASSED - Lancuch BPSK dziala poprawnie")
        tests_passed += 1
    except Exception as e:
        print(f"  ✗ FAILED - Blad: {e}")
    print()
    
    # Podsumowanie
    print("=" * 60)
    print(f"WYNIK: {tests_passed}/{tests_total} testow zakonczone sukcesem")
    print("=" * 60)
    print()
    
    if tests_passed == tests_total:
        print("✓ Wszystkie testy przeszly pomyslnie!")
        print("  Srodowisko jest poprawnie skonfigurowane.")
        print("  Mozesz przejsc do dalszego rozwoju projektu.")
        return True
    else:
        print("✗ Niektore testy nie powiodly sie.")
        print("  Sprawdz komunikaty powyzej i zainstaluj brakujace biblioteki.")
        print("  Uruchom: pip install -r requirements.txt")
        return False

if __name__ == "__main__":
    success = test_imports()
    sys.exit(0 if success else 1)
