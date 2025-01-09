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
        surface_blit = surface.blit
        _sprites = self.sprites()

        _dh = self.dh
        _dv = self.dv
        _width, _height = Constants.width, Constants.height

        for spr in _sprites:
            rect = spr.rect
            pos = rect.topleft
            if ((rect.left - _dh < _width and rect.right - _dh > 0) and
                    (rect.top - _dv < _height and rect.bottom - _dv > 0)):
                surface_blit(spr.image, (pos[0] - _dh, pos[1] - _dv))
