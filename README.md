# SUNDAE Crypto Futures Analyst

A powerful Streamlit application that uses Google's Gemini AI to automatically analyze crypto trading charts and provide ready-to-execute trading signals using the SUNDAE system prompt.

## 🚀 Features

- **🔥 SUNDAE AI Analysis**: Automatic crypto futures analysis with predefined professional prompts
- **📊 Trading Chart Upload**: Support for multiple image formats (PNG, JPG, JPEG, GIF, BMP, WebP)
- **🎯 Ready-to-Execute Signals**: Complete trading setups with Entry, SL, TP, Risk-Reward, and Confidence
- **⏰ Multi-Timeframe Analysis**: Includes 1D, 4H, 1H timeframe confirmation
- **📈 Professional Format**: Structured output with emojis and clear technical reasoning
- **💾 Download Results**: Save analysis results as text files
- **🔧 Multiple Models**: Choose from different Gemini AI models

## 🛠️ Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd SUNDAE
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Get your Gemini API Key**:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Copy the key for use in the application

## 🚀 Running the Application

### Method 1: Using the launcher script

```bash
python run_app.py
```

### Method 2: Direct Streamlit command

```bash
streamlit run src/ui/app.py
```

The application will open in your default web browser at `http://localhost:8501`

## 📱 How to Use

1. **Enter API Key**: Input your Gemini API key in the sidebar
2. **Upload Trading Chart**: Use the file uploader to select a crypto trading chart image
3. **Automatic Analysis**: Click "🔥 Analyze with SUNDAE AI" to get automatic trading signals
4. **View Results**: See the complete SUNDAE analysis with entry, stop loss, take profit levels
5. **Download Analysis**: Save the trading signal for your records

## 🔥 SUNDAE Analysis Features

The SUNDAE AI automatically provides:

- **Entry Point**: Precise entry price for the trade
- **Stop Loss**: Risk management level
- **Take Profit**: Multiple profit targets (TP1, TP2, TP3)
- **Risk-Reward Ratio**: Calculated risk vs. reward
- **Confidence Level**: AI confidence in the signal
- **Technical Analysis**: Multi-timeframe confirmation
- **Execution Notes**: Trade setup instructions

## ⚙️ Configuration

### Environment Variables

- `GEMINI_API_KEY`: Your Gemini API key (optional, can be entered in UI)
- `GEMINI_MODEL`: Default model to use (optional)

### Supported Models

- `gemini-2.5-flash` (default)
- `gemini-2.0-flash-exp`
- `gemini-1.5-flash`

## 🔧 Development

### Project Structure

- **`src/core/`**: Contains the Gemini AI client and core logic
- **`src/ui/`**: SUNDAE Streamlit user interface components
- **`src/utils/`**: Configuration and utility functions
- **`assets/`**: Sample trading charts and data files

## 📋 Requirements

- Python 3.8+
- Streamlit 1.28+
- Google Generative AI 0.8+
- Pillow 10.0+
- Other dependencies listed in `requirements.txt`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google Gemini AI for providing the AI capabilities
- Streamlit for the excellent web application framework
- SUNDAE system prompt for professional crypto analysis
- Open source community for inspiration and tools

⭐ **Don't forget to star this repository if you find this project helpful!**

---

**Note**: Make sure to keep your API keys secure and never commit them to version control.

**VinLvy ADIOS**
