# 🧠 Mental Health Treatment Prediction

A machine learning web application that predicts whether a person may require mental health treatment based on survey responses.

The model analyzes user inputs and provides a prediction along with confidence and helpful suggestions. This project demonstrates the complete machine learning pipeline including data preprocessing, model training, and deployment using Streamlit.

---

## 🚀 Live Application

Try the deployed application here:

https://mental-health-treatment-prediction-4togpeymspnofgei9d2whr.streamlit.app/

---

## 📌 Project Overview

Mental health awareness has become increasingly important in modern workplaces. This project uses machine learning techniques to predict whether an individual might need mental health treatment based on various factors such as age, family history, work interference, and employer support.

The goal is to demonstrate how AI can assist in identifying potential mental health concerns.

---

## 📊 Dataset

Dataset used: **Mental Health Survey Dataset (Kaggle)**

The dataset contains responses related to:

- Age
- Gender
- Family history of mental illness
- Work interference due to mental health
- Employer mental health benefits
- Treatment history

The dataset was cleaned and preprocessed before training the machine learning models.

---

## 🤖 Machine Learning Models Used

Two models were trained and evaluated:

- Logistic Regression
- Random Forest Classifier

The **Random Forest model** was selected for deployment due to better performance.

**Model Accuracy:** ~74%

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
- Git & GitHub

---

## ⚙️ Features

- Interactive web interface
- Real-time prediction
- Prediction confidence score
- Mental health recommendations
- Cloud deployment using Streamlit

---

## 📂 Project Structure
mental-health-treatment-prediction
│
├── app.py
├── model.pkl
├── requirements.txt
├── Mental_Health.ipynb
├── Mental Health Dataset.csv
└── README.md

---

## 🖥️ How to Run Locally

Clone the repository
git clone https://github.com/aasrithanarra/mental-health-treatment-prediction.git

Navigate to the project folder
cd mental-health-treatment-prediction

Install dependencies
pip install -r requirements.txt

Run the Streamlit application
streamlit run app.py

---

## ⚠️ Disclaimer

This application is intended for educational purposes only.  
It does **not provide medical diagnosis** and should not replace professional mental health consultation.

---

## 👩‍💻 Author

**Aasritha Narra**  
B.Tech – Computer Science (AI & ML)

GitHub:  
https://github.com/aasrithanarra

---

## 🌟 Future Improvements

- Improve model accuracy with additional features
- Add more mental health indicators
- Improve UI/UX design
- Deploy using Docker or other cloud platforms
