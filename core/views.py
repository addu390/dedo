from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from .serializers import UserSerializer, LoginSerializer, TripSerializer
from .models import Trip
from rest_framework_simplejwt.views import TokenObtainPairView


class Signup(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class Login(TokenObtainPairView):
    serializer_class = LoginSerializer


class TripRequest(TokenObtainPairView):
    serializer_class = TripSerializer


class TripList(generics.RetrieveAPIView):
    lookup_field = 'source_user'
    lookup_url_kwarg = 'user_id'
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class TripDetail(generics.RetrieveAPIView):
    lookup_field = 'id'
    lookup_url_kwarg = 'trip_id'
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

