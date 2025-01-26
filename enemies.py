import math as m

import pygame as pg

from characters import Character
from constants import Constants
from groups import CameraGroup


class Enemy(Character):

    def update_movement(self, events, player):
        if m.dist(self.game.player.pos, self.position) < 500:
            target_pos = self.game.player.pos
            angle = m.atan2(target_pos[1] - self.position[1], target_pos[0] - self.position[0])
            self.dh = m.cos(angle) * self.speed * events['delta_time']
            self.dv = m.sin(angle) * self.speed * events['delta_time']
            self.position[0] += self.dh
            self.position[1] += self.dv
            self.set_position()

    def attack(self, player):
        if self.state != 'attack':
            self.state = 'attack'
            self.states[self.state].start()
            player.sprite.hit(10)

    def update_state(self, player, bullets):
        self.flipped = player.pos[0] < self.position[0]

        if pg.sprite.spritecollideany(self, player):
            self.attack(player)

        _collided = pg.sprite.spritecollide(self, bullets, False)
        for spr in _collided:
            if hasattr(spr, 'damage'):
                self.hit(spr.damage)
                spr.kill()

        if self.health <= 0:
            self.kill()

        super().update_state()

    def update(self, events, player, bullets):
        self.update_movement(events, player)
        self.update_state(player, bullets)


class Enemies(CameraGroup):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.start()

    def start(self):
        cell_size = Constants.cell_size
        for y, row in enumerate(self.game.environment.level):
            for x, col in enumerate(row):
                if col in {3, 5}:
                    Enemy(self.game, ('skull',), ((x + 0.5) * cell_size, (y + 0.5) * cell_size), 7.5, 150).add(self)

    def new_level(self):
        self.empty()
        self.start()
