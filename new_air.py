import numpy as np
import streamlit as st
import pickle
import matplotlib.pyplot as plt

# Load Model
with open('air_quality_index.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit UI
st.title('Air Quality Prediction App')
st.write('This app predicts the **Air Quality** type!')
st.write('Please input the following parameters:')

# Input form
Soi = st.number_input('Sulphur Dioxide (SO₂) [Soi]')
Noi = st.number_input('Nitrogen Dioxide (NO₂) [Noi]')
Rpi = st.number_input('Respirable Suspended Particulate Matter (RSPM) [Rpi]')
SPMi = st.number_input('Suspended Particulate Matter (SPM) [SPMi]')

# Prediction
if st.button('Predict'):
    user_input = np.array([[Soi, Noi, Rpi, SPMi]])
    prediction = model.predict(user_input)

    st.write(f"Raw model output: {prediction}")  # Debugging step

    # AQI Mapping and Colors
    AQI_mapping = {0: 'Good', 1: 'Hazardous', 2: 'Moderate', 3: 'Poor', 4: 'Unhealthy', 5: 'Very unhealthy'}
    AQI_colors = {'Good': 'green', 'Moderate': 'lightgreen', 'Poor': 'orange', 'Unhealthy': 'darkorange', 'Very unhealthy': 'red', 'Hazardous': 'darkred'}

    if isinstance(prediction[0], str):
        predicted_AQI = prediction[0]  # Use the label directly
    else:
        predicted_AQI = AQI_mapping.get(int(prediction[0]), 'Unknown')

    # Display results
    st.write(f'The predicted AQI is: {predicted_AQI}')
    st.write(f"Sulphur Dioxide (SO₂) [Soi]: {Soi}")
    st.write(f"Nitrogen Dioxide (NO₂) [Noi]: {Noi}")
    st.write(f"Respirable Suspended Particulate Matter (RSPM) [Rpi]: {Rpi}")
    st.write(f"Suspended Particulate Matter (SPM) [SPMi]: {SPMi}")

    # Chart
    fig, ax = plt.subplots()
    ax.bar([0], [1], color=AQI_colors.get(predicted_AQI, 'gray'))
    ax.set_ylabel('Air Quality Level')
    ax.set_title('AQI Prediction')
    ax.set_ylim(0, 1.5)
    ax.set_xticks([0])
    ax.set_xticklabels([predicted_AQI], fontsize=12)
    st.pyplot(fig)



