from django.conf.urls import url
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('wifi_spot', WifiSpotViewSet, 'wifi_spot')

urlpatterns = router.urls

urlpatterns += [
    url(r'^notebook$', TemplateView.as_view(
        template_name="nyc_wifi/Mapping Wifi.html")),
]
