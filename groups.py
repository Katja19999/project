from pygame import sprite

from constants import Constants


# Group that manages "camera"
class CameraGroup(sprite.AbstractGroup):

    aph, apv = Constants.absolute_center
    dh = 0
    dv = 0

    def update_camera(self, relative_position_h, relative_position_v):
        self.dh = relative_position_h - self.aph
        self.dv = relative_position_v - self.apv

    def update(self, relative_position, *args, **kwargs):
        self.update_camera(*relative_position)
        super().update(*args, **kwargs)

    def draw(self, surface, *args):
        sprites = self.sprites()
        dh = self.dh
        dv = self.dv

        surface.blits([(spr.image, (spr.rect.topleft[0] - dh, spr.rect.topleft[1] - dv)) for spr in sprites])
