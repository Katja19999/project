import pygame as pg

from pygame import sprite
from math import sqrt

from states import State


class Character(sprite.Sprite):

    normalize = sqrt(2)

    def __init__(self, game, path, position, speed, health):
        super().__init__()

        self.game = game

        self.states = {
            'stand': State(path, 'stand.png'),
            'walk': State(path, 'walk.png'),
            'attack': State(path, 'attack.png', auto_reset=False),
            'damage': State(path, 'damage.png', auto_reset=False),
            'die': State(path, 'die.png', auto_reset=False)
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

    def update_state(self):
        if self.state in {'attack', 'damage'} and not self.states[self.state].end:
            return

        if self.health <= 0:
            self.state = 'die'
        elif self.dh == 0 and self.dv == 0:
            self.state = 'stand'
        else:
            self.state = 'walk'

    def control(self, *args, **kwargs):
        pass

    def hit(self, obj2):
        pass

    def update(self, delta_time, *args, **kwargs):
        self.states[self.state].update()

        if self.dh != 0 and self.dv != 0:
            self.dh /= self.normalize
            self.dv /= self.normalize

        self.position[0] += self.dh * delta_time / 100
        self.position[1] += self.dv * delta_time / 100

        self.set_position()
