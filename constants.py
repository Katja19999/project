import pygame as pg


class GameConstants:

    # display
    flags = pg.FULLSCREEN | pg.HWSURFACE
    depth = 32
    display = pg.display.set_mode((0, 0), flags, depth)

    # size
    width, height = display.get_size()
    print(width, height)
    absolute_center = width // 2, height // 2
    scale = 2

    # in-game parameters
    fps = 90
    clock = pg.time.Clock()

    # files
    image_path = 'images'
    sound_path = 'sounds'


Constants = GameConstants()
