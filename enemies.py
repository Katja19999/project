from constants import Constants
from random import randint
from characters import Character
from groups import CameraGroup


class Enemy(Character):
    pass


class Enemies(CameraGroup):

    def __init__(self, level, enemies):
        super().__init__()
        self.start(enemies, level)

    def start(self, enemies, level):
        _size = Constants.cell_size
        for _ in range(enemies):
            x = randint(0, len(level[0]) - 1)
            y = randint(0, len(level) - 1)
            while level[y][x] == 0:
                x = randint(0, len(level[0]) - 1)
                y = randint(0, len(level) - 1)

            Enemy(('game', 'characters', 'skull'), (x * _size, y * _size), 5, 100).add(self)
