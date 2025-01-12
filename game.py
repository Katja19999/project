from environment import Environment
from enemies import Enemies
from player import PlayerGroup
from objects import ObjectGroup
from menu import Menu
from ui import ui


class InGameHandler(Menu):

    def __init__(self, handler, elements, cursor, special_keys):
        super().__init__(handler, elements, cursor, special_keys)
        self.functions.update({'#pause': self.pause, '#unpause': self.unpause})

        self.environment = Environment()
        self.enemies = Enemies(self.environment.level)
        self.objects = ObjectGroup()
        self.player = PlayerGroup(self.objects, self.environment.level)

        self.paused = False

    def pause(self):
        self.ui.add(ui['unpause_button'])
        self.paused = True

    def unpause(self):
        self.ui.remove(ui['unpause_button'])
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
            self.objects.update(_position, _events['delta_time'])

    def draw(self, surface):
        self.environment.draw(surface)
        self.enemies.draw(surface)
        self.player.draw(surface)
        self.objects.draw(surface)

        super().draw(surface)
