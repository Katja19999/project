import os as os
import sys as sys

import pygame as pg
from pygame import mixer

from constants import Constants


def load(path, file):
    # load sound files

    try:
        return mixer.Sound(os.path.join(Constants.sound_path, *path, file))
    except FileNotFoundError or FileExistsError:
        print(f'FILE {file} CAN NOT BE FOUND OR DOES NOT EXIST.')

        pg.quit()
        sys.exit()
