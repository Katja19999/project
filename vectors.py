import math


class VectorPoint:
    # manage coordinates and speeds

    def __init__(self, x, y, starting_x=None, starting_y=None):

        self.starting_x = starting_x if starting_x else x
        self.starting_y = starting_y if starting_y else y

        self.x = x
        self.y = y

    @property
    def position(self):
        return self.x, self.y

    @property
    def distance(self):
        return int(math.dist(
            (self.starting_x, self.starting_y),
            (self.x, self.y)
        ))

    def update(self, other):
        self.x += other.x
        self.y += other.y
