from math import radians, sin, cos, hypot

from pygame import sprite


class Object(sprite.Sprite):

    def __init__(self, coordinates, animation):
        super().__init__()

        self.animation = animation
        self.image = self.animation()

        self.x = coordinates[0]
        self.y = coordinates[1]

        self.rect = self.image.get_rect(int(self.x), int(self.y))

    def update(self, dx, dy, delta):
        self.x += dx * delta
        self.y += dy * delta

        self.image = self.animation.image

        self.rect.center = int(self.x, self.y)

    def hit(self, other):
        if hasattr(self, 'damage') and hasattr(other, 'health'):
            other.damage(self.damage)


class Explosion(Object):

    def __init__(self, coordinates, animation, damage):
        super().__init__(coordinates, animation)

        self.damage = damage

    def update(self, dx, dy, delta):
        super().update(dx, dy, delta)

        if self.animation.end:
            self.kill()


class Bullet(Object):

    def __init__(self, coordinates, angle, speed, distance, animation, damage, death_event=None):
        super().__init__(coordinates, animation)

        self.animation.rotate(angle)

        rads = radians(angle)
        self.dx = cos(rads) * speed
        self.dy = sin(rads) * speed

        self.start = coordinates
        self.distance = distance

        self.damage = damage
        if death_event:
            self.death_event = death_event

    def update(self, dx, dy, delta):
        super().update(dx + self.dx, dy + self.dy, delta)

        if hypot(self.x - self.start[0], self.y - self.start[1]) > self.distance:
            self.kill()

    def hit(self, other):
        super().hit(other)
        self.kill()

    def kill(self):
        if self.death_event:
            self.death_event.add(self.groups())
        super().kill()


class Collectables(Object):

    def __init__(self, coordinates, animation, attribute, value):
        super().__init__(coordinates, animation)

        self.attribute = attribute
        self.value = value

    def hit(self, other):
        if hasattr(other, 'collect'):
            other.collect(self.attribute, self.value)
            self.kill()
