# -*- coding: utf-8 -*-
from django.views.generic import ListView
from core.models import Movie


class movies(ListView):
    template_name = "movies/movie-list.html"
    model = Movie
