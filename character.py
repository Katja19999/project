from pygame import sprite


class Character(sprite.Sprite):

    def __init__(self, position, animation, move_speed):
        super().__init__()

        self.speed_x = move_speed[0]
        self.speed_y = move_speed[1]

        self.animation = animation
        self.current_direction = self.animation.keys()[0]
        self.current_state = self.animation[0][0]
        self.image = self.current_animation.current_image

        self.rect = self.image.get_rect(center=position)

    @property
    def current_animation(self):
        return self.animation[self.current_direction][self.current_state]

    @staticmethod
    def control_movement(walls, aim):
        return 0, 0

    def update(self, delta_x, delta_y, delta_time, walls, aim):
        delta_movement = self.control_movement(walls, aim)

        self.rect.move_ip(
            (delta_movement + delta_x) * delta_time,
            (delta_movement + delta_y) * delta_time,
        )
        self.image = self.current_animation.current_image
