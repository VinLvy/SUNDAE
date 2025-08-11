# Prototype-3

## Introduction
This document outlines a project plan for building a simple web/local application using Python and Streamlit. The goal is to automatically validate futures trading signals (Long/Short) by analyzing trading chart screenshots using the Gemini API model. This project is intended as a tool for experimentation and learning, not for actual trading decisions.

## Project Goals
The main objectives of this project are to create a tool that can perform the following:
1.	Receive an image input (screenshot) of a trading chart.
2.	Send the image to the Gemini API.
3.	Analyze the image based on a predefined prompt.
4.	Return a consistent text output, such as "Long" or "Short".
5.	Display the AI's response on a simple web interface.

## Limitations and Risks
This project has important limitations and risks that must be understood:
-	**Financial Risk:** Using an AI model to make trading decisions, especially on high-risk instruments like futures, carries a very high risk of financial loss. This AI is an experimental tool and is not recommended for use in live trading.
-	**AI Uncertainty:** The Gemini model is a general-purpose, multimodal model, not one specifically trained for technical trading analysis. Therefore, its responses may not always be consistent or accurate.
-	**Dependency on System Instructions Quality:** The success of this project is highly dependent on the quality and specificity of the System Instructions you provide to the Gemini API.

## License

This project is licensed under the MIT License.