import pygame as pg
from pygame import sprite

from constants import Constants
from images import load, sprite_sheet


class Cursor(pg.sprite.Sprite):

    def __init__(self, path, file, size=(16, 16)):
        super().__init__()

        self.images = dict(zip(['normal', 'click'], sprite_sheet(path, file, size)))
        self.state = 'normal'

        self.rect = self.image.get_rect()

    @property
    def image(self):
        return self.images[self.state]

    def update(self, mouse_click, mouse_pos):
        self.rect.center = mouse_pos
        if mouse_click:
            self.state = 'click'
        else:
            self.state = 'normal'


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

    def __init__(self, position, path, file, size, hashcode):
        super().__init__()

        self.images = dict(zip(['normal', 'hover'], sprite_sheet(path, file, size)))
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


ui = {
    'background': Image((0, 0), ('menu',), 'menu.png'),
    'play_button': Button((Constants.width // 2, Constants.height // 2 + 64),
                          ('menu', 'start'), 'play_button.png', (144, 48),
                          '#play'),
    'quit_button': Button((Constants.width // 2, Constants.height // 2 + 192),
                          ('menu', 'start'), 'quit_button.png', (144, 48),
                          '#exit'),
    'menu_cursor': Cursor(('menu', 'start'), 'menu_cursor.png'),
    'game_cursor': Cursor(('game',), 'game_cursor.png'),
}
special_keys = ((pg.K_ESCAPE, '#exit'), (pg.K_q, '#quit'))
start_menu = (ui['background'], ui['play_button'], ui['quit_button'], ui['menu_cursor'])
game = (ui['game_cursor'], )
