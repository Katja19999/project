from pygame import transform

from images import sprite_sheet
from timers import Timer


class Animation:

    def __init__(self, path, file, time, flip, angle=None, auto_reset=True):
        super().__init__()
        self.animation = sprite_sheet(path, file, flip)
        if angle:
            self.set_angle(angle)

        self.timer = Timer(time)
        self.auto_reset = auto_reset

        self._frame = 0
        self._length = len(self.animation) - 1

    def set_angle(self, angle):
        self.animation = [transform.rotate(img, angle) for img in self.animation]

    @property
    def animation_ended(self):
        return self._frame >= self._length

    @property
    def current_image(self):
        if self.timer.ready and not self.animation_ended:
            self._frame += 1

        if self.auto_reset:
            self._frame %= self._length

        return self.animation[self._frame]
