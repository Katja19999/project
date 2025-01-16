from pygame.time import get_ticks


class Timer:
    # manage time

    def __init__(self, time, auto_reset=True):
        self.time = time
        self.prev = get_ticks()

        self.auto_reset = auto_reset

    def reset(self):
        self.prev = get_ticks()

    @property
    def ready(self):
        left = get_ticks() - self.prev > self.time
        if left and self.auto_reset:
            self.reset()
        return left
