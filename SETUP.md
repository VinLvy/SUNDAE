# Setup Guide - Gemini 2.5 Integration

This guide will help you set up the SUNDAE Crypto Analyst project with the latest Gemini 2.5 AI model.

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

#### Method C: Local Configuration File

```bash
mkdir config
echo "your_api_key_here" > config/gemini_api_key.txt
```

### 4. Test the Setup

```bash
python test_gemini.py
```

## 🔧 Advanced Configuration

### Model Selection

The script automatically uses the best available model:

- **Primary**: `gemini-2.0-flash-exp` (Gemini 2.5 capabilities)
- **Fallback**: `gemini-1.5-flash` (if 2.5 unavailable)

### Custom Model Configuration

You can modify the model selection in `test_gemini.py`:

```python
def load_gemini_model():
    try:
        # Use specific model
        model = genai.GenerativeModel('gemini-2.0-flash-exp')
        return model
    except Exception as e:
        # Fallback logic
        pass
```

### Image Format Support

Supported formats:

- PNG (recommended)
- JPEG/JPG
- WebP
- BMP
- TIFF

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
- The script will automatically fall back to Gemini 1.5

#### 3. Image Processing Error

```
❌ Error loading image: [error message]
```

**Solution**:

- Ensure the image file exists
- Check file permissions
- Verify image format is supported

#### 4. Import Error

```
ModuleNotFoundError: No module named 'google.genai'
```

**Solution**:

```bash
pip install -r requirements.txt
```

### Performance Optimization

- **Image Size**: Keep images under 4MB for optimal performance
- **Format**: PNG provides best quality for charts
- **Resolution**: 1920x1080 or lower recommended

## 📱 Google AI Studio Configuration

### Setting Up SUNDAE System Prompt

1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Create a new chat
3. Configure system instructions for crypto analysis
4. Test with sample trading charts
5. Refine the prompt based on results

### Recommended System Prompt Structure

```
You are SUNDAE, an expert crypto trading analyst. Your role is to:

1. Analyze trading charts for technical patterns
2. Identify support/resistance levels
3. Provide clear Long/Short signals
4. Explain your reasoning
5. Include risk management notes

Always be consistent and professional in your analysis.
```

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
   python test_gemini.py
   ```

## 📊 Testing Your Setup

### 1. Basic Test

```bash
python test_gemini.py
```

### 2. Custom Image Test

Modify the `image_path` variable in the script to test with your own images.

### 3. API Response Test

The script should output:

- ✅ Gemini API configured successfully
- ✅ Gemini 2.5 Flash model loaded successfully
- ✅ Image loaded successfully
- 🔄 Sending image to Gemini 2.5 API for analysis...
- ✅ Received response from Gemini 2.5 API

## 🎯 Next Steps

After successful setup:

1. **Customize the system prompt** in Google AI Studio
2. **Test with various chart types** (candlestick, line, etc.)
3. **Integrate with your trading workflow**
4. **Monitor API usage** and costs
5. **Fine-tune analysis parameters**

## 📞 Support

If you encounter issues:

1. Check the troubleshooting section above
2. Verify your API key is active
3. Test with a simple image first
4. Check the [Google AI Studio documentation](https://ai.google.dev/docs)

## 🔒 Security Notes

- Never commit your API key to version control
- Use environment variables for production deployments
- Regularly rotate your API keys
- Monitor API usage for unusual activity
