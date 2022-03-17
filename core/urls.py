from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('v1/signup', views.Signup.as_view(), name="Sign Up"),
    path('v1/login', views.Login.as_view(), name="Login"),
    path('v1/token/refresh', TokenRefreshView.as_view(), name="Token Refresh"),
    path('v1/trip', views.TripRequest.as_view(), name="Request Trip"),
    path('v1/trips/<user_id>', views.TripList.as_view(), name="Show Trips"),
    path('v1/trip/<uuid:trip_id>', views.TripDetail.as_view(), name="Trip Details")
]
