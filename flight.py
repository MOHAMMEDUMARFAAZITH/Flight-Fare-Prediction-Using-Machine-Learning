import streamlit as st
import pickle
import pandas as pd 
import numpy as np
import datetime
import time

model = open('flight_rf.pkl','rb')
forest = pickle.load(model)

Departure_Date = st.date_input(
    "Departure Date",
    datetime.date(2019, 7, 6))
st.write('Departure Date:', Departure_Date)

Departure_Time = st.time_input(
"Departure_Time",datetime.time(8,45))
st.write('Departure Time:', Departure_Time)

Arrival_Date = st.date_input(
    "Arrival Date",
    datetime.date(2019, 7, 6))
st.write('Arrival Date:', Arrival_Date)

Arrival_Time = st.time_input(
"Arrival_Time",datetime.time(8,45))
st.write('Arrival Time:', Arrival_Time)