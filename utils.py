
from geopy.distance import geodesic

def calculate_distance_miles(user_location, cafe_location=(36.1627, -86.7816)):
    return round(geodesic(user_location, cafe_location).miles, 2)
