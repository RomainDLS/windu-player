# -*- coding: utf-8 -*-

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIFO_PATH = BASE_DIR + "/omxfifo"
CMD_SEND_STR = " > " + FIFO_PATH


def play_movie(**kwargs):
    print(BASE_DIR)
    movie = kwargs['movie']
    os.system("screen -d -m -S omx_screen omxplayer -r {}".format(movie.path, FIFO_PATH))


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
