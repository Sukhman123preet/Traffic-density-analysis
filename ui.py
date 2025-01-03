import streamlit as st

def setup_ui():
    # Set page configuration
    st.set_page_config(
        page_title="Traffic-Density Analysis System",
        page_icon="🚗",
        layout="wide"
    )
    
    # Add custom CSS for dark theme
    st.markdown("""
    <style>
    /* Dark theme colors */
    :root {
        --primary-color: #BB86FC;
        --background-color: #121212;
        --surface-color: #1E1E1E;
        --text-primary: #FFFFFF;
        --text-secondary: rgba(255, 255, 255, 0.7);
        --hover-color: rgba(255, 255, 255, 0.1);
    }
    
    body {
        margin: 0;
        padding: 0;
        font-family: 'Arial', sans-serif;
        background-color: var(--background-color);
        color: var(--text-primary);
        line-height: 1.6;
        overflow-x: hidden;
    }
    .st-emotion-cache-1yiq2ps{
        background-color: var(--background-color);
    }
    header{
        background-color: var(--background-color);
    }
    
    /* Header Styling */
    .main-header {
        padding-top: 15px;
        font-size: 2rem;
        color: var(--primary-color);
        text-align: center;
        margin-bottom: 0.5rem;
        text-shadow: 1px 1px 5px rgba(255, 255, 255, 0.2);
    }
    
    .subheader {
        font-size: 1rem;
        color: var(--text-secondary);
        text-align: center;
        margin-bottom: 0.7rem;
    }
    
    /* Project Info Section */
    .project-info {
        font-size: 1.75rem;
        background-color: var(--surface-color);
        padding: 0.4rem;
        border-radius: 10px;
        border: 1px solid var(--hover-color);
        margin-bottom: 0.7rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.4);
        transition: transform 0.2s, box-shadow 0.2s;
    }
    
    .project-info:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 10px rgba(0, 0, 0, 0.6);
    }
    
    .project-info h3 {
        color: var(--primary-color);
        margin-bottom: 1rem;
    }
    
    .project-info p {
        color: var(--text-secondary);
    }
    
    /* Info Grid */
    .info-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1.5rem;
        margin-top: 0.70rem;
    }
    
    .info-card {
        background: var(--surface-color);
        padding: 0.8rem;
        border-radius: 8px;
        border: 1px solid var(--hover-color);
        transition: transform 0.2s, box-shadow 0.2s;
    }
    
    .info-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 10px rgba(0, 0, 0, 0.6);
    }
    
    .info-card h4 {
        color: var(--primary-color);
        margin-bottom: 1rem;
    }
    
    .info-card p {
        color: var(--text-secondary);
    }
    
    /* Image Container */
    .image-container {
        margin-top: 1rem;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.4);
    }
    
    .image-container img {
        width: 100%;
        height: auto;
        border-radius: 10px;
        object-fit: cover;
    }
    
    /* Transitions and Interactivity */
    a {
        color: var(--primary-color);
        text-decoration: none;
        transition: color 0.3s ease;
    }
    
    a:hover {
        color: var(--text-secondary);
    }
    
    button {
        background-color: var(--primary-color);
        color: var(--text-primary);
        border: none;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        cursor: pointer;
        font-size: 1rem;
        transition: background-color 0.3s ease, transform 0.2s;
    }
    
    button:hover {
        transform: scale(1.05);
    }
    
    </style>
    """, unsafe_allow_html=True)
    
    # Header Section
    st.markdown("<h1 class='main-header'>Traffic-Density Analysis System</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subheader'>Real-time Vehicle Detection & Traffic Analysis</p>", unsafe_allow_html=True)
    
    # Project Info Section and Image
    col1 ,col2, col3 = st.columns([0.5,4, 0.5])
    with col2:
        # Project Info
        st.markdown("""
        <div class="project-info">
            <h3>About This Project</h3>
            <p>The Traffic-Density Analysis System leverages the power of advanced YOLOv8 technology  to provide real-time vehicle detection and comprehensive traffic pattern analysis. This project uses a model trained on a custom dataset to ensure high accuracy and adaptability to various traffic scenarios. Designed to monitor two lanes simultaneously, the system delivers instant insights into traffic density and flow patterns, facilitating smarter traffic management solutions.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Features Grid
    st.markdown("""
    <div class="info-grid">
        <div class="info-card">
            <h4>🚗 Real-time Detection</h4>
            <p>Advanced YOLOv8 algorithm for accurate vehicle detection and counting in real-time</p>
        </div>
        <div class="info-card">
            <h4>📊 Traffic Analysis</h4>
            <p>Comprehensive analysis of traffic patterns and density in multiple lanes</p>
        </div>
        <div class="info-card">
            <h4>📈 Dynamic Updates</h4>
            <p>Live updates and visualization of traffic intensity and vehicle distribution</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize session state for analytics
    if 'frame_data' not in st.session_state:
        st.session_state.frame_data = []