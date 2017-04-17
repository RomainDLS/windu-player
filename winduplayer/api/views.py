# -*- coding: utf-8 -*-

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.models import Movie
import os


@api_view(['POST'])
def global_cmd(request, movie_pk):
    response = {}
    command = request.data['command']
    try:
        movie = Movie.objects.get(pk=movie_pk)
        path = movie.path
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if command == 'play':
        response['path'] = path
        os.system("omxplayer -r {}".format(path))

    return Response(response)
