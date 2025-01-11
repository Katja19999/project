from environment import Environment
from enemies import Enemies
from player import PlayerGroup
from menu import Menu


class InGameHandler(Menu):

    def __init__(self, handler, elements, special_keys):
        super().__init__(handler, elements, special_keys)

        self.environment = Environment()
        self.enemies = Enemies(self.environment.level, 30)
        self.player = PlayerGroup()

        self.paused = False

    def update(self):
        _events = self.handler.events
        self.handle_buttons(_events)
        self.handle_keys(_events)

        if not self.paused:
            self.player.update(_events)
            _position = self.player.pos

            self.environment.update(_position)
            self.enemies.update(_position, _events['delta_time'])

    def draw(self, surface):
        self.environment.draw(surface)
        self.enemies.draw(surface)
        self.player.draw(surface)

        self.ui.draw(surface)
