import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
import tempfile
import pandas as pd
import plotly.express as px


def process_video(uploaded_file):
    
    if uploaded_file is not None:
        # Save uploaded file to temporary file
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_file.read())
        
        # Load the model
        try:
            model = YOLO('models/best.pt')
            st.success("Model loaded successfully!")
        except Exception as e:
            st.error(f"Error loading model: {str(e)}")
            return
        # Analysis parameters
        heavy_traffic_threshold = st.slider(
            "Heavy Traffic Threshold",
            min_value=1,
            max_value=5,
            value=2,
            help="Number of vehicles that indicates heavy traffic"
        )
        
        # Process button
        if st.button("Start Analysis"):
                # Reset frame data for new analysis
                st.session_state.frame_data = []
                
                # Define the positions for the text annotations on the image
                text_position_left_lane = (10, 50)
                text_position_right_lane = (820, 50)
                intensity_position_left_lane = (10, 100)
                intensity_position_right_lane = (820, 100)
                # Define font, scale, and colors for the annotations
                font = cv2.FONT_HERSHEY_SIMPLEX
                font_scale = 1
                font_color = (255, 0, 0)
                background_color = (0, 0, 255)
                # Define vertices and parameters
                vertices1 = np.array([(465, 350), (609, 350), (510, 630), (2, 630)], dtype=np.int32)
                vertices2 = np.array([(678, 350), (815, 350), (1203, 630), (743, 630)], dtype=np.int32)
                x1, x2 = 325, 635
                lane_threshold = 609
                # Video processing
                cap = cv2.VideoCapture(tfile.name)
                if not cap.isOpened():
                    st.error("Error opening video file")
                    return
                
                # Get original video dimensions
                frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                
                # Create progress bar and frame placeholder
                progress_bar = st.progress(0)
                frame_placeholder = st.empty()
                
                # Create placeholders for real-time analytics
                analytics_cols = st.columns(2)
                chart_placeholder_left = analytics_cols[0].empty()
                chart_placeholder_right = analytics_cols[1].empty()
                
                frame_count = 0
                total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        break
                    # Process frame
                    detection_frame = frame.copy()
                    detection_frame[:x1, :] = 0
                    detection_frame[x2:, :] = 0
                    
                    # Perform inference on the modified frame
                    results = model.predict(detection_frame, conf=0.4)
                    processed_frame = results[0].plot(line_width=1)
                    
                    # Restore the original top and bottom parts of the frame
                    processed_frame[:x1, :] = frame[:x1, :].copy()
                    processed_frame[x2:, :] = frame[x2:, :].copy()
                    
                    # Draw the quadrilaterals
                    cv2.polylines(processed_frame, [vertices1], isClosed=True, color=(0, 255, 0), thickness=2)
                    cv2.polylines(processed_frame, [vertices2], isClosed=True, color=(255, 0, 0), thickness=2)
                    
                    # Count vehicles in each lane
                    bounding_boxes = results[0].boxes
                    vehicles_in_left_lane = 0
                    vehicles_in_right_lane = 0
                    for box in bounding_boxes.xyxy:
                        if box[0] < lane_threshold:
                            vehicles_in_left_lane += 1
                        else:
                            vehicles_in_right_lane += 1
                    # Determine traffic intensity
                    traffic_intensity_left = "Heavy" if vehicles_in_left_lane > heavy_traffic_threshold else "Smooth"
                    traffic_intensity_right = "Heavy" if vehicles_in_right_lane > heavy_traffic_threshold else "Smooth"
                    # Store frame data for analytics
                    st.session_state.frame_data.append({
                        "frame": frame_count,
                        "left_lane": vehicles_in_left_lane,
                        "right_lane": vehicles_in_right_lane,
                        "left_intensity": traffic_intensity_left,
                        "right_intensity": traffic_intensity_right
                    })
                    # Update real-time charts every 10 frames
                    if frame_count % 10 == 0 and len(st.session_state.frame_data) > 0:
                        df = pd.DataFrame(st.session_state.frame_data)
                        
                        # Left lane chart
                        fig_left = px.line(df, x="frame", y="left_lane", 
                                         title="Left Lane Traffic",
                                         labels={"frame": "Frame", "left_lane": "Vehicle Count"})
                        chart_placeholder_left.plotly_chart(fig_left, use_container_width=True)
                        
                        # Right lane chart
                        fig_right = px.line(df, x="frame", y="right_lane", 
                                          title="Right Lane Traffic",
                                          labels={"frame": "Frame", "right_lane": "Vehicle Count"})
                        chart_placeholder_right.plotly_chart(fig_right, use_container_width=True)
                    # Add text overlays to the frame
                    cv2.putText(processed_frame, f'Vehicles in Left Lane: {vehicles_in_left_lane}',
                              text_position_left_lane, font, font_scale, font_color, 2, cv2.LINE_AA)
                    cv2.putText(processed_frame, f'Traffic Intensity: {traffic_intensity_left}',
                              intensity_position_left_lane, font, font_scale, font_color, 2, cv2.LINE_AA)
                    cv2.putText(processed_frame, f'Vehicles in Right Lane: {vehicles_in_right_lane}',
                              text_position_right_lane, font, font_scale, font_color, 2, cv2.LINE_AA)
                    cv2.putText(processed_frame, f'Traffic Intensity: {traffic_intensity_right}',
                              intensity_position_right_lane, font, font_scale, font_color, 2, cv2.LINE_AA)
                    # Convert BGR to RGB for Streamlit
                    processed_frame_rgb = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)
                    
                    # Display the frame
                    frame_placeholder.image(processed_frame_rgb, channels="RGB", use_column_width=True)
                    
                    # Update progress
                    frame_count += 1
                    progress_bar.progress(min(frame_count / total_frames, 1.0))
                cap.release()
                st.success("Video processing completed!")