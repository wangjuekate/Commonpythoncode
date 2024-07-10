import math

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a)) 
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r

def find_closest_location(target_lat, target_lon, locations):
    """
    Find the closest location from a list of locations based on latitude and longitude.
    
    :param target_lat: Latitude of the target location
    :param target_lon: Longitude of the target location
    :param locations: List of tuples containing (latitude, longitude, location_name)
    :return: The closest location tuple (latitude, longitude, location_name)
    """
    closest_location = None
    min_distance = float('inf')
    
    for lat, lon, name in locations:
        distance = haversine(target_lon, target_lat, lon, lat)
        if distance < min_distance:
            min_distance = distance
            closest_location = (lat, lon, name)
    
    return closest_location

# Example usage
locations = [
    (34.0522, -118.2437, 'Los Angeles, CA'),
    (36.1699, -115.1398, 'Las Vegas, NV'),
    (37.7749, -122.4194, 'San Francisco, CA'),
    (40.7128, -74.0060, 'New York, NY')
]

target_lat = 34.0522
target_lon = -118.2437

closest_location = find_closest_location(target_lat, target_lon, locations)
print(f"The closest location is: {closest_location}")
