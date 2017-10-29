from rest_framework import serializers

from .models import *


class WifiSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = WifiSpot
        fields = '__all__'
