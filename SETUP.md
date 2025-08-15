# Setup Guide - SUNDAE Crypto Futures Analyst with Gemini 2.5

This guide will help you set up the SUNDAE Crypto Futures Analyst project with the latest Gemini 2.5 AI model. The system provides ready-to-execute trading signals in a professional format using the SUNDAE crypto futures analyst system prompt through a modern Streamlit web interface.

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Get Your Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Navigate to "Get API key" section
4. Create a new API key
5. Copy the key (it starts with "AI...")

### 3. Configure API Key

Choose one of these methods:

#### Method A: Environment Variable (Recommended)

```bash
# Windows PowerShell
$env:GEMINI_API_KEY="your_api_key_here"

# Windows Command Prompt
set GEMINI_API_KEY=your_api_key_here

# Linux/Mac
export GEMINI_API_KEY="your_api_key_here"
```

#### Method B: .env File

```bash
echo "GEMINI_API_KEY=your_api_key_here" > .env
```

#### Method C: Configuration File

Copy the example configuration and update it:

```bash
cp config.example .env
# Then edit .env with your actual API key
```

### 4. Launch the Application

#### Option 1: Using the Launcher Script (Recommended)

```bash
# Windows
run_app.bat

# Linux/Mac
./run_app.sh

# Python (cross-platform)
python run_app.py
```

#### Option 2: Direct Streamlit Command

```bash
streamlit run src/ui/app.py --server.port 8501
```

The application will automatically open in your default web browser at `http://localhost:8501`.

## 🔧 Advanced Configuration

### Model Selection

The application supports multiple Gemini models:

- **Primary**: `gemini-2.5-flash` (latest stable Gemini 2.5 model)
- **Alternative**: `gemini-2.0-flash-exp` (experimental 2.0 model)
- **Fallback**: `gemini-1.5-flash` (stable 1.5 model)

You can change the model in the web interface sidebar or set it in your `.env` file:

```bash
GEMINI_MODEL=gemini-2.5-flash
```

### Application Settings

Customize the application behavior in your `.env` file:

```bash
# Server configuration
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=localhost

# Gemini configuration
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.5-flash
```

### Image Format Support

Supported formats:

- PNG (recommended)
- JPEG/JPG
- WebP
- GIF
- BMP

## 🐛 Troubleshooting

### Common Issues

#### 1. API Key Not Found

```
❌ Gemini API key not found!
```

**Solution**: Ensure your API key is set using one of the three methods above.

#### 2. Model Loading Error

```
❌ Error loading Gemini model: [error message]
```

**Solution**:

- Check your internet connection
- Verify your API key is valid
- The application will automatically fall back to alternative models

#### 3. Image Processing Error

```
❌ Error loading image: [error message]
```

**Solution**:

- Ensure the image file exists and is not corrupted
- Check file permissions
- Verify image format is supported
- Keep images under 4MB for optimal performance

#### 4. Import Error

```
ModuleNotFoundError: No module named 'google.genai'
```

**Solution**:

```bash
pip install -r requirements.txt
```

#### 5. Streamlit Not Found

```
❌ Streamlit is not installed
```

**Solution**: The launcher script will automatically install Streamlit if needed, or install manually:

```bash
pip install streamlit
```

### Performance Optimization

- **Image Size**: Keep images under 4MB for optimal performance
- **Format**: PNG provides best quality for charts
- **Resolution**: 1920x1080 or lower recommended
- **Browser**: Use modern browsers (Chrome, Firefox, Safari, Edge)

## 📱 SUNDAE System Prompt

### Built-in SUNDAE Prompt

The SUNDAE crypto futures analyst system prompt is now built directly into the code. This means:

1. **No External Configuration Needed**: The prompt is automatically included with every analysis
2. **Consistent Format**: Every analysis follows the same professional SUNDAE format
3. **Ready-to-Execute Signals**: Includes Entry, SL, TP, Risk-Reward, and Confidence levels
4. **Multi-Timeframe Analysis**: Automatically includes 1D, 4H, 1H confirmation
5. **Professional Structure**: Uses emojis and clear technical reasoning

### What SUNDAE Provides

The SUNDAE system automatically analyzes charts and provides:

- 🔥 **Trading Signal**: Pair, Direction, and Setup type
- 📍 **Entry Point**: Specific entry price
- 🛑 **Stop Loss**: Risk management level
- 🎯 **Take Profit**: TP1, TP2, TP3 targets
- 📊 **Risk-Reward Ratio**: Risk vs. potential reward
- ✅ **Confidence Level**: Signal strength percentage
- 🔍 **Technical Analysis**: Multi-timeframe confirmation, volume, VWAP, BOS/CHoCH
- ⏰ **Move Duration**: Estimated time for the trade
- 📈📉 **Scenarios**: What happens if TP or SL is hit
- ⚠️ **Execution Notes**: Specific entry conditions

## 🔄 Updating from Previous Version

If you're upgrading from the old `google-generativeai` SDK:

1. **Backup your current setup**
2. **Update dependencies**:
   ```bash
   pip uninstall google-generativeai
   pip install -r requirements.txt
   ```
3. **Test the new setup**:
   ```bash
   python run_app.py
   ```

## 📊 Using the Application

### 1. Launch the App

Run one of the launcher scripts or commands above.

### 2. Configure API Key

Enter your Gemini API key in the sidebar.

### 3. Upload Trading Chart

Use the file uploader to select your crypto trading chart image.

### 4. Select Model

Choose your preferred Gemini model from the dropdown.

### 5. Analyze

Click the "🔥 Analyze with SUNDAE AI" button to get your trading signals.

### 6. View Results

The analysis will appear below with the complete SUNDAE format.

**Expected SUNDAE Output Format:**

```
🔥 SUNDAE: [PAIR] – [DIRECTION] ([SETUP])
📍 Entry: [PRICE]
🛑 Stop Loss: [PRICE]
🎯 Take Profit: TP1: [PRICE], TP2: [PRICE], TP3: [PRICE]
📊 Risk-Reward: [RATIO]
✅ Confidence Level: [PERCENTAGE]%
🔍 Reason / Analysis: [TECHNICAL ANALYSIS]
⏰ Estimated Move Duration: [TIME]
📈 Scenario if TP: [DESCRIPTION]
📉 Scenario if SL: [DESCRIPTION]
⚠️ Execution Notes: [ENTRY CONDITIONS]
```

## 🎯 Next Steps

After successful setup:

1. **Test with various chart types** (candlestick, line, etc.)
2. **Customize analysis parameters** in the web interface
3. **Integrate with your trading workflow**
4. **Monitor API usage** and costs
5. **Fine-tune the SUNDAE prompt** for your specific needs

## 📞 Support

If you encounter issues:

1. Check the troubleshooting section above
2. Verify your API key is active
3. Test with a simple image first
4. Check the [Google AI Studio documentation](https://ai.google.dev/docs)
5. Ensure all dependencies are properly installed

## 🔒 Security Notes

- Never commit your API key to version control
- Use environment variables for production deployments
- Regularly rotate your API keys
- Monitor API usage for unusual activity
- The `.env` file is automatically ignored by git

## 🚀 Deployment Options

### Local Development

```bash
python run_app.py
```

### Production Server

```bash
streamlit run src/ui/app.py --server.port 8501 --server.address 0.0.0.0
```

### Docker (Future Enhancement)

Docker support will be added in future versions for easy deployment.
