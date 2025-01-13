import os as os
import sys as sys

import pygame as pg

from constants import Constants


def load(path, file, scale=Constants.scale, alpha=True):
    # load image files

    try:
        img = pg.image.load(os.path.join(Constants.data_directory, Constants.image_directory, *path, file))
        img = pg.transform.scale_by(img, scale)

        return img.convert_alpha() if alpha else img.convert()

    except FileNotFoundError or FileExistsError:
        print(f'FILE {file} CAN NOT BE FOUND OR DOES NOT EXIST.')

        pg.quit()
        sys.exit()


def sprite_sheet(path, file, size, alpha=True):
    # load sprite sheets

    sheet = load(path, file, alpha=alpha)

    crop_width = size[0] * Constants.scale
    crop_height = size[1] * Constants.scale

    image_width = sheet.get_width()
    image_height = sheet.get_height()

    cropped_images = []
    for x in range(image_width // crop_width):
        for y in range(image_height // crop_height):
            cropped_images.append(
                sheet.subsurface((x * crop_width, y * crop_height, crop_width, crop_height))
            )

    return cropped_images
