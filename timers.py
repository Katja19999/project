from pygame.time import get_ticks


class Timer:
    def __init__(self, delta, auto_reset=True):

        self.delta = delta
        self.prev = get_ticks()

        self.auto_reset = auto_reset

    def reset(self):
        self.prev = get_ticks()

    def __call__(self):
        left = get_ticks() - self.prev > self.delta
        if left and self.auto_reset:
            self.reset()
        return left
