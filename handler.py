import pygame as pg
import sys as sys

from constants import Constants


class GameHandler:

    pg.event.set_allowed([pg.MOUSEBUTTONDOWN, pg.MOUSEBUTTONUP, pg.KEYDOWN, pg.KEYUP])

    display = Constants.display
    clock = Constants.clock
    fps = Constants.fps

    modes = {'start': None, 'game': None, 'end': None}
    mode = modes['start']

    events = {'keys': [], 'mouse': (False, None)}

    @staticmethod
    def end():
        pg.quit()
        sys.exit()

    def _events(self):
        _events = pg.event.get()

        for event in _events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.events['mouse'] = (True, event.pos)

            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    self.events['mouse'] = (False, None)

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.end()
                self.events['keys'].append(event.key)

            if event.type == pg.KEYUP:
                self.events['keys'].remove(event.key)

    def update(self):
        self._events()
        self.mode.update(*self.events['mouse'])

    def draw(self):
        self.mode.draw(self.display)

        pg.display.flip()

    def run(self):
        while True:
            self.update()
            self.draw()

            self.clock.tick_busy_loop(self.fps)
