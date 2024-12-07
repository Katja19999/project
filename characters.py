from pygame import sprite

from animations import CharacterAnimation
from sounds import Sounds


class Character(sprite.Sprite):

    def __init__(self, coordinates, speed, states, sheets_path, sounds_path, sheets, sounds, time, rect=None):
        super().__init__()

        self.map_x = coordinates[0]
        self.map_y = coordinates[1]
        self.speed_x = speed[0]
        self.speed_y = speed[1]

        self.states = states
        self.sound = Sounds(sounds_path, self.states, sounds)
        self.animation = CharacterAnimation( sheets_path, self.states, sheets, time)
        self.image = self.animation.current_image

        self.rect = self.image.get_rect(int(self.map_x), int(self.map_y))

    def update(self, delta_x, delta_y, delta_time):
        self.map_x += delta_x * delta_time
        self.map_y += delta_y * delta_time

        self.image = self.animation.current_image

        self.rect.center = int(self.map_x), int(self.map_y)
