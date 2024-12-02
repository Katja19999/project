from pygame.time import get_ticks


class Timer:
    def __init__(self, delta, reset=True):

        self.delta = delta
        self.prev = get_ticks()

        self.reset = reset

    def set(self):
        self.prev = get_ticks()

    def __call__(self):
        left = get_ticks() - self.prev > self.delta
        if left and self.reset:
            self.set()
        return left
