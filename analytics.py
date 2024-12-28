import streamlit as st
import pandas as pd
from charts import generate_pie_charts

def display_analytics():
    if len(st.session_state.frame_data) > 0:
        st.markdown("### Final Traffic Analysis")
        
        df = pd.DataFrame(st.session_state.frame_data)
        
        # Summary statistics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Average Vehicles (Left Lane)", f"{df['left_lane'].mean():.1f}")
        with col2:
            st.metric("Average Vehicles (Right Lane)", f"{df['right_lane'].mean():.1f}")
        with col3:
            st.metric("Total Vehicles Detected", f"{df['left_lane'].sum() + df['right_lane'].sum()}")

        # Generate traffic proportion charts
        generate_pie_charts(df)
