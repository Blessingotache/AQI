import numpy as np
import streamlit as st
import pickle
import matplotlib.pyplot as plt

# Load Model
with open('air_quality_index.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit UI
st.title('Air Quality Prediction App')
st.write('This app helps assess **air quality** by analyzing pollutant levels (SO₂, NO₂, RSPM, and SPM).')
st.write('Fill in the details below and click Predict to see the air quality status:')

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
    AQI_colors = {'Good': 'green', 'Moderate': 'yellow', 'Poor': 'orange', 'Unhealthy': 'red', 'Very unhealthy': 'purple', 'Hazardous': 'maroon'}

    if isinstance(prediction[0], str):
        predicted_AQI = prediction[0]  # Use the label directly
    else:
        predicted_AQI = AQI_mapping.get(int(prediction[0]), 'Unknown')



    # Display results
    st.write(f'The predicted AQI is: {predicted_AQI}')

    # AQI interpretation messages
    AQI_messages = {
        'Good': "✅ Air quality is satisfactory, and air pollution poses little or no risk.",
        'Moderate': "🟡 Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution.",
        'Poor': "🟠 Members of sensitive groups may experience health effects. The general public is less likely to be affected.",
        'Unhealthy': "🔴 Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects.",
        'Very unhealthy': "🟣 Health alert: The risk of health effects is increased for everyone.",
        'Hazardous': "🚨 Health warnings of emergency conditions. Everyone is more likely to be affected."
    }

    # Display AQI category explanation
    st.write(AQI_messages.get(predicted_AQI, "⚠️ Unknown AQI category. Please check the model output."))

   
    # Chart
    fig, ax = plt.subplots()
    ax.bar([0], [1], color=AQI_colors.get(predicted_AQI, 'gray'))
    ax.set_ylabel('Air Quality Level')
    ax.set_title('AQI Prediction')
    ax.set_ylim(0, 1.5)
    ax.set_xticks([0])
    ax.set_xticklabels([predicted_AQI], fontsize=12)
    st.pyplot(fig)

    # Created 
    st.write(f'Created by: {"Blessing Otache"}')

