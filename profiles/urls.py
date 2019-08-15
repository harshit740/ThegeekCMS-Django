from django.conf.urls import url
from django.urls import path

from profiles import views


urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/$', views.getProfile, name='about'),
]