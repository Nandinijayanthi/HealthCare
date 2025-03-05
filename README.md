# HealthCare

## Overview
This is a **HealthCare** built using **Streamlit** and **Scikit-Learn**. The app allows users to input their health details and predicts whether they are diabetic or not based on a trained machine learning model.

## Features
- Interactive web interface built with **Streamlit**.
- Accepts user inputs such as glucose level, BMI, age, and other relevant medical data.
- Utilizes a **trained machine learning model** to predict diabetes.
- **Real-time predictions** with feature scaling applied.
- Accuracy around **75%**
- It consists of complete data analysis through matplolib,plotly,seaborne

## Technologies Used
- **Python**
- **Streamlit** (for UI and deployment)
- **Scikit-Learn** (for model training and feature scaling)
- **NumPy** (for numerical operations)
- **Pickle** (for model serialization)

## Dataset
The model was trained on a diabetes dataset containing medical information such as:
- Pregnancies
- Glucose Level
- Blood Pressure
- Skin Thickness
- Insulin Level
- BMI
- Diabetes Pedigree Function
- Age

## Installation and Setup
Follow these steps to run the app locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/diabetes-prediction-app.git
   cd diabetes-prediction-app
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run diabetes_app.py
   ```
   
## How It Works
1. The user provides medical details through the web app UI.
2. The input values are scaled using a **pre-trained scaler**.
3. The trained **machine learning model** predicts whether the user is diabetic or not.
4. The result is displayed in real-time.

## Future Improvements
- Enhance the model with better feature selection and optimization.
- Deploy the application on a cloud platform (e.g., Heroku, AWS, or Streamlit Sharing).
- Improve UI/UX with more interactive elements.

## Acknowledgments
- **Scikit-Learn** for providing easy-to-use machine learning tools.
- **Streamlit** for simplifying web app development.
- The dataset source for providing medical data for training.

---
**Author:** Nandini Jayanthi  
**GitHub:** [GitHub Profile](https://github.com/Nandinijayanthi/)

