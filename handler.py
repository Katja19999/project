import sys as sys
import os
import pygame as pg

from constants import Constants
from menu import start_menu
from game import game


class GameHandler:

    pg.mixer.music.load(os.path.join(Constants.data_directory, 'music.mp3'))
    pg.mixer.music.play()

    def __init__(self):

        self.display = Constants.display
        self.clock = Constants.clock
        self.fps = Constants.fps

        self.delta_time = 0
        self.previous = pg.time.get_ticks()

        self.modes = {'start': start_menu, 'game': game, 'end': None}
        self.mode = self.modes['start']

        self._events = {'keys': pg.key.get_pressed(), 'mouse': [False, (0, 0)]}

        self.functions = {
            '#quit': self.end,
            '#exit': (self.open, 'start'),
            '#play': (self.open, 'game'),
        }

    @staticmethod
    def end():
        pg.quit()
        sys.exit()

    def open(self, mode):
        self.mode = self.modes[mode]

    def events(self):
        _events = pg.event.get()

        self._events['mouse'][1] = pg.mouse.get_pos()
        self._events['keys'] = pg.key.get_pressed()

        for event in _events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self._events['mouse'][0] = True

            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    self._events['mouse'][0] = False

    def update(self):
        self.delta_time = pg.time.get_ticks() - self.previous
        self.previous = pg.time.get_ticks()

        self.events()
        _result = self.mode.update(self.delta_time, self._events['keys'], *self._events['mouse'])
        if _result:
            function = self.functions[_result]
            if type(function) is tuple:
                function[0](function[1])
            else:
                function()
        elif self._events['keys'][pg.K_ESCAPE]:
            self.end()
        elif self._events['keys'][pg.K_q]:
            self.open('start')

    def draw(self):
        self.mode.draw(self.display)

        pg.display.flip()

    def run(self):
        while True:
            self.update()
            self.draw()

            self.clock.tick_busy_loop(self.fps)
