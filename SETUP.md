# Setup Guide for Gemini API Test Script

## Prerequisites

1. **Python 3.7+** installed on your system
2. **Gemini API Key** from Google AI Studio

## Installation Steps

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Get Your Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Navigate to "Get API key" section
4. Create a new API key
5. Copy the API key

### 3. Set Up API Key

#### Option A: Environment Variable (Recommended)

```bash
# On Windows (PowerShell)
$env:GEMINI_API_KEY="your_api_key_here"

# On Windows (Command Prompt)
set GEMINI_API_KEY=your_api_key_here

# On macOS/Linux
export GEMINI_API_KEY="your_api_key_here"
```

#### Option B: Direct in Script (Less Secure)

Edit `test_gemini.py` and replace the environment variable check with:

```python
api_key = "your_actual_api_key_here"
```

### 4. Prepare Test Image

Place a trading chart screenshot in your project directory with the name `trading_chart.png`, or update the `image_path` variable in the script to point to your image.

## Running the Script

```bash
python test_gemini.py
```

## Expected Output

The script will:

1. ✅ Configure Gemini API
2. ✅ Load the Gemini Pro Vision model
3. ✅ Load and encode your image
4. ✅ Send the image to Gemini for analysis
5. ✅ Display the trading signal response (Long/Short/Neutral)

## Troubleshooting

### Common Issues:

1. **"GEMINI_API_KEY environment variable not found"**

   - Make sure you've set the environment variable correctly
   - Restart your terminal after setting the variable

2. **"Image file not found"**

   - Ensure the image file exists in the specified path
   - Update the `image_path` variable in the script

3. **Import errors**

   - Make sure you've installed all dependencies: `pip install -r requirements.txt`

4. **API errors**
   - Verify your API key is correct
   - Check if you have sufficient API quota
   - Ensure the image format is supported (PNG, JPEG, etc.)

## Supported Image Formats

- PNG
- JPEG/JPG
- WebP
- BMP
- TIFF

## Security Notes

- Never commit your API key to version control
- Use environment variables for production deployments
- The API key gives access to your Gemini account and quota
