# -*- coding: utf-8 -*-

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.generic import ListView
from core.models import Movie


class movies(ListView):
    template_name = "movies/movie-list.html"
    model = Movie


@api_view(['POST'])
def global_cmd(request, movie_id):
    print('global_cmd_received', movie_id)
    return Response('cmd')
