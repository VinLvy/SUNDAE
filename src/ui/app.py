import streamlit as st
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.gemini_client import GeminiClient

def main():
    """Main Streamlit application for Gemini AI Image Analysis"""
    
    # Set page configuration
    st.set_page_config(
        page_title="Gemini AI Image Analyzer",
        page_icon="🔍",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Application title
    st.title("🔍 Gemini AI Image Analyzer")
    st.markdown("---")
    
    # Sidebar for configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # API Key input
        api_key = st.text_input(
            "Enter your Gemini API Key:",
            type="password",
            help="Enter your Google Gemini API key to enable the application"
        )
        
        # Model selection
        model = st.selectbox(
            "Select Model:",
            ["gemini-2.5-flash", "gemini-2.0-flash-exp", "gemini-1.5-flash"],
            index=0,
            help="Choose the Gemini model to use for analysis"
        )
        
        st.markdown("---")
        st.markdown("### 📖 Instructions")
        st.markdown("""
        1. Upload an image using the file uploader
        2. Enter your prompt/question about the image
        3. Click 'Analyze Image' to get AI insights
        4. View the results below
        """)
    
    # Main content area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("📸 Image Upload")
        
        # File uploader for images
        uploaded_file = st.file_uploader(
            "Choose an image file",
            type=['png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'],
            help="Upload an image file to analyze with Gemini AI"
        )
        
        # Display uploaded image
        if uploaded_file is not None:
            st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
            
            # Show file details
            file_details = {
                "Filename": uploaded_file.name,
                "File size": f"{uploaded_file.size / 1024:.2f} KB",
                "File type": uploaded_file.type
            }
            st.json(file_details)
    
    with col2:
        st.header("💬 Analysis Prompt")
        
        # Text input for the prompt
        prompt = st.text_area(
            "Enter your prompt or question about the image:",
            height=150,
            placeholder="Describe what you want to know about this image...",
            help="Ask questions, request analysis, or describe what you want to know about the image"
        )
        
        # Example prompts
        with st.expander("💡 Example Prompts"):
            st.markdown("""
            - "What do you see in this image?"
            - "Analyze the trading chart and provide insights"
            - "Describe the key elements in this image"
            - "What patterns can you identify?"
            - "Summarize the main points from this chart"
            """)
    
    # Process button and results
    st.markdown("---")
    
    # Center the analyze button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        analyze_button = st.button(
            "🚀 Analyze Image",
            type="primary",
            use_container_width=True,
            disabled=not (uploaded_file and prompt and api_key)
        )
    
    # Results section
    st.header("📊 Analysis Results")
    
    if analyze_button and uploaded_file and prompt and api_key:
        try:
            with st.spinner("🤖 Analyzing image with Gemini AI..."):
                # Initialize Gemini client
                gemini_client = GeminiClient(api_key=api_key, model=model)
                
                # Process the image
                result = gemini_client.analyze_image_with_prompt(
                    image_path=uploaded_file,
                    prompt=prompt
                )
                
                # Display results
                st.success("✅ Analysis completed successfully!")
                
                # Display the result
                st.subheader("🤖 AI Response:")
                st.write(result)
                
                # Add download button for results
                st.download_button(
                    label="📥 Download Results",
                    data=result,
                    file_name=f"analysis_result_{uploaded_file.name}.txt",
                    mime="text/plain"
                )
                
        except Exception as e:
            st.error(f"❌ Error during analysis: {str(e)}")
            st.exception(e)
    
    elif not api_key:
        st.warning("⚠️ Please enter your Gemini API key in the sidebar to start analyzing images.")
    
    elif not uploaded_file:
        st.info("📸 Please upload an image to begin analysis.")
    
    elif not prompt:
        st.info("💬 Please enter a prompt or question about the image.")
    
    else:
        # Placeholder for results
        st.info("👆 Click 'Analyze Image' to start the analysis process.")
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #666;'>"
        "Built with ❤️ using Streamlit and Google Gemini AI"
        "</div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
