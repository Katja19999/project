import math as m

import pygame as pg
from constants import Constants
from characters import Character
from objects import FireBall


class Player(Character):

    def __init__(self, position, bullet_group, bullet):
        super().__init__(('player', ), position, 15, 100)

        self.bullet_group = bullet_group
        self.bullet = bullet

    @property
    def pos(self):
        return self.position

    def control(self, events):
        keys = events['keys']
        mouse_click, mouse_pos = events['mouse']

        if self.state == 'die':
            if self.states[self.state].end:
                self.kill()
            return

        self.dh = self.dv = 0
        if keys[pg.K_a] or keys[pg.K_LEFT]:
            self.dh = -self.speed
            self.flipped = True
        elif keys[pg.K_d] or keys[pg.K_RIGHT]:
            self.dh = self.speed
            self.flipped = False

        if keys[pg.K_w] or keys[pg.K_UP]:
            self.dv = -self.speed
        elif keys[pg.K_s] or keys[pg.K_DOWN]:
            self.dv = self.speed

        self.flipped = mouse_pos[0] < Constants.width // 2

        if mouse_click[0] and self.state != 'attack':
            self.attack(mouse_pos)

        self.update_state()

    def attack(self, mouse_pos):
        self.state = 'attack'
        self.states[self.state].start()

        self.bullet_group.add(self.bullet(self.position,
                                          m.atan2(mouse_pos[1] - Constants.height // 2,
                                                  mouse_pos[0] - Constants.width // 2)))

    def update(self, events, *args):
        self.control(events)
        super().update(events['delta_time'])


class PlayerGroup(pg.sprite.GroupSingle):
    def __init__(self, bullet_group, level):
        super().__init__()

        self.start(bullet_group, level)

    def start(self, bullet_group, level):
        _size = Constants.cell_size
        for y, row in enumerate(level):
            for x, col in enumerate(row):
                if col == 9:
                    Player(((x + 0.5) * _size, (y + 0.5) * _size), bullet_group, FireBall).add(self)
                    break

    @property
    def pos(self):
        return self.sprite.pos

    def draw(self, surface, *args):
        sprite = self.sprite
        center_h, center_v = Constants.absolute_center
        surface.blit(
            sprite.image,
            (center_h - sprite.rect.width // 2, center_v - sprite.rect.height // 2),
        )
