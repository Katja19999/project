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

    def update_movement(self, events):
        keys = events['keys']

        self.dh = self.dv = 0
        if keys[pg.K_a] or keys[pg.K_LEFT]:
            self.dh = -self.speed
            self.flipped = True
        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            self.dh = self.speed
            self.flipped = False

        if keys[pg.K_w] or keys[pg.K_UP]:
            self.dv = -self.speed
        if keys[pg.K_s] or keys[pg.K_DOWN]:
            self.dv = self.speed

        _move_x = self.dh * events['delta_time'] / 100
        _move_y = self.dv * events['delta_time'] / 100

        _walls = self.game.environment

        self.rect.x += _move_x
        if pg.sprite.spritecollideany(self, _walls):
            self.rect.x -= _move_x
            _move_x = 0

        self.rect.y += _move_y
        if pg.sprite.spritecollideany(self, _walls):
            self.rect.y -= _move_y
            _move_y = 0

        if _move_x != 0 and _move_y != 0:
            _move_x /= self.normalize
            _move_y /= self.normalize

        self.position[0] += _move_x
        self.position[1] += _move_y

        self.set_position()

    def update_state(self, events=None, *args):
        self.flipped = events['mouse'][1][0] < Constants.width // 2
        if events['mouse'][0][0]:
            self.attack(events['mouse'][1])
        super().update_state()

    def attack(self, mouse_pos):
        if self.state not in {'attack', 'damage'}:
            self.state = 'attack'
            self.states[self.state].start()

            self.game.objects.add(self.bullet(self.position, m.atan2(mouse_pos[1] - Constants.height // 2,
                                              mouse_pos[0] - Constants.width // 2)))


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
