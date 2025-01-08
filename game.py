import pygame as pg

from constants import Constants
from environment import Environment


class InGameHandler:

    def __init__(self):

        self.environment = Environment(Constants.level1)

        self.paused = False

    def _events(self, keys):
        if keys[pg.K_p]:
            self.paused = not self.paused

    def update(self, keys, mouse_click, mouse_pos):
        self._events(keys)

        if not self.paused:
            self.environment.update((0, 0))

    def draw(self, surface):
        self.environment.draw(surface)


game = InGameHandler()
