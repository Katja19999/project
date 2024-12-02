import os as os
import sys as sys

import pygame as pg
from pygame import mixer


# READY
def load(file, path=()):
    # Load SOUND FILE
    # By specified PATH
    # IF EXISTS

    try:
        return mixer.Sound(os.path.join(*path, file))
    except FileNotFoundError or FileExistsError:
        print(f'FILE {file} CAN NOT BE FOUND OR DOES NOT EXIST.')

        pg.quit()
        sys.exit()
