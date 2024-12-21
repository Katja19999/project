from pygame import sprite

from basefiles.animations import Animation


class Character(sprite.Sprite):

    def __init__(self, position, states, path, animation_files, speed, attack):
        super().__init__()

        _animations = [Animation(path, file) for file in animation_files]
        _animations_flipped = [Animation(path, file, flip=True) for file in animation_files]
        self.animations = {'left': _animations, 'right': _animations_flipped}

        self.states = states
        self.directions = ['left', 'right']
        self.current_state = self.states[0]
        self.current_direction = self.directions[0]

        self.image = self.animations[self.current_direction][self.current_state]

        self.rect = self.image.get_rect(center=position)
        self.speed_x = speed[0]
        self.speed_y = speed[1]

        self.attack = attack

    def update(self, delta_x, delta_y, delta_time, *args, **kwargs):
        self.rect.move_ip(
            delta_x * delta_time,
            delta_y * delta_time
        )

        self.image = self.animations[self.current_direction][self.current_state]
