# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib import admin

from .views import movies, global_cmd

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^movies/', movies.as_view(), name='movie-list'),
    url(r'^api/movies/(?P<movie_id>[0-1]+)$', global_cmd)
]
