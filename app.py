import streamlit as st 
import numpy as np
import pandas as pd 
import pickle

# Load the model
model = pickle.load(open('model.pkl','rb'))

## making the streamlit app
st.title("Student Package Predictor")
st.write("This app predicts your package using your CGPA and IQ data")

cgpa = st.number_input("Enter your CGPA: ", min_value=0.0, max_value=10.0, step=0.1)
iq = st.number_input("Enter your IQ: ", min_value=70, max_value=200, step=1)

# Capture the button click
predict_clicked = st.button("Predict Package")

# Only predict when the button is clicked
if predict_clicked:
    
    if iq > 70 and cgpa > 0:
        input_data = np.array([[cgpa, iq]])
        print(input_data)
        prediction = model.predict(input_data)
        print(prediction)

         # Display the result
        if prediction == 1:
            st.success("Congrats!! You are likely to be placed")
        else:
            st.error("Work harder to get better results")
    else:
        st.error("Enter valid input")