from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('v1/signup', views.SignupApiView.as_view(), name="Sign Up"),
    path('v1/login', views.LoginApiView.as_view(), name="Login"),
    path('v1/token/refresh', TokenRefreshView.as_view(), name="Token Refresh"),
    path('v1/trip', views.TripApiView.as_view(), name="Request Trip"),
    path('v1/trips', views.TripApiView.as_view(), name="Show Trips"),
    path('v1/trip/<uuid:trip_id>', views.TripDetailApiView.as_view(), name="Trip Details")
]
