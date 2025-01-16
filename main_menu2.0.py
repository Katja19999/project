import sys
import pygame

from button import Buttons


class StartMenu:
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 864, 576
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Main menu')
        pygame.mixer.music.load('sounds/mainwindow_sound.mp3')
        self.start_btn = Buttons(15, 150, 252, 74, 'Играть', 'images/btn_main_window1.jpg',
                                 'images/btn_main_window2.jpg', 'sounds/btn_sound.mp3')
        self.exit_btn = Buttons(15, 250, 252, 74, 'Выйти', 'images/btn_main_window1.jpg', 'images/btn_main_window2.jpg',
                                'sounds/btn_sound.mp3')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play()

    def text_create(self, text, size, x, y, color='white'):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)

    def run(self):
        running = True
        while running:
            self.screen.fill((0, 0, 0))
            self.screen.blit(pygame.transform.scale(pygame.image.load('images/image_mainwindow.jpg'), (864, 576)),
                             (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if self.start_btn.handle_event(event):
                    pygame.mixer.music.stop()
                if self.exit_btn.handle_event(event):
                    running = False

            mouse_pos = pygame.mouse.get_pos()
            self.start_btn.check_hover(mouse_pos)
            self.exit_btn.check_hover(mouse_pos)

            self.start_btn.draw(self.screen)
            self.exit_btn.draw(self.screen)

            pygame.display.flip()
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    main_menu = StartMenu()
    main_menu.run()
