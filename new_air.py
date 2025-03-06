import numpy as np
import streamlit as st
import pickle
#Load Model
with open('air_quality_index.pkl', 'rb') as file:
    model = pickle.load(file)

    #streamlit UI

st.title('Air Quality Prediction App')
st.write('This app predicts the **Air Quality** type!')
st.write('Please input the following parameters:')

#Input form

Soi=st.number_input('Soi')
Noi=st.number_input('Noi')
Rpi=st.number_input('Rpi')
SPMi=st.number_input('SPMi')

# Prediction
if st.button('Predict'):
    user_input = np.array([[Soi, Noi, Rpi, SPMi]])
    prediction = model.predict(user_input)

    st.write(f"Raw model output: {prediction}")  # Debugging step

    # Check if the model is returning a string label
    if isinstance(prediction[0], str):
        predicted_AQI = prediction[0]  # Use the label directly
    else:
        AQI_mapping = {0: 'Good', 1: 'Hazardous', 2: 'Moderate', 3: 'Poor', 4: 'Unhealthy', 5: 'Very unhealthy'}
        predicted_AQI = AQI_mapping.get(int(prediction[0]), 'Unknown')

    st.write(f'The predicted AQI is: {predicted_AQI}')
