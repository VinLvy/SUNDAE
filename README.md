# SUNDAE Crypto Analyst - Gemini 2.5 Integration

This project demonstrates the integration of Google's Gemini 2.5 AI model for advanced trading chart analysis. The system is configured with a specialized "SUNDAE" crypto analyst prompt in Google AI Studio.

## 🚀 Features

- **Gemini 2.5 Integration**: Uses the latest Gemini 2.0 Flash Experimental model for enhanced analysis capabilities
- **Image Processing**: Analyzes trading chart images with advanced AI capabilities
- **Fallback Support**: Automatically falls back to Gemini 1.5 if 2.5 is not available
- **Multiple API Key Sources**: Supports environment variables, .env files, and local configuration files

## 📋 Prerequisites

- Python 3.9+
- Gemini API key from [Google AI Studio](https://aistudio.google.com/)
- Trading chart images for analysis

## 🛠️ Installation

1. Clone this repository:

```bash
git clone <repository-url>
cd prototype-3
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up your Gemini API key using one of these methods:

   **Option A: Environment Variable**

   ```bash
   export GEMINI_API_KEY="your_api_key_here"
   ```

   **Option B: .env File**

   ```bash
   echo "GEMINI_API_KEY=your_api_key_here" > .env
   ```

   **Option C: Local File**

   ```bash
   mkdir config
   echo "your_api_key_here" > config/gemini_api_key.txt
   ```

## 🎯 Usage

### Basic Usage

Run the test script to analyze a trading chart:

```bash
python test_gemini.py
```

Make sure you have a `trading_chart.png` file in the project directory, or update the `image_path` variable in the script.

### Advanced Configuration

The script automatically detects and uses the best available Gemini model:

- **Primary**: Gemini 2.0 Flash Experimental (2.5 capabilities)
- **Fallback**: Gemini 1.5 Flash

## 🔧 Technical Details

### SDK Version

- **New**: `google-genai` (latest version)
- **Previous**: `google-generativeai`

### Model Capabilities

- **Gemini 2.5**: Enhanced multimodal understanding, better image analysis
- **Image Support**: PNG, JPEG, and other common formats
- **API Integration**: Direct image byte processing for optimal performance

### Error Handling

- Graceful fallback between model versions
- Comprehensive error reporting
- Multiple API key source support

## 📊 Example Output

```
🚀 Starting SUNDAE Crypto Analyst Test Script with Gemini 2.5
============================================================
ℹ️  This script tests the SUNDAE system prompt configured in Google AI Studio
ℹ️  The AI will analyze trading charts and provide detailed trading signals
ℹ️  Using the latest Gemini 2.5 model for enhanced analysis capabilities
============================================================
✅ Gemini API configured successfully
✅ Gemini 2.5 Flash model loaded successfully
✅ Image loaded successfully: trading_chart.png
🔄 Sending image to Gemini 2.5 API for analysis...
✅ Received response from Gemini 2.5 API

============================================================
🔥 SUNDAE ANALYSIS RESPONSE (Gemini 2.5):
============================================================
[AI analysis of your trading chart will appear here]
============================================================
```

## 🔄 Migration from Previous Version

If you're upgrading from the previous `google-generativeai` SDK:

1. **Update dependencies**: `pip install -r requirements.txt`
2. **API changes**: The new SDK uses `genai.types.Part.from_data()` for image handling
3. **Model names**: Updated to use `gemini-2.0-flash-exp` for 2.5 capabilities

## 📝 Notes

- The system prompt "SUNDAE" is configured in Google AI Studio
- Gemini 2.5 provides enhanced analysis capabilities for trading charts
- The script includes automatic fallback to ensure compatibility
- Image processing is optimized for the new SDK architecture

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

This project is licensed under the terms specified in the LICENSE file.
