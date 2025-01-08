import pygame as pg

from environment import Environment
from player import PlayerGroup


class InGameHandler:

    def __init__(self):

        self.environment = Environment()
        self.player = PlayerGroup()

        self.paused = False

    def _events(self, keys):
        if keys[pg.K_p]:
            self.paused = not self.paused

    def update(self, delta_time, keys, mouse_click, mouse_pos):
        self._events(keys)

        if not self.paused:
            self.player.update(delta_time, keys, mouse_pos, mouse_click)
            self.environment.update(self.player.pos)

    def draw(self, surface):
        self.environment.draw(surface)
        self.player.draw(surface)


game = InGameHandler()
