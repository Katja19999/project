import pygame as pg

from constants import Constants
from environment import Environment


class InGameHandler:

    environment = Environment(Constants.level1)

    paused = False

    x = 0
    y = 0

    def _events(self, keys):
        if keys[pg.K_p]:
            self.paused = not self.paused

    def update(self, keys, *args):
        self._events(keys)

        if keys[pg.K_w]:
            self.y -= 5
        elif keys[pg.K_s]:
            self.y += 5

        if keys[pg.K_a]:
            self.x -= 5
        elif keys[pg.K_d]:
            self.x += 5

        if not self.paused:

            self.environment.update((self.x, self.y))

    def draw(self, surface):
        self.environment.draw(surface)


game = InGameHandler()
