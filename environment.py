from constants import Constants
from groups import CameraGroup
from images import sprite_sheet


class Environment(CameraGroup):

    cell_size = Constants.cell_size
    images = dict(zip([0, 1, 2, 3, 4, 5, 6], sprite_sheet(('game', 'map'), 'tilemap.png', (16, 16), alpha=False)))
    objects = []

    def __init__(self, level):
        super().__init__()

        self.level = level

    def draw(self, surface, *args):
        surface_blit = surface.blit
        _level = self.level
        _images = self.images

        _size = self.cell_size
        _width, _height = Constants.width, Constants.height

        _cells_h, _cells_v = Constants.cells_h, Constants.cells_v

        _dh = self.dh
        _dv = self.dv

        _start_h = self.dh // _size
        _start_v = self.dv // _size

        surface.fill('#12051b')
        for row in range(_start_v, _start_v + _cells_v + 1):
            for col in range(_start_h, _start_h + _cells_h + 1):
                if 0 <= row < len(_level) and 0 <= col < len(_level[0]) and _level[row][col]:
                    surface_blit(_images[_level[row][col]], (col * _size - _dh, row * _size - _dv))
