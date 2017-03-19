from django.core.management import BaseCommand
from conf.settings import VARENVS
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
from hachoir.stream.input import InputStreamError
from sys import argv, stderr, exit
from core.models import Movie

from datetime import time

import os
import re


class Command(BaseCommand):
    help = 'Populate app database with movie folder'

    def handle(self, *args, **options):
        for file in os.listdir(VARENVS['MOVIE_PATH']):
            try:
                self.parse_file(os.path.join(VARENVS['MOVIE_PATH'], file))
            except InputStreamError:
                print(file)

    def parse_file(self, file):
        parser = createParser(file)
        if not parser:
            return None
        with parser:
            try:
                metadata = extractMetadata(parser)
            except Exception as err:
                print("Metadata extraction error: %s" % err)
                metadata = None
        if not metadata:
            print("Unable to extract metadata")
            exit(1)

        movie_metadata = [l for l in metadata.exportPlaintext()]
        file_name = file.split('/')[-1]
        print(" -", file_name)
        movie, new = Movie.objects.get_or_create(path=file)
        movie.title = '.'.join(file_name.split('.')[:-1])
        movie.file_type = file_name.split('.')[-1]
        # extract time informations to datetime.time object
        try:
            timeargs = re.split("hours|min|sec", movie_metadata[1].split(':')[1].replace(' ',''))[:-1]
            timeargs = list(map(int, timeargs))
            movie.duration = time(*timeargs)
        except ValueError:
            print("Bad time interpretation :",  movie_metadata[1].split(':')[1].replace(' ',''))
        movie.save()
