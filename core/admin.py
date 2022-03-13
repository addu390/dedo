from django.contrib import admin
from .models import Trip, User
from leaflet.admin import LeafletGeoAdmin


def start_ride(modeladmin, request, queryset):
    queryset.update(status='STARTED')


class TripAdmin(LeafletGeoAdmin):
    list_display = ('id', 'source_address', 'source_location', 'destination_address', 'destination_location',
                    'status', 'driver', 'passenger', 'created_at', 'updated_at',)
    list_filter = ('status',)
    readonly_fields = ('id', 'created_at', 'updated_at')
    actions = [start_ride]


admin.site.register(User)
admin.site.register(Trip, TripAdmin)
