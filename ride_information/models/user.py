from django.db import models


class User(models.Model):
    id_user = models.IntegerField(primary_key=True)
    role = models.CharField(max_length=150)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=150)