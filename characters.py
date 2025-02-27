from math import sqrt

import pygame as pg
from pygame import sprite

from states import State


class Character(sprite.Sprite):
    normalize = sqrt(2)

    def __init__(self, game, path, position, speed, health):
        super().__init__()
        self.game = game
        self.states = {
            'stand': State(path, 'stand.png'),
            'walk': State(path, 'walk.png'),
            'attack': State(path, 'attack.png', 'attack.wav', auto_reset=False),
            'damage': State(path, 'damage.png', 'damage.wav', auto_reset=False),
        }
        self.state = 'stand'
        self.flipped = False
        self.position = list(position)
        self.render_rect = pg.Rect(0, 0, 64, 64)
        self.rect = pg.Rect(0, 0, 32, 32)
        self.set_position()
        self.speed = speed
        self.dh, self.dv = 0, 0
        self.health = health

    @property
    def image(self):
        return pg.transform.flip(self.states[self.state].image, self.flipped, False)

    def set_position(self):
        self.rect.center = self.position
        self.render_rect.center = self.position

    def update_state(self, *args, **kwargs):
        self.states[self.state].update()

        if (self.state in {'damage', 'attack'} and not self.states[self.state].end) or self.health <= 0:
            return

        self.state = 'stand' if self.dh == self.dv == 0 else 'walk'

    def update_movement(self, *args, **kwargs):
        pass

    def hit(self, damage):
        self.health -= damage
        self.state = 'damage'
        self.states[self.state].start()
