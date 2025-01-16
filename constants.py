import pygame as pg


class GameConstants:
    pg.mixer.init()
    pg.init()
    pg.event.set_allowed([pg.MOUSEBUTTONDOWN, pg.MOUSEBUTTONUP, pg.KEYDOWN, pg.KEYUP])
    pg.mouse.set_visible(False)

    # display
    flags = pg.FULLSCREEN | pg.HWSURFACE
    depth = 32
    display = pg.display.set_mode((0, 0), flags, depth)

    # size
    width, height = display.get_size()
    absolute_center = width // 2, height // 2
    scale = 2
    cell_size = 16 * scale
    cells_h = width // cell_size + 2
    cells_v = height // cell_size + 2

    # in-game parameters
    fps = 90
    clock = pg.time.Clock()

    # files
    data_directory = 'data'
    image_directory = 'images'
    sound_directory = 'sounds'


Constants = GameConstants()
