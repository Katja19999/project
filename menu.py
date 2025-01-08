from pygame import sprite
from constants import Constants
from images import sprite_sheet
from ui import Image, Button


class Menu:

    def __init__(self, background, *elements):

        self.ui = sprite.Group(background, *elements)

    def update(self, _delta_time, _keys, mouse_click, mouse_pos):
        button_hash = None
        _sprites = self.ui.sprites()
        for spr in _sprites:
            button_hash = spr.update(mouse_pos, mouse_click)
            if button_hash:
                break

        return button_hash

    def draw(self, surface):
        self.ui.draw(surface)


start_menu = Menu(Image((0, 0), ('menu', 'start'), 'menu.png'),
                  Button((Constants.absolute_center[0], Constants.absolute_center[1] + 112),
                         sprite_sheet(('menu', 'start'), 'play_button.png', (144, 48)),
                         '#play'),
                  Button((Constants.absolute_center[0], Constants.absolute_center[1] + 224),
                         sprite_sheet(('menu', 'start'), 'quit_button.png', (144, 48)),
                         '#quit'),
                  )
