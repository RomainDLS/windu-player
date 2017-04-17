# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import global_cmd

urlpatterns = [
    url(r'movies/(?P<movie_pk>[0-9]+)$', global_cmd)
]
