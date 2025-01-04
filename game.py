import pygame as pg


class InGameHAndler:

    player = None
    objects = None
    enemies = None
    environment = None

    def __init__(self, game):

        self.game = game
        self.functions = {'#quit': (self.game.open, 'start')}

    def update(self, keys):
        if keys[pg.K_q]:
            function = self.functions['#quit']
            function[0](function[1])

        self.player.update()
        relative_position = self.player.rect.topleft

        self.objects.update(relative_position)
        self.enemies.update(relative_position)
        self.environment.update(relative_position)

    def draw(self, surface):
        self.environment.draw(surface)
        self.enemies.draw(surface)
        self.player.draw(surface)
        self.objects.draw(surface)
