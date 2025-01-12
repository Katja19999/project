import math as m

from pygame import sprite

from images import load
from timers import Timer
from groups import CameraGroup


class Bullet(sprite.Sprite):

    def __init__(self, position, path, file, angle, speed, damage):
        super().__init__()

        self.image = load(path, file)

        self.dh = m.cos(angle) * speed
        self.dv = m.sin(angle) * speed

        self.position = list(position)
        self.rect = self.image.get_rect(center=self.position)

        self.damage = damage
        self.death_timer = Timer(500, auto_reset=False)

    def set_position(self, position):
        self.rect.center = position

    def update(self, delta_time):
        self.position[0] += self.dh
        self.position[1] += self.dv

        self.set_position(self.position)

        if self.death_timer.ready:
            self.kill()


class FireBall(Bullet):

    def __init__(self, position, angle):
        super().__init__(position, (), 'fireball.png', angle, 12, 40)


class ObjectGroup(CameraGroup):
    pass
