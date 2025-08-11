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

def setup_gemini_api():
    """Set up the Gemini API with your API key."""
    # You can set your API key as an environment variable
    api_key = os.getenv('GEMINI_API_KEY')
    
    if not api_key:
        print("❌ GEMINI_API_KEY environment variable not found!")
        print("Please set your API key using one of these methods:")
        print("1. Set environment variable: export GEMINI_API_KEY='your_api_key_here'")
        print("2. Or modify this script to directly set the API key")
        return None
    
    # Configure the Gemini API
    genai.configure(api_key=api_key)
    print("✅ Gemini API configured successfully")
    return True

def load_gemini_model():
    """Load the Gemini Pro Vision model for image analysis."""
    try:
        # Use Gemini Pro Vision model for image processing
        model = genai.GenerativeModel('gemini-pro-vision')
        print("✅ Gemini Pro Vision model loaded successfully")
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
        
        # Send just the image - the system prompt will be automatically applied
        response = model.generate_content(image)
        
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
