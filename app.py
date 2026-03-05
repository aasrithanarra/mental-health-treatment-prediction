import streamlit as st
import pandas as pd
import joblib
import os

# Page configuration
st.set_page_config(page_title="Mental Health Treatment Predictor", page_icon="🧠")

st.title("Mental Health Treatment Prediction")
st.write("Fill in the details below to predict if mental health treatment may be required.")

# Load trained model
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model = joblib.load(model_path)

# User Inputs
age = st.number_input("Age", min_value=18, max_value=100, value=25)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

family_history = st.selectbox(
    "Family History of Mental Illness",
    ["Yes", "No"]
)

work_interfere = st.selectbox(
    "Does mental health interfere with work?",
    ["Never", "Rarely", "Sometimes", "Often"]
)

benefits = st.selectbox(
    "Does your employer provide mental health benefits?",
    ["Yes", "No", "Don't know"]
)

# Convert categorical inputs to numeric values
gender = 1 if gender == "Male" else 0
family_history = 1 if family_history == "Yes" else 0

work_map = {
    "Never": 0,
    "Rarely": 1,
    "Sometimes": 2,
    "Often": 3
}

benefits_map = {
    "No": 0,
    "Yes": 1,
    "Don't know": 2
}

work_interfere = work_map[work_interfere]
benefits = benefits_map[benefits]

# Prediction button
if st.button("Predict Treatment Need"):

    input_data = pd.DataFrame(
        [[age, gender, family_history, work_interfere, benefits]],
        columns=[
            "Age",
            "Gender",
            "family_history",
            "work_interfere",
            "benefits"
        ]
    )

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1]

    if prediction[0] == 1:
        st.error("⚠️ The model predicts that mental health treatment may be needed.")
    else:
        st.success("✅ The model predicts that treatment may not be required.")

    st.write(f"Prediction Confidence: **{probability*100:.2f}%**")

    st.subheader("Helpful Suggestions")
    
    if prediction[0] == 1:
        st.write("- Consider speaking with a mental health professional.")
        st.write("- Practice stress management techniques.")
        st.write("- Take regular breaks and maintain work-life balance.")
    else:
        st.write("- Maintain healthy lifestyle habits.")
        st.write("- Continue monitoring mental wellbeing.")
        st.write("- Stay socially connected with friends and family.")