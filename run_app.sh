#!/bin/bash

echo "========================================"
echo "    SUNDAE Crypto Futures Analyst"
echo "========================================"
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8+ and try again"
    exit 1
fi

# Check if requirements are installed
echo "Checking dependencies..."
if ! python3 -c "import streamlit" &> /dev/null; then
    echo "Installing dependencies..."
    pip3 install -r requirements.txt
fi

# Make the script executable
chmod +x run_app.py

# Run the application
echo
echo "Starting SUNDAE Streamlit application..."
echo "The app will open in your browser at: http://localhost:8501"
echo "Press Ctrl+C to stop the application"
echo

python3 run_app.py
