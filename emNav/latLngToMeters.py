from math import pi, sin, cos, sqrt, atan2


def lat_lon_to_meters(lat_1, lon_1, lat_2, lon_2):
    # Radius of earth in KM
    earth_radius = 6378.137
    d_lat = lat_2 * pi / 180 - lat_1 * pi / 180
    d_lon = lon_2 * pi / 180 - lon_1 * pi / 180
    a = sin(d_lat / 2) * sin(d_lat / 2) + cos(lat_1 * pi / 180) * cos(lat_2 * pi / 180) * sin(d_lon / 2) * sin(d_lon / 2)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    d = earth_radius * c
    # return in meters
    return d * 1000
