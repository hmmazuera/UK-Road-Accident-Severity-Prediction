import requests
import streamlit as st


API_URL = "http://127.0.0.1:8000/predict"


DAY_CODES = {
    "Sunday": 1,
    "Monday": 2,
    "Tuesday": 3,
    "Wednesday": 4,
    "Thursday": 5,
    "Friday": 6,
    "Saturday": 7,
}


ROAD_TYPE_CODES = {
    "Roundabout": 1,
    "One way street": 2,
    "Dual carriageway": 3,
    "Single carriageway": 6,
    "Slip road": 7,
    "Unknown": 9,
}


WEATHER_CODES = {
    "Fine no high winds": 1,
    "Raining no high winds": 2,
    "Snowing no high winds": 3,
    "Fine with high winds": 4,
    "Raining with high winds": 5,
    "Snowing with high winds": 6,
    "Fog or mist": 7,
    "Other": 8,
    "Unknown": 9,
}


LIGHT_CODES = {
    "Daylight": 1,
    "Darkness - lights lit": 4,
    "Darkness - lights unlit": 5,
    "Darkness - no lighting": 6,
    "Darkness - lighting unknown": 7,
}


ROAD_SURFACE_CODES = {
    "Dry": 1,
    "Wet or damp": 2,
    "Snow": 3,
    "Frost or ice": 4,
    "Flood over 3cm": 5,
    "Oil or diesel": 6,
    "Mud": 7,
}


URBAN_RURAL_CODES = {
    "Urban": 1,
    "Rural": 2,
}


CASUALTY_TYPE_CODES = {
    "Pedestrian": 0,
    "Cyclist": 1,
    "Motorcyclist": 5,
    "Car occupant": 9,
    "Bus/coach occupant": 11,
    "Goods vehicle occupant": 19,
}


def get_season(month: int) -> str:
    if month in [12, 1, 2]:
        return "Winter"
    if month in [3, 4, 5]:
        return "Spring"
    if month in [6, 7, 8]:
        return "Summer"
    return "Autumn"


def build_payload(
    collision_year,
    longitude,
    latitude,
    number_of_vehicles,
    number_of_casualties,
    day_of_week,
    hour,
    month,
    road_type,
    speed_limit,
    light_conditions,
    weather_conditions,
    road_surface_conditions,
    urban_or_rural_area,
    average_driver_age,
    maximum_driver_age,
    average_vehicle_age,
    maximum_vehicle_age,
    average_casualty_age,
    maximum_casualty_age,
    pedestrian_count,
    most_common_casualty_type,
):
    weekend = 1 if day_of_week in [1, 7] else 0
    rush_hour = 1 if hour in [7, 8, 9, 16, 17, 18] else 0
    season = get_season(month)

    return {
        "collision_year": collision_year,
        "location_easting_osgr": 433493.0,
        "location_northing_osgr": 258232.0,
        "longitude": longitude,
        "latitude": latitude,
        "police_force": 23,
        "number_of_vehicles": number_of_vehicles,
        "number_of_casualties": number_of_casualties,
        "day_of_week": day_of_week,
        "first_road_class": 3,
        "road_type": road_type,
        "speed_limit": speed_limit,
        "junction_detail": 0,
        "junction_control": -1,
        "second_road_class": 0,
        "pedestrian_crossing": 0,
        "light_conditions": light_conditions,
        "weather_conditions": weather_conditions,
        "road_surface_conditions": road_surface_conditions,
        "special_conditions_at_site": 0,
        "carriageway_hazards": 0,
        "urban_or_rural_area": urban_or_rural_area,
        "did_police_officer_attend_scene_of_accident": 1,
        "trunk_road_flag": 2,
        "average_driver_age": average_driver_age,
        "maximum_driver_age": maximum_driver_age,
        "average_vehicle_age": average_vehicle_age,
        "maximum_vehicle_age": maximum_vehicle_age,
        "left_hand_drive_count": number_of_vehicles,
        "average_casualty_age": average_casualty_age,
        "maximum_casualty_age": maximum_casualty_age,
        "casualty_count": number_of_casualties,
        "pedestrian_count": pedestrian_count,
        "most_common_casualty_type": most_common_casualty_type,
        "hour": hour,
        "month": month,
        "weekend": weekend,
        "rush_hour": rush_hour,
        "season": season,
    }


st.set_page_config(
    page_title="UK Road Accident Severity Predictor",
    page_icon="🚗",
    layout="wide",
)


st.title("🚗 UK Road Accident Severity Predictor")

st.write(
    "Predict the severity of a road traffic collision using a machine learning model "
    "trained on official UK Department for Transport data."
)


with st.form("prediction_form"):

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Collision Details")

        collision_year = st.number_input(
            "Collision Year",
            min_value=2010,
            max_value=2024,
            value=2024,
        )

        day_name = st.selectbox("Day of Week", list(DAY_CODES.keys()), index=1)
        day_of_week = DAY_CODES[day_name]

        hour = st.slider("Hour of Day", 0, 23, 12)
        month = st.slider("Month", 1, 12, 6)

        number_of_vehicles = st.number_input(
            "Number of Vehicles",
            min_value=1,
            max_value=20,
            value=2,
        )

        number_of_casualties = st.number_input(
            "Number of Casualties",
            min_value=1,
            max_value=20,
            value=1,
        )

        speed_limit = st.number_input(
            "Speed Limit",
            min_value=10.0,
            max_value=100.0,
            value=30.0,
        )

    with col2:
        st.subheader("Road & Environment")

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

    st.subheader("People & Vehicles")

    col3, col4 = st.columns(2)

    with col3:
        average_driver_age = st.number_input("Average Driver Age", 0.0, 100.0, 40.0)
        maximum_driver_age = st.number_input("Maximum Driver Age", 0, 110, 50)
        average_vehicle_age = st.number_input("Average Vehicle Age", 0.0, 50.0, 6.0)
        maximum_vehicle_age = st.number_input("Maximum Vehicle Age", 0, 60, 10)

    with col4:
        average_casualty_age = st.number_input("Average Casualty Age", 0.0, 100.0, 35.0)
        maximum_casualty_age = st.number_input("Maximum Casualty Age", 0, 110, 35)
        pedestrian_count = st.number_input("Number of Pedestrians", 0, 20, 0)

        casualty_type_label = st.selectbox(
            "Most Common Casualty Type",
            list(CASUALTY_TYPE_CODES.keys()),
            index=3,
        )

        most_common_casualty_type = CASUALTY_TYPE_CODES[casualty_type_label]

    with st.expander("Advanced location settings"):
        longitude = st.number_input("Longitude", value=-1.511123, format="%.6f")
        latitude = st.number_input("Latitude", value=52.221299, format="%.6f")

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
        maximum_driver_age=maximum_driver_age,
        average_vehicle_age=average_vehicle_age,
        maximum_vehicle_age=maximum_vehicle_age,
        average_casualty_age=average_casualty_age,
        maximum_casualty_age=maximum_casualty_age,
        pedestrian_count=pedestrian_count,
        most_common_casualty_type=most_common_casualty_type,
    )

    try:
        response = requests.post(API_URL, json=payload, timeout=10)
        response.raise_for_status()

        result = response.json()

        label = result["prediction_label"]

        if label == "Fatal":
            st.error("🔴 Predicted Severity: Fatal")
        elif label == "Serious":
            st.warning("🟠 Predicted Severity: Serious")
        else:
            st.success("🟢 Predicted Severity: Slight")

        st.write(f"Prediction Code: `{result['prediction_code']}`")

        if result.get("probabilities"):
            st.subheader("Prediction Probabilities")
            st.bar_chart(result["probabilities"])

    except requests.exceptions.RequestException as error:
        st.error("Could not connect to the prediction API.")
        st.write(error)