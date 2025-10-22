# Technical Code Documentation

Reference manual for ModulationPSKProject codebase.
Line-by-line analysis of all functions with technical details.

---

## GetBytes.py

### `gen_bites(n_bits)`

**Purpose:** Generate random binary bits (0 or 1)

**Parameters:**

- `n_bits` (int): Number of bits to generate

**Returns:** `np.ndarray` of shape (n_bits,) with dtype int64, values in {0, 1}

**Dependencies:** numpy.random.randint

**Time complexity:** O(n)

**Space complexity:** O(n)

**Line-by-line:**

```python
def gen_bites(n_bits):
    return np.random.randint(0, 2, size=n_bits)
    # np.random.randint(low, high, size):
    #   - low=0: inclusive lower bound
    #   - high=2: exclusive upper bound -> generates {0, 1}
    #   - size=n_bits: output array length
    # Returns: ndarray of random integers
```

**Example:**

```python
bits = gen_bites(10)  # array([1, 0, 1, 1, 0, ...])
```

**Notes:**

- Name typo: "bites" should be "bits" (kept for backward compatibility)
- Each call produces different random sequence
- Uses numpy's Mersenne Twister PRNG

---

## Modulator.py

### `bpsk_modulation(bits)`

**Purpose:** Map binary bits to BPSK constellation symbols

**Parameters:**

- `bits` (np.ndarray): Binary array of 0s and 1s

**Returns:** `np.ndarray` of dtype complex128, values in {-1+0j, 1+0j}

**Dependencies:** None (pure numpy operations)

**Time complexity:** O(n) where n = len(bits)

**Space complexity:** O(n)

**Line-by-line:**

```python
def bpsk_modulation(bits):
    symbols = 1 - 2 * bits
    # Arithmetic mapping:
    #   bit=0: 1 - 2*0 = 1
    #   bit=1: 1 - 2*1 = -1
    # Vectorized operation (no loop)

    return symbols.astype(complex)
    # Cast to complex128
    # Real part = symbol value
    # Imaginary part = 0
    # Reason: Uniform interface with other modulations (QPSK, QAM use complex)
```

**Example:**

```python
symbols = bpsk_modulation(np.array([0, 1, 0]))  # [1+0j, -1+0j, 1+0j]
```

**Notes:**

- Energy per symbol: |s|² = 1
- No normalization needed
- Unused imports in original file (scipy.signal.windows.cosine, main)

---

### `qpsk_modulation(bits)`

**Purpose:** Map bit pairs to QPSK constellation symbols with Gray coding

**Parameters:**

- `bits` (np.ndarray): Binary array, length must be even

**Returns:** `np.ndarray` of dtype complex128, length = len(bits)/2

**Dependencies:** None

**Time complexity:** O(n) where n = len(bits)

**Space complexity:** O(n/2)

**Raises:** `ValueError` if len(bits) is odd

**Line-by-line:**

```python
def qpsk_modulation(bits):
    if len(bits) % 2 != 0:
        raise ValueError("Number of bits must be even for QPSK")
    # Validation: QPSK requires 2 bits per symbol

    bit_pairs = bits.reshape(-1, 2)
    # Reshape to (n/2, 2) array
    # -1 infers dimension automatically
    # Each row = one symbol's bit pair

    norm = 1 / np.sqrt(2)
    # Normalization factor
    # Ensures E[|s|²] = 1
    # Without: |1+1j|² = 2, With: |(1+1j)/√2|² = 1

    qpsk_map = {
        (0, 0): norm * (1 + 1j),   # 45°
        (0, 1): norm * (-1 + 1j),  # 135°
        (1, 1): norm * (-1 - 1j),  # 225°
        (1, 0): norm * (1 - 1j)    # 315°
    }
    # Gray coding: adjacent symbols differ by 1 bit
    # Dictionary for O(1) lookup

    symbols = np.array([qpsk_map[tuple(pair)] for pair in bit_pairs], dtype=complex)
    # List comprehension over bit_pairs
    # tuple() converts ndarray row to hashable key
    # dtype=complex explicit to avoid promotion issues

    return symbols
```

**Example:**

```python
symbols = qpsk_modulation(np.array([0,0,1,1]))  # [0.707+0.707j, -0.707-0.707j]
```

**Notes:**

- All symbols have equal magnitude: |s| = 1
- Dictionary lookup O(1), alternative: indexing into constellation array

---

### `psk8_modulation(bits)`

**Purpose:** Map bit triplets to 8-PSK constellation symbols with Gray coding

**Parameters:**

- `bits` (np.ndarray): Binary array, length must be multiple of 3

**Returns:** `np.ndarray` of dtype complex128, length = len(bits)/3

**Dependencies:** None

**Time complexity:** O(n) where n = len(bits)

**Space complexity:** O(n/3)

**Raises:** `ValueError` if len(bits) % 3 != 0

**Line-by-line:**

```python
def psk8_modulation(bits):
    if len(bits) % 3 != 0:
        raise ValueError("Number of bits must be multiple of 3 for 8-PSK")
    # Validation: 3 bits per symbol

    bit_triplets = bits.reshape(-1, 3)
    # Reshape to (n/3, 3) array

    angles = np.array([0, 1, 3, 2, 6, 7, 5, 4]) * np.pi / 4
    # Gray coding sequence for 8-PSK
    # Indices [0,1,3,2,6,7,5,4] not [0,1,2,3,4,5,6,7]
    # Adjacent angles differ by 1 bit in binary representation
    # Multiply by π/4: angles = [0°, 45°, 90°, 135°, 180°, 225°, 270°, 315°]

    constellation = np.exp(1j * angles)
    # Euler's formula: e^(jθ) = cos(θ) + j*sin(θ)
    # Creates 8 equally-spaced points on unit circle
    # All have magnitude = 1

    symbol_indices = bit_triplets[:, 0] * 4 + bit_triplets[:, 1] * 2 + bit_triplets[:, 2]
    # Binary to decimal conversion
    # bit0*2² + bit1*2¹ + bit2*2⁰
    # Vectorized for all triplets

    symbols = constellation[symbol_indices]
    # Index into constellation using computed indices
    # Advanced indexing: O(n)

    return symbols
```

**Example:**

```python
symbols = psk8_modulation(np.array([0,0,0,1,1,1]))  # [1+0j, -0.707-0.707j]
```

**Notes:**

- Unit energy: |s|² = 1 for all symbols
- Gray coding reduces bit error propagation

---

### `qam16_modulation(bits)`

**Purpose:** Map bit quadruplets to 16-QAM constellation symbols with Gray coding

**Parameters:**

- `bits` (np.ndarray): Binary array, length must be multiple of 4

**Returns:** `np.ndarray` of dtype complex128, length = len(bits)/4

**Dependencies:** None

**Time complexity:** O(n) where n = len(bits)

**Space complexity:** O(n/4)

**Raises:** `ValueError` if len(bits) % 4 != 0

**Line-by-line:**

```python
def qam16_modulation(bits):
    if len(bits) % 4 != 0:
        raise ValueError("Number of bits must be multiple of 4 for 16-QAM")
    # Validation: 4 bits per symbol

    bit_groups = bits.reshape(-1, 4)
    # Reshape to (n/4, 4) array

    i_bits = bit_groups[:, 0:2]
    q_bits = bit_groups[:, 2:4]
    # Split each 4-bit group:
    #   First 2 bits -> I component (real)
    #   Last 2 bits -> Q component (imaginary)

    pam4_map = {
        (0, 0): -3,
        (0, 1): -1,
        (1, 1): +1,
        (1, 0): +3
    }
    # PAM-4 (4-level Pulse Amplitude Modulation) with Gray coding
    # Maps 2 bits to one of 4 amplitude levels
    # Gray coding: adjacent levels differ by 1 bit

    i_components = np.array([pam4_map[tuple(pair)] for pair in i_bits])
    q_components = np.array([pam4_map[tuple(pair)] for pair in q_bits])
    # Map I and Q bit pairs independently
    # List comprehension + dictionary lookup

    symbols = i_components + 1j * q_components
    # Construct complex symbols
    # Real part = I component
    # Imaginary part = Q component

    norm = 1 / np.sqrt(10)
    symbols = symbols * norm
    # Normalization factor for unit average energy
    # E[|s|²] = (4*18 + 8*10 + 4*2)/16 = 10 before normalization
    # After: 10 * (1/√10)² = 10 * 1/10 = 1

    return symbols
```

**Example:**

```python
symbols = qam16_modulation(np.array([0,0,0,0,1,0,1,0]))  # [-0.949-0.949j, 0.949-0.316j]
```

**Notes:**

- Non-constant envelope (amplitude varies)
- Levels {-3,-1,+1,+3} chosen for Gray coding and symmetric thresholds
- Average energy = 1 after normalization

---

## AddAWGNNoise.py

### `add_awgn_noise(symbols, eb_n0_db)`

**Purpose:** Add complex AWGN noise to modulated symbols

**Parameters:**

- `symbols` (np.ndarray[complex]): Input symbols
- `eb_n0_db` (float): Energy per bit to noise ratio in dB

**Returns:** `np.ndarray[complex]` of same shape as input, symbols + noise

**Dependencies:** numpy.random.normal

**Time complexity:** O(n) where n = len(symbols)

**Space complexity:** O(n)

**Line-by-line:**

```python
def add_awgn_noise(symbols, eb_n0_db):
    eb_n0 = 10 ** (eb_n0_db / 10.0)
    # Convert dB to linear scale
    # Formula: linear = 10^(dB/10)
    # Example: 10 dB -> 10^(10/10) = 10

    eb = 1.0
    # Normalized energy per bit
    # Assumption: symbols are already normalized to unit energy

    n0 = eb / eb_n0
    # Noise power spectral density
    # N0 = Eb / (Eb/N0)
    # Higher Eb/N0 -> lower N0 -> less noise

    sigma = np.sqrt(n0 / 2)
    # Standard deviation for each noise component (I and Q)
    # Divide by 2 because noise is split between I and Q
    # Total noise power = σ²_I + σ²_Q = 2*σ² = N0

    n_symbols = symbols.shape[0]
    # Get array length
    # Use .shape[0] not len() for consistency with multidimensional arrays

    noise_i = sigma * np.random.normal(0, 1, size=n_symbols)
    # In-phase noise component
    # normal(mean=0, std=1, size): standard normal distribution
    # Multiply by sigma to scale

    noise_q = sigma * np.random.normal(0, 1, size=n_symbols)
    # Quadrature noise component
    # Independent from noise_i

    awgn_noise = noise_i + 1j * noise_q
    # Construct complex noise
    # Real part = I noise
    # Imaginary part = Q noise

    received_symbols = symbols + awgn_noise
    # Additive noise model: y = s + n
    # Vectorized addition

    return received_symbols
```

**Example:**

```python
noisy = add_awgn_noise(np.array([1+0j, -1+0j]), eb_n0_db=10)
# noisy ≈ [1.05+0.12j, -0.93-0.08j]
```

**Notes:**

- Each call generates different noise (random)
- Noise is Gaussian: mean=0, variance=σ²
- Complex noise: both I and Q are independent Gaussian

---

## TransmissionChannel.py

### `transmission_channel(symbols, eb_n0_db)`

**Purpose:** Simulate transmission through AWGN channel

**Parameters:**

- `symbols` (np.ndarray[complex]): Transmitted symbols
- `eb_n0_db` (float): Channel quality in dB

**Returns:** `np.ndarray[complex]` received symbols with noise

**Dependencies:** add_awgn_noise (from AddAWGNNoise)

**Time complexity:** O(n) where n = len(symbols)

**Space complexity:** O(n)

**Line-by-line:**

```python
def transmission_channel(symbols, eb_n0_db):
    received_symbols = add_awgn_noise(symbols, eb_n0_db)
    # Delegate to noise generation function
    # Simple wrapper for extensibility

    return received_symbols
```

**Example:**

```python
received = transmission_channel(symbols, eb_n0_db=5)
```

**Notes:**

- Minimal implementation for basic AWGN channel
- Easily extensible: add fading, frequency offset, etc.
- Separation of concerns: channel ≠ noise generation

---

## Demodulator.py

### `bpsk_demodulation(received_symbols)`

**Purpose:** Demodulate BPSK symbols to bits using threshold detection

**Parameters:**

- `received_symbols` (np.ndarray[complex]): Received noisy symbols

**Returns:** `np.ndarray[int]` of shape (n,), values in {0, 1}

**Dependencies:** None

**Time complexity:** O(n)

**Space complexity:** O(n)

**Line-by-line:**

```python
def bpsk_demodulation(received_symbols):
    decoded_bits = (received_symbols.real < 0).astype(int)
    # Threshold detection on real component:
    #   Re(symbol) < 0 -> bit = 1
    #   Re(symbol) >= 0 -> bit = 0
    # Comparison returns boolean array
    # .astype(int): False->0, True->1
    # Vectorized: no loop

    return decoded_bits
```

**Example:**

```python
bits = bpsk_demodulation(np.array([0.95+0.1j, -1.05-0.2j]))  # [0, 1]
```

**Notes:**

- Ignores imaginary part (BPSK is real-valued)
- Decision threshold = 0
- Optimal for AWGN channel (Maximum Likelihood)

---

### `qpsk_demodulation(received_symbols)`

**Purpose:** Demodulate QPSK symbols to bits using quadrant detection

**Parameters:**

- `received_symbols` (np.ndarray[complex]): Received noisy symbols

**Returns:** `np.ndarray[int]` of shape (2\*n,), values in {0, 1}

**Dependencies:** None

**Time complexity:** O(n) where n = len(received_symbols)

**Space complexity:** O(2n)

**Line-by-line:**

```python
def qpsk_demodulation(received_symbols):
    n_symbols = len(received_symbols)
    bits = np.zeros(n_symbols * 2, dtype=int)
    # Preallocate output array
    # Length = 2 * number of symbols (2 bits per symbol)

    i_component = received_symbols.real
    q_component = received_symbols.imag
    # Extract I and Q components
    # .real and .imag are O(1) views, not copies

    for idx, (i, q) in enumerate(zip(i_component, q_component)):
        # Iterate over I and Q pairs
        # zip() creates iterator of tuples
        # enumerate() adds index

        if i >= 0 and q >= 0:      # Quadrant I
            bits[2*idx:2*idx+2] = [0, 0]
        elif i < 0 and q >= 0:     # Quadrant II
            bits[2*idx:2*idx+2] = [0, 1]
        elif i < 0 and q < 0:      # Quadrant III
            bits[2*idx:2*idx+2] = [1, 1]
        else:                       # Quadrant IV (i >= 0, q < 0)
            bits[2*idx:2*idx+2] = [1, 0]
        # Decision regions based on sign of I and Q
        # Gray coding preserved
        # Slice assignment: bits[start:end] = [b0, b1]

    return bits
```

**Example:**

```python
bits = qpsk_demodulation(np.array([0.8+0.7j, -0.6-0.9j]))  # [0,0,1,1]
```

**Notes:**

- Loop-based (not vectorized) for clarity
- Could be optimized with boolean indexing
- Decision boundaries at I=0, Q=0

---

### `psk8_demodulation(received_symbols)`

**Purpose:** Demodulate 8-PSK symbols using minimum distance detection

**Parameters:**

- `received_symbols` (np.ndarray[complex]): Received noisy symbols

**Returns:** `np.ndarray[int]` of shape (3\*n,), values in {0, 1}

**Dependencies:** None

**Time complexity:** O(8n) = O(n) where n = len(received_symbols)

**Space complexity:** O(3n)

**Line-by-line:**

```python
def psk8_demodulation(received_symbols):
    angles = np.array([0, 1, 3, 2, 6, 7, 5, 4]) * np.pi / 4
    constellation = np.exp(1j * angles)
    # Create reference constellation
    # Same as in modulator (Gray coding)
    # Could be precomputed for efficiency

    n_symbols = len(received_symbols)
    bits = np.zeros(n_symbols * 3, dtype=int)
    # Preallocate: 3 bits per symbol

    for idx, symbol in enumerate(received_symbols):
        # Iterate over received symbols

        distances = np.abs(symbol - constellation)
        # Compute Euclidean distance to all 8 constellation points
        # np.abs() for complex = sqrt(Re²+Im²)
        # Vectorized over constellation (8 distances computed)

        closest_idx = np.argmin(distances)
        # Find index of minimum distance
        # Maximum Likelihood (ML) detection for AWGN
        # O(8) operation

        bit0 = (closest_idx >> 2) & 1
        bit1 = (closest_idx >> 1) & 1
        bit2 = closest_idx & 1
        # Binary decomposition of index
        # >> : right shift (divide by 2^k)
        # & 1 : extract LSB
        # Example: idx=5 (101 binary)
        #   bit0 = (101 >> 2) & 1 = 001 & 1 = 1
        #   bit1 = (101 >> 1) & 1 = 010 & 1 = 0
        #   bit2 = 101 & 1 = 1

        bits[3*idx:3*idx+3] = [bit0, bit1, bit2]
        # Store 3 bits in output array

    return bits
```

**Example:**

```python
bits = psk8_demodulation(np.array([0.95+0.1j, -0.7-0.7j]))  # [0,0,1,1,1,0]
```

**Notes:**

- Minimum distance = Maximum Likelihood for equal-probability symbols
- Alternative: phase-based detection (compute angle, discretize)
- Complexity: O(8n) for 8 distance computations per symbol

---

### `qam16_demodulation(received_symbols)`

**Purpose:** Demodulate 16-QAM symbols using threshold detection on I and Q

**Parameters:**

- `received_symbols` (np.ndarray[complex]): Received noisy symbols (normalized)

**Returns:** `np.ndarray[int]` of shape (4\*n,), values in {0, 1}

**Dependencies:** None

**Time complexity:** O(n)

**Space complexity:** O(4n)

**Line-by-line:**

```python
def qam16_demodulation(received_symbols):
    norm = np.sqrt(10)
    denorm_symbols = received_symbols * norm
    # Denormalize symbols
    # Reverse the normalization from modulator (1/√10)
    # Now symbols are at levels {-3,-1,+1,+3} for I and Q

    n_symbols = len(received_symbols)
    bits = np.zeros(n_symbols * 4, dtype=int)
    # Preallocate: 4 bits per symbol

    def pam4_demod(value):
        # Nested helper function
        # Demodulate single PAM-4 value to 2 bits

        if value < -2:
            return [0, 0]  # Level -3
        elif value < 0:
            return [0, 1]  # Level -1
        elif value < 2:
            return [1, 1]  # Level +1
        else:
            return [1, 0]  # Level +3
        # Threshold detection with thresholds at -2, 0, +2
        # Gray coding: adjacent levels differ by 1 bit

    for idx, symbol in enumerate(denorm_symbols):
        # Iterate over symbols

        i_bits = pam4_demod(symbol.real)
        q_bits = pam4_demod(symbol.imag)
        # Demodulate I and Q independently
        # Each produces 2 bits

        bits[4*idx:4*idx+4] = i_bits + q_bits
        # Concatenate I and Q bits
        # List addition: [a,b] + [c,d] = [a,b,c,d]
        # Store 4 bits in output

    return bits
```

**Example:**

```python
bits = qam16_demodulation(np.array([0.95+0.32j, -0.32-0.95j]))  # [1,1,1,1,0,1,0,0]
```

**Notes:**

- Independent demodulation of I and Q (simplified ML)
- Thresholds at midpoints: -2, 0, +2
- Nested function for code reuse

---

## main.py

### `calculate_ber(original_bits, decoded_bits)`

**Purpose:** Calculate Bit Error Rate

**Parameters:**

- `original_bits` (np.ndarray[int]): Transmitted bits
- `decoded_bits` (np.ndarray[int]): Received bits

**Returns:** `float` in [0, 1], BER value

**Dependencies:** None

**Time complexity:** O(n) where n = len(bits)

**Space complexity:** O(n) temporary for comparison

**Line-by-line:**

```python
def calculate_ber(original_bits, decoded_bits):
    errors = np.sum(original_bits != decoded_bits)
    # Element-wise comparison: != returns boolean array
    # True where bits differ
    # np.sum() counts True values (True=1, False=0)
    # Vectorized comparison and sum

    ber = errors / len(original_bits)
    # BER = number_of_errors / total_bits
    # Float division

    return ber
```

**Example:**

```python
ber = calculate_ber(np.array([0,1,0]), np.array([0,1,1]))  # 0.333...
```

**Notes:**

- Assumes equal-length arrays (no validation)
- BER ∈ [0, 1] where 0=perfect, 1=all wrong

---

### `simulate_bpsk(eb_n0_range, n_bits=10000)`

**Purpose:** Run full BPSK simulation over range of Eb/N0 values

**Parameters:**

- `eb_n0_range` (iterable): Eb/N0 values in dB to simulate
- `n_bits` (int): Number of bits per simulation

**Returns:** `list[float]` BER values corresponding to each Eb/N0

**Dependencies:**

- gen_bites (GetBytes)
- bpsk_modulation (Modulator)
- transmission_channel (TransmissionChannel)
- bpsk_demodulation (Demodulator)
- calculate_ber (main)

**Time complexity:** O(k\*n) where k=len(eb_n0_range), n=n_bits

**Space complexity:** O(n)

**Line-by-line:**

```python
def simulate_bpsk(eb_n0_range, n_bits=10000):
    ber_values = []
    # Accumulator list for BER results

    for eb_n0_db in eb_n0_range:
        # Iterate over SNR values

        bits = gen_bites(n_bits)
        # Generate fresh random bits for each Eb/N0
        # Ensures independent trials

        symbols = bpsk_modulation(bits)
        # Modulate bits to BPSK symbols

        received_symbols = transmission_channel(symbols, eb_n0_db)
        # Pass through AWGN channel
        # Different noise for each Eb/N0

        decoded_bits = bpsk_demodulation(received_symbols)
        # Demodulate received symbols

        ber = calculate_ber(bits, decoded_bits)
        # Compare original and decoded

        ber_values.append(ber)
        # Store BER for this Eb/N0

    return ber_values
```

**Example:**

```python
ber_list = simulate_bpsk(range(0, 11), n_bits=1000)  # [0.087, 0.023, ...]
```

**Notes:**

- New random bits per iteration (not same bits at different noise levels)
- Sequential processing (not parallelized)
- Similar functions exist: simulate_qpsk, simulate_8psk, simulate_16qam

---

### `plot_ber_comparison(eb_n0_range, ber_bpsk, ber_qpsk, ber_8psk, ber_16qam)`

**Purpose:** Generate comparison plot of BER curves for all modulations

**Parameters:**

- `eb_n0_range` (iterable): X-axis values (Eb/N0 in dB)
- `ber_*` (list[float]): Y-axis values (BER) for each modulation

**Returns:** None (saves plot to file and displays)

**Dependencies:**

- matplotlib.pyplot
- get_results_path (main)

**Side effects:**

- Saves PNG file to results/modulation_comparison.png
- Opens plot window (if GUI available)

**Line-by-line:**

```python
def plot_ber_comparison(eb_n0_range, ber_bpsk, ber_qpsk, ber_8psk, ber_16qam):
    results_dir = get_results_path()
    save_path = results_dir / 'modulation_comparison.png'
    # Construct save path using pathlib

    plt.figure(figsize=(12, 8))
    # Create figure with specified size in inches

    plt.semilogy(eb_n0_range, ber_bpsk, 'bo-', linewidth=2, markersize=8, label='BPSK')
    # semilogy: linear x-axis, logarithmic y-axis
    # 'bo-': blue color, circle markers, solid line
    # Repeat for other modulations...

    plt.grid(True, which='both', linestyle='--', alpha=0.7)
    # which='both': major and minor grid lines
    # alpha=0.7: semi-transparent

    plt.xlabel('Eb/N0 (dB)', fontsize=14, fontweight='bold')
    plt.ylabel('Bit Error Rate (BER)', fontsize=14, fontweight='bold')
    # Axis labels with styling

    plt.title('Modulation Performance Comparison in AWGN Channel',
              fontsize=16, fontweight='bold')
    # Plot title

    plt.legend(fontsize=12, loc='best')
    # loc='best': automatically choose position

    plt.xlim([eb_n0_range[0], eb_n0_range[-1]])
    plt.ylim([1e-6, 1])
    # Set axis limits
    # ylim logarithmic: 10^-6 to 10^0

    plt.tight_layout()
    # Adjust spacing to prevent label cutoff

    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    # Save to file
    # dpi=300: high resolution
    # bbox_inches='tight': crop whitespace

    plt.show()
    # Display plot (blocking call if GUI)
```

**Example:**

```python
plot_ber_comparison(range(0,11), ber1, ber2, ber3, ber4)
# Creates and displays comparison plot
```

**Notes:**

- Uses semilogy for exponential BER range (10^0 to 10^-6)
- Results directory created if doesn't exist (via get_results_path)

---

### `get_results_path()`

**Purpose:** Determine and create results directory path (cross-platform)

**Parameters:** None

**Returns:** `pathlib.Path` object pointing to results directory

**Dependencies:** pathlib.Path

**Side effects:** Creates results/ directory if it doesn't exist

**Time complexity:** O(1)

**Space complexity:** O(1)

**Line-by-line:**

```python
def get_results_path():
    script_dir = Path(__file__).parent.resolve()
    # __file__: path to current script
    # .parent: directory containing script
    # .resolve(): absolute path (resolves symlinks)

    if script_dir.name == 'src':
        # Check if running from src/ subdirectory
        # .name: last component of path

        results_dir = script_dir.parent / 'results'
        # Go up one level, then down to results/
        # Operator /: path concatenation
    else:
        results_dir = script_dir / 'results'
        # Already in project root

    results_dir.mkdir(parents=True, exist_ok=True)
    # Create directory
    # parents=True: create parent directories if needed
    # exist_ok=True: no error if already exists

    return results_dir
```

**Example:**

```python
path = get_results_path()  # Path('/project/results')
```

**Notes:**

- Handles two execution contexts: src/ and project root
- pathlib preferred over os.path (more Pythonic, cross-platform)
- Safe: mkdir with exist_ok=True is idempotent

---

### `plot_constellations()`

**Purpose:** Generate subplot with constellation diagrams for all modulations

**Parameters:** None

**Returns:** None (saves plot to file and displays)

**Dependencies:**

- All modulation functions
- transmission_channel
- gen_bites
- matplotlib

**Side effects:**

- Saves PNG file to results/constellations.png
- Opens plot window

**Line-by-line (key parts):**

```python
def plot_constellations():
    results_dir = get_results_path()
    save_path = results_dir / 'constellations.png'

    fig, axes = plt.subplots(2, 2, figsize=(12, 12))
    # Create 2x2 grid of subplots
    # axes: 2D array of subplot objects

    # Generate and modulate sample bits
    sample_bits_bpsk = gen_bites(100)
    bpsk_symbols = bpsk_modulation(sample_bits_bpsk)
    # ... (similar for other modulations)

    # Add noise at fixed Eb/N0
    eb_n0_db = 10
    bpsk_noisy = transmission_channel(bpsk_symbols, eb_n0_db)
    # ... (similar for others)

    # Plot BPSK
    ax = axes[0, 0]
    # Access subplot: axes[row, col]

    ax.scatter(bpsk_noisy.real, bpsk_noisy.imag, alpha=0.5, s=30, c='blue', label='Received')
    # Scatter plot: x=real, y=imag
    # alpha=0.5: semi-transparent
    # s=30: marker size

    ax.scatter(bpsk_symbols.real, bpsk_symbols.imag, s=200, c='red', marker='x',
               linewidths=3, label='Ideal')
    # Overlay ideal constellation points
    # marker='x': X markers
    # linewidths=3: thick lines

    ax.set_xlabel('In-Phase (I)', fontsize=12)
    ax.set_ylabel('Quadrature (Q)', fontsize=12)
    ax.set_title('BPSK Constellation', fontsize=14, fontweight='bold')
    # Axis labels and title

    ax.grid(True, alpha=0.3)
    ax.legend()
    # Grid and legend

    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    # Fixed axis limits for comparison

    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)
    # Draw axes through origin

    # ... (repeat for QPSK, 8-PSK, QAM in other subplots)

    fig.suptitle(f'Constellation Diagrams (Eb/N0 = {eb_n0_db} dB)',
                 fontsize=16, fontweight='bold', y=0.995)
    # Overall figure title
    # y=0.995: vertical position (near top)

    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()
```

**Notes:**

- Fixed Eb/N0=10dB for all constellations (consistent comparison)
- Blue dots: received noisy symbols
- Red X: ideal constellation points
- Shows effect of noise visually

---

### `main()`

**Purpose:** Entry point - orchestrates complete simulation pipeline

**Parameters:** None

**Returns:** None

**Dependencies:** All simulation and plotting functions

**Side effects:**

- Prints progress to stdout
- Saves plots to files
- May take several minutes to complete

**Line-by-line (structure):**

```python
def main():
    results_dir = get_results_path()
    # Ensure results directory exists

    # Print header
    print("=" * 70)
    print("DIGITAL MODULATION SIMULATION")
    # ... informational output

    # Parameters
    eb_n0_range = range(-2, 16)  # -2 to 15 dB
    n_bits = 10000
    # Configuration

    # Run simulations
    ber_bpsk = simulate_bpsk(eb_n0_range, n_bits)
    ber_qpsk = simulate_qpsk(eb_n0_range, n_bits)
    ber_8psk = simulate_8psk(eb_n0_range, n_bits)
    ber_16qam = simulate_16qam(eb_n0_range, n_bits)
    # Each simulation returns list of BER values
    # Sequential execution (not parallel)

    # Generate plots
    plot_ber_comparison(eb_n0_range, ber_bpsk, ber_qpsk, ber_8psk, ber_16qam)
    plot_constellations()

    # Print summary table
    # ... (formatted output)

if __name__ == "__main__":
    main()
    # Execute only if script run directly (not imported)
```

**Notes:**

- Single-threaded (could parallelize simulations)
- Progress printed to console
- Total runtime: ~30-60 seconds depending on n_bits

---

## Performance Characteristics

### Memory usage

- Dominated by symbol arrays: O(n_bits) where n_bits typically 10000
- Each complex128 symbol: 16 bytes
- Total: ~160 KB for main arrays + overhead

### Computational bottlenecks

1. **Noise generation**: `np.random.normal()` - cannot vectorize further
2. **QAM demodulation**: Loop-based (not vectorized)
3. **8-PSK demodulation**: 8 distance calculations per symbol

### Optimization opportunities

1. Vectorize QAM demodulation (boolean indexing)
2. Precompute 8-PSK constellation (currently recomputed)
3. Parallelize simulations across Eb/N0 values (multiprocessing)
4. Use numba JIT for hot loops

---

## Common Pitfalls

### Array length mismatches

- QPSK requires even number of bits
- 8-PSK requires multiple of 3
- QAM requires multiple of 4
  **Solution:** Validate or pad bits before modulation

### Type issues

- Ensure complex dtype: `.astype(complex)`
- Mixing float32 and float64 can cause precision loss
  **Solution:** Explicit dtype specifications

### Random seed

- No seed set → non-reproducible results
  **Solution:** `np.random.seed(42)` at start of simulation

### Normalization

- Forgetting to denormalize in QAM demodulation
- Wrong normalization factor
  **Solution:** Verify E[|s|²] = 1 after modulation

---

## Testing Recommendations

### Unit tests

```python
def test_bpsk_zero_noise():
    bits = np.array([0, 1, 0, 1])
    symbols = bpsk_modulation(bits)
    # No noise: eb_n0_db = inf (use very high value)
    received = transmission_channel(symbols, eb_n0_db=50)
    decoded = bpsk_demodulation(received)
    assert np.array_equal(bits, decoded)  # Should be perfect
```

### Integration tests

```python
def test_full_pipeline():
    ber = simulate_bpsk([10], n_bits=10000)[0]
    assert 0 < ber < 0.001  # Typical BER at 10 dB
```

### Edge cases

- Single bit: `gen_bites(1)`
- Empty array: `gen_bites(0)` (should handle gracefully)
- Very high noise: `eb_n0_db = -10` (BER → 0.5)
- Perfect channel: `eb_n0_db = 100` (BER → 0)

---

## End of Technical Documentation

This reference covers all functions with line-by-line analysis.
For conceptual understanding, see `code-documentation.md`.
For theory, see `theoretical-background.md`.
