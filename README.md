# SUNDAE Crypto Futures Analyst - Gemini 2.5 Integration

This project demonstrates the integration of Google's Gemini 2.5 AI model with the SUNDAE system prompt for advanced crypto futures trading chart analysis. The system provides ready-to-execute trading signals in a predefined professional format, including entry points, stop losses, take profits, and comprehensive technical analysis.

## 🚀 Features

- **SUNDAE Integration**: Uses the SUNDAE crypto futures analyst system prompt for professional trading analysis
- **Gemini 2.5 Integration**: Uses the latest Gemini 2.5 Flash model for enhanced analysis capabilities
- **Ready-to-Execute Signals**: Provides complete trading setups with Entry, SL, TP, Risk-Reward, and Confidence
- **Multi-Timeframe Analysis**: Includes 1D, 4H, 1H timeframe confirmation
- **Professional Format**: Structured output with emojis and clear technical reasoning
- **Image Processing**: Analyzes trading chart images with advanced AI capabilities
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
- **Model Used**: `gemini-2.5-flash` (latest stable Gemini 2.5 model)
- **Image Support**: PNG, JPEG, and other common formats
- **API Integration**: Direct image byte processing for optimal performance

### Error Handling

- Graceful fallback between model versions
- Comprehensive error reporting
- Multiple API key source support

## 📊 Example Output

```
🚀 Starting SUNDAE Crypto Futures Analyst with Gemini 2.5
============================================================
ℹ️  This script uses the SUNDAE system prompt for professional crypto analysis
ℹ️  The AI will analyze trading charts and provide ready-to-execute trading signals
ℹ️  Using Gemini 2.5 Flash model with SUNDAE crypto futures expertise
============================================================
✅ Gemini API key configured successfully
✅ Gemini 2.5 Flash model loaded successfully
✅ Image loaded successfully: trading_chart.png
🔄 Sending image to Gemini 2.5 API for SUNDAE analysis...
✅ Received SUNDAE analysis from Gemini 2.5 API

============================================================
🔥 SUNDAE CRYPTO FUTURES ANALYSIS (Gemini 2.5):
============================================================
🔥 SUNDAE: BTC/USDT – LONG (Breakout Setup)
📍 Entry: $45,200
🛑 Stop Loss: $44,800
🎯 Take Profit: TP1: $46,000, TP2: $47,200, TP3: $48,500
📊 Risk-Reward: 1:2.5
✅ Confidence Level: 85%
🔍 Reason / Analysis:
• Current Trend: Bullish breakout from consolidation
• Multi-Timeframe: 1D uptrend, 4H breakout, 1H momentum
• Volume Analysis: Increasing volume on breakout
• VWAP: Price above VWAP indicating bullish momentum
• BOS/CHoCH: Break of Structure confirmed at $45,000
⏰ Estimated Move Duration: 2-3 days
📈 Scenario if TP: Strong continuation to $48,500
📉 Scenario if SL: False breakout, return to consolidation
⚠️ Execution Notes: Wait for candle close above $45,200
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
