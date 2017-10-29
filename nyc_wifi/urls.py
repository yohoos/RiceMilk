from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^notebook$', TemplateView.as_view(template_name="nyc_wifi/Mapping Wifi.html")),
]
