from math import atan2, hypot

from basefiles.timers import Timer


# Callable classes used for managing attacks
class Shoot:

    def __init__(self, bullet, bullet_group, reload):

        self.attack = bullet
        self._group = bullet_group

        self.reload = Timer(reload)

    @property
    def on_reload(self):
        return self.reload.ready

    def __call__(self, self_position, aim_position):
        self._group.add(self.attack(self_position, atan2(aim_position[1] - self_position[1],
                                                         aim_position[0] - self_position)))
        self.reload.reset()


class Attack:

    def __init__(self, damage, max_range, reload):

        self.damage = damage
        self.range = max_range

        self.reload = Timer(reload)

    @property
    def on_reload(self):
        return self.reload.ready

    def __call__(self, self_object, aim_object):
        if self.range > hypot(aim_object[0] - self_object[0], aim_object[1] - self_object[1]):
            aim_object.health -= self.damage
        self.reload.reset()
