import pygame as pg
import sys as sys

from constants import Constants
from menu import start_menu


class GameHandler:

    pg.event.set_allowed([pg.MOUSEBUTTONDOWN, pg.MOUSEBUTTONUP, pg.KEYDOWN, pg.KEYUP])

    display = Constants.display
    clock = Constants.clock
    fps = Constants.fps

    modes = {'start': start_menu, 'game': None, 'end': None}
    mode = modes['start']

    _events = {'keys': [], 'mouse': [False, (0, 0)]}

    @staticmethod
    def end():
        pg.quit()
        sys.exit()

    def open(self, mode):
        self.mode = self.modes[mode]

    def events(self):
        _events = pg.event.get()

        self._events['mouse'][1] = pg.mouse.get_pos()

        for event in _events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self._events['mouse'][0] = True

            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    self._events['mouse'][0] = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.end()
                self._events['keys'].append(event.key)

            if event.type == pg.KEYUP:
                self._events['keys'].remove(event.key)

    def update(self):
        self.events()
        _result = self.mode.update(*self._events['mouse'])
        if _result:
            pass

    def draw(self):
        self.mode.draw(self.display)

        pg.display.flip()

    def run(self):
        while True:
            self.update()
            self.draw()

            self.clock.tick_busy_loop(self.fps)
