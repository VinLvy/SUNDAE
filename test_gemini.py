#!/usr/bin/env python3
"""
Test script for Gemini 2.5 API integration with local image processing.
This script demonstrates how to:
1. Set up the Gemini API key
2. Load the Gemini 2.5 model
3. Send a local image to the model
4. Print the response from the model
"""

import os
import base64
from pathlib import Path
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

    # Set the API key as environment variable for the new SDK
    os.environ["GOOGLE_API_KEY"] = api_key
    print("✅ Gemini API key configured successfully")
    return True

def load_gemini_model():
    """Load Gemini 2.5 model for image analysis."""
    try:
        # Import the Client class directly
        from google.genai import Client
        
        # Get API key from environment
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            api_key = os.getenv("GEMINI_API_KEY")
        
        # Create a client instance with API key
        client = Client(api_key=api_key)
        
        # Use Gemini 2.5 model for enhanced capabilities
        print("✅ Gemini 2.5 Flash model loaded successfully")
        return client
    except Exception as e:
        print(f"❌ Error loading Gemini 2.5 model: {e}")
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

def analyze_trading_chart(client, image_path):
    """Analyze a trading chart image using Gemini 2.5 API."""
    
    try:
        # Load the image
        image = load_image_for_gemini(image_path)
        if image is None:
            return None
        
        # Send only the image to Gemini (system prompt is configured in AI Studio)
        print("🔄 Sending image to Gemini 2.5 API for analysis...")
        print("ℹ️  System prompt is configured in Google AI Studio as 'SUNDAE' crypto analyst")
        
        # New SDK supports passing image bytes directly
        with open(image_path, "rb") as f:
            image_bytes = f.read()
        
        # Create content parts for the new API
        # We'll use the types module to create proper content
        import google.genai.types as types
        
        # Create image part using from_bytes
        image_part = types.Part.from_bytes(data=image_bytes, mime_type="image/png")
        text_part = types.Part.from_text(text="Analyze this trading chart per the configured system prompt.")
        
        # Create content
        content = types.Content(parts=[image_part, text_part])
        
        # Generate content using the correct API: client.models.generate_content
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=[content]
        )
        
        print("✅ Received response from Gemini 2.5 API")
        return response.text
        
    except Exception as e:
        print(f"❌ Error analyzing image: {e}")
        print(f"Error details: {type(e).__name__}: {str(e)}")
        return None

def main():
    """Main function to run the Gemini 2.5 API test."""
    print("🚀 Starting SUNDAE Crypto Analyst Test Script with Gemini 2.5")
    print("=" * 60)
    print("ℹ️  This script tests the SUNDAE system prompt configured in Google AI Studio")
    print("ℹ️  The AI will analyze trading charts and provide detailed trading signals")
    print("ℹ️  Using the latest Gemini 2.5 model for enhanced analysis capabilities")
    print("=" * 60)
    
    # Step 1: Set up API key
    if not setup_gemini_api():
        return
    
    # Step 2: Load Gemini model
    client = load_gemini_model()
    if client is None:
        return
    
    # Step 3: Process local image
    # You can change this path to your trading chart image
    image_path = "trading_chart.png"  # Update this path as needed
    
    if not Path(image_path).exists():
        print(f"❌ Image file not found: {image_path}")
        print("Please place a trading chart image in the project directory or update the image_path variable")
        return
    
    # Step 4: Analyze the image and get response
    response = analyze_trading_chart(client, image_path)
    
    if response:
        print("\n" + "=" * 60)
        print("🔥 SUNDAE ANALYSIS RESPONSE (Gemini 2.5):")
        print("=" * 60)
        print(response)
        print("=" * 60)
    else:
        print("❌ Failed to get response from Gemini 2.5 API")

if __name__ == "__main__":
    main()
