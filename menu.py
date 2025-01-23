from pygame import sprite


class Menu:

    def __init__(self, handler, elements, cursor, special_keys=()):

        self.handler = handler

        self.ui = sprite.Group(*elements)
        self.cursor = cursor
        self.special_keys = dict(special_keys)

        self.functions = self.handler.functions

    def start(self):
        pass

    @staticmethod
    def function(function):
        if isinstance(function, tuple):
            function[0](function[1])
        else:
            function()

    def handle_buttons(self, events, *args):
        _sprites = self.ui.sprites()
        for spr in _sprites:
            button_hash = spr.update(*events['mouse'], args)
            if button_hash:
                self.function(self.functions[button_hash])
                break
        self.cursor.update(*events['mouse'])

    def handle_keys(self, events):
        _keys = events['keys']
        _special_keys = self.special_keys.keys()
        for key in _special_keys:
            if _keys[key]:
                self.function(self.functions[self.special_keys[key]])
                break

    def update(self):
        _events = self.handler.events
        self.handle_buttons(_events)
        self.handle_keys(_events)

    def draw(self, surface):
        self.ui.draw(surface)
        surface.blit(self.cursor.image, self.cursor.rect)
