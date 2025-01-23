import math as m

import pygame as pg

from characters import Character
from constants import Constants
from objects import FireBall
from environment import Wall, Exit


class Player(Character):

    def __init__(self, game, position, bullet):
        super().__init__(game, ('player',), position, 15, 150)

        self.bullet = bullet

    @property
    def pos(self):
        return self.position

    def update_movement(self, events, walls):
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

        _move_x = self.dh * events['delta_time']
        _move_y = self.dv * events['delta_time']

        self.rect.x += _move_x
        _collided = pg.sprite.spritecollide(self, walls, False)
        if _collided:
            for spr in _collided:
                if isinstance(spr, Wall) and _move_x:
                    self.rect.x -= _move_x
                    _move_x = 0
                elif isinstance(spr, Exit):
                    self.game.new_level()

        self.rect.y += _move_y
        _collided = pg.sprite.spritecollide(self, walls, False)
        if _collided:
            for spr in _collided:
                if isinstance(spr, Wall) and _move_y:
                    self.rect.y -= _move_y
                    _move_y = 0
                elif isinstance(spr, Exit):
                    self.game.new_level()

        if _move_x != 0 and _move_y != 0:
            _move_x /= self.normalize
            _move_y /= self.normalize

        self.position[0] += _move_x
        self.position[1] += _move_y

        self.set_position()

    def update_state(self, events):
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

    def update(self, events, walls):
        self.update_movement(events, walls)
        self.update_state(events)


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

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
        if self.sprite.health <= 0:
            self.game.function(self.game.functions['#end'])

    @property
    def pos(self):
        return self.sprite.pos

    @property
    def health(self):
        return self.sprite.health

    def draw(self, surface, *args):
        sprite = self.sprite
        center_h, center_v = Constants.absolute_center
        surface.blit(
            sprite.image,
            (center_h - sprite.render_rect.width // 2, center_v - sprite.render_rect.height // 2),
        )
