import os as os
import sys as sys

import pygame as pg

from constants import IMAGE_PATH, SCALE


def load(path, file, scale=SCALE, alpha=True):
    try:
        img = pg.image.load(os.path.join(IMAGE_PATH, *path, file))
        img = pg.transform.scale_by(img, scale)

        return img.convert_alpha() if alpha else img.convert()

    except FileNotFoundError or FileExistsError:
        print(f'FILE {file} CAN NOT BE FOUND OR DOES NOT EXIST.')

        pg.quit()
        sys.exit()


def crop(surface, x, y, width, height):
    return surface.subsurface(x, y, width, height)


def sprite_sheet(path, file, flipped=False):
    sheet = load(path, file)

    _width = _height = sheet.get_height()

    return [pg.transform.flip(crop(sheet, row, 0, _width, _height), flipped, False)
            for row in range(sheet.get_width() // _width)]
