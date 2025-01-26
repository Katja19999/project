from database import get_result
from ui import Text
from menu import Menu
from constants import Constants


class ResultMenu(Menu):

    def __init__(self, handler, elements, cursor, special_keys=()):
        super().__init__(handler, elements, cursor, special_keys)

        self.text = None

    def start(self):
        result = get_result()
        self.text = Text((0, 0), f'"{get_result()} enemies killed" best so far.' if result
                         else "You haven't played the game yet.", 64)
        self.text.rect.topleft = ((Constants.width - self.text.rect.width) // 2,
                                  (Constants.height - self.text.rect.height) // 2)

    def draw(self, surface):
        surface.fill('#12051b')
        self.ui.draw(surface)
        surface.blit(self.text.image, self.text.rect)
        surface.blit(self.cursor.image, self.cursor.rect)
