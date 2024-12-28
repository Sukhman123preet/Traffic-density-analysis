import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

def generate_pie_charts(df):
    st.markdown("### Traffic Proportion Analysis")
    st.write("""
    These pie charts illustrate the traffic intensity for the **left lane** and **right lane** throughout the video:
    - **Heavy Traffic**: Frames where the lane had more vehicles than the set threshold.
    - **Smooth Traffic**: Frames where the lane had fewer or equal vehicles compared to the threshold.
    - **Result**: How much Percentage of total time each lane is under Heavy and smooth traffic intensity state .
    """)
    
    total_frames = len(df)
    heavy_left_frames = len(df[df["left_intensity"] == "Heavy"])
    smooth_left_frames = total_frames - heavy_left_frames

    heavy_right_frames = len(df[df["right_intensity"] == "Heavy"])
    smooth_right_frames = total_frames - heavy_right_frames

    fig = make_subplots(rows=1, cols=2, subplot_titles=("Left Lane Traffic", "Right Lane Traffic"),
                        specs=[[{"type": "domain"}, {"type": "domain"}]])

    fig.add_trace(
        go.Pie(labels=["Heavy", "Smooth"], values=[heavy_left_frames, smooth_left_frames], name="Left Lane"),
        row=1, col=1
    )

    fig.add_trace(
        go.Pie(labels=["Heavy", "Smooth"], values=[heavy_right_frames, smooth_right_frames], name="Right Lane"),
        row=1, col=2
    )

    fig.update_layout(title_text="Traffic Proportion Analysis", showlegend=True)
    st.plotly_chart(fig)
