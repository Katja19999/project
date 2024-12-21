import os as os
import sys as sys

import pygame as pg
from pygame import mixer

from constants.constants import SOUND_PATH


# READY
class Sounds:
    def __init__(self, path, names, files):
        self.sounds = dict(zip(names, [self.load(file, path) for file in files]))

    @staticmethod
    def load(file, path):
        # Load SOUND FILE
        # By specified PATH
        # IF EXISTS

        try:
            return mixer.Sound(os.path.join(SOUND_PATH, *path, file))
        except FileNotFoundError or FileExistsError:
            print(f'FILE {file} CAN NOT BE FOUND OR DOES NOT EXIST.')

            pg.quit()
            sys.exit()

    def play(self, value):
        if value in self.sounds.keys():
            mixer.Sound.play(self.sounds[value])
