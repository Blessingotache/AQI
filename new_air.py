import numpy as np
import streamlit as st
#Load Model
with open('air_quality.pkl', 'rb') as file:
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

#Prediction

if st.button('predict'):
    user_input = np.array([[Soi, Noi, Rpi, SPMi]])
    prediction = model.predict(user_input)
    
    AQI_mapping = {0: 'Good', 1: 'Hazardous', 2: 'Moderate', 3:'Poor', 4:'Unhealthy', 5:'Very unhealthy'}
    #st.write(prediction)
    
    predicted_AQI = AQI_mapping.get(int(prediction[0]), 'unknown')
    st.write(f'The predicted AQI is: {predicted_AQI}')