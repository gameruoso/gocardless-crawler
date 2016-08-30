#!/bin/bash

# Create Virtual Environment
echo -- Creating python3 virtual environment --
virtualenv ve -p python3

# Activate the environment
echo -- Activating virtual environment --
source ve/bin/activate

# Install dependencies
echo -- Installing libraries --
pip install requests
pip install beautifulsoup4

# Run Crawler
echo -- Running Crawler --
python main.py

# Deactivate virtual environment
echo -- Deactivate virtual environment --
deactivate

# Remove virtual environment
echo -- Clean up environment --
rm -rf ve __pycache__