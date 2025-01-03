import streamlit as st
from ui import setup_ui
from video_processing import process_video
from analytics import display_analytics

def main():
    try:
        setup_ui()  # Set up UI
        uploaded_file = st.file_uploader("Choose a video file", type=['mp4', 'avi'])
        
        if uploaded_file is not None:
            process_video(uploaded_file)  # Process the uploaded video
            display_analytics()          # Display analytics from processed data

    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
