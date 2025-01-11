import sys as sys
import os
import pygame as pg

from constants import Constants
from menu import Menu
from ui import start_menu, game, special_keys
from game import InGameHandler


class GameHandler:

    pg.mixer.music.load(os.path.join(Constants.data_directory, 'music.mp3'))
    pg.mixer.music.play()

    def __init__(self):

        self.display = Constants.display
        self.clock = Constants.clock
        self.fps = Constants.fps
        self.previous = pg.time.get_ticks()

        self.modes = {'start': Menu(self, start_menu, special_keys),
                      'game': InGameHandler(self, game, special_keys),
                      'end': None}
        self.mode = self.modes['start']

        self.events = {'delta_time': 0, 'keys': pg.key.get_pressed(), 'mouse': [False, (0, 0)]}
        self.functions = {'#exit': self.end, '#quit': (self.open, 'start'), '#play': (self.open, 'game')}

    @staticmethod
    def end():
        pg.quit()
        sys.exit()

    def open(self, mode):
        self.mode = self.modes[mode]

    def handle_events(self):
        _events = pg.event.get()

        self.events['delta_time'] = pg.time.get_ticks() - self.previous
        self.previous = pg.time.get_ticks()
        self.events['mouse'][1] = pg.mouse.get_pos()
        self.events['keys'] = pg.key.get_pressed()

        for event in _events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.events['mouse'][0] = True

            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    self.events['mouse'][0] = False

    def update(self):
        self.handle_events()
        self.mode.update()

    def draw(self):
        self.mode.draw(self.display)

        pg.display.flip()

    def run(self):
        while True:
            self.update()
            self.draw()

            self.clock.tick_busy_loop(self.fps)
