from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from taxi import settings
from django.shortcuts import reverse


class User(AbstractUser):
    pass


class Trip(models.Model):
    REQUESTED = 'REQUESTED'
    STARTED = 'STARTED'
    IN_PROGRESS = 'IN_PROGRESS'
    COMPLETED = 'COMPLETED'
    STATUSES = ((REQUESTED, REQUESTED), (STARTED, STARTED), (IN_PROGRESS, IN_PROGRESS), (COMPLETED, COMPLETED))
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    source_address = models.CharField(max_length=255)
    destination_address = models.CharField(max_length=255)
    passenger = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.DO_NOTHING,
                                  related_name="trip_passenger")
    driver = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.DO_NOTHING,
                               related_name="trip_driver")
    status = models.CharField(max_length=100, choices=STATUSES, default=REQUESTED)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('trip_detail', kwargs={'trip_id': self.id})
