from django.contrib import admin
from .models import Trip, User
from leaflet.admin import LeafletGeoAdmin


def start_ride(modeladmin, request, queryset):
    queryset.update(status='STARTED')


class UserAdmin(LeafletGeoAdmin):
    list_display = ('email', 'first_name', 'last_name', 'status', 'type')
    list_filter = ('type',)


class TripAdmin(LeafletGeoAdmin):
    list_display = ('driver', 'passenger', 'source_address', 'destination_address', 'status')
    list_filter = ('status', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')
    actions = [start_ride]


admin.site.register(User, UserAdmin)
admin.site.register(Trip, TripAdmin)
