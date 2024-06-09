#!/bin/bash

# Install pip if not already installed
if ! command -v pip &> /dev/null; then
    echo "Installing pip..."
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py
    rm get-pip.py
fi

# Install virtualenv if not already installed
if ! command -v virtualenv &> /dev/null; then
    echo "Installing virtualenv..."
    pip install virtualenv
fi

# Create a virtual environment
echo "Creating virtual environment..."
virtualenv fvg_venv
source fvg_venv/bin/activate

# Install packages from requirements.txt
echo "Installing packages from requirements.txt..."
pip install -r requirements.txt

# Deactivate the virtual environment
deactivate

echo "Packages installed successfully!"