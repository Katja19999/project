from pygame import sprite


class GameObject(sprite.Sprite):

    def __init__(self, coordinates, animation):
        super().__init__()

        self.animation = animation
        self.image = self.animation.current_image

        self.rect = self.image.get_rect(center=coordinates)

    def update(self, delta_x, delta_y, delta_time):
        self.rect.move_ip(
            delta_x * delta_time,
            delta_y * delta_time
        )

        self.image = self.animation.current_image

