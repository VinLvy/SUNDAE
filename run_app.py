#!/usr/bin/env python3
"""
Main launcher script for the SUNDAE Crypto Futures Analyst Streamlit application.
Run this script to start the application.
"""

import subprocess
import sys
import os

def main():
    """Launch the SUNDAE Crypto Futures Analyst Streamlit application"""
    
    # Check if streamlit is installed
    try:
        import streamlit
        print("✅ Streamlit is installed")
    except ImportError:
        print("❌ Streamlit is not installed. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "streamlit"])
        print("✅ Streamlit installed successfully")
    
    # Get the path to the app.py file
    app_path = os.path.join("src", "ui", "app.py")
    
    if not os.path.exists(app_path):
        print(f"❌ Application file not found at: {app_path}")
        return
    
    print("🔥 Starting SUNDAE Crypto Futures Analyst...")
    print("📱 The application will open in your default web browser")
    print("🔗 If it doesn't open automatically, go to: http://localhost:8501")
    print("⏹️  Press Ctrl+C to stop the application")
    print("-" * 50)
    
    # Launch the Streamlit app
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", app_path,
            "--server.port", "8501",
            "--server.address", "localhost"
        ])
    except KeyboardInterrupt:
        print("\n👋 SUNDAE application stopped by user")
    except Exception as e:
        print(f"❌ Error running SUNDAE application: {e}")

if __name__ == "__main__":
    main()
