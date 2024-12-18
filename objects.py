from object import GameObject


class Explosion(GameObject):

    def __init__(self, position, animation, damage):
        super().__init__(position, animation)

        self.damage = damage

    def collide(self, object2):
        if hasattr(object2, 'health'):
            object2.health -= self.damage


class Bullet(GameObject):

    def __init__(self, position, animation, speed, angle, damage, after_death):
        super().__init__(position, animation)

        self.speed_x = speed[0]
        self.speed_y = speed[1]

        self.damage = damage
        self.animation.set_angle(angle)

        self.after_death = after_death

    def kill(self):
        if self.after_death:
            _self_in_groups = self.groups()
            for group in _self_in_groups:
                group.add(self.after_death(self.rect.center))

        super().kill()

    def collide(self, object2):
        if hasattr(object2, 'health'):
            object2.health -= self.damage

        self.kill()
