import os
import sys as sys

import pygame as pg

from constants import Constants
from game import InGameHandler
from menu import Menu
from ui import ui, start_menu, game, end_menu, special_keys


class GameHandler:
    pg.mixer.music.load(os.path.join(Constants.data_directory, Constants.sound_directory, 'music.mp3'))
    pg.mixer.music.play()

    def __init__(self):
        self.display = Constants.display
        self.clock = Constants.clock
        self.fps = Constants.fps

        self.events = {'delta_time': 0,
                       'keys': pg.key.get_pressed(),
                       'mouse': (pg.mouse.get_pressed(), pg.mouse.get_pos())}

        self.functions = {'#exit': self.end,
                          '#quit': (self.open, 'start'),
                          '#play': (self.open, 'game'),
                          '#end': (self.open, 'end')
                          }

        self.modes = {'start': Menu(self, start_menu, ui['menu_cursor'], special_keys),
                      'game': InGameHandler(self, game, ui['game_cursor'], special_keys),
                      'end': Menu(self, end_menu, ui['menu_cursor'], special_keys)}

        self.mode = self.modes['start']

    @staticmethod
    def end():
        pg.quit()
        sys.exit()

    def open(self, mode):
        self.mode = self.modes[mode]
        self.mode.start()

    def handle_events(self):
        pg.event.clear()

        self.events['delta_time'] = self.clock.tick_busy_loop(self.fps) / 100
        self.events['mouse'] = (pg.mouse.get_pressed(), pg.mouse.get_pos())
        self.events['keys'] = pg.key.get_pressed()

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
