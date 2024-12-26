from collections import deque

from images import sprite_sheet
from timers import Timer


# Custom animation
class Animation:

    def __init__(self, path, file, size, duration):

        self.animation = deque(sprite_sheet(path, file, size))
        self.timer = Timer(duration)

    @property
    def frame(self):
        if self.timer.ready:
            self.animation.rotate(-1)

        return self.animation[0]
