import streamlit as st   # for creating web app UI
import pandas as pd      # for data handling (not heavily used here)
import pickle            # for loading saved ML model

# Load the trained machine learning model
import streamlit as st

st.title("App is working environment check ✔")
st.write("Dependencies installed correctly.")

# App title displayed on web page
st.title("Intern Performance Prediction System")

# User input fields
time = st.number_input("Task Completion Time")   # input: time taken
feedback = st.number_input("Feedback Rating")    # input: feedback score
attendance = st.number_input("Attendance")       # input: attendance %

# Run prediction when button is clicked
if st.button("Predict"):
    
    # Prepare input in required format (2D array)
    input_data = [[time, feedback, attendance]]
    
    # Predict performance using trained model
    prediction = model.predict(input_data)

    # Display numeric prediction (rounded to 2 decimals)
    st.write("Predicted Performance:", round(prediction[0], 2))

    # Convert prediction into readable category
    if prediction[0] >= 0.7:
        st.success("Excel ⭐")          # high performance
    elif prediction[0] >= 0.4:
        st.warning("Average ⚠️")       # medium performance
    else:
        st.error("Struggling ❌")      # low performance