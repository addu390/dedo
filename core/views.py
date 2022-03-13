from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from .serializers import UserSerializer, LoginSerializer, TripSerializer
from .models import User, Trip
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from rest_framework_simplejwt.views import TokenObtainPairView


class Signup(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class Login(TokenObtainPairView):
    serializer_class = LoginSerializer


class TripRequest(TokenObtainPairView):
    serializer_class = TripSerializer


class TripList(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class TripDetail(generics.RetrieveAPIView):
    lookup_field = 'id'
    lookup_url_kwarg = 'trip_id'
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class DriverSearch(generics.RetrieveAPIView):
    lat = 52.5
    lng = 1.0
    radius = 10
    point = Point(lng, lat)
    User.objects.filter(current_location__distance_lt=(point, Distance(km=radius)))
