import pygame as pg
from pygame import sprite

from animations import CharacterAnimation


class Character(sprite.Sprite):

    def __init__(self, coordinates, speed, states, path, sheets, time, rect=None):
        super().__init__()

        self.x = coordinates[0]
        self.y = coordinates[1]
        self.speed_x = speed[0]
        self.speed_y = speed[1]

        self.states = states
        self.animation = CharacterAnimation(self.states, sheets, path, time)
        self.image = self.animation.current_image

        self.rect = rect if rect else self.image.get_rect()
        self.rect.center = int(self.x), int(self.y)

    def update(self, delta_x, delta_y, delta_time, current_state=None):
        self.x += delta_x * delta_time
        self.y += delta_y * delta_time

        self.animation.change_direction('left' if delta_x < 0 else 'right')
        if current_state:
            self.animation.change_state(current_state)

        self.image = self.animation.current_image

        self.rect.center = int(self.x), int(self.y)
