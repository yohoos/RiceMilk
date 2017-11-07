from rest_framework import viewsets
from .serializers import *


class WifiSpotViewSet(viewsets.ModelViewSet):
    queryset = WifiSpot.objects.all()
    serializer_class = WifiSpotSerializer
