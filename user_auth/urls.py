from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^api_token_create$', TokenView.as_view()),
    url(r'^api_auth_check$', TokenView.as_view()),
    url(r'^api_token_refresh$', RefreshView.as_view()),
    url(r'^api_token_logout', LogoutView.as_view())
]
