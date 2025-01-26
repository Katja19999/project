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
        self.rect.topleft = mouse_pos
        if mouse_click[0]:
            self.state = 'click'
        else:
            self.state = 'normal'


class Image(sprite.Sprite):

    def __init__(self, position, path, file, alpha=False):
        super().__init__()

        self.image = load(path, file, alpha=alpha)
        self.rect = self.image.get_rect(topleft=position)


class HealthBar(sprite.Sprite):

    def __init__(self, position, size, color):
        super().__init__()

        self.rect = pg.Rect(0, 0, *size)
        self.rect.center = position
        self.height = size[1]

        self.color = color
        self.image = pg.Surface(self.rect.size)
        self.image.fill(self.color)

    def update(self, _mouse_click, _mouse_pos, health, max_health=200):
        pos = self.rect.bottom
        self.rect.height = self.height * (health[0] / max_health)
        self.rect.bottom = pos
        if self.rect.height > 0:
            self.image = pg.Surface(self.rect.size)
            self.image.fill(self.color)


class Text(sprite.Sprite):

    def __init__(self, position, text, size):
        super().__init__()

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

    def update(self, mouse_click, mouse_pos, *args):
        if self.rect.collidepoint(mouse_pos):
            self.state = 'hover'

            if mouse_click[0]:
                return self.hashcode
        else:
            self.state = 'normal'


ui = {
    'start_background': Image((0, 0), (), 'menu.png'),
    'end_background': Image((0, 0), (), 'game_over.png'),
    'pause_text': Image((Constants.width // 2 - 160, Constants.height // 2 - 96), (), 'pause_image.png', True),
    'restart_button': Button((Constants.width // 2, Constants.height // 2 + 48),
                             (), 'restart_button.png', (192, 48),
                             '#play'),
    'play_button': Button((Constants.width // 2, Constants.height // 2 + 48),
                          (), 'play_button.png', (144, 48),
                          '#play'),
    'quit_button': Button((Constants.width // 2, Constants.height // 2 + 160),
                          (), 'quit_button.png', (144, 48),
                          '#exit'),
    'result_button': Button((Constants.width // 2, Constants.height // 2 + 272),
                            (), 'result_button.png', (192, 48),
                            '#result'),
    'pause_button': Button((Constants.width - 96, 0 + 32),
                           (), 'pause_button.png', (96, 32),
                           '#pause'),
    'unpause_button': Button((Constants.width // 2, Constants.height // 2),
                             (), 'unpause_button.png', (128, 32),
                             '#unpause'),
    'menu_cursor': Cursor((), 'menu_cursor.png'),
    'game_cursor': Cursor((), 'game_cursor.png'),

    'game_ui': Image((0, 0), (), 'ui.png', True),
    'health_bar': HealthBar((32, 80), (32, 256), '#cb3129')
}
special_keys = ((pg.K_ESCAPE, '#exit'), (pg.K_q, '#quit'))
start_menu = (ui['start_background'], ui['play_button'], ui['quit_button'], ui['result_button'])
game = (ui['pause_button'], ui['health_bar'], ui['game_ui'])
end_menu = (ui['end_background'], ui['quit_button'], ui['restart_button'])
