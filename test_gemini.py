#!/usr/bin/env python3
"""
Test script for Gemini API integration with local image processing.
This script demonstrates how to:
1. Set up the Gemini API key
2. Load the Gemini model
3. Send a local image to the model
4. Print the response from the model
"""

import os
import base64
from pathlib import Path
import google.generativeai as genai
from PIL import Image
import io
from typing import Optional

try:
    # Optional dependency for loading environment variables from a .env file
    from dotenv import load_dotenv  # type: ignore
except Exception:
    load_dotenv = None  # Gracefully handle absence of python-dotenv

def _read_api_key_from_file(file_path: str = "config/gemini_api_key.txt") -> Optional[str]:
    """Read API key from a local file if present."""
    key_file = Path(file_path)
    if not key_file.exists():
        return None
    try:
        api_key_from_file = key_file.read_text(encoding="utf-8").strip()
        return api_key_from_file or None
    except Exception:
        return None


def setup_gemini_api():
    """Set up the Gemini API with your API key.

    Priority order:
    1) `.env` file (if python-dotenv is installed)
    2) Environment variable `GEMINI_API_KEY`
    3) Local file `config/gemini_api_key.txt`
    """
    # Load from .env if available
    if callable(load_dotenv):
        try:
            load_dotenv()
        except Exception:
            pass

    # Try environment variable
    api_key: Optional[str] = os.getenv("GEMINI_API_KEY")

    # Fallback to local file if env var not set
    if not api_key:
        api_key = _read_api_key_from_file()

    if not api_key:
        print("❌ Gemini API key not found!")
        print("Please set your API key using one of these methods:")
        print("1) .env file: add a line GEMINI_API_KEY=your_api_key_here")
        print("2) Environment variable: set GEMINI_API_KEY in your shell")
        print("3) File: put your key into config/gemini_api_key.txt")
        return None

    # Configure the Gemini API
    genai.configure(api_key=api_key)
    print("✅ Gemini API configured successfully")
    return True

def load_gemini_model():
    """Load a current image-capable Gemini model for image analysis."""
    try:
        # Use a current multimodal model for image processing
        model = genai.GenerativeModel('gemini-1.5-flash')
        print("✅ Gemini 1.5 Flash model loaded successfully")
        return model
    except Exception as e:
        print(f"❌ Error loading Gemini model: {e}")
        return None

def encode_image_to_base64(image_path):
    """Convert a local image to base64 encoding."""
    try:
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
            base64_image = base64.b64encode(image_data).decode('utf-8')
            print(f"✅ Image encoded successfully: {image_path}")
            return base64_image
    except Exception as e:
        print(f"❌ Error encoding image: {e}")
        return None

def load_image_for_gemini(image_path):
    """Load and prepare image for Gemini API."""
    try:
        image = Image.open(image_path)
        print(f"✅ Image loaded successfully: {image_path}")
        return image
    except Exception as e:
        print(f"❌ Error loading image: {e}")
        return None

def analyze_trading_chart(model, image_path):
    """Analyze a trading chart image using Gemini API."""
    
    try:
        # Load the image
        image = load_image_for_gemini(image_path)
        if image is None:
            return None
        
        # Send only the image to Gemini (system prompt is configured in AI Studio)
        print("🔄 Sending image to Gemini API for analysis...")
        print("ℹ️  System prompt is configured in Google AI Studio as 'SUNDAE' crypto analyst")
        
        # Send image in supported format. New SDK supports passing dicts with inline data.
        with open(image_path, "rb") as f:
            image_bytes = f.read()
        response = model.generate_content([
            {"mime_type": "image/png", "data": image_bytes},
            "Analyze this trading chart per the configured system prompt.",
        ])
        
        print("✅ Received response from Gemini API")
        return response.text
        
    except Exception as e:
        print(f"❌ Error analyzing image: {e}")
        return None

def main():
    """Main function to run the Gemini API test."""
    print("🚀 Starting SUNDAE Crypto Analyst Test Script")
    print("=" * 50)
    print("ℹ️  This script tests the SUNDAE system prompt configured in Google AI Studio")
    print("ℹ️  The AI will analyze trading charts and provide detailed trading signals")
    print("=" * 50)
    
    # Step 1: Set up API key
    if not setup_gemini_api():
        return
    
    # Step 2: Load Gemini model
    model = load_gemini_model()
    if model is None:
        return
    
    # Step 3: Process local image
    # You can change this path to your trading chart image
    image_path = "trading_chart.png"  # Update this path as needed
    
    if not Path(image_path).exists():
        print(f"❌ Image file not found: {image_path}")
        print("Please place a trading chart image in the project directory or update the image_path variable")
        return
    
    # Step 4: Analyze the image and get response
    response = analyze_trading_chart(model, image_path)
    
    if response:
        print("\n" + "=" * 50)
        print("🔥 SUNDAE ANALYSIS RESPONSE:")
        print("=" * 50)
        print(response)
        print("=" * 50)
    else:
        print("❌ Failed to get response from Gemini API")

if __name__ == "__main__":
    main()
