from pygame import sprite
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

        self.all_sprites = sprite.Group()
        self.environment = Environment()
        self.enemies = Enemies(self.environment.level)
        self.objects = ObjectGroup()
        self.player = PlayerGroup((self.objects, self.all_sprites), self.environment.level)

        self.all_sprites.add(self.environment.sprites(),
                             self.enemies.sprites(),
                             self.objects.sprites(),
                             self.player.sprites())

        self.paused = False

    def pause(self):
        self.ui.add(ui['unpause_button'])
        self.paused = True

    def unpause(self):
        self.ui.remove(ui['unpause_button'])
        self.paused = False

    def check_collisions(self):
        checked = set()
        _sprites = self.all_sprites.sprites()
        for spr1 in _sprites:
            for spr2 in _sprites:
                if spr1 == spr2 or spr1 in checked:
                    continue
                rect1 = spr1.collision_rect if hasattr(spr1, 'collision_rect') else spr1.rect
                rect2 = spr2.collision_rect if hasattr(spr2, 'collision_rect') else spr2.rect

                if rect1.colliderect(rect2):
                    if hasattr(spr1, 'hit'):
                        spr1.hit(spr2)
                    if hasattr(spr2, 'hit'):
                        spr2.hit(spr1)

            checked.add(spr1)

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

            self.check_collisions()

    def draw(self, surface):
        self.environment.draw(surface)
        self.enemies.draw(surface)
        self.player.draw(surface)
        self.objects.draw(surface)

        super().draw(surface)
