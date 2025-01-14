from pygame import sprite
from constants import Constants
from groups import CameraGroup
from images import sprite_sheet
from levels import load_level


class Wall(sprite.Sprite):

    def __init__(self, position, image):
        super().__init__()

        self.image = image
        self.render_rect = self.rect = self.image.get_rect(topleft=position)


class Box(sprite.Sprite):

    def __init__(self, position, image, health, objects_group, attributes):
        super().__init__()

        self.image = image
        self.render_rect = self.rect = self.image.get_rect(topleft=position)

        self.health = health

        self.objects_group = objects_group
        self.attribute = attributes

    def update(self, bullets):
        _collided = sprite.spritecollide(self, bullets, False)
        for spr in _collided:
            self.health -= spr.damage
            spr.kill()
        if self.health <= 0:
            if self.attribute:
                self.objects_group.add(self.attribute(self.render_rect.topleft))
            self.kill()


class Chest(Box):

    def __init__(self, position, image):
        super().__init__(position, image, 200, None, None)


class Vase(Box):

    def __init__(self, position, image):
        super().__init__(position, image, 100, None, None)


class Environment(CameraGroup):

    def __init__(self):
        super().__init__()

        self.cell_size = Constants.cell_size
        _images = sprite_sheet((), 'tilemap.png', (16, 16), alpha=False)
        self.images = dict(zip(range(len(_images)), _images))
        self.walls = {
            0: (Wall, _images[0]),
            1: (Wall, _images[1]),
            6: (Wall, _images[6]),
        }
        self.boxes = {
            7: (Vase, _images[7]),
            8: (Chest, _images[8]),
        }

        self.levels = [load_level((Constants.data_directory, 'levels'), 'level1.csv')]
        self.level = self.levels[0]
        self.start(self.level)

    def start(self, level):
        _size = Constants.cell_size
        for y, row in enumerate(level):
            for x, col in enumerate(row):
                if col in self.walls.keys():
                    obj = self.walls[col]
                    obj[0]((x * _size, y * _size), obj[1]).add(self)
                elif col in self.boxes.keys():
                    obj = self.boxes[col]
                    obj[0]((x * _size, y * _size), obj[1]).add(self)

    def set_level(self, level):
        self.level = self.levels[level]

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
        for row in range(int(_start_v), int(_start_v + _cells_v + 1)):
            for col in range(int(_start_h), int(_start_h + _cells_h + 1)):
                if 0 <= row < len(_level) and 0 <= col < len(_level[0]) and _level[row][col]:
                    if _level[row][col] in self.boxes:
                        surface_blit(_images[2], (col * _size - _dh, row * _size - _dv))
                    elif _level[row][col] not in self.walls:
                        surface_blit(_images[_level[row][col]], (col * _size - _dh, row * _size - _dv))

        super().draw(surface)
