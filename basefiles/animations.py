from images import sprite_sheet
from timers import Timer


# Custom animation
class Animation:

    def __init__(self, path, file, size, duration, auto_reset):

        self.animation = sprite_sheet(path, file, size)

        self.length = len(self.animation) - 2
        self.frame = 0

        self.timer = Timer(duration // self.length)
        self.auto_reset = auto_reset

    @property
    def end(self):
        return self.frame > self.length

    @property
    def image(self):
        self.update()
        return self.animation[self.frame]

    def reset(self):
        self.frame = 0

    def update(self):
        if self.timer.ready:
            if not self.end:
                self.frame += 1
            else:
                if self.auto_reset:
                    self.reset()
