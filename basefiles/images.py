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


def sprite_sheet(path, file, size):
    sheet = load(path, file)

    crop_width = size[0]
    crop_height = size[1]

    image_width = sheet.get_width()
    image_height = sheet.get_height()

    cropped_images = []
    for x in range(image_width // crop_width):
        for y in range(image_height // crop_height):
            cropped_images.append(
                sheet.subsurface((x, y, crop_width, crop_height))
            )

    return cropped_images
