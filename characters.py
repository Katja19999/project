import pygame as pg

from pygame import sprite
from images import sprite_sheet
from sounds import load
from timers import Timer


class Character(sprite.Sprite):

    def __init__(self, animation_path, sound_path, position, health, speed):
        super().__init__()

        self.animations = self.load_animations(animation_path)
        self.sounds = self.load_sounds(sound_path)

        self.health = health
        self.speed_h, self.speed_v = speed

        self.rect = pg.Rect(0, 0, 64, 64)
        self.collision_rect = pg.Rect(0, 0, 32, 32)

        self.action_timer = Timer(1000)
        self.action = 'stand'
        self.frame = 0

        self.dh = 0
        self.dv = 0

        self.rect.center = position
        self.collision_rect.center = position

    def load_animations(self, path):
        _size = self.rect.size
        animations = {
            'stand': sprite_sheet(path, 'stand.png', _size),
            'walk': sprite_sheet(path, 'stand.png', _size),
            'attack': sprite_sheet(path, 'stand.png', _size),
            'damage': sprite_sheet(path, 'stand.png', _size),
            'die': sprite_sheet(path, 'stand.png', _size),
        }
        return animations

    @staticmethod
    def load_sounds(path):
        animations = {
            'stand': load(path, 'stand'),
            'walk': load(path, 'walk'),
            'attack': load(path, 'attack'),
            'damage': load(path, 'damage'),
            'die': load(path, 'die'),
        }
        return animations

    def update_animation(self):
        if self.action_timer.ready:
            self.frame = (self.frame + 1) % len(self.animations[self.action])
