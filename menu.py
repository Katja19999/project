import pygame as pg

from pygame import sprite


class Menu:

    def __init__(self, game, background, elements, functions, music):

        self.game = game
        self.ui = sprite.Group(background, *elements)

        self.functions = functions

        pg.mixer.music.load(music)
        pg.mixer.music.play()

    def update(self, mouse_pos, mouse_click):
        button_hash = None
        _sprites = self.ui
        for spr in _sprites:
            button_hash = spr.update(mouse_pos, mouse_click)

        if button_hash:
            self.functions[button_hash]()

    def draw(self, surface):
        self.ui.draw(surface)
