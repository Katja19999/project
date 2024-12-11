import pygame as pg
import sys as sys

from constants import RESOLUTION, SCREEN_FLAGS, SCREEN_DEPTH, BLACK, FPS


class GameHandler:

    pg.init()

    def __init__(self):
        pg.display.set_caption('Game')
        # pg.display.set_icon("SOME IMAGE")

        pg.event.set_allowed([pg.QUIT])

        self.display = pg.display.set_mode(RESOLUTION, SCREEN_FLAGS, SCREEN_DEPTH)
        self.clock = pg.time.Clock()

        self.modes = {
            'game': None
        }
        self.current_mode = self.modes['game']
        self._previous = pg.time.get_ticks()
        self._delta_time = 0

    @staticmethod
    def handle_quit():
        if pg.event.peek(pg.QUIT):
            pg.quit()
            sys.exit()

    def update_delta_time(self):
        self._delta_time = pg.time.get_ticks() - self._previous
        self._previous = pg.time.get_ticks()

    def set_mode(self, mode):
        if mode in self.modes.keys():
            self.current_mode = self.modes[mode]

    def update(self):
        self.current_mode.update(self._delta_time)

    def draw(self):
        self.display.fill(BLACK)
        self.current_mode.draw(self.display)

        pg.display.flip()

    def run(self):
        while True:
            self.handle_quit()
            self.update()
            self.draw()

            self.clock.tick_busy_loop(FPS)
