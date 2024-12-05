from math import radians, sin, cos, hypot

from pygame import sprite


class Object(sprite.Sprite):

    def __init__(self, coordinates, animation):
        super().__init__()

        self.animation = animation
        self.image = self.animation.current_image

        self.x = coordinates[0]
        self.y = coordinates[1]

        self.rect = self.image.get_rect(int(self.x), int(self.y))

    def update(self, delta_x, delta_y, delta_time):
        self.x += delta_x * delta_time
        self.y += delta_y * delta_time

        self.image = self.animation.current_image

        self.rect.center = int(self.x, self.y)


class Explosion(Object):

    def __init__(self, coordinates, animation, damage):
        super().__init__(coordinates, animation)

        self.damage = damage

    def update(self, delta_x, delta_y, delta_time):
        super().update(delta_x, delta_y, delta_time)

        if self.animation.end:
            self.kill()


class Bullet(Object):

    def __init__(self, coordinates, angle, speed, distance, animation, damage):
        super().__init__(coordinates, animation)

        self.animation.rotate(angle)

        rads = radians(angle)
        self.speed_x = cos(rads) * speed
        self.speed_y = sin(rads) * speed

        self.start = coordinates
        self.distance = distance

        self.damage = damage

    def update(self, delta_x, delta_y, delta_time):
        super().update(delta_x + self.speed_x, delta_y + self.speed_y, delta_time)

        if hypot(self.x - self.start[0], self.y - self.start[1]) > self.distance:
            self.kill()


class Collectable(Object):

    def __init__(self, coordinates, animation, attribute, value):
        super().__init__(coordinates, animation)

        self.attribute = attribute
        self.value = value

    def hit(self, other):
        if hasattr(other, 'collect'):
            other.collect(self.attribute, self.value)
            self.kill()
