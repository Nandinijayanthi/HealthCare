import streamlit as st
import pickle
import numpy as np

# Load the trained model and scaler
with open("diabetes_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

def predict_diabetes(features):
    features_scaled = scaler.transform([features])  # Scale input
    prediction = model.predict(features_scaled)  # Predict
    return "Diabetic" if prediction[0] == 1 else "Not Diabetic"

def main():
    st.title("Diabetes Prediction App")
    st.write("Enter your health details to check if you have diabetes.")

    pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1)
    glucose = st.number_input("Glucose Level", min_value=0, max_value=200, value=100)
    blood_pressure = st.number_input("Blood Pressure (mm Hg)", min_value=0, max_value=150, value=70)
    skin_thickness = st.number_input("Skin Thickness (mm)", min_value=0, max_value=100, value=20)
    insulin = st.number_input("Insulin Level (mu U/ml)", min_value=0, max_value=1000, value=80)
    bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0)
    diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
    age = st.number_input("Age", min_value=0, max_value=120, value=30)

    if st.button("Predict"):
        features = np.array([pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age])
        result = predict_diabetes(features)
        st.write(f"Prediction: **{result}**")

if __name__ == "__main__":
    main()
