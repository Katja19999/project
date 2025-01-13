from constants import Constants
from random import randint
from characters import Character
from groups import CameraGroup


class Enemy(Character):
    pass


class Enemies(CameraGroup):

    def __init__(self, game):
        super().__init__()

        self.game = game

        self.start(self.game.environment.level)

    def start(self, level):
        _size = Constants.cell_size
        for y, row in enumerate(level):
            for x, col in enumerate(row):
                if col in {3, 5}:
                    Enemy(self.game,('skull', ), ((x + 0.5) * _size, (y + 0.5) * _size), 5, 100).add(self)
