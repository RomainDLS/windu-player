# -*- coding: utf-8 -*-

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIFO_PATH = BASE_DIR + "/winduplayer/omxfifo"
CMD_SEND_STR = " > " + FIFO_PATH


def play_movie(**kwargs):
    movie = kwargs['movie']
    response = {'content': 'movie launched', 'status': 200}
    print(BASE_DIR)
    os.system("omxplayer -r {} {}".format(movie.path, FIFO_PATH))
    return response


def stop(**kwargs):
    os.system("echo -n q" + CMD_SEND_STR)


def fastbackward(**kwargs):
    os.system("echo -n $'\x1b\x5b\x42'" + CMD_SEND_STR)


def backward(**kwargs):
    os.system("echo -n $'\x1b\x5b\x44'" + CMD_SEND_STR)


def pause(**kwargs):
    os.system("echo -n p" + CMD_SEND_STR)


def forward(**kwargs):
    os.system("echo -n $'\x1b\x5b\x43'" + CMD_SEND_STR)


def fastforward(**kwargs):
    os.system("echo -n $'\x1b\x5b\x41'" + CMD_SEND_STR)


def lang(**kwargs):
    os.system("echo -n k" + CMD_SEND_STR)


def text(**kwargs):
    os.system("echo -n m" + CMD_SEND_STR)


def volumedown(**kwargs):
    os.system("echo -n '-'" + CMD_SEND_STR)
    os.system("echo -n '-'" + CMD_SEND_STR)


def volumeup(**kwargs):
    os.system("echo -n '+' " + CMD_SEND_STR)
    os.system("echo -n '+' " + CMD_SEND_STR)
