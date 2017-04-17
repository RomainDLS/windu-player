# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import global_cmd

urlpatterns = [
    url(r'^movies/(?P<movie_id>[0-1]+)$', global_cmd)
]
