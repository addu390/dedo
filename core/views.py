from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from .serializers import UserSerializer, LoginSerializer, TripSerializer, UserLocationSerializer, TripModelSerializer
from .models import Trip, User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from django.db import IntegrityError
from rest_framework import status
from .constants import ASSIGNED, BUSY
from .service import get_available_drivers
from django.db.models import Q
import random


class Signup(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class Login(TokenObtainPairView):
    serializer_class = LoginSerializer


class UserDetails(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user_id = request.user.id
        user_object = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(user_object)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


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

        user_object = get_object_or_404(User, email=trip_request["destination_email"])
        trip_request["destination_user"] = user_object.id

        trip_request["source_pin"] = random.randint(1000, 9999)
        trip_request["destination_pin"] = random.randint(1000, 9999)
        serializer = TripModelSerializer(data=trip_request)

        if serializer.is_valid(raise_exception=True):
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StartRequest(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, trip_id):
        trip_object = get_object_or_404(Trip, id=trip_id)
        radius = [3, 5, 10, 17, 25]

        latitude = trip_object.source_location.coords[0]
        longitude = trip_object.source_location.coords[1]
        for r in radius:
            drivers = get_available_drivers(latitude, longitude, r)
            if len(drivers) > 0:
                driver = drivers[0]
                User.objects.filter(id=driver.id).update(status=BUSY)
                print("driver", driver.id)
                data = {"driver": driver.id, "status": ASSIGNED}
                serializer = TripSerializer(trip_object, data=data, partial=True)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data)
            else:
                return Response({"error": "No driver available"}, status=status.HTTP_400_BAD_REQUEST)


class TripList(APIView):

    def get(self, request):
        user_id = request.user.id
        trips = Trip.objects.all()
        trip_objects = trips.filter(Q(source_user=user_id) | Q(destination_user=user_id) | Q(driver=user_id))
        serializer = TripSerializer(trip_objects, many=True)
        return Response(serializer.data)


class TripDetail(APIView):

    def get(self, request, trip_id):
        trip_object = get_object_or_404(Trip, id=trip_id)
        serializer = TripSerializer(trip_object)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

