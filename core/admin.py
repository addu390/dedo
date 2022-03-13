from django.contrib import admin
from .models import Trip, User
from .constants import ASSIGNED, BUSY
from leaflet.admin import LeafletGeoAdmin
from .service import assign_driver


def start_ride(modeladmin, request, queryset):
    trips = queryset
    radius = 20
    for trip in trips:
        latitude = trip.source_location.coords[0]
        longitude = trip.source_location.coords[1]
        drivers = assign_driver(latitude, longitude, radius)
        if len(drivers) > 0:
            driver = drivers[0]
            User.objects.filter(id=driver.id).update(status=BUSY)
            queryset.update(driver=driver, status=ASSIGNED)


class UserAdmin(LeafletGeoAdmin):
    list_display = ('email', 'first_name', 'last_name', 'status', 'type')
    list_filter = ('type',)


class TripAdmin(LeafletGeoAdmin):
    list_display = ('source_user', 'destination_user', 'driver', 'source_address', 'destination_address', 'status')
    list_filter = ('status', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')
    actions = [start_ride]


admin.site.register(User, UserAdmin)
admin.site.register(Trip, TripAdmin)
