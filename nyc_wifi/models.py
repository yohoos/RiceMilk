from django.db import models


# Create your models here.
class WifiSpot(models.Model):
    borough = models.CharField(max_length=2)
    type = models.CharField(max_length=50)
    provider = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    location_type = models.CharField(max_length=50)
    remarks = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    ssid = models.CharField(max_length=50)
    lat = models.FloatField()  # PlateCarree projected lats
    lon = models.FloatField()  # PlateCarree projected lons
