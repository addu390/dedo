from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from . import models


@admin.register(models.User)
class UserAdmin(DefaultUserAdmin):
    pass


@admin.register(models.Trip)
class TripAdmin(admin.ModelAdmin):
    fields = ('id', 'source_address', 'destination_address', 'status', 'driver', 'passenger', 'created_at', 'updated_at')
    list_display = ('id', 'source_address', 'destination_address', 'status', 'driver', 'passenger',
                    'created_at', 'updated_at',)
    list_filter = ('status',)
    readonly_fields = ('id', 'created_at', 'updated_at')
