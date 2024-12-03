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
        self.length = len(self.animation) - 1
        self.reset = reset

    def rotate(self, angle):
        self._animation = [transform.rotate(img, angle) for img in self.animation]

    @property
    def end(self):
        return self.frame >= self.length

    @property
    def image(self):
        if self.timer and not self.end:
            self.frame += 1

        if self.reset:
            self.frame %= self.length

        return self._animation[self.frame]


class CharacterAnimation:
    # Create ANIMATION
    # For multiple-animation
    # OBJECTS: characters

    def __init__(self, states, sheets, path, time):

        self.directions = ['up', 'left', 'down', 'right']
        self.states = states

        self.animation = {}
        self.load_animation(sheets, path)

        self.timer = Timer(time)
        self.dir = self.directions[0]
        self.state = self.states[0]
        self.frame = 0

    @staticmethod
    def load_sheet(path, file, width, height):
        return sheet(file, path, width, height, True)

    def load_animation(self, sheets, path):
        ind = 0
        for direction in self.directions[:-1]:
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
    def length(self):
        return len(self.playing) - 1

    @property
    def end(self):
        return self.frame >= self.length

    def change_state(self, value):
        if value in self.states:
            self.state = value

    def change_dir(self, value):
        if value in self.directions:
            self.dir = value

    @property
    def image(self):
        if self.timer and not self.end:
            self.frame += 1
            self.frame %= self.length

        return self.playing[self.frame]
