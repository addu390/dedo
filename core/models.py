from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models
import uuid
from taxi import settings
from django.shortcuts import reverse
from .constants import USER_TRIP_STATUS, TRIP_STATUS, AVAILABLE, REQUESTED


class User(AbstractUser):
    DRIVER = 'DRIVER'
    PASSENGER = 'PASSENGER'
    TYPES = ((DRIVER, DRIVER), (PASSENGER, PASSENGER))
    type = models.CharField(max_length=100, choices=TYPES, default=PASSENGER)
    current_location = models.PointField(null=True)
    status = models.CharField(max_length=100, choices=USER_TRIP_STATUS, default=AVAILABLE)


class Trip(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    source_address = models.CharField(max_length=255)
    source_location = models.PointField(null=True)
    destination_address = models.CharField(max_length=255)
    destination_location = models.PointField(null=True)
    passenger = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.DO_NOTHING,
                                  related_name="trip_passenger")
    driver = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.DO_NOTHING,
                               related_name="trip_driver")
    status = models.CharField(max_length=100, choices=TRIP_STATUS, default=REQUESTED)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('trip_detail', kwargs={'trip_id': self.id})
