import pygame

class Buttons:
    def __init__(self, x, y, width, height, text, image, image_on=None, sound=None, color='white'):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.image = pygame.transform.scale(pygame.image.load(image), (width, height))
        if image_on:
            self.image_on = pygame.transform.scale(pygame.image.load(image_on), (width, height))
        else:
            self.image_on = self.image
        self.rect = self.image.get_rect(topleft=(x, y))
        if sound:
            self.sound = pygame.mixer.Sound(sound)
        else:
            self.sound = None
        self.is_hovered = False

    def draw(self, screen):
        if self.is_hovered:
            current_image = self.image_on
        else:
            current_image = self.image
        screen.blit(current_image, self.rect.topleft)
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))