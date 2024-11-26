from rest_framework import serializers
from ..models.ride import Ride


class RiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = "__all__"
        read_only_fields = ['id_ride']
