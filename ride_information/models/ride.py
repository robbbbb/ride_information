from django.db import models
from ..models.user import User
from django.utils.translation import gettext_lazy as _


class Ride(models.Model):
    # Using choices ensures the database or API only accepts valid values, reducing errors.
    class StatusChoices(models.TextChoices):
        EN_ROUTE = 'en-route', _('En-Route')
        PICKUP = 'pickup', _('Pickup')
        DROPOFF = 'dropoff', _('Dropoff')

    id_ride = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=150, choices=StatusChoices, default=StatusChoices.EN_ROUTE)
    id_driver = models.ForeignKey(User, on_delete=models.CASCADE)
    pickup_latitude = models.FloatField()
    pickup_longitude = models.FloatField()
    dropoff_latitude = models.FloatField()
    dropoff_longitude = models.FloatField()
    pickup_time = models.FloatField()


