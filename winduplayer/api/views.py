# -*- coding: utf-8 -*-

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.models import Movie
from core import omx_commands


@api_view(['POST'])
def global_cmd(request, movie_pk):
    try:
        movie = Movie.objects.get(pk=movie_pk)
        command = request.data['command']
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    response_data = 'Command {} not found'.format(command)
    r = dict(data=response_data, status=status.HTTP_400_BAD_REQUEST)

    command_map = {
        'play': 'play_movie',
        'stop': 'stop',
        'fast-backward': 'fastbackward',
        'backward': 'backward',
        'pause': 'pause',
        'forward': 'forward',
        'fast-forward': 'fastforward',
        'lang': 'lang',
        'text': 'text',
        'volume-down': 'volumedown',
        'volume-up': 'volumeup'
    }

    command_function = getattr(omx_commands, command_map[command])
    no_response = {'content': '', 'status': 200}
    r = command_function(movie=movie) or no_response

    return Response(data=r['content'], status=r['status'])
