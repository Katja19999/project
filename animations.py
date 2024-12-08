from images import Image
from timers import Timer


class Animation(Image):

    def __init__(self, path, sheets, time, states=('main', ), auto_reset=True):

        self.animation = {
            'right': dict(zip(states, [self.sprite_sheet(path, sheet) for sheet in sheets])),
            'left': dict(zip(states, [self.sprite_sheet(path, sheet, True) for sheet in sheets]))
        }
        self.timer = Timer(time)
        self.auto_reset = auto_reset

        self.current_direction = 'right'
        self.current_state = states[0]
        self.current_frame = 0

    @property
    def current_animation(self):
        return self.animation[self.current_direction][self.current_state]

    @property
    def animation_length(self):
        return len(self.current_animation) - 1

    @property
    def animation_ended(self):
        return self.current_frame >= self.animation_length

    @property
    def current_image(self):
        if self.timer.ready and not self.animation_ended:
            self.current_frame += 1

            if self.auto_reset:
                self.current_frame %= self.animation_length

        return self.current_animation[self.current_frame]

    def set_direction(self, direction):
        self.current_direction = direction

    def set_state(self, state):
        self.current_state = state
