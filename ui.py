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
        }
        
        .main-header {
            padding-top:0px;
            font-size: 2.5rem;
            color: var(--primary-color);
            text-align: center;
            margin-bottom: 0.5rem;
        }
        
        .subheader {
            font-size: 1.2rem;
            color: var(--text-secondary);
            text-align: center;
            margin-bottom: 0.75rem;
        }
        
        .project-info {
            font-size: 1.5rem;
            background-color: var(--surface-color);
            padding: 0.5rem;
            border-radius: 10px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            margin-bottom: 0.75rem;
        }
        
        .project-info h3 {
            color: var(--primary-color);
            margin-bottom: 1rem;
        }
        
        .project-info p {
            color: var(--text-secondary);
        }
        
        .info-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
            margin-top: 0.75rem;
        }
        
        .info-card {
            background: var(--surface-color);
            padding: 1rem;
            border-radius: 8px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .info-card h4 {
            color: var(--primary-color);
            margin-bottom: 1rem;
        }
        
        .info-card p {
            color: var(--text-secondary);
        }

        .image-container {
            margin-top: 1rem;
            border-radius: 10px;
            overflow: hidden;
        }
        
        .image-container img {
            width: 100%;
            height: auto;
            border-radius: 10px;
            object-fit: cover;
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
            <p>Traffic-Density Analysis System leverages advanced YOLOv8 technology to provide real-time vehicle detection 
            and traffic pattern analysis. The system monitors two lanes simultaneously, delivering instant insights 
            about traffic density and flow patterns.</p>
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