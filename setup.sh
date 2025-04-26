#!/bin/bash

# Install required system dependencies
echo "Installing system dependencies..."
sudo apt update
sudo apt install -y python3-venv python3-dev portaudio19-dev

# Create and activate virtual environment
echo "Setting up Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install Python packages
echo "Installing Python packages..."
pip install --upgrade pip
pip install vosk pyaudio pyttsx3