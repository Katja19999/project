import os as os
import sys as sys

import pygame as pg

from constants.constants import IMAGE_PATH, SCALE


def load(path, file, scale=SCALE, alpha=True):
    try:
        img = pg.image.load(os.path.join(IMAGE_PATH, *path, file))
        img = pg.transform.scale_by(img, scale)

        return img.convert_alpha() if alpha else img.convert()

    except FileNotFoundError or FileExistsError:
        print(f'FILE {file} CAN NOT BE FOUND OR DOES NOT EXIST.')

        pg.quit()
        sys.exit()
