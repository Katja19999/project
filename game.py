import pygame as pg
import sys as sys

from constants import RESOLUTION, SCREEN_FLAGS, SCREEN_DEPTH, BLACK, FPS


class GameHandler:

    pg.init()
    pg.display.set_caption('Game')
    # pg.display.set_icon("SOME IMAGE")
    pg.event.set_allowed([pg.QUIT, pg.MOUSEBUTTONDOWN, pg.MOUSEBUTTONUP, pg.KEYDOWN, pg.KEYUP])

    def __init__(self):

        self.display = pg.display.set_mode(RESOLUTION, SCREEN_FLAGS, SCREEN_DEPTH)
        self.clock = pg.time.Clock()

        self.states = {}
        self.current_state = None

        self._events = {'quit': False, 'mouse_click': (False, None), 'button_press': (False, None)}
        self._delta_time = 0
        self._previous = pg.time.get_ticks()

    @staticmethod
    def quit():
        pg.quit()
        sys.exit()

    def update_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self._events['quit'] = True

            if event.type == pg.MOUSEBUTTONDOWN:
                self._events['mouse_click'] = (True, event.pos)
            elif event.type == pg.MOUSEBUTTONUP:
                self._events['mouse_click'] = (False, None)

            if event.type == pg.KEYDOWN:
                self._events['button_press'] = (True, event.key)
            elif event.type == pg.KEYUP:
                self._events['button_press'] = (False, None)

    def update_delta_time(self):
        self._delta_time = pg.time.get_ticks() - self._previous
        self._previous = pg.time.get_ticks()

    def update_state(self, state):
        self.current_state = self.states[state]

    def update(self):
        self.update_events()
        self.update_delta_time()

        if self._events['quit']:
            self.quit()

        self.current_state.update(self._delta_time, self._events['mouse_click'], self._events['button_press'])

    def draw(self):
        self.display.fill(BLACK)
        self.current_state.draw(self.display)

        pg.display.flip()

    def run(self):
        while True:
            self.update()
            self.draw()

            self.clock.tick_busy_loop(FPS)
