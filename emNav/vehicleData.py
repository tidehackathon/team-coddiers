def get_lat(vehicle):
    return vehicle.location.global_relative_frame.lat


def get_lon(vehicle):
    return vehicle.location.global_relative_frame.lon


def get_alt(vehicle):
    return vehicle.location.global_relative_frame.alt


def get_lon_alt(vehicle):
    return vehicle.location.global_relative_frame


def get_heading(vehicle):
    return vehicle.heading
