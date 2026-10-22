import streamlit as st
import joblib
import pandas as pd

# Load the medical model
model = joblib.load('heart_attack_model.pkl')

st.title("🏥 HeartGuard AI — Heart Attack Detector")
st.write("Enter patient medical metrics to diagnose heart status:")

# User Input Fields (6 features)
age = st.slider("Patient Age", 1, 100, 45)
gender = st.selectbox("Gender", ["Female", "Male"])
cp = st.selectbox("Chest Pain Severity Level", ["0: No Pain", "1: Light Pain", "2: Medium Pain", "3: Severe Pain"])
bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 220, 120)
chol = st.number_input("Serum Cholesterol (mg/dl)", 100, 600, 200)
hr = st.slider("Maximum Heart Rate Achieved", 60, 220, 150)

# Format Inputs for English Model
sex_value = 1 if gender == "Male" else 0
cp_value = int(cp.split(":")[0])

input_data = pd.DataFrame([{
    'age': age,
    'sex': sex_value,
    'chest_pain_type': cp_value,
    'resting_blood_pressure': bp,
    'cholesterol': chol,
    'max_heart_rate': hr
}])

# Prediction Button with Pure English Professional Outputs
if st.button("Run Heart Diagnosis"):
    prediction = model.predict(input_data)
    if prediction == 1:
        st.error("🚨 CRITICAL ALERT: Heart attack detected! Emergency medical attention required immediately. Please rush the patient to the hospital!")
    else:
        st.success("✅ DIAGNOSIS CLEAR: The patient is safe. No signs of a heart attack detected.")
