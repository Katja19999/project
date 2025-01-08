from pygame import sprite


class StaticObject(sprite.Sprite):

    def __init__(self, image, position):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect(topleft=position)
