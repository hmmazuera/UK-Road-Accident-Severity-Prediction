from api.prediction import predict_collision_severity


sample_input = {
    "collision_year": 2020,
    "location_easting_osgr": 433493.0,
    "location_northing_osgr": 258232.0,
    "longitude": -1.511123,
    "latitude": 52.221299,
    "police_force": 23,
    "number_of_vehicles": 5,
    "number_of_casualties": 2,
    "day_of_week": 2,
    "first_road_class": 1,
    "road_type": 3,
    "speed_limit": 70.0,
    "junction_detail": 0,
    "junction_control": -1,
    "second_road_class": 0,
    "pedestrian_crossing": 0,
    "light_conditions": 6,
    "weather_conditions": 1,
    "road_surface_conditions": 1,
    "special_conditions_at_site": 4,
    "carriageway_hazards": 13,
    "urban_or_rural_area": 2,
    "did_police_officer_attend_scene_of_accident": 1,
    "trunk_road_flag": 1,
    "average_driver_age": 49.2,
    "max_driver_age": 64,
    "average_vehicle_age": 6.4,
    "max_vehicle_age": 14,
    "left_hand_drive_count": 5,
    "average_casualty_age": 42.0,
    "max_casualty_age": 48,
    "casualty_count": 2,
    "pedestrian_count": 0,
    "most_common_casualty_type": 9,
    "hour": 23,
    "month": 9,
    "weekend": 0,
    "rush_hour": 0,
    "season": "Autumn"
}


result = predict_collision_severity(sample_input)

print(result)