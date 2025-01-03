# **🚦 Traffic-Density Analysis System**  
**Real-time Vehicle Detection & Traffic Analysis**


## **📝 About This Project**  
The **Traffic-Density Analysis System** leverages the power of advanced YOLOv8 technology to provide real-time vehicle detection and comprehensive traffic pattern analysis. This project uses a **model trained on a custom dataset**, which is publicly available on Roboflow:  
🌐 [Vehicle Detection YOLOv8 Dataset](https://universe.roboflow.com/farzad/vehicle_detection_yolov8)  

### **🔄 Pre-processing**  
Each image in the dataset is carefully pre-processed and standardized to ensure consistency and high-quality training data for our model.  

### **🔢 Dataset Split**  
The dataset is meticulously split into:  
- **Training Set:** 536 images for model training with diverse scenarios.  
- **Validation Set:** 90 images for unbiased model performance evaluation.  

Designed to monitor two lanes simultaneously, the system delivers instant insights into traffic density and flow patterns, facilitating smarter traffic management solutions.

---

## **⚙️ Features**

### **🚗 Real-time Detection**  
- Utilizes the **YOLOv8 algorithm** for accurate vehicle detection and counting in real-time.  
- Supports monitoring of multiple lanes simultaneously.  

### **📊 Traffic Analysis**  
- Comprehensive analysis of traffic patterns and density.  
- Enables data-driven insights to optimize traffic flow.  

### **📈 Dynamic Updates**  
- Live updates and visualization of traffic intensity.  
- Real-time vehicle distribution monitoring for better awareness.  

---
## **Datasets used for model training ** 


---
## **🔗 Links**  
- **GitHub Repository:** [Traffic-Density Analysis System](https://github.com/Sukhman123preet/Traffic-density-analysis)  
- **Live Deployment:** [Traffic-Density Analysis System Live](https://traffic-density-analysis.onrender.com/)

---

## **🛠️ Installation and Usage**

1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/Sukhman123preet/Traffic-density-analysis.git
   cd Traffic-density-analysis

2. **Install Dependencies:**  
   ```bash
   pip install -r requirements.txt

3. **Run the project:**  
   ```bash
   streamlit run main.py
