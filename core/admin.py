from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from . import models
from leaflet.admin import LeafletGeoAdmin


@admin.register(models.User)
class UserAdmin(DefaultUserAdmin):
    pass


@admin.register(models.Trip)
class TripAdmin(LeafletGeoAdmin):
    list_display = ('id', 'source_address', 'source_location', 'destination_address', 'destination_location',
                    'status', 'driver', 'passenger', 'created_at', 'updated_at',)
    list_filter = ('status',)
    readonly_fields = ('id', 'created_at', 'updated_at')
