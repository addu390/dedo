from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from .models import User


def assign_driver(latitude, longitude, radius):
    point = Point(longitude, latitude)
    User.objects.filter(current_location__distance_lt=(point, Distance(km=radius)))