# -*- coding: utf-8 -*-

import os
from core.management.commands import populate


def update_movie_list(**kwargs):
    command = populate.Command()
    command.handle()


def play_movie(**kwargs):
    movie_path = kwargs['movie'].path
    movie_path = movie_path.replace("'", "\\'")
    movie_path = movie_path.replace(" ", "\\ ")
    print(movie_path)
    os.system("screen -X -S omx_screen quit")
    os.system("screen -d -m -S omx_screen omxplayer -r {}".format(movie_path))


def stop(**kwargs):
    os.system("screen -S omx_screen -X stuff q")


def fastbackward(**kwargs):
    os.system("screen -S omx_screen -X stuff $'\x1b\x5b\x42'")


def backward(**kwargs):
    os.system("screen -S omx_screen -X stuff $'\x1b\x5b\x44'")


def pause(**kwargs):
    os.system("screen -S omx_screen -X stuff p")


def forward(**kwargs):
    os.system("screen -S omx_screen -X stuff $'\x1b\x5b\x43'")


def fastforward(**kwargs):
    os.system("screen -S omx_screen -X stuff $'\x1b\x5b\x41'")


def lang(**kwargs):
    os.system("screen -S omx_screen -X stuff k")


def text(**kwargs):
    os.system("screen -S omx_screen -X stuff m")


def volumedown(**kwargs):
    os.system("screen -S omx_screen -X stuff '-'")
    os.system("screen -S omx_screen -X stuff '-'")


def volumeup(**kwargs):
    os.system("screen -S omx_screen -X stuff '+' ")
    os.system("screen -S omx_screen -X stuff '+' ")
