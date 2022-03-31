from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView
from django.contrib import admin


urlpatterns = [
    path('v1/signup', views.Signup.as_view(), name="Sign Up"),
    path('v1/login', views.Login.as_view(), name="Login"),
    path('v1/token/refresh', TokenRefreshView.as_view(), name="Token Refresh"),
    path('v1/current-location', views.UserLocation.as_view(), name="Set current location"),
    path('v1/trip', views.TripRequest.as_view(), name="Request Trip"),
    path('v1/trips', views.TripList.as_view(), name="Show Trips"),
    path('v1/trip/<uuid:trip_id>', views.StartRequest.as_view(), name="Start Trip"),
    path('v1/trip/<uuid:trip_id>', views.TripDetail.as_view(), name="Trip Details")
]

admin.site.site_header = 'Dedo Administration Dashboard V1'
admin.site.index_title = 'Index'
admin.site.site_title = 'Dedo'
