from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^api_token_refresh$', TokenView.as_view()),
    url(r'^api_token_create$', TokenView.as_view()),
    url(r'^is_authenticated$', is_authenticated)
]
