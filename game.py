from enemies import Enemies
from environment import Environment
from menu import Menu
from objects import ObjectGroup
from player import PlayerGroup
from results import Result
from database import write_result
from ui import ui


class InGameHandler(Menu):

    def __init__(self, handler, elements, cursor, special_keys):
        super().__init__(handler, elements, cursor, special_keys)
        self.functions.update({'#pause': self.pause, '#unpause': self.unpause})

        self.environment = Environment()
        self.enemies = Enemies(self)
        self.objects = ObjectGroup()
        self.player = PlayerGroup(self)
        self.stats = Result()

        self.paused = False

    def start(self):
        self.environment = Environment()
        self.enemies = Enemies(self)
        self.objects = ObjectGroup()
        self.player = PlayerGroup(self)

    def pause(self):
        self.ui.add(ui['unpause_button'], ui['pause_text'])
        self.paused = True

    def unpause(self):
        self.ui.remove(ui['unpause_button'], ui['pause_text'])
        self.paused = False

    def new_level(self):
        if self.environment.end:
            self.end()
        elif not self.enemies.sprites():
            self.environment.new_level()
            self.player.new_level()
            self.enemies.new_level()

    def end(self):
        write_result(self.stats.get('enemies killed'))
        self.function(self.functions['#end'])

    def update(self):
        _events = self.handler.events
        self.handle_buttons(_events, self.player.health)
        self.handle_keys(_events)

        if not self.paused:
            self.player.update(_events, self.environment)
            _position = self.player.pos

            self.environment.update(_position, self.objects)
            self.enemies.update(_position, _events, self.player, self.objects)
            self.objects.update(_position, _events)

    def draw(self, surface):
        self.environment.draw(surface)
        self.player.draw(surface)
        self.enemies.draw(surface)
        self.objects.draw(surface)

        super().draw(surface)
