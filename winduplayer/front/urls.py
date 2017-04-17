# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import movies

urlpatterns = [
    url(r'^movies/', movies.as_view(), name='movie-list'),
]
