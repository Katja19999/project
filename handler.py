import pygame as pg
import sys as sys

from constants import Constants
from menu import start_menu
from game import game


class GameHandler:

    pg.event.set_allowed([pg.MOUSEBUTTONDOWN, pg.MOUSEBUTTONUP, pg.KEYDOWN, pg.KEYUP])

    display = Constants.display
    clock = Constants.clock
    fps = Constants.fps

    modes = {'start': start_menu, 'game': game, 'end': None}
    mode = modes['start']

    _events = {'keys': pg.key.get_pressed(), 'mouse': [False, (0, 0)]}

    def __init__(self):

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
        self.events()
        _result = self.mode.update(self._events['keys'], *self._events['mouse'])
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
