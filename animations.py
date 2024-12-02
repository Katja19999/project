from pygame import transform

from images import sheet
from timers import Timer


# Готово
class ObjectAnimation:
    # Create ANIMATION
    # For one-animation
    # OBJECTS: decorations, walls, bullets, explosions

    def __init__(self, path, file, width, height, time, reset=True):

        self.animation = sheet(file, path, width, height, True)
        self._animation = self.animation.copy()

        self.timer = Timer(time)
        self.frame = 0
        self._len = len(self.animation) - 1
        self.reset = reset

    def rotate(self, angle):
        self._animation = [transform.rotate(img, angle) for img in self.animation]

    def __call__(self):
        if self.timer and not self.end:
            self.frame += 1

        if self.reset:
            self.frame %= self._len

        return self._animation[self.frame]

    @property
    def end(self):
        return self.frame >= self._len


class CharacterAnimation:
    # Create ANIMATION
    # For multiple-animation
    # OBJECTS: characters

    def __init__(self, states, sheets, path, time):

        self.dirs = ['up', 'left', 'down', 'right']
        self.states = states

        self.animation = {}
        self.load_animation(sheets, path)

        self.timer = Timer(time)
        self.dir = self.dirs[0]
        self.state = self.states[0]
        self.frame = 0

    @staticmethod
    def load_sheet(path, file, width, height):
        return sheet(file, path, width, height, True)

    def load_animation(self, sheets, path):
        ind = 0
        for direction in self.dirs[:-1]:
            self.animation[direction] = {}

            for state in self.states:
                self.animation[direction][state] = self.load_sheet(path, *sheets[ind])
                ind += 1

        self.animation[self.dir[-1]] = {}
        for state in self.states:
            self.animation[self.dir[-1]][state] = transform.flip(self.animation[self.dir[1]][state], True, False)

    @property
    def playing(self):
        return self.animation[self.dir][self.state]

    @property
    def _len(self):
        return len(self.playing) - 1

    @property
    def end(self):
        return self.frame >= self._len

    def change_state(self, value):
        if value in self.states:
            self.state = value

    def change_dir(self, value):
        if value in self.dirs:
            self.dir = value

    def __call__(self):
        if self.timer and not self.end:
            self.frame += 1
            self.frame %= self._len

        return self.playing[self.frame]
