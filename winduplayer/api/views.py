# -*- coding: utf-8 -*-

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.models import Movie
from core.omx_commands import (play_movie)


@api_view(['POST'])
def global_cmd(request, movie_pk):
    try:
        movie = Movie.objects.get(pk=movie_pk)
        command = request.data['command']
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    response_data = 'Command {} not found'.format(command)
    r = dict(data=response_data, status=status.HTTP_400_BAD_REQUEST)

    if command == 'play':
        r = play_movie(movie)
    elif command == "stop":
        r = play_movie(movie)
    elif command == "fast-backward":
        r = play_movie(movie)
    elif command == "backward":
        r = play_movie(movie)
    elif command == "pause":
        r = play_movie(movie)
    elif command == "forward":
        r = play_movie(movie)
    elif command == "fast-forward":
        r = play_movie(movie)
    elif command == "lang":
        r = play_movie(movie)
    elif command == "text":
        r = play_movie(movie)
    elif command == "volume-down":
        r = play_movie(movie)
    elif command == "volume-up":
        r = play_movie(movie)

    return Response(data=r['content'], status=r['status'])
