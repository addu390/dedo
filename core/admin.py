from django.contrib import admin
from .models import Trip, User
from .constants import ASSIGNED, BUSY
from leaflet.admin import LeafletGeoAdmin
from .service import get_available_drivers


def start_ride(modeladmin, request, queryset):
    trips = queryset
    radius = [3, 5, 10, 17, 25]
    for trip in trips:
        latitude = trip.source_location.coords[0]
        longitude = trip.source_location.coords[1]
        for r in radius:
            drivers = get_available_drivers(latitude, longitude, r)
            if len(drivers) > 0:
                driver = drivers[0]
                User.objects.filter(id=driver.id).update(status=BUSY)
                queryset.update(driver=driver, status=ASSIGNED)
                break


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
