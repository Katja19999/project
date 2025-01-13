import math as m

import pygame as pg
from constants import Constants
from characters import Character
from objects import FireBall


class Player(Character):

    def __init__(self, game, position, bullet):
        super().__init__(game, ('player', ), position, 15, 100)

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

        _walls = self.game.environment

        self.dh = self.dv = 0
        if keys[pg.K_a] or keys[pg.K_LEFT]:
            self.dh = -self.speed
            self.flipped = True
        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            self.dh = self.speed
            self.flipped = False

        if self.dh != 0:
            self.rect.x += self.dh
            if pg.sprite.spritecollide(self, _walls, False):
                self.dh = 0
            self.rect.x -= self.dh

        if keys[pg.K_w] or keys[pg.K_UP]:
            self.dv = -self.speed
        if keys[pg.K_s] or keys[pg.K_DOWN]:
            self.dv = self.speed

        if self.dv != 0:
            self.rect.y += self.dv
            if pg.sprite.spritecollide(self, _walls, False):
                self.dv = 0
            self.rect.y -= self.dv

        self.flipped = mouse_pos[0] < Constants.width // 2

        if mouse_click[0] and self.state not in {'attack', 'damage'}:
            self.attack(mouse_pos)

        self.update_state()

    def attack(self, mouse_pos):
        self.state = 'attack'
        self.states[self.state].start()

        self.game.objects.add(self.bullet(self.position, m.atan2(mouse_pos[1] - Constants.height // 2,
                                          mouse_pos[0] - Constants.width // 2)))

    def damage(self, damage):
        self.state = 'damage'
        self.states[self.state].start()
        self.health -= damage

    def update(self, events, *args):
        self.control(events)
        super().update(events['delta_time'])


class PlayerGroup(pg.sprite.GroupSingle):
    def __init__(self, game):
        super().__init__()
        self.game = game

        self.start(self.game.environment.level)

    def start(self, level):
        _size = Constants.cell_size
        for y, row in enumerate(level):
            for x, col in enumerate(row):
                if col == 9:
                    Player(self.game, ((x + 0.5) * _size, (y + 0.5) * _size), FireBall).add(self)
                    break

    @property
    def pos(self):
        return self.sprite.pos

    def draw(self, surface, *args):
        sprite = self.sprite
        center_h, center_v = Constants.absolute_center
        surface.blit(
            sprite.image,
            (center_h - sprite.render_rect.width // 2, center_v - sprite.render_rect.height // 2),
        )
