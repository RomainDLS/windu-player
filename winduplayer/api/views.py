# -*- coding: utf-8 -*-

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def global_cmd(request, movie_id):
    response = {}
    print('global_cmd_received', movie_id)
    response['movie_id'] = movie_id
    return Response(response)
