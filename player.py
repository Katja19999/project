import pygame as pg
from constants import Constants
from characters import Character


class Player(Character):
    def __init__(self):
        super().__init__(('game', 'characters', 'player'), (1000, 1000), 10, 100)

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
        elif keys[pg.K_d] or keys[pg.K_RIGHT]:
            self.dh = self.speed

        if keys[pg.K_w] or keys[pg.K_UP]:
            self.dv = -self.speed
        elif keys[pg.K_s] or keys[pg.K_DOWN]:
            self.dv = self.speed

        if mouse_click and self.state != 'attack':
            self.attack(mouse_pos)

        if self.state in {'attack', 'damage'} and self.states[self.state].end:
            self.update_state()
        elif self.state not in {'attack', 'damage'}:
            self.update_state()

    def attack(self, mouse_pos):
        self.state = 'attack'
        self.states[self.state].start()

    def update(self, events, *args):
        self.control(events)
        super().update(events['delta_time'])


class PlayerGroup(pg.sprite.GroupSingle):
    def __init__(self):
        super().__init__()
        Player().add(self)

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
