import streamlit as st
import requests
import datetime
import pandas as pd

'''
# New York taxi fare estimator 
'''

'''
## Please, provide the following information:
'''
date = st.date_input(
    "Date",
    datetime.date(2021, 6, 4))

time = st.time_input('Time', datetime.time(8, 45))

pickup_longitude = st.text_input('Pickup longitude', -74.0059413)

pickup_latitude = st.text_input('Pickup latitude', 40.7127837)

dropoff_longitude = st.text_input('Dropoff longitude', -73.7822222222)

dropoff_latitude = st.text_input('Dropoff latitude', 40.6441666667)

passenger_count = st.selectbox('Number of passengers', range(1,9))

# Calling the API
taxifare_api_url = 'https://taxifare.lewagon.ai/predict'

params = {
        'key': '2013-07-06 17:18:00.000000119',
        "pickup_datetime": [f"{date} {time}"],
        "pickup_longitude": [float(pickup_longitude)],
        "pickup_latitude": [float(pickup_latitude)],
        "dropoff_longitude": [float(dropoff_longitude)],
        "dropoff_latitude": [float(dropoff_latitude)],
        "passenger_count": [int(passenger_count)]
    }

response = requests.get(
        taxifare_api_url,
        params=params
)

pred = response.json()

if st.button('Get fare'):
    st.write(f"${round(pred['prediction'], 1)}")

map_dict = dict(
    lat=[float(pickup_latitude), float(dropoff_latitude)],
    lon=[float(pickup_longitude), float(dropoff_longitude)]
)
   
st.map(pd.DataFrame(map_dict))