from math import radians, sin, cos, hypot

from pygame import sprite


class Object(sprite.Sprite):

    def __init__(self, coordinates, animation):
        super().__init__()

        self.animation = animation
        self.image = self.animation.current_image

        self.map_x = coordinates[0]
        self.map_y = coordinates[1]

        self.rect = self.image.get_rect(int(self.map_x), int(self.map_y))

    def update(self, delta_x, delta_y, delta_time):
        self.map_x += delta_x * delta_time
        self.map_y += delta_y * delta_time

        self.image = self.animation.current_image

        self.rect.center = int(self.map_x, self.map_y)


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

        if hypot(self.map_x - self.start[0], self.map_y - self.start[1]) > self.distance:
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
