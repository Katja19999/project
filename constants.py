import pygame as pg


class Constants:
    # size
    size = 16
    scale = 2
    cells_h = 30
    cells_v = 20
    width = size * scale * cells_h
    height = size * scale * cells_v
    absolute_center = (width // 2 - size * 2 * scale, height // 2 - size * 2 * scale)

    # display
    window = (width, height)
    flags = pg.FULLSCREEN | pg.HWSURFACE
    depth = 32
    display = pg.display.set_mode(window, flags, depth)

    # in-game parameters
    fps = 90
    clock = pg.time.Clock()

    # files
    image_path = 'images'
    sound_path = 'sounds'
