from pygame import transform

from images import Image
from timers import Timer


class Animation(Image):

    def __init__(self, path, file, time, flip, angle, auto_reset=True):

        self.animation = self.sprite_sheet(path, file, flip)
        self.animation = [transform.rotate(img, angle) for img in self.animation]

        self.timer = Timer(time)
        self.auto_reset = auto_reset

        self._frame = 0
        self._length = len(self.animation) - 1

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
