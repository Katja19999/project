import os
import sys as sys

import pygame as pg
from pygame import mixer

from constants import Constants


def load(path, file):
    # load sound files

    try:
        return mixer.Sound(os.path.join(Constants.data_directory, Constants.sound_directory, *path, file))
    except FileNotFoundError or FileExistsError:
        print(f'FILE {file} CAN NOT BE FOUND OR DOES NOT EXIST.')

        pg.quit()
        sys.exit()
