from images import sprite_sheet
from sounds import load
from timers import Timer


class State:

    def __init__(self, path, animation, sound=None, time=500, auto_reset=True):

        self.animation = sprite_sheet(path, animation, (32, 32))
        self.sound = load(path, sound) if sound else None

        self.length = len(self.animation)
        self.frame = 0

        self.timer = Timer(time // self.length)

        self.auto_reset = auto_reset

    @property
    def end(self):
        return self.frame == self.length - 1

    @property
    def image(self):
        return self.animation[self.frame]

    def reset(self):
        self.frame = 0

    def start(self):
        if self.end:
            self.reset()
        if self.sound:
            self.sound.play()

    def update(self):
        if self.timer.ready:
            if self.end and self.auto_reset:
                self.reset()
            elif not self.end:
                self.frame += 1
