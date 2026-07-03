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
    max_driver_age,
    average_vehicle_age,
    max_vehicle_age,
    average_casualty_age,
    max_casualty_age,
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
        "max_driver_age": max_driver_age,
        "average_vehicle_age": average_vehicle_age,
        "max_vehicle_age": max_vehicle_age,
        "left_hand_drive_count": number_of_vehicles,
        "average_casualty_age": average_casualty_age,
        "max_casualty_age": max_casualty_age,
        "casualty_count": number_of_casualties,
        "pedestrian_count": pedestrian_count,
        "most_common_casualty_type": most_common_casualty_type,
        "hour": hour,
        "month": month,
        "weekend": weekend,
        "rush_hour": rush_hour,
        "season": season,
    }
