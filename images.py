import os as os
import sys as sys

import pygame as pg
from pygame import image, transform

from constants import IMAGE_PATH, SCALE


# READY
def load(file, alpha=False, path=(IMAGE_PATH, )):
    # Load IMAGE FILE
    # By specified PATH
    # IF EXISTS

    try:
        img = transform.scale_by(image.load(os.path.join(*path, file)), SCALE)
        return img.convert_alpha() if alpha else img.convert()
    except FileNotFoundError or FileExistsError:
        print(f'FILE {file} CAN NOT BE FOUND OR DOES NOT EXIST.')

        pg.quit()
        sys.exit()


def crop(img, x, y, width, height):
    # Cut out
    # Part of the IMAGE
    # At specified COORDINATES

    return img.subsurface((x, y, width, height))


def sheet(file, width, height, alpha, path=(IMAGE_PATH, )):
    # Create a SPRITE SHEET
    # Out of an IMAGE
    # And return a list of FRAMES

    sprite_sheet = load(file, path=path, alpha=alpha)

    width = width * SCALE
    height = height * SCALE

    images = []
    for x in range(sprite_sheet.get_width() // width):
        for y in range(sprite_sheet.get_height() // height):
            images.append(crop(sprite_sheet, x, y, width, height))

    return images
