#!/bin/bash

echo "=========================================="
echo "Konfiguracja srodowiska Python"
echo "ModulationPSKProject"
echo "=========================================="
echo ""

# Sprawdzenie wersji Pythona
echo "Sprawdzanie wersji Pythona..."
python3 --version

# Tworzenie wirtualnego srodowiska
echo ""
echo "Tworzenie wirtualnego srodowiska..."
python3 -m venv venv

# Aktywacja wirtualnego srodowiska
echo ""
echo "Aktywacja wirtualnego srodowiska..."
source venv/bin/activate

# Aktualizacja pip
echo ""
echo "Aktualizacja pip..."
pip install --upgrade pip

# Instalacja zaleznosci
echo ""
echo "Instalacja zaleznosci z requirements.txt..."
pip install -r requirements.txt

echo ""
echo "=========================================="
echo "Konfiguracja zakonczona pomyslnie!"
echo "=========================================="
echo ""
echo "Aby aktywowac srodowisko uruchom:"
echo "source venv/bin/activate"
echo ""
echo "Aby dezaktywowac srodowisko uruchom:"
echo "deactivate"
