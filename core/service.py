from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from .models import User
from .constants import AVAILABLE, DRIVER


def get_available_drivers(latitude, longitude, radius):
    point = Point(latitude, longitude)
    drivers = User.objects \
        .filter(current_location__distance_lt=(point, Distance(km=radius))) \
        .filter(type=DRIVER) \
        .filter(status=AVAILABLE)
    return drivers
