import streamlit as st
import pandas as pd
import joblib
import os

# -------------------------------
# App Title
# -------------------------------
st.title("Intern Performance Prediction System")

# -------------------------------
# Load trained ML model safely
# (fixes Streamlit Cloud path issue)
# -------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # current file directory
model_path = os.path.join(BASE_DIR, "model.pkl")       # model file path

model = joblib.load(model_path)

# -------------------------------
# Input features from user
# -------------------------------
time = st.number_input("Task Completion Time")     # time taken to complete task
feedback = st.number_input("Feedback Rating")      # performance feedback score
attendance = st.number_input("Attendance")         # attendance percentage

# -------------------------------
# Prediction section
# -------------------------------
if st.button("Predict"):

    # convert inputs into model format
    input_data = [[time, feedback, attendance]]

    # make prediction using trained model
    prediction = model.predict(input_data)

    # show numeric prediction
    st.write("Predicted Performance:", round(prediction[0], 2))

    # classification logic
    if prediction[0] >= 0.7:
        st.success("Excellent ⭐")   # high performer
    elif prediction[0] >= 0.4:
        st.warning("Average ⚠️")     # medium performer
    else:
        st.error("Struggling ❌")    # low performer