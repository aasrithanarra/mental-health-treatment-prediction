import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("model.pkl")

st.title("Mental Health Treatment Prediction")

st.write("Fill the details below to predict if mental health treatment may be required.")

# Inputs
age = st.number_input("Age", 18, 100, 25)

gender = st.selectbox(
    "Gender",
    ["Male", "Female", "Other"]
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

# Convert inputs to numeric
gender = 1 if gender == "Male" else 0
family_history = 1 if family_history == "Yes" else 0
work_interfere = ["Never","Rarely","Sometimes","Often"].index(work_interfere)
benefits = 1 if benefits == "Yes" else 0

input_data = pd.DataFrame({
    "Age":[age],
    "Gender":[gender],
    "Family_History":[family_history],
    "Work_Interfere":[work_interfere],
    "Benefits":[benefits]
})

# Predict button
if st.button("Predict Treatment Need"):

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("The person may need mental health treatment.")
    else:
        st.success("The person may not require treatment currently.")