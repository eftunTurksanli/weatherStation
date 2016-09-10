from __future__ import unicode_literals
from django.db import models


class Station(models.Model):
    name = models.CharField(max_length=255)
    location_lat = models.FloatField(default=0)
    location_lng = models.FloatField(default=0)
    address = models.TextField(max_length=255)


