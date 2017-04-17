# -*- coding: utf-8 -*-

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def global_cmd(request, movie_pk):
    response = {}
    print('global_cmd_received', movie_pk)
    response['movie_id'] = movie_pk
    response['command'] = request.data['command']
    return Response(response)
