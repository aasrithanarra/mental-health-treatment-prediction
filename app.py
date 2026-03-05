import streamlit as st
import pandas as pd
import joblib
import os

# Page config
st.set_page_config(page_title="Mental Health Treatment Predictor", page_icon="🧠")

st.title("Mental Health Treatment Prediction")

st.write("Enter the details below to check if mental health treatment may be needed.")

# Load model
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model = joblib.load(model_path)

# Inputs
age = st.number_input("Age", 18, 100, 25)

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

# Convert to numeric
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

# Create input dictionary
input_dict = {
    "Age": age,
    "Gender": gender,
    "family_history": family_history,
    "work_interfere": work_interfere,
    "benefits": benefits
}

# Convert to dataframe
input_data = pd.DataFrame([input_dict])

# Ensure column order matches training data
input_data = input_data.reindex(columns=model.feature_names_in_)

# Prediction
if st.button("Predict Treatment Need"):

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1]

    if prediction[0] == 1:
        st.error("⚠️ The model predicts that mental health treatment may be required.")
    else:
        st.success("✅ The model predicts that treatment may not be required.")

    st.write(f"Prediction Confidence: **{probability*100:.2f}%**")

    st.subheader("Suggestions")

    if prediction[0] == 1:
        st.write("- Consider speaking with a mental health professional.")
        st.write("- Practice relaxation techniques like meditation.")
        st.write("- Maintain a balanced work-life schedule.")
    else:
        st.write("- Maintain a healthy routine.")
        st.write("- Stay socially connected.")
        st.write("- Monitor stress levels regularly.")