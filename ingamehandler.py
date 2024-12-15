from pygame import sprite


class InGameHandler:

    def __init__(self, handler):

        self.main_handler = handler

        self.player = None
        self.enemies = None
        self.objects = None
        self.environment = None

    @staticmethod
    def handle_collision(sprite1, sprite2):
        return sprite.collide_rect(sprite1, sprite2) and sprite.collide_mask(sprite1, sprite2)

    def handle_collisions(self):
        pass

    def update(self, events, delta_time):
        self.player.update(events, delta_time)

        _delta_x = self.player.dx
        _delta_y = self.player.dy

        self.enemies.update(_delta_x, _delta_y, delta_time)
        self.objects.update(_delta_x, _delta_y, delta_time)
        self.environment.update(_delta_x, _delta_y, delta_time)

    def draw(self, surface):
        self.environment.draw(surface)
        self.player.draw(surface)
        self.enemies.draw(surface)
        self.objects.draw(surface)
