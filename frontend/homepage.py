import streamlit as st
import requests

URL_PATH = "http://127.0.0.1:8000"
ENDPOINT = "/predict"
FULL_URL = URL_PATH + ENDPOINT

st.title("House Price Prediction App")

st.divider()

st.write("Please fill the fields below to get a prediction")

st.divider()

longitude = st.number_input("Longitude", 
                            min_value=float(-124.35), 
                            max_value=float(-114.31), 
                            value=float(-119.00))
latitude = st.number_input("Longitude", 
                            min_value=float(32.54), 
                            max_value=float(41.95), 
                            value=float(37.25))
housing_median_age = st.number_input("Housing_median_age", 
                            min_value=float(1), 
                            max_value=float(52), 
                            value=float(26.5))
total_rooms = st.number_input("Total_rooms", 
                            min_value=float(2.00), 
                            max_value=float(39320), 
                            value=float(19661))
total_bedrooms = st.number_input("Total_bedrooms", 
                            min_value=float(1.00), 
                            max_value=float(6445.00), 
                            value=float(3223.00))
population = st.number_input("Population", 
                            min_value=float(3.00), 
                            max_value=float(35682.00), 
                            value=float(17842.50))
household = st.number_input("Household", 
                            min_value=float(1.00), 
                            max_value=float(6082.00), 
                            value=float(3041.5))
median_income = st.number_input("Median_income", 
                            min_value=float(0.499), 
                            max_value=float(15.00), 
                            value=float(7.750))

st.divider()

if st.button("Predict median house value"):
    
    payload = {
    "longitude":longitude,
    "latitude":latitude,
    "housing_median_age":housing_median_age,
    "total_rooms":total_rooms,
    "total_bedrooms":total_bedrooms,
    "population":population,
    "household":household,
    "median_income":median_income,
    }

    response = requests.post(
        FULL_URL,
        json = payload
    )

    if response.status_code == 200:
        prediction = response.json()
        st.success(f"Median house value: {prediction['prediction']:.2f}")

