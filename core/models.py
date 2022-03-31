from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models
import uuid
from taxi import settings
from django.shortcuts import reverse
from .constants import USER_TRIP_STATUS, TRIP_STATUS, USER_TYPE, AVAILABLE, REQUESTED, CUSTOMER, OTHERS, ITEM_TYPE


class User(AbstractUser):
    type = models.CharField(max_length=100, choices=USER_TYPE, default=CUSTOMER)
    current_location = models.PointField(null=True)
    status = models.CharField(max_length=100, choices=USER_TRIP_STATUS, default=AVAILABLE)


class Trip(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=100, choices=TRIP_STATUS, default=REQUESTED)

    item_type = models.CharField(max_length=100, choices=ITEM_TYPE, default=OTHERS)

    source_address = models.CharField(max_length=255)
    destination_address = models.CharField(max_length=255)

    source_location = models.PointField(null=True)
    destination_location = models.PointField(null=True)

    source_user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.DO_NOTHING,
                                    related_name="trip_source_user")
    destination_user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.DO_NOTHING,
                                         related_name="trip_destination_user")

    source_pin = models.CharField(max_length=10, null=True)
    destination_pin = models.CharField(max_length=10, null=True)

    driver = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.DO_NOTHING,
                               related_name="trip_driver")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('trip_detail', kwargs={'trip_id': self.id})
