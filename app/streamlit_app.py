import requests
import streamlit as st
import pandas as pd
from constants import *
from utils import *
import os

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/predict")

GITHUB_URL = "https://github.com/hmmazuera/UK-Road-Accident-Severity-Prediction"
LINKEDIN_URL = "https://www.linkedin.com/in/mauricio-mazuera-a0a7a933b/"

st.set_page_config(
    page_title="UK Road Accident Severity Predictor",
    page_icon="🚗",
    layout="wide",
)

st.markdown(
    """
    <div style="background-color:#0E1117;padding:25px;border-radius:12px;margin-bottom:25px">
        <h1 style="color:white;margin-bottom:5px;">🚗 UK Road Accident Severity Predictor</h1>
        <p style="color:#D3D3D3;font-size:18px;">
        Machine Learning application trained on official UK Department for Transport road collision data.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.form("prediction_form"):

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🚦 Collision Details")

        collision_year = st.number_input("Collision Year", 2010, 2024, 2024)

        day_name = st.selectbox("Day of Week", list(DAY_CODES.keys()), index=1)
        day_of_week = DAY_CODES[day_name]

        hour = st.slider("Hour of Day", 0, 23, 12)
        month = st.slider("Month", 1, 12, 6)

        number_of_vehicles = st.number_input("Number of Vehicles", 1, 20, 2)
        number_of_casualties = st.number_input("Number of Casualties", 1, 20, 1)

        speed_limit = st.number_input("Speed Limit", 10.0, 100.0, 30.0)

    with col2:
        st.subheader("🌧️ Road & Environment")

        road_type_label = st.selectbox("Road Type", list(ROAD_TYPE_CODES.keys()), index=3)
        weather_label = st.selectbox("Weather Conditions", list(WEATHER_CODES.keys()), index=0)
        light_label = st.selectbox("Light Conditions", list(LIGHT_CODES.keys()), index=0)
        surface_label = st.selectbox("Road Surface", list(ROAD_SURFACE_CODES.keys()), index=0)
        area_label = st.selectbox("Area Type", list(URBAN_RURAL_CODES.keys()), index=0)

        road_type = ROAD_TYPE_CODES[road_type_label]
        weather_conditions = WEATHER_CODES[weather_label]
        light_conditions = LIGHT_CODES[light_label]
        road_surface_conditions = ROAD_SURFACE_CODES[surface_label]
        urban_or_rural_area = URBAN_RURAL_CODES[area_label]

    st.subheader("👥 People & Vehicles")

    col3, col4 = st.columns(2)

    with col3:
        average_driver_age = st.number_input("Average Driver Age", 0.0, 100.0, 40.0)
        max_driver_age = st.number_input("Maximum Driver Age", 0, 110, 50)
        average_vehicle_age = st.number_input("Average Vehicle Age", 0.0, 50.0, 6.0)
        max_vehicle_age = st.number_input("Maximum Vehicle Age", 0, 60, 10)

    with col4:
        average_casualty_age = st.number_input("Average Casualty Age", 0.0, 100.0, 35.0)
        max_casualty_age = st.number_input("Maximum Casualty Age", 0, 110, 35)
        pedestrian_count = st.number_input("Number of Pedestrians", 0, 20, 0)

        casualty_type_label = st.selectbox(
            "Most Common Casualty Type",
            list(CASUALTY_TYPE_CODES.keys()),
            index=3,
        )
        most_common_casualty_type = CASUALTY_TYPE_CODES[casualty_type_label]

    st.subheader("📍 Collision Location")

    col5, col6 = st.columns(2)

    with col5:
        latitude = st.number_input("Latitude", value=52.221299, format="%.6f")

    with col6:
        longitude = st.number_input("Longitude", value=-1.511123, format="%.6f")

    map_df = pd.DataFrame(
        {
            "lat": [latitude],
            "lon": [longitude],
        }
    )
    st.map(map_df, zoom=8)

    submitted = st.form_submit_button("Predict Severity")

if submitted:
    payload = build_payload(
        collision_year=collision_year,
        longitude=longitude,
        latitude=latitude,
        number_of_vehicles=number_of_vehicles,
        number_of_casualties=number_of_casualties,
        day_of_week=day_of_week,
        hour=hour,
        month=month,
        road_type=road_type,
        speed_limit=speed_limit,
        light_conditions=light_conditions,
        weather_conditions=weather_conditions,
        road_surface_conditions=road_surface_conditions,
        urban_or_rural_area=urban_or_rural_area,
        average_driver_age=average_driver_age,
        max_driver_age=max_driver_age,
        average_vehicle_age=average_vehicle_age,
        max_vehicle_age=max_vehicle_age,
        average_casualty_age=average_casualty_age,
        max_casualty_age=max_casualty_age,
        pedestrian_count=pedestrian_count,
        most_common_casualty_type=most_common_casualty_type,
    )

    try:
        response = requests.post(API_URL, json=payload, timeout=60)
        response.raise_for_status()
        result = response.json()

        label = result["prediction_label"]

        st.markdown("---")
        st.subheader("🎯 Prediction Result")

        if label == "Fatal":
            st.markdown(
                """
                <div style="background-color:#8B0000;padding:25px;border-radius:12px">
                    <h2 style="color:white;">🔴 Fatal</h2>
                    <p style="color:white;">The model predicts a fatal collision severity.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
        elif label == "Serious":
            st.markdown(
                """
                <div style="background-color:#FF8C00;padding:25px;border-radius:12px">
                    <h2 style="color:white;">🟠 Serious</h2>
                    <p style="color:white;">The model predicts a serious collision severity.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                """
                <div style="background-color:#2E8B57;padding:25px;border-radius:12px">
                    <h2 style="color:white;">🟢 Slight</h2>
                    <p style="color:white;">The model predicts a slight collision severity.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

        if result.get("probabilities"):
            st.subheader("📊 Prediction Probabilities")

            for severity, probability in result["probabilities"].items():
                st.write(f"{severity}: {probability:.2%}")
                st.progress(probability)

    except requests.exceptions.HTTPError as error:
        st.error(f"HTTP Error {error.response.status_code}")
        st.json(error.response.json())

    except requests.exceptions.RequestException as error:
        st.error("Could not connect to the prediction API.")
        st.write(error)

st.markdown("---")
st.markdown(
    f"""
    <div style="text-align:center;color:gray">
        Developed by Mauricio Mazuera · 
        <a href="{GITHUB_URL}" target="_blank">GitHub</a> · 
        <a href="{LINKEDIN_URL}" target="_blank">LinkedIn</a>
    </div>
    """,
    unsafe_allow_html=True,
)