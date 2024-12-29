import pygame as pg
from pygame import sprite

from objects import StaticObject


class Image(StaticObject):
    pass


class Text(sprite.Sprite):

    def __init__(self, group, position, text, size):
        super().__init__(group)

        self.text = text
        self.font = pg.font.SysFont(self.text, size)
        self.image = self.font.render(self.text, True, 'white')

        self.rect = self.image.get_rect(center=position)


class Button(sprite.Sprite):

    def __init__(self, group, position, animations, hashcode):
        super().__init__(group)

        self.animations = dict(zip(['normal', 'hover'], animations))
        self.state = 'normal'

        self.rect = self.image.get_rect(center=position)

        self.hashcode = hashcode

    @property
    def image(self):
        return self.animations[self.state].frame

    def update(self, mouse_pos, mouse_click):
        if self.rect.collidepoint(mouse_pos):
            self.state = 'hover'

            if mouse_click:
                return self.hashcode
