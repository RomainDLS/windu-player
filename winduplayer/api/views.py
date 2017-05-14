# -*- coding: utf-8 -*-

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.models import Movie
from core import commands


@api_view(['POST'])
def global_cmd(request, movie_pk):
    command = request.data['command']
    try:
        movie = Movie.objects.get(pk=movie_pk)
    except Movie.DoesNotExist:
        movie = movie_pk

    response_data = 'Command {} not found'.format(command)
    r = dict(data=response_data, status=status.HTTP_400_BAD_REQUEST)

    command_map = {
        'update_movie_list': 'update_movie_list',
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
    try:
        command_function = getattr(commands, command_map[command])
        command_function(movie=movie)
        print('Command {} sent successfully'.format(command_map[command]))
        r = {'content': 'command sent successfully', 'status': 201}
    except KeyError:
        r = {'content': 'Unknown command {}'.format(command), 'status': 200}

    return Response(data=r['content'], status=r['status'])
