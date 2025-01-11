from pygame import sprite


class Menu:

    def __init__(self, handler, elements, special_keys=()):

        self.handler = handler

        self.ui = sprite.Group(*elements)
        self.special_keys = dict(special_keys)

    @staticmethod
    def function(function):
        if isinstance(function, tuple):
            function[0](function[1])
        else:
            function()

    def handle_buttons(self, events):
        _sprites = self.ui.sprites()
        for spr in _sprites:
            button_hash = spr.update(*events['mouse'])
            if button_hash:
                self.function(self.handler.functions[button_hash])
                break

    def handle_keys(self, events):
        _keys = events['keys']
        _special_keys = self.special_keys.keys()
        for key in _special_keys:
            if _keys[key]:
                self.function(self.handler.functions[self.special_keys[key]])
                break

    def update(self):
        _events = self.handler.events
        self.handle_buttons(_events)
        self.handle_keys(_events)

    def draw(self, surface):
        self.ui.draw(surface)
