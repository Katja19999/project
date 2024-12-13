from object import GameObject


class Explosion(GameObject):

    def __init__(self, position, animation, damage):
        super().__init__(position, animation)

        self.damage = damage


class Bullet(GameObject):

    def __init__(self, position, animation, speed, angle, damage):
        super().__init__(position, animation)

        self.speed_x = speed[0]
        self.speed_y = speed[1]

        self.damage = damage
        self.animation.set_angle(angle)
