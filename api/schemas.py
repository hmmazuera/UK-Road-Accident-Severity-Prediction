from pydantic import BaseModel
from typing import Dict, Optional

class CollisionInput(BaseModel):
    collision_year: int
    location_easting_osgr: float
    location_northing_osgr: float
    longitude: float
    latitude: float
    police_force: int
    number_of_vehicles: int
    number_of_casualties: int
    day_of_week: int
    first_road_class: int
    road_type: int
    speed_limit: float
    junction_detail: int
    junction_control: int
    second_road_class: int
    pedestrian_crossing: int
    light_conditions: int
    weather_conditions: int
    road_surface_conditions: int
    special_conditions_at_site: int
    carriageway_hazards: int
    urban_or_rural_area: int
    did_police_officer_attend_scene_of_accident: int
    trunk_road_flag: int
    average_driver_age: float
    max_driver_age: int
    average_vehicle_age: float
    max_vehicle_age: int
    left_hand_drive_count: int
    average_casualty_age: float
    max_casualty_age: int
    casualty_count: int
    pedestrian_count: int
    most_common_casualty_type: int
    hour: int
    month: int
    weekend: int
    rush_hour: int
    season: str

class PredictionOutput(BaseModel):
    prediction_code: int
    prediction_label: str
    probabilities: Optional[Dict[str, float]] = None

