import pygame as pg

from pygame import sprite

from states import State


class Character(sprite.Sprite):

    def __init__(self, path, position, speed, health):
        super().__init__()

        self.states = {
            'stand': State(path, 'stand.png'),
            'walk': State(path, 'walk.png'),
            'attack': State(path, 'attack.png', auto_reset=False),
            'damage': State(path, 'damage.png', auto_reset=False),
            'die': State(path, 'die.png', auto_reset=False)
        }
        self.state = 'stand'

        self.position = list(position)
        self.rect = pg.Rect(0, 0, 64, 64)
        self._collision_rect = pg.Rect(0, 0, 32, 32)
        self.set_position(self.position)

        self.speed_h, self.speed_v = speed
        self.dh, self.dv = 0, 0

        self.health = health

    @property
    def image(self):
        return self.states[self.state].image

    def set_position(self, position):
        self.rect.center = position
        self._collision_rect.center = position

    def update_state(self):
        if self.health <= 0:
            self.state = 'die'
        elif self.dh == 0 and self.dv == 0:
            self.state = 'stand'
        else:
            self.state = 'walk'

    def control(self, *args, **kwargs):
        pass

    def update(self, delta_time, *args, **kwargs):
        self.states[self.state].update()

        self.position[0] += self.dh * delta_time / 100
        self.position[1] += self.dv * delta_time / 100

        self.set_position(self.position)
