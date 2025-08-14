#!/usr/bin/env python3
"""
Gemini AI Client for Image Analysis
This module provides a client class for interacting with Google's Gemini AI API
to analyze images with custom prompts.
"""

import os
import base64
from pathlib import Path
from PIL import Image
import io
from typing import Optional, Union
import streamlit as st

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None

class GeminiClient:
    """Client class for interacting with Google Gemini AI API"""
    
    def __init__(self, api_key: str, model: str = "gemini-2.5-flash"):
        """
        Initialize the Gemini client
        
        Args:
            api_key (str): Your Gemini API key
            model (str): The Gemini model to use
        """
        self.api_key = api_key
        self.model = model
        self.client = None
        
        # Set up the API key
        os.environ["GOOGLE_API_KEY"] = api_key
        
        # Initialize the client
        self._initialize_client()
    
    def _initialize_client(self):
        """Initialize the Gemini client"""
        try:
            from google.genai import Client
            self.client = Client(api_key=self.api_key)
            print(f"✅ Gemini client initialized with model: {self.model}")
        except ImportError:
            st.error("❌ Google GenAI library not found. Please install it with: pip install google-genai")
            raise
        except Exception as e:
            st.error(f"❌ Error initializing Gemini client: {e}")
            raise
    
    def analyze_image_with_prompt(self, image_path: Union[str, Path, bytes], prompt: str) -> str:
        """
        Analyze an image with a custom prompt using Gemini AI
        
        Args:
            image_path: Path to image file, Path object, or image bytes
            prompt (str): The prompt/question about the image
            
        Returns:
            str: The AI response
        """
        try:
            if self.client is None:
                raise RuntimeError("Gemini client not initialized")
            
            # Handle different input types
            if isinstance(image_path, (str, Path)):
                # Read image from file
                with open(image_path, "rb") as f:
                    image_bytes = f.read()
            elif isinstance(image_path, bytes):
                # Direct bytes
                image_bytes = image_bytes
            else:
                # Assume it's a Streamlit uploaded file
                image_bytes = image_path.read()
                image_path.seek(0)  # Reset file pointer
            
            # Import types from the new SDK
            from google.genai import types
            
            # Create image part
            image_part = types.Part.from_bytes(data=image_bytes, mime_type="image/png")
            text_part = types.Part.from_text(text=prompt)
            
            # Create content
            content = types.Content(parts=[image_part, text_part])
            
            # Generate content
            response = self.client.models.generate_content(
                model=self.model,
                contents=[content]
            )
            
            return response.text
            
        except Exception as e:
            error_msg = f"Error analyzing image: {str(e)}"
            st.error(error_msg)
            raise RuntimeError(error_msg)
    
    def analyze_image_simple(self, image_path: Union[str, Path, bytes]) -> str:
        """
        Simple image analysis without custom prompt
        
        Args:
            image_path: Path to image file, Path object, or image bytes
            
        Returns:
            str: The AI response
        """
        default_prompt = "Please analyze this image and describe what you see in detail."
        return self.analyze_image_with_prompt(image_path, default_prompt)
    
    def get_supported_models(self) -> list:
        """Get list of supported Gemini models"""
        return [
            "gemini-2.5-flash",
            "gemini-2.0-flash-exp", 
            "gemini-1.5-flash"
        ]
    
    def change_model(self, new_model: str):
        """Change the model being used"""
        if new_model in self.get_supported_models():
            self.model = new_model
            print(f"✅ Model changed to: {new_model}")
        else:
            raise ValueError(f"Unsupported model: {new_model}")
    
    def test_connection(self) -> bool:
        """Test if the API connection is working"""
        try:
            # Simple test with a basic prompt
            test_response = self.analyze_image_with_prompt(
                image_path=b"",  # Empty bytes for test
                prompt="Hello, this is a test."
            )
            return True
        except Exception:
            return False

# Legacy functions for backward compatibility
def setup_gemini_api():
    """Legacy function - use GeminiClient class instead"""
    print("⚠️ This function is deprecated. Use GeminiClient class instead.")
    return None

def load_gemini_model():
    """Legacy function - use GeminiClient class instead"""
    print("⚠️ This function is deprecated. Use GeminiClient class instead.")
    return None

def analyze_trading_chart(client, image_path):
    """Legacy function - use GeminiClient class instead"""
    print("⚠️ This function is deprecated. Use GeminiClient class instead.")
    return None

if __name__ == "__main__":
    # Example usage
    print("🚀 Gemini AI Client Example")
    print("=" * 40)
    
    # Check if API key is available
    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
    
    if api_key:
        try:
            client = GeminiClient(api_key)
            print("✅ Client created successfully")
            print(f"📋 Supported models: {client.get_supported_models()}")
        except Exception as e:
            print(f"❌ Error creating client: {e}")
    else:
        print("❌ No API key found. Please set GOOGLE_API_KEY or GEMINI_API_KEY environment variable.")
