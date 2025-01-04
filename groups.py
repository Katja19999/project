from pygame import sprite

from constants import Constants


# Group that manages "camera"
class RelativeGroup(sprite.AbstractGroup):

    absolute_position_h, absolute_position_v = Constants.absolute_center

    def __init__(self):
        super().__init__()

        self.dh = 0
        self.dv = 0

    def update_camera(self, relative_position_h, relative_position_v):
        self.dh = self.absolute_position_h - relative_position_h
        self.dv = self.absolute_position_v - relative_position_v

    def update(self, relative_position, *args, **kwargs):
        self.update_camera(*relative_position)
        super().update(*args, **kwargs)

    def draw(self, surface, *args):
        sprites = self.sprites()
        surface_blit = surface.blit

        for spr in sprites:
            relative_pos_h, relative_pos_v = spr.rect.topleft
            surface_blit(spr.image, (relative_pos_h - self.dh, relative_pos_v - self.dv))
