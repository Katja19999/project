import pygame as pg

from constants import Constants
from characters import Character


class Player(Character):

    def __init__(self):
        super().__init__(('game', 'characters', 'player'), (1000, 1000), (4, 4), 100)

    @property
    def pos(self):
        return self.position

    def control(self, keys, mouse_pos, mouse_click):
        if self.state != 'die':
            if keys[pg.K_a] or keys[pg.K_LEFT]:
                self.dh = -self.speed_h
            elif keys[pg.K_d] or keys[pg.K_RIGHT]:
                self.dh = self.speed_h
            else:
                self.dh = 0

            if keys[pg.K_w] or keys[pg.K_UP]:
                self.dv = -self.speed_v
            elif keys[pg.K_s] or keys[pg.K_DOWN]:
                self.dv = self.speed_v
            else:
                self.dv = 0

            if mouse_click:
                self.attack(mouse_pos)

            if self.state in 'attack, damage':
                if self.states[self.state].end:
                    self.update_state()
            else:
                self.update_state()
        else:
            if self.states[self.state].end:
                self.kill()

    def attack(self, mouse_pos):
        self.state = 'attack'
        self.states[self.state].start()

    def update(self, delta_time, *args):
        self.control(*args)
        super().update(delta_time)


class PlayerGroup(pg.sprite.GroupSingle):

    def __init__(self):
        super().__init__()
        Player().add(self)

    @property
    def pos(self):
        return self.sprite.pos

    def draw(self, surface, *args):
        _sprite = self.sprite
        _center_h, _center_v = Constants.absolute_center
        surface.blit(_sprite.image, (_center_h - _sprite.rect.width // 2, _center_v - _sprite.rect.height // 2))
