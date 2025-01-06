from collections import deque
from pygame import transform

from images import sprite_sheet
from timers import Timer


# Custom animation
class Animation:

    def __init__(self, path, file, size, duration):

        self.animation = sprite_sheet(path, file, size)
        self._current = 0
        self._length = len(self.animation)
        self.timer = Timer(duration // self._length)

    @property
    def flipped(self):
        return [transform.flip(image, False, True) for image in self.animation]

    @property
    def frame(self):
        if self.timer.ready:
            self._current = (self._current + 1) % self._length

        return self.animation[self._current]
