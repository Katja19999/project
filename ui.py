import pygame as pg
from pygame import sprite

from images import load


class Image(sprite.Sprite):

    def __init__(self, position, path, file, alpha=False):
        super().__init__()

        self.image = load(path, file, alpha=alpha)
        self.rect = self.image.get_rect(topleft=position)


class Text(sprite.Sprite):

    def __init__(self, group, position, text, size):
        super().__init__(group)

        self.text = text
        self.font = pg.font.SysFont(self.text, size)
        self.image = self.font.render(self.text, True, 'white')

        self.rect = self.image.get_rect(center=position)


class Button(sprite.Sprite):

    def __init__(self, position, images, hashcode):
        super().__init__()

        self.images = dict(zip(['normal', 'hover'], images))
        self.state = 'normal'

        self.rect = self.image.get_rect(center=position)

        self.hashcode = hashcode

    @property
    def image(self):
        return self.images[self.state]

    def update(self, mouse_click, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.state = 'hover'

            if mouse_click:
                return self.hashcode
        else:
            self.state = 'normal'


menu_background = Image((0, 0), 'menu', 'menu.png')
quit_button = Button(())
