import math as m

import pygame as pg
from constants import Constants
from characters import Character
from objects import FireBall


class Player(Character):

    def __init__(self, position, bullet_groups, bullet):
        super().__init__(('player', ), position, 15, 100)

        self.bullet_groups = bullet_groups
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
        if (keys[pg.K_a] or keys[pg.K_LEFT]) and not self.blocked['left']:
            self.dh = -self.speed
            self.flipped = True
        elif (keys[pg.K_d] or keys[pg.K_RIGHT]) and not self.blocked['right']:
            self.dh = self.speed
            self.flipped = False

        if (keys[pg.K_w] or keys[pg.K_UP]) and not self.blocked['top']:
            self.dv = -self.speed
        elif (keys[pg.K_s] or keys[pg.K_DOWN]) and not self.blocked['bottom']:
            self.dv = self.speed

        self.blocked['left'] = False
        self.blocked['right'] = False
        self.blocked['top'] = False
        self.blocked['bottom'] = False

        self.flipped = mouse_pos[0] < Constants.width // 2

        if mouse_click[0] and self.state not in {'attack', 'damage'}:
            self.attack(mouse_pos)

        self.update_state()

    def attack(self, mouse_pos):
        self.state = 'attack'
        self.states[self.state].start()

        for group in self.bullet_groups:
            group.add(self.bullet(self.position, m.atan2(mouse_pos[1] - Constants.height // 2,
                                  mouse_pos[0] - Constants.width // 2)))

    def damage(self, damage):
        self.state = 'damage'
        self.states[self.state].start()
        self.health -= damage

    def stop(self, object2):
        rect1 = self.collision_rect
        rect2 = object2.collision_rect if hasattr(object2, 'collision_rect') else object2.rect
        print(rect1.left, rect1.right, rect1.top, rect1.bottom)
        print(rect2.right, rect2.left, rect2.bottom, rect2.top)

        self.blocked['left'] = rect1.left < rect2.right
        self.blocked['right'] = rect1.right > rect2.left
        self.blocked['top'] = rect1.top < rect2.bottom
        self.blocked['bottom'] = rect1.bottom > rect2.top

    def hit(self, object2):
        if hasattr(object2, 'damage'):
            if not isinstance(object2, self.bullet):
                self.hit(object2.damage)
        else:
            self.stop(object2)

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
