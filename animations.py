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

        self.shift_timer = Timer(time)
        self.current_frame = 0
        self.anim_length = len(self.animation) - 1
        self.auto_reset = reset

    def rotate(self, angle):
        self._animation = [transform.rotate(img, angle) for img in self.animation]

    @property
    def end(self):
        return self.current_frame >= self.anim_length

    @property
    def current_image(self):
        if self.shift_timer and not self.end:
            self.current_frame += 1

        if self.auto_reset:
            self.current_frame %= self.anim_length

        return self._animation[self.current_frame]


class CharacterAnimation:
    # Create ANIMATION
    # For multiple-animation
    # OBJECTS: characters

    def __init__(self, states, sheets, path, time):

        self.directions = ['left', 'right']
        self.states = states

        self.animation = {}
        self.load_animation(sheets, path)

        self.shift_timer = Timer(time)
        self.current_direction = self.directions[0]
        self.current_state = self.states[0]
        self.current_frame = 0

    @staticmethod
    def load_sheet(path, file, width, height):
        return sheet(file, path, width, height, True)

    def load_animation(self, sheets, path):
        self.animation[self.directions[0]] = {}
        self.animation[self.directions[1]] = {}

        for ind, state in enumerate(self.states):
            self.animation[self.directions[0]][state] = self.load_sheet(path, *sheets[ind])

        for state, animation in self.animation[self.directions[0]].items():
            self.animation[self.directions[1]][state] = [transform.flip(img, True, False)
                                                         for img in animation]

    @property
    def current_animation(self):
        return self.animation[self.directions][self.current_state]

    @property
    def animation_length(self):
        return len(self.current_animation) - 1

    @property
    def end(self):
        return self.current_frame >= self.animation_length

    @property
    def current_image(self):
        if self.shift_timer and not self.end:
            self.current_frame += 1
            self.current_frame %= self.animation_length

        return self.current_animation[self.current_frame], self.current_frame

    def change_state(self, value):
        if value in self.states:
            self.current_state = value

    def change_direction(self, value):
        if value in self.directions:
            self.current_direction = value
