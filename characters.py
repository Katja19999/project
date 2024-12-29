from pygame import sprite

from constants import Constants


class Character(sprite.Sprite):

    def __init__(self, group, position, animations):
        super().__init__(group)

        _animations_flipped = [animation.flipped for animation in animations]
        self.animations = {
            'right': dict(zip(['stand', 'walk', 'attack'], animations)),
            'left': dict(zip(['stand', 'walk', 'attack'], _animations_flipped))
        }

        self.direction = 'right'
        self.state = 'stand'

        self.move_h = 0
        self.move_v = 0

        self.rect = self.image.get_rect(topleft=position)

    @property
    def image(self):
        return self.animations[self.direction][self.state].frame

    def update_movement(self):
        pass

    def update_attack(self):
        pass

    def update_animation(self):
        self.direction = 'left' if self.move_h < 0 else 'right'

    def update(self, delta_time):
        self.update_movement()
        self.update_attack()

        self.rect.move_ip(
            self.move_h * delta_time,
            self.move_v * delta_time
        )
