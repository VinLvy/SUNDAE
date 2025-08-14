"""
Configuration utilities for the Gemini AI Image Analyzer application.
"""

import os
from typing import Optional

class Config:
    """Application configuration class"""
    
    # Default Gemini model
    DEFAULT_MODEL = "gemini-2.5-flash"
    
    # Supported image formats
    SUPPORTED_IMAGE_FORMATS = ['png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp']
    
    # Maximum file size (10MB)
    MAX_FILE_SIZE = 10 * 1024 * 1024
    
    @staticmethod
    def get_api_key() -> Optional[str]:
        """Get API key from environment variable"""
        return os.getenv('GEMINI_API_KEY')
    
    @staticmethod
    def get_model() -> str:
        """Get default model from environment variable or use default"""
        return os.getenv('GEMINI_MODEL', Config.DEFAULT_MODEL)
    
    @staticmethod
    def validate_image_format(filename: str) -> bool:
        """Validate if the file format is supported"""
        if not filename:
            return False
        
        file_ext = filename.lower().split('.')[-1]
        return file_ext in Config.SUPPORTED_IMAGE_FORMATS
    
    @staticmethod
    def validate_file_size(file_size: int) -> bool:
        """Validate if the file size is within limits"""
        return file_size <= Config.MAX_FILE_SIZE
