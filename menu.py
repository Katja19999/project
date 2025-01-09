from pygame import sprite


class Menu:

    def __init__(self, handler, background, *elements):

        self.handler = handler

        self.ui = sprite.Group(background, *elements)

    def update(self):
        button_hash = None
        _sprites = self.ui.sprites()
        for spr in _sprites:
            button_hash = spr.update(*self.handler.events['mouse'])
            if button_hash:
                break

        return button_hash

    def draw(self, surface):
        self.ui.draw(surface)
