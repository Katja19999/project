import pygame as pg

from constants import Constants
from environment import Environment


class InGameHandler:

    environment = Environment(Constants.level1)

    paused = False

    def _events(self, keys):
        if keys[pg.K_p]:
            self.paused = not self.paused

    def update(self, keys, *args):
        self._events(keys)

        if self.paused:
            relative_position = (0, 0)

            self.environment.update(relative_position)

    def draw(self, surface):
        self.environment.draw(surface)


game = InGameHandler()
