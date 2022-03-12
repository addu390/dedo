from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from . import serializers, models
from rest_framework_simplejwt.views import TokenObtainPairView


class SignupApiView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer


class LoginApiView(TokenObtainPairView):
    serializer_class = serializers.LoginSerializer


class TripStartView(TokenObtainPairView):
    serializer_class = serializers.TripSerializer


class TripApiView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Trip.objects.all()
    serializer_class = serializers.TripSerializer


class TripDetailApiView(generics.RetrieveAPIView):
    lookup_field = 'id'
    lookup_url_kwarg = 'trip_id'
    permission_classes = (permissions.IsAuthenticated, )
    queryset = models.Trip.objects.all()
    serializer_class = serializers.TripSerializer
