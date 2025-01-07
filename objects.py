from pygame import sprite


class StaticObject(sprite.Sprite):
    # manage static objects like walls and environment

    def __init__(self, group, position, image):
        super().__init__(group)

        self.image = image
        self.rect = self.image.get_rect(center=position)
