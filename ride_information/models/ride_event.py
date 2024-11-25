from django.db import models
from ..models.ride import Ride


class RideEvent(models.Model):
    id_ride_event = models.IntegerField(primary_key=True)
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    created_at = models.DateField()
