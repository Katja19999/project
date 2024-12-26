from pygame import sprite


class StaticObject(sprite.Sprite):
    # manage static objects like walls and environment

    def __init__(self, group, position, animation):
        super().__init__(group)

        self.animation = animation
        self.rect = self.image.get_rect(center=position)

    @property
    def image(self):
        return self.animation.frame
