#!/bin/bash

# ============================================================
# ModulationPSKProject - Setup Script for Linux/Mac
# Version: 1.4.0
# ============================================================

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Functions
print_success() {
    echo -e "${GREEN}SUCCESS: $1${NC}"
}

print_error() {
    echo -e "${RED}ERROR: $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}WARNING: $1${NC}"
}

print_info() {
    echo -e "${BLUE}$1${NC}"
}

# Header
echo ""
echo "============================================================"
echo "ModulationPSKProject - Environment Setup"
echo "Version: 1.4.0"
echo "============================================================"
echo ""

# [1/6] Check Python installation
print_info "[1/6] Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    print_error "Python 3 is not installed!"
    echo ""
    echo "Please install Python 3.8 or higher:"
    echo "  - Ubuntu/Debian: sudo apt-get install python3 python3-venv python3-pip"
    echo "  - Fedora/RHEL: sudo dnf install python3 python3-pip"
    echo "  - macOS: brew install python3"
    echo ""
    exit 1
fi

PYTHON_VERSION=$(python3 --version)
print_success "Found $PYTHON_VERSION"
echo ""

# Check Python version (must be 3.8+)
PYTHON_MINOR=$(python3 -c 'import sys; print(sys.version_info.minor)')
if [ "$PYTHON_MINOR" -lt 8 ]; then
    print_warning "Python version is below 3.8, some features may not work"
    echo ""
fi

# [2/6] Check requirements.txt
print_info "[2/6] Checking requirements.txt..."
if [ ! -f "requirements.txt" ]; then
    print_error "requirements.txt not found!"
    echo ""
    echo "Please make sure you are running this script from the project root directory."
    exit 1
fi
print_success "requirements.txt found"
echo ""

# [3/6] Remove old virtual environment if exists
if [ -d "venv" ]; then
    print_info "[3/6] Removing old virtual environment..."
    rm -rf venv
    print_success "Old environment removed"
    echo ""
fi

# [3/6] Create virtual environment
print_info "[3/6] Creating virtual environment..."
if ! python3 -m venv venv; then
    print_error "Failed to create virtual environment!"
    echo ""
    echo "This might be caused by:"
    echo "  - Missing python3-venv package"
    echo "  - Insufficient permissions"
    echo ""
    echo "Try installing: sudo apt-get install python3-venv (Ubuntu/Debian)"
    exit 1
fi
print_success "Virtual environment created"
echo ""

# [4/6] Activate virtual environment
print_info "[4/6] Activating virtual environment..."
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
    print_success "Virtual environment activated"
else
    print_error "Failed to find activation script!"
    exit 1
fi
echo ""

# [5/6] Upgrade pip
print_info "[5/6] Upgrading pip..."
if python -m pip install --upgrade pip --quiet; then
    print_success "pip upgraded"
else
    print_warning "Failed to upgrade pip (continuing anyway)"
fi
echo ""

# [6/6] Install dependencies
print_info "[6/6] Installing dependencies..."
echo "This may take a few minutes..."
echo ""
if pip install -r requirements.txt; then
    print_success "All dependencies installed"
else
    print_error "Failed to install dependencies!"
    echo ""
    echo "Please check your internet connection and try again."
    echo ""
    echo "If the problem persists, try installing packages manually:"
    echo "  pip install numpy scipy matplotlib"
    exit 1
fi
echo ""

# Create necessary directories
print_info "Creating project directories..."
mkdir -p results
mkdir -p docs
print_success "Directories created"
echo ""

# Verification
echo "============================================================"
echo "Verifying installation..."
echo "============================================================"
echo ""

if python -c "import numpy; print('  NumPy version:', numpy.__version__)" 2>/dev/null; then
    print_success "NumPy verified"
else
    print_warning "NumPy verification failed"
fi

if python -c "import scipy; print('  SciPy version:', scipy.__version__)" 2>/dev/null; then
    print_success "SciPy verified"
else
    print_warning "SciPy verification failed"
fi

if python -c "import matplotlib; print('  Matplotlib version:', matplotlib.__version__)" 2>/dev/null; then
    print_success "Matplotlib verified"
else
    print_warning "Matplotlib verification failed"
fi

echo ""
echo "============================================================"
echo "Setup completed successfully!"
echo "============================================================"
echo ""
echo "Next steps:"
echo ""
echo "1. Activate the virtual environment:"
echo "   source venv/bin/activate"
echo ""
echo "2. Navigate to src directory:"
echo "   cd src"
echo ""
echo "3. Run the simulation:"
echo "   python main.py"
echo ""
echo "4. To deactivate the environment:"
echo "   deactivate"
echo ""
echo "For more information, see docs/index.md"
echo "============================================================"
echo ""