from environment import Environment
from enemies import Enemies
from player import PlayerGroup


class InGameHandler:

    def __init__(self, handler):

        self.handler = handler

        self.environment = Environment()
        self.enemies = Enemies(self.environment.level, 30)
        self.player = PlayerGroup()

        self.paused = False

    def update(self):
        events = self.handler.events

        if not self.paused:
            self.player.update(events)
            _position = self.player.pos

            self.enemies.update(_position, events['delta_time'])
            self.environment.update(_position)

    def draw(self, surface):
        self.environment.draw(surface)
        self.enemies.draw(surface)
        self.player.draw(surface)
