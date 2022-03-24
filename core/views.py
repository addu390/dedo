from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from .serializers import UserSerializer, LoginSerializer, TripSerializer, UserLocationSerializer
from .models import Trip, User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from django.db import IntegrityError
from rest_framework import status


class Signup(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class Login(TokenObtainPairView):
    serializer_class = LoginSerializer


class UserLocation(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        user_id = request.user.id
        user_object = get_object_or_404(User, id=user_id)
        serializer = UserLocationSerializer(user_object, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TripRequest(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        user_id = request.user.id
        trip_request = request.data
        trip_request["source_user"] = user_id
        serializer = TripSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TripList(APIView):

    def get(self, request):
        user_id = request.user.id
        trips = Trip.objects.all()
        trip_objects = trips.filter(source_user=user_id)
        serializer = TripSerializer(trip_objects, many=True)
        return Response(serializer.data)


class TripDetail(APIView):

    def get(self, request, trip_id):
        trip_object = get_object_or_404(Trip, id=trip_id)
        serializer = TripSerializer(trip_object)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

